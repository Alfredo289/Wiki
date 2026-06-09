---
description: Compile unprocessed raw/ artifacts into wiki/ pages
allowed-tools: Read, Write, Edit, Glob, Grep, mcp__qmd
---

Read CONTEXT.md and AGENTS.md before acting. Where they
conflict, CONTEXT.md wins.

# /wiki-ingest

Compiles every `raw/` artifact that is not yet cited by any
`wiki/` page into one or more `wiki/` pages.

## Scan

1. List all files in `raw/` (flat folder; no subfolders by
   design — CONTEXT.md §`raw/`).
2. Via qmd, list every `wiki/` page's `raw_sources:` field.
3. The ingest set is `raw/` files whose filename appears in
   no page's `raw_sources:`. Process each member of the
   set in turn. If the set is empty, report "nothing to
   ingest" and stop.

## Per artifact

1. Read the `raw/` file. Do not modify it. Do not move it.
   Do not rename it. `raw/` is human-curated and immutable
   after entry (Integrity Rules 2, 3).
2. Apply the read test and the relevance filter
   (CONTEXT.md). Skip a candidate `wiki/` page if either
   gate fails. Surface skipped candidates in the final
   report so Tom can override.
3. Identify the page types this artifact warrants:
   - One `source` page (always — one artifact, one source
     summary).
   - Zero or more `concept` pages — only if the relevance
     filter passes (2+ raw_sources covering the concept, or
     explicit Tom-relevance evidenced in `raw/`).
   - Zero or more `entity` pages — same filter.
   - Other page types (`sop`, `decision`, `output`,
     `synthesis`) are not produced by ingest. They are
     authored deliberately via `/wiki-new-page`.

## Writing pages

For each page to create:

1. Use the matching template from `.obsidian/templates/`:
   `wiki-source.md`, `wiki-concept.md`, `wiki-entity.md`.
   The template enforces the frontmatter contract; do not
   hand-roll frontmatter.
2. Frontmatter must satisfy AGENTS.md §Frontmatter for the
   chosen type. `explored: false` always (Rule 4). The
   ingested artifact's filename goes into `raw_sources:`.
   `source` pages additionally require `source_url:`.
3. Kebab-case slug. Place the file under
   `wiki/<type>s/<slug>.md`. Path encodes type.
4. Body in English (Rule 7). Translate from German on the
   way in if needed.
5. `[[wikilinks]]` only to pages that already exist or that
   this run will create. No links into the void (Rule 6) —
   if the relevance filter rejects a candidate, drop the
   link rather than stubbing.

## Updating existing pages

If the artifact substantively extends a page that already
exists:

1. Append the artifact's filename to that page's
   `raw_sources:`.
2. Add or refine prose where the new artifact warrants it.
   Append; do not rewrite.
3. If the change is substantive, set `explored: false`.
   Tom re-validates (Rule 4).

## Out of scope

- No writes to `raw/`. None. No sorting, no in-place edits,
  no media extraction, no URL fetching, no asset downloads.
  Ingest into `raw/` is Tom's hand only, mediated by his
  `raw-*` templates.
- No stub pages created solely to satisfy a wikilink.
- No writes to `wiki/index.md` or `wiki/log.md` — neither
  exists in this vault by design (CONTEXT.md §Meta-files).
- No counter-arguments or data-gaps sections unless the
  template defines them.

## Report

Chat-only output:

- Artifacts processed (filename).
- Pages created (path, type).
- Pages updated (path, what was appended).
- Wikilinks added.
- Candidates rejected by the read test or relevance filter,
  with the artifact and the proposed slug — so Tom can
  override if a rejection was wrong.
