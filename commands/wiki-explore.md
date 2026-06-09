---
description: Identify gaps in a wiki/ page and propose external sources for Tom to curate
allowed-tools: Read, Glob, Grep, WebFetch, WebSearch, mcp__qmd
argument-hint: <wiki-page-slug-or-topic>
---

Read CONTEXT.md and AGENTS.md before acting. Where they
conflict, CONTEXT.md wins.

# /wiki-explore <topic>

A **read-only proposal command**. It identifies gaps in a
`wiki/` page (or a topic the wiki does not yet cover) and
proposes external sources Tom can decide to curate into
`raw/`. It never writes to `wiki/` or `raw/`.

## Why this command does not write

CONTEXT.md Integrity Rule 2: Tom is the sole curator of
`raw/`. Every `wiki/` claim traces back to a human-curated
`raw/` artifact. A command that fetches the web and writes
findings into `wiki/` would unite both halves of the
validation chain in the agent and erase the audit trail. So
`/wiki-explore` stops one step short: it surfaces
candidates; Tom decides what enters `raw/`.

## Inputs

- `$ARGUMENTS` is either:
  - the slug of an existing `wiki/` page, e.g.
    `agentic-loops` — read that page and find gaps; or
  - a free topic, e.g. `vector databases` — search `wiki/`
    via qmd for adjacent coverage, then proceed as if
    proposing a new page.

If empty, stop and ask Tom.

## Resolve current state

1. If the argument matches a `wiki/` page, load it.
2. Via qmd, list adjacent pages (linked from or to the
   target page, or covering related concepts).
3. Note each related page's `explored:` status. Treat
   `explored: false` claims as provisional when reasoning
   about gaps.

## Identify gaps

Compose a short gap analysis. A gap is one of:

- An assertion in the page that has no backing in any
  listed `raw_sources:` (verify by reading the relevant
  raw artifact).
- An adjacent concept the page references without
  defining, where the relevance filter would justify a new
  page (2+ raw sources or Tom-relevance).
- A claim where `explored: false` evidence is the only
  support — flag for Tom's validation pass, not for
  external corroboration.
- An open question Tom marked in the page body.

## Search the web

For each gap, run web search and/or fetch candidate
sources. Limits:

- Prefer primary sources (papers, official docs, original
  posts) over aggregators.
- Capture the canonical URL, the title, the publication
  date if available, and a one-sentence reason this source
  addresses the gap.
- Do not paste long quotes; the goal is a curation
  proposal, not a substitute for `raw/`.

## Out of scope

- No writes to `raw/`. None.
- No writes to `wiki/`. No edits, no appends, no new
  pages, no new wikilinks.
- No writes to `wiki/index.md` or `wiki/log.md` — neither
  exists in this vault by design.
- No `confidence:` scoring (no field is written, since
  nothing is written).
- No claim invention. If a gap has no good external
  source, say so.

## Report

Chat-only output, structured per gap:

1. **The gap** — one sentence, citing the page and the
   passage.
2. **Proposed sources** — list of 1–3 candidates, each
   with URL, title, date, and the one-sentence reason.
3. **Suggested `raw/` template** — which of Tom's
   `raw-article`, `raw-paper`, `raw-youtube`, etc., fits
   this candidate, so curation is one step away.
4. **What happens after curation** — name the `wiki/`
   page(s) `wiki-ingest` would touch once the source lands
   in `raw/`, so Tom can see the downstream effect before
   deciding.

End the report with a one-line summary: gaps surfaced,
candidates proposed, gaps with no good source found.
