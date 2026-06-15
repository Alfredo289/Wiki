---
name: wiki-lint
description: >
  Validate the vault against the frontmatter contract and Integrity Rules in
  CONTEXT.md. Use before declaring any wiki write done, or whenever Tom asks to
  check / lint the vault. Reports per-file rule violations; never edits raw/.
---

# wiki-lint

Run the validator and report results. Do not auto-fix `raw/` and never change
`explored`.

## How to run (macOS)

```bash
python3 tools/wiki_lint.py .          # lint the live vault (wiki/ + raw/)
python3 tools/wiki_lint.py . --json   # machine-readable, for the test runner
```

Python 3 ships with macOS; no `pip install` needed (stdlib only).

## Hard rules (exit non-zero — must be fixed)

- `FM-PARSE` frontmatter present and the `---` block is closed.
- `FM-REQ` required fields present for the page's `type` (decisions also need `status`).
- `FM-TYPE` `explored` boolean, `confidence` a number 0–1, `date` is `YYYY-MM-DD`.
- `GATE` no agent-set `explored: true` (Integrity Rule 4).
- `LINK` every `[[wikilink]]` resolves to a real page (filename slug or title).
- `PATH` the `type:` field matches the folder (`wiki/concepts/` → `concept`).
- `PROV-REF` every `raw_sources` entry exists as a file in `raw/`.
- `PROV-MISSING` a wiki page has at least one source (raw_sources or wiki_sources).
- `FLAT` `raw/` has no subfolders (Integrity Rule 1).

## Advisory (reported, not gated)

- `ORPHAN` page is not linked from any other page (roots like `dashboard.md` excepted).
- `PROV-SINGLE` exactly one `raw_source` — justify in the body or merge into a larger page.

## Reporting

List each violation as `RULE  path  message`. End with a count. If the count of
hard violations is zero, say the vault passes.
