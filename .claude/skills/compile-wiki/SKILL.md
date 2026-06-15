---
name: compile-wiki
description: >
  Compile raw/ artifacts into a wiki/ page under the CONTEXT.md contract. Use when
  asked to write up a concept/entity/source/sop/decision/synthesis/output from the
  substrate. Writes explored:false, full frontmatter, resolving provenance links.
---

# compile-wiki

Compile substrate into a single readable `wiki/` page. Apply the gates before you
write, not after.

## Before writing — the gates

- **Read test (Rule 5):** would Tom open this page months from now? If not, stop —
  leave it in `raw/` or add it as a section of an existing page.
- **Relevance / provenance (Rule 3):** gather **≥ 2** relevant `raw_sources`. A
  single source is allowed only if you write an explicit relevance justification
  in the body.

## Writing

1. Pick the `type` and put the file in the matching folder (`wiki/<type-plural>/`).
2. Use the matching template in `.obsidian/templates/`.
3. Fill frontmatter: `title`, `type`, `date`, `explored: false`, `tags`,
   `confidence` (number — `0.5` if unsure), `raw_sources` (and/or `wiki_sources`).
4. In the body, cite provenance as `[[wikilinks]]`; every link must resolve.

## After writing

1. Run **wiki-lint**; fix every hard violation.
2. Append one line to `log.md`.
3. Leave `explored: false` — only Tom flips it (Rule 4).
