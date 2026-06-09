---
description: Health-check the wiki against integrity rules and the frontmatter contract
allowed-tools: Read, Write, Glob, Grep, mcp__qmd
---

Read CONTEXT.md, AGENTS.md, and learnings.md before acting.
Where they conflict, CONTEXT.md wins.

# /wiki-lint

A read-only health check. The lint never edits `wiki/` or
`raw/`. It surfaces findings as a chat report and,
optionally, as one `output` page.

## Pre-flight

1. Read `learnings.md`. Every entry is a prior decision
   Tom made on a previous lint proposal — do not re-surface
   anything Tom has already rejected for the same page or
   the same reason.
2. Index `wiki/` via qmd (AGENTS.md §qmd). Bodies on demand.

## The ten checks

Each check is grounded in either an Integrity Rule
(CONTEXT.md §Integrity rules) or a named frontmatter field
(AGENTS.md §Frontmatter).

1. **Required frontmatter per page type.** For every
   `wiki/` page, verify baseline fields (`title`, `type`,
   `date`, `explored`, `raw_sources`) and per-type required
   fields (e.g. `source_url` on `source`, `status` on
   `decision`, `wiki_sources` on `synthesis`). Source:
   AGENTS.md §Frontmatter table.
2. **`raw_sources:` validation.** Each filename listed in a
   page's `raw_sources:` must exist in `raw/`. Exception:
   `synthesis` (uses `wiki_sources:` instead, may be empty).
   Source: CONTEXT.md §Named frontmatter; Rule 6.
3. **`[[wikilink]]` validation.** Resolve every wikilink.
   Distinguish three classes in the report:
   - broken — target was clearly meant to exist but is
     missing (typo, deleted page).
   - stub — target exists but is near-empty.
   - void — target does not exist and was not justified by
     the relevance filter. Source: Rule 6.
4. **Path/type drift.** `type:` frontmatter must agree with
   the subfolder. Surface mismatches as re-typing proposals;
   Tom decides via `learnings.md` whether path or
   frontmatter moves. Source: CONTEXT.md §The seven page
   types; AGENTS.md §Lint check 4.
5. **Orphan check.** Pages with no inbound `[[wikilink]]`
   from any other `wiki/` page. Not always a defect — flag,
   do not condemn.
6. **Stale `explored: false`.** Pages with `explored: false`
   older than 6 months (date measured against `date:`
   field). Surface for Tom's validation pass. Source: Rule
   4; AGENTS.md §Lint check 6 (threshold: 6 months).
7. **`explored: true` set by anything other than Tom.** If
   git history attributes the flip to the agent, flag as a
   Rule 4 violation. Source: Rule 4.
8. **Contradictions.** Pages with a non-empty
   `contradictedBy:` list. Report the pair so Tom can
   resolve. Source: AGENTS.md §Lint check 8.
9. **Domain drift.** Pages whose topic falls outside the
   vault's domain scope (Tech / Tooling / LLM, per Tom's
   stated focus). Heuristic, not a hard rule — surface as
   proposals, never auto-action. Source: AGENTS.md §Lint
   check 9.
10. **Relevance-filter violations.** Pages with fewer than
    two `raw_sources` AND no marker of Tom-relevance in
    body or frontmatter. `synthesis` pages exempt. Source:
    CONTEXT.md §Relevance filter; Rule 6.

## What the lint never does

- No edits to any `wiki/` page. No auto-fix of frontmatter,
  no auto-fix of wikilinks, no slug renames. Rule 4
  prohibits the agent from touching the validation gate;
  the same logic extends to all corrective action on
  validated pages.
- No writes to `raw/`. Rules 2, 3.
- No writes to `wiki/index.md` or `wiki/log.md` — neither
  exists in this vault by design.
- No new pages, no stubs, no link injection.
- No re-surfacing of proposals Tom already declined in
  `learnings.md`.

## Output

Always: a chat report, organised by check (1–10). For each
finding, include the page path, the line or field involved,
and the Integrity Rule or named frontmatter field it
implicates.

Ask Tom, at the end of the chat report, whether to persist
the report as `wiki/outputs/lint-report-YYYY-MM-DD.md`
(legitimate `output` page; AGENTS.md §Lint). Only on
explicit "yes" write the file. Frontmatter for that page:

```
type: output
title: Lint Report YYYY-MM-DD
date: YYYY-MM-DD
explored: false
raw_sources: []
```

Tom's decisions on the surfaced proposals — accept, reject,
defer — are appended to `learnings.md` by `/wiki-learn` (or
manually by Tom). `/wiki-lint` itself does not write
`learnings.md`.
