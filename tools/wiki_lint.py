#!/usr/bin/env python3
"""wiki-lint — validate the vault against the frontmatter contract + Integrity Rules.

Stdlib only (macOS ships python3; no `pip install` needed).

Usage:
    python3 tools/wiki_lint.py [ROOT] [--json]

ROOT defaults to ".". The linter looks only at ROOT/wiki (pages) and ROOT/raw
(substrate) — it never recurses into .docs, .obsidian, .git, etc. Exit code =
number of HARD violations (0 = pass).

Rules
-----
HARD (exit non-zero, must be fixed):
  FM-PARSE      frontmatter present and the `---` block is closed
  FM-REQ        required field present for the page type (decision also needs status)
  FM-TYPE       explored boolean, confidence number 0..1, date YYYY-MM-DD, known type
  GATE          no agent-set `explored: true`            (Integrity Rule 4)
  LINK          every [[wikilink]] resolves to a real page (filename slug or title)
  PATH          `type:` matches the folder (wiki/concepts -> concept)
  PROV-REF      every raw_sources entry exists as a file in raw/
  PROV-MISSING  a wiki page has at least one source (raw_sources or wiki_sources)
  FLAT          raw/ has no subfolders                   (Integrity Rule 1)

ADVISORY (reported, not gated):
  ORPHAN        page not linked from any other page
  PROV-SINGLE   exactly one raw_source — justify in body or merge
"""
from __future__ import annotations
import json
import os
import re
import sys

# ---- contract -------------------------------------------------------------
WIKI_TYPES = {"concept", "entity", "source", "sop", "decision", "synthesis", "output"}
WORKING_TYPES = {"project"}                       # allowed, exempt from provenance
SUBSTRATE_TYPES = {"concept", "entity", "source", "sop"}
COMPOSED_TYPES = {"synthesis", "output"}
FOLDER_TO_TYPE = {
    "concepts": "concept", "entities": "entity", "sources": "source",
    "sops": "sop", "decisions": "decision", "syntheses": "synthesis",
    "outputs": "output",
}
HARD = {"FM-PARSE", "FM-REQ", "FM-TYPE", "GATE", "LINK", "PATH",
        "PROV-REF", "PROV-MISSING", "FLAT"}
SOFT = {"ORPHAN", "PROV-SINGLE"}

WIKILINK = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
EXPLORED_TRUE = re.compile(r"^\s*explored:\s*true\s*$", re.M)


def slugify(s: str) -> str:
    s = str(s).strip().strip("\"'").lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def _unquote(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] in "\"'" and s[-1] == s[0]:
        return s[1:-1]
    return s


