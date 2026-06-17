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
- When Tom invokes `wiki-capture-triage`, write a note of the conversation into
  `raw/clippings/` — the one permitted agent write to `raw/`.
- Run `wiki-lint` and report results.
- Append a one-line entry to `log.md` after a writing session.

## What you may never do

- **Never write or move a file in `raw/`** (Integrity Rule 2) — the sole
  exception is the Tom-invoked `wiki-capture-triage` skill writing a conversation
  note to `raw/clippings/`.
- **Never set `explored: true`** (Integrity Rule 4). Every page you write or edit
  keeps `explored: false`.
- **Never add a fourth top-level layer** (Rule 1). Inside `raw/` the only
  structure is `raw/clippings/` (sources) and `raw/clippings/assets/`
  (attachments) — add no other subfolders.
- **Never write a `wiki/` page that fails the read test, the relevance filter, or
  provenance** (Rule 3). When in doubt, leave it in the substrate.
- **Never create or hand-maintain `index.md` / `hot.md`** or any meta-file beyond the append-only `log.md` and the live `dashboard.md`.

## Every `wiki/` page you write

- `explored: false`.
- A `source` page cites `raw_sources` (its `raw/clippings/` file). Every other
  page cites `wiki_sources` → source pages (≥ 2 ideal). Rule 3.
- Provenance as `[[wikilinks]]` in the body, every link resolving to a real page.
- Passes `wiki-lint` with zero errors before you declare it done.

## Interacting with Obsidian pages

Read and write `wiki/` pages through the **`obsidian-cli`** skill (the `obsidian`
command — `read`, `create`, `append`, `property:set`, `search`, `backlinks`) —
not by hand-editing files. Obsidian must be open. Create new pages from the
matching Templater template via `obsidian create … template=…` so Templater
fills the dynamic frontmatter; then set the contract fields and write the body.
Author all Obsidian-flavoured markdown (wikilinks, callouts, properties) per the
**`obsidian-markdown`** skill. `raw/` stays Tom-only (Rule 2); `wiki-lint` still
reads files directly to validate — that's fine.

## Skills (trimmed core set)

Use the smallest skill that does the job. The core set lives in `.agents/skills/`
(exposed to Claude Code as symlinks under `.claude/skills/`):

- **`wiki-lint`** — validate the frontmatter contract and Integrity Rules. Run
  before declaring any write done.
- **`wiki-capture-triage`** — on Tom's invocation, write a note of the current
  conversation into `raw/clippings/` as a source artifact. The one skill that
  writes to `raw/`.
- **`wiki-compile`** — write a single `wiki/` page under the contract (read test,
  relevance filter, provenance, `explored:false`). The page-writing primitive.
- **`wiki-ingest`** — the full ingest operation: turn one new `raw/clippings/`
  source into its `source` page plus the entity/concept pages it touches,
  cross-linked. Builds on `wiki-compile`; this is what makes the wiki compound.
- **`wiki-query`** — answer a question against the wiki (qmd + `obsidian search`),
  synthesise a cited answer, optionally file it back as an `output`/`synthesis`.
- **`wiki-health`** — semantic health-check (contradictions, stale claims, missing
  pages, orphans, data gaps). Advisory; proposes, never edits. Karpathy's "lint".

## Logging

After a session that wrote to `wiki/`, append **one line** to `log.md`:
`YYYY-MM-DD — <what changed> — <pages touched>`. Append-only. Never reconcile or
rewrite earlier entries; git is the history of record.

## Definition of done

A unit of work is done when: `wiki-lint` passes, provenance wikilinks resolve,
`explored: false`, and (for a writing session) `log.md` has its one-line entry.
