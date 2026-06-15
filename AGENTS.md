---
title: "AGENTS — operating rules for agents acting on this vault"
type: schema
date: 2026-06-10
explored: false
---

# AGENTS.md

Operating rules for any agent (Claude, Cogito, qmd, a script) that acts on this
vault. **Load order: `CONTEXT.md` → `learnings.md` → this file.** `CONTEXT.md` is
the conceptual ground; this file is what you may and may not *do*.

## What you may do

- Read everything in `raw/` and `wiki/`.
- Compile `wiki/` pages from `raw/` artifacts under the frontmatter contract.
- Propose captures: a kebab-case slug and complete frontmatter for items sitting
  in `~/Inbox/`.
- Run `wiki-lint` and report results.
- Append a one-line entry to `log.md` after a writing session.

## What you may never do

- **Never write or move a file in `raw/`** (Integrity Rule 2). You propose; Tom
  moves.
- **Never set `explored: true`** (Integrity Rule 4). Every page you write or edit
  keeps `explored: false`.
- **Never add a fourth top-level layer or a subfolder inside `raw/`** (Rule 1).
- **Never write a `wiki/` page that fails the read test, the relevance filter, or
  provenance** (Rule 3). When in doubt, leave it in the substrate.
- **Never create or hand-maintain `index.md` / `hot.md`** or any meta-file beyond
  the append-only `log.md` and the live `dashboard.md`.

## Every `wiki/` page you write

- `explored: false`.
- ≥ 2 `raw_sources` for `concept|entity|source|sop`; `wiki_sources` for
  `synthesis|output`.
- Provenance as `[[wikilinks]]` in the body, every link resolving to a real page.
- Passes `wiki-lint` with zero errors before you declare it done.

## Skills (trimmed core set)

Use the smallest skill that does the job. The core set lives in
`.claude/skills/` (see the implementation plan):

- **`wiki-lint`** — validate the frontmatter contract and Integrity Rules. Run
  before declaring any write done.
- **`capture-triage`** — turn a `~/Inbox/` item into a proposed slug + frontmatter
  for Tom to file. Proposes only; never moves.
- **`compile-wiki`** — compile `raw/` artifacts into a `wiki/` page under the
  contract (read test, relevance filter, ≥2 sources, provenance, `explored:false`).

## Logging

After a session that wrote to `wiki/`, append **one line** to `log.md`:
`YYYY-MM-DD — <what changed> — <pages touched>`. Append-only. Never reconcile or
rewrite earlier entries; git is the history of record.

## Definition of done

A unit of work is done when: `wiki-lint` passes, provenance wikilinks resolve,
`explored: false`, and (for a writing session) `log.md` has its one-line entry.
