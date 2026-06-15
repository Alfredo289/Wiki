---
title: "CONTEXT — conceptual ground for the vault"
type: schema
date: 2026-06-10
explored: false
---

# CONTEXT.md

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
| **Substrate** | `raw/` | Tom only | Immutable once filed |
| **Compiled wiki** | `wiki/` | Agent, validated by Tom | Rewritable |
| **Schema** | `CONTEXT.md`, `AGENTS.md`, `learnings.md` | Tom (+ agent proposals) | Versioned |

`raw/` is a **flat** folder of curated artifacts. Origin and format live in
frontmatter, **not** in subfolders. `wiki/` is organised into type subfolders
(`concepts/`, `entities/`, `sources/`, `sops/`, `decisions/`, `syntheses/`,
`outputs/`).

## Integrity Rules

1. **Three layers, no fourth.** No new top-level layer; no subfolders inside
   `raw/`. Operational drop-zones for capture tools live *outside* the vault
   (`~/Inbox/`), never as a fourth layer.
2. **Only Tom writes `raw/`.** Agents may *propose* captures, slugs and
   frontmatter, but only Tom moves a file into `raw/`. The proposer/curator
   split is structural, not a guideline.
3. **No claim without provenance.** Provenance is non-negotiable. Every `wiki/`
   page traces back to named artifacts: substrate-derived pages (`concept`,
   `entity`, `source`, `sop`) cite `raw_sources`; syntheses and outputs cite
   `wiki_sources` **and/or** `raw_sources`. The ideal is **≥ 2** `raw_sources`; a
   single source is allowed only with an explicit relevance justification in the
   body. A page with no provenance is a defect. *(Exact rule-3 wording is
   reconstructed from the source notes — confirm before treating as canonical.)*
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
raw_sources: [ ... ]     # required for concept|entity|source|sop (ideally ≥2, Rule 3)
wiki_sources: [ ... ]    # for synthesis|output (which use wiki_sources and/or raw_sources)
provenanceState: merged | single | unverified   # optional
# decisions only:
status: active | superseded
supersedes: [ ... ]
# sops only:
tools: [ "[[wikilink]]", ... ]
```

> Note: the Obsidian templates in `.obsidian/templates/` currently drift from
> this contract (`confidence: medium` as a string, `date_created`/`date_modified`,
> `sources`, `tldr`). The templates must be reconciled to this contract — see the
> implementation plan.

## The relevance filter and the read test

A `wiki/` page may exist only if **both** hold:

- **Read test** — it is something Tom would deliberately open months later. If
  not, the content stays in the substrate or is not written at all.
- **Relevance filter** — it is a current Tom-interest **and** backed by ≥ 2 raw
  artifacts (or composed from existing wiki pages). A wikilink whose target is
  neither is a "link into the void" and is linted.

## Navigation: no maintained `index.md`

Maintained meta-files (`index`, `hot`, `log`) caused the previous vault's
collapse — every workflow grew an "and update the index" tail. Therefore:

- **No `index.md`.** Navigation uses Obsidian's file explorer plus a single live
  **Dataview** dashboard note (`dashboard.md`), authored once and rendered live.
- **One `log.md` is permitted, append-only.** It is *only ever appended to* and
  never reconciled or summarised by hand. This is the single allowed exception to
  the meta-file ban; it must be encoded as a decision page when `wiki/decisions/`
  is built. The "what changed" history of record remains git.

## Page types

`concept` · `entity` · `source` · `sop` · `decision` · `synthesis` · `output`.
