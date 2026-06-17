---
title: "CONTEXT — conceptual ground for the vault"
type: schema
date: 2026-06-10
explored: false
---

## CONTEXT.md

The first file any agent or tool loads. It defines what this vault **is** and the
rules every layer obeys. It is conceptual ground — not a task list. Operating
instructions for agents live in `AGENTS.md`; accumulated corrections live in
`learnings.md`.

## The model: a three-layer vault

A personal knowledge vault organised as three explicit layers. The split is what
makes provenance auditable; removing any layer collapses it into the "single
notes folder" that erodes over time.

| Layer | Folder | Who writes it | Mutability |
|-------|--------|---------------|------------|
| **Substrate** | `raw/` | Tom (+ wiki-capture-triage on request) | Immutable once filed |
| **Compiled wiki** | `wiki/` | Agent, validated by Tom | Rewritable |
| **Schema** | `CONTEXT.md`, `AGENTS.md`, `learnings.md` | Tom (+ agent proposals) | Versioned |

`raw/` holds curated artifacts under **`raw/clippings/`** — the capture target
for Obsidian Web Clipper / Readwise — with image and file attachments in
**`raw/clippings/assets/`**. That is the only nesting inside `raw/`; there are no
per-topic or per-format subfolders. Origin and format live in frontmatter.
`wiki/` is organised into type subfolders (`concepts/`, `entities/`, `sources/`,
`sops/`, `decisions/`, `syntheses/`, `outputs/`).

## Integrity Rules

1. **Three layers, no fourth.** No new top-level layer. Inside `raw/` the only
   structure is `raw/clippings/` for source artifacts and `raw/clippings/assets/`
   for their attachments — no other subfolders.
2. **Tom curates `raw/`.** What goes into `raw/` is Tom's call — he fills it with
   the sources the wiki is built from. Agents never add to `raw/` on their own
   initiative. The one exception is the **wiki-capture-triage** skill: when Tom invokes
   it, it writes a note of the current conversation into `raw/clippings/`. No
   other agent action ever creates, edits, or moves a file in `raw/`.
3. **No claim without provenance — anchored once per source.** Each
   `raw/clippings/` file is summarised by exactly one `source` page, and that
   source page is the only page that cites `raw_sources`. Every other page type
   (`concept`, `entity`, `sop`, `decision`, `synthesis`, `output`) traces back
   through `wiki_sources` pointing at those source pages (and may add extra
   `raw_sources` only with justification). The ideal is **≥ 2** sources; a single
   source is allowed only with an explicit relevance justification in the body. A
   page with no provenance is a defect.
4. **The validation gate.** Agents always write `explored: false`. Only Tom
   flips it to `true`, and only after reading. `explored: true` introduced by an
   agent is a Rule 4 breach.
5. **The read test.** A page exists only if Tom would deliberately open it months
   later. If not, the content stays in the substrate or is not written at all.

## The frontmatter contract

The contract is the only shared source of truth across tools that cannot call
Dataview (`qmd`, `wiki-lint`). Both schemas below are mandatory and linted.

### `raw/` artifacts

```yaml
title: string          # required
origin: own | external # required
format: md | image | audio | video | pdf   # required
added: YYYY-MM-DD       # required
source_url: string      # required when origin: external
```

### `wiki/` pages

```yaml
title: string           # required
type: concept | entity | source | sop | decision | synthesis | output   # required
date: YYYY-MM-DD         # required
explored: false          # required boolean; agent always false (Rule 4)
tags: [ ... ]            # required, ≥1
confidence: 0.0–1.0       # required number
raw_sources: [ ... ]     # required for `source` (its raw/clippings file); optional elsewhere
wiki_sources: [ ... ]    # provenance for every non-source page → its source pages (Rule 3)
provenanceState: merged | single | unverified   # optional
# decisions only:
status: active | superseded
supersedes: [ ... ]
# sops only:
tools: [ "[[wikilink]]", ... ]
# source only:
source_url: string
source_type: transcript | paper | report | article | notes
fetched: YYYY-MM-DD
# output only:
query: string
```

> The Obsidian templates in `.obsidian/templates/` match this contract: a number
> for `confidence`, `date`, `raw_sources`/`wiki_sources`, and the type-specific
> fields above. `wiki-lint` checks the required fields and ignores extra ones.

## The relevance filter and the read test

A `wiki/` page may exist only if **both** hold:

- **Read test** — it is something Tom would deliberately open months later. If
  not, the content stays in the substrate or is not written at all.
- **Relevance filter** — it is a current Tom-interest **and** has real
  provenance: a `source` page summarises a raw artifact; every other page is
  backed by ≥ 2 source pages (one only with justification). A wikilink whose
  target is no real page is a "link into the void" and is linted.

## Navigation: no maintained `index.md`

Maintained meta-files (`index`, `hot`, `log`) caused the previous vault's
collapse — every workflow grew an "and update the index" tail. Therefore:

- **No `index.md`.** Navigation uses Obsidian's file explorer plus a single live
  **Dataview** dashboard note (`dashboard.md`), authored once and rendered live.
- **One `log.md` is permitted, append-only.** It is *only ever appended to* and
  never reconciled or summarised by hand. This is the single allowed exception to
  the meta-file ban. The "what changed" history of record remains git.

## Page types

`concept` · `entity` · `source` · `sop` · `decision` · `synthesis` · `output`.