def split_frontmatter(text):
    """Return (fm_text, body, ok). ok=False if the --- block is absent/unclosed."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return "", text, False
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:]), True
    # unclosed: best-effort up to the first markdown heading or EOF
    for i in range(1, len(lines)):
        if lines[i].startswith("# "):
            return "\n".join(lines[1:i]), "\n".join(lines[i:]), False
    return "\n".join(lines[1:]), "", False


def parse_fm(fm_text):
    """Tiny YAML-ish parser for the flat contract (scalars + block/inline lists)."""
    fm, key = {}, None
    for ln in fm_text.split("\n"):
        if not ln.strip():
            continue
        m = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", ln)
        if m and not ln[0].isspace():
            key, val = m.group(1), m.group(2).strip()
            if val == "" or val == "[]":
                fm[key] = []
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                fm[key] = [_unquote(x.strip()) for x in inner.split(",")] if inner else []
            else:
                fm[key] = _unquote(val)
        elif re.match(r"^\s*-\s+", ln) and key is not None:
            if not isinstance(fm.get(key), list):
                fm[key] = []
            fm[key].append(_unquote(re.sub(r"^\s*-\s+", "", ln).strip()))
    return fm


class Page:
    __slots__ = ("path", "rel", "folder", "slug", "title_slug",
                 "fm", "fm_ok", "fm_text", "links")


def discover(root):
    wiki_dir, raw_dir = os.path.join(root, "wiki"), os.path.join(root, "raw")
    wiki_files = []
    for dirpath, _dirs, files in os.walk(wiki_dir):
        for f in files:
            if f.endswith(".md"):
                wiki_files.append(os.path.join(dirpath, f))
    raw_names, raw_present = set(), False
    if os.path.isdir(raw_dir):
        for f in os.listdir(raw_dir):
            if os.path.isfile(os.path.join(raw_dir, f)) and not f.startswith("."):
                raw_present = True
                raw_names.add(f)
                raw_names.add(os.path.splitext(f)[0])
    return sorted(wiki_files), raw_dir, raw_names, raw_present


def lint(root="."):
    """Return {relpath: [(rule, message), ...]} for every wiki page (+ 'raw/')."""
    wiki_files, raw_dir, raw_names, raw_present = discover(root)
    pages = []
    for path in wiki_files:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        fm_text, _body, ok = split_frontmatter(text)
        p = Page()
        p.path = path
        p.rel = os.path.relpath(path, root).replace(os.sep, "/")
        p.folder = os.path.basename(os.path.dirname(path))
        p.slug = os.path.splitext(os.path.basename(path))[0]
        p.fm_text = fm_text
        p.fm_ok = ok
        p.fm = parse_fm(fm_text)
        title = p.fm.get("title")
        p.title_slug = slugify(title) if isinstance(title, str) and title.strip() else ""
        p.links = [m.group(1).strip() for m in WIKILINK.finditer(text)]
        pages.append(p)

    resolved, inbound = set(), set()
    for p in pages:
        resolved.add(p.slug)
        if p.title_slug:
            resolved.add(p.title_slug)
    for p in pages:
        for t in p.links:
            inbound.add(slugify(t))

    results = {}
    for p in pages:
        v = []
        if not p.fm_ok:
            v.append(("FM-PARSE", "frontmatter missing or `---` block not closed"))
        if EXPLORED_TRUE.search(p.fm_text):
            v.append(("GATE", "explored: true must be set by Tom, not an agent (Rule 4)"))

        if p.fm_ok:
            fm = p.fm
            typ = fm.get("type")
            title = fm.get("title")
            if not (isinstance(title, str) and title.strip()):
                v.append(("FM-REQ", "missing required field: title"))
            if not typ:
                v.append(("FM-REQ", "missing required field: type"))
            elif typ not in WIKI_TYPES and typ not in WORKING_TYPES:
                v.append(("FM-TYPE", f"unknown type: {typ}"))
            if not fm.get("date"):
                v.append(("FM-REQ", "missing required field: date"))
            elif not DATE_RE.match(str(fm.get("date"))):
                v.append(("FM-TYPE", f"date not YYYY-MM-DD: {fm.get('date')}"))
            if "explored" not in fm:
                v.append(("FM-REQ", "missing required field: explored"))
            elif str(fm.get("explored")).lower() not in ("true", "false"):
                v.append(("FM-TYPE", f"explored not boolean: {fm.get('explored')}"))
            tags = fm.get("tags")
            if not isinstance(tags, list) or not tags:
                v.append(("FM-REQ", "missing required field: tags"))
            conf = fm.get("confidence")
            if conf in (None, "", []):
                v.append(("FM-REQ", "missing required field: confidence"))
            else:
                try:
                    c = float(conf)
                    if not 0.0 <= c <= 1.0:
                        v.append(("FM-TYPE", f"confidence out of range 0..1: {conf}"))
                except (TypeError, ValueError):
                    v.append(("FM-TYPE", f"confidence not a number: {conf}"))
            if typ == "decision" and not fm.get("status"):
                v.append(("FM-REQ", "decision page missing required field: status"))

            want = FOLDER_TO_TYPE.get(p.folder)
            if want and typ in (WIKI_TYPES | WORKING_TYPES) and typ != want:
                v.append(("PATH", f"type '{typ}' != folder '{p.folder}' (expected '{want}')"))

            rs = fm.get("raw_sources") if isinstance(fm.get("raw_sources"), list) else []
            ws = fm.get("wiki_sources") if isinstance(fm.get("wiki_sources"), list) else []
            if typ in SUBSTRATE_TYPES:
                if not rs:
                    v.append(("PROV-MISSING", "substrate page has no raw_sources"))
                else:
                    if raw_present:
                        for r in rs:
                            base = r[:-3] if r.endswith(".md") else r
                            if r not in raw_names and base not in raw_names:
                                v.append(("PROV-REF", f"raw_sources referent not in raw/: {r}"))
                    if len(rs) == 1:
                        v.append(("PROV-SINGLE", "single raw_source — justify in body or merge"))
            elif typ in COMPOSED_TYPES:
                if not rs and not ws:
                    v.append(("PROV-MISSING", "synthesis/output has no raw_sources or wiki_sources"))
                elif raw_present and rs:
                    for r in rs:
                        base = r[:-3] if r.endswith(".md") else r
                        if r not in raw_names and base not in raw_names:
                            v.append(("PROV-REF", f"raw_sources referent not in raw/: {r}"))

        for t in p.links:
            if slugify(t) not in resolved:
                v.append(("LINK", f"unresolved wikilink: [[{t}]]"))

        if p.slug not in inbound and (not p.title_slug or p.title_slug not in inbound):
            v.append(("ORPHAN", "page is not linked from any other page"))

        results[p.rel] = v

    flat = []
    if os.path.isdir(raw_dir):
        for f in os.listdir(raw_dir):
            if os.path.isdir(os.path.join(raw_dir, f)):
                flat.append(("FLAT", f"raw/ must be flat — found subfolder: {f}/"))
    results["raw/"] = flat
    return results


def main(argv):
    root, as_json = ".", False
    for a in argv:
        if a == "--json":
            as_json = True
        elif not a.startswith("-"):
            root = a

    results = lint(root)
    hard = soft = 0
    lines = []
    for rel in sorted(results):
        for rule, msg in results[rel]:
            if rule in HARD:
                hard += 1
                lines.append(f"ERROR {rule:13} {rel}: {msg}")
            else:
                soft += 1
                lines.append(f"warn  {rule:13} {rel}: {msg}")

    if as_json:
        out = {rel: [r for r, _ in vs] for rel, vs in results.items() if vs}
        print(json.dumps(out, indent=2, sort_keys=True))
    else:
        print("\n".join(lines) if lines else "No issues.")
        print(f"\n{hard} hard error(s), {soft} advisory warning(s).")
    return hard


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
