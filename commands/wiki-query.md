---
description: Answer a question against the wiki; optionally persist as a synthesis page
allowed-tools: Read, Write, Edit, mcp__qmd
argument-hint: <question>
---

Read CONTEXT.md and AGENTS.md before acting. Where they
conflict, CONTEXT.md wins.

# /wiki-query <question>

Answers a question by reading across `wiki/` pages. The
default deliverable is a chat answer with citations. A
persisted `synthesis` page is created only when the read
test passes — i.e. Tom will want to re-open the answer
later.

## Inputs

- `$ARGUMENTS` is the question. If empty, stop and ask Tom.

## Resolve sources

1. Use qmd to index across `wiki/` (AGENTS.md §qmd —
   "index-via-query, body-on-demand"). Do not load full
   page bodies until a page is judged relevant.
2. Identify the candidate `wiki/` pages that bear on the
   question. Load their bodies.
3. Note any candidate page with `explored: false` — its
   claims are not validated by Tom and must be treated as
   provisional. Cite, but flag.

## Synthesise

1. Compose an answer that draws on the loaded pages.
2. Cite every claim with `[[wikilink]]` to its source page.
   No claim without a cite. If a claim has no `wiki/`
   source, drop it — `/wiki-query` does not invent.
3. Distinguish `explored: true` evidence from
   `explored: false` evidence in the answer.

## Decide whether to persist

Apply the read test (CONTEXT.md §"The read test"):

> *If Tom opens this page in 6 months — does he want to
> read it, or is it just agent context that he never looks
> at again?*

- If no: deliver the answer in chat only. Stop.
- If yes: persist as a `synthesis` page (next section).

## Persist as synthesis page

1. Use the `wiki-synthesis.md` template from
   `.obsidian/templates/`. The template enforces the
   frontmatter contract; do not hand-roll.
2. Path: `wiki/syntheses/<slug>.md`. Slug kebab-case,
   derived from the question (Tom may rename later).
3. Frontmatter per AGENTS.md §per-page-type for
   `synthesis`:
   - `type: synthesis`
   - `explored: false` (Rule 4 — only Tom flips this)
   - `raw_sources:` may be empty (CONTEXT.md §Named
     frontmatter).
   - `wiki_sources:` lists every cited `wiki/` page slug.
4. Body in English (Rule 7). Preserve the cites as
   `[[wikilinks]]`. No links into the void (Rule 6).

## Out of scope

- No writes to `raw/`.
- No writes to `wiki/index.md` or `wiki/log.md` — neither
  exists in this vault by design.
- No fabricated claims, no fetching outside the wiki.
- No persistence under `wiki/outputs/`. A
  `wiki/`-internal answer is `synthesis`, not `output`
  (CONTEXT.md §The seven page types).

## Report

Chat output, in this order:

- The answer itself, with cites.
- Pages cited (path, `explored:` status).
- If persisted: the new synthesis page path.
- If not persisted: a one-line note that the read test
  failed and why — so Tom can override.
