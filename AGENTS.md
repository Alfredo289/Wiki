# AGENTS.md — Wiki

Operational layer for `~/Documents/Wiki/`. Loaded after
[[CONTEXT.md]] (the conceptual ground). This file owns the
full frontmatter schema, the template list, the command set,
the lint rules, and the conventions. 
Where this file
conflicts with `CONTEXT.md`, 
`CONTEXT.md` wins.

## Schema files

The schema layer lives at vault root. Currently:

- `CONTEXT.md` — conceptual ground, integrity rules, named
  frontmatter, meta-file stance.
- `AGENTS.md` — this file.
- `learnings.md` — append-only log of Tom's decisions on
  agent proposals. Loaded only when `/wiki-lint` runs.
  Format and scope: TBD.

New schema files are added only when an integrity rule or
downstream tool genuinely requires one.

## Frontmatter — full schema

`CONTEXT.md` names the load-bearing fields. This section is
the complete contract.

### Every `wiki/` page (baseline)

| Field             | Type     | Required | Notes                                                                                                                  |
| ----------------- | -------- | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| `title`           | string   | yes      | Human-readable title.                                                                                                  |
| `type`            | enum     | yes      | `concept` \| `entity` \| `source` \| `sop` \| `decision` \| `output` \| `synthesis`. Frontmatter follows path.         |
| `date`            | ISO date | yes      | Creation date.                                                                                                         |
| `explored`        | bool     | yes      | Default `false`. Only Tom flips to `true`.                                                                             |
| `raw_sources`     | list     | yes      | `raw/` filenames the page rests on. May be empty only for `synthesis` and explicitly-Tom-relevant single-source stubs. |
| `tags`            | list     | no       | Free-form topic tags.                                                                                                  |
| `confidence`      | 0.0–1.0  | no       | LLM-reported confidence.                                                                                               |
| `provenanceState` | enum     | no       | `extracted` \| `merged` \| `inferred` \| `ambiguous`.                                                                  |
| `contradictedBy`  | list     | no       | Slugs of `wiki/` pages that conflict with this one.                                                                    |

### Per page type, additional fields

- `source` — `source_url` (string, **required**, live link
  to the external artifact), `source_type` (enum: `article`
  \| `tweet` \| `thread` \| `video` \| `paper` \| `notes` \|
  `skill`), `fetched` (ISO date).
- `sop` — `tools` (list of `[[entity]]` links).
- `decision` — `status` (`active` \| `superseded` \|
  `reverted`), `supersedes` (list), `superseded_by`
  (single).
- `synthesis` — `wiki_sources` (list of `wiki/` page slugs
  the synthesis traces to). Replaces `raw_sources`
  semantically; `raw_sources` may be empty.
- `concept`, `entity`, `output` — baseline only.

### Every `raw/` artifact

| Field        | Type     | Required                  | Notes                                                           |
| ------------ | -------- | ------------------------- | --------------------------------------------------------------- |
| `title`      | string   | yes                       | Human-readable.                                                 |
| `origin`     | enum     | yes                       | `own` \| `external`.                                            |
| `format`     | enum     | yes                       | `md` \| `pdf` \| `image` \| `audio` \| `video` \| `url` \| `…`. |
| `added`      | ISO date | yes                       | Date Tom curated this artifact into `raw/`.                     |
| `source_url` | string   | yes if `origin: external` | Live link.                                                      |

## Templates

Templater + Web Clipper. Templates live in
`.obsidian/templates/`. They are the enforcement mechanism
for the frontmatter contract above.

### `wiki/` templates — one per page type

Seven templates: `wiki-concept.md`, `wiki-entity.md`,
`wiki-source.md`, `wiki-sop.md`, `wiki-decision.md`,
`wiki-output.md`, `wiki-synthesis.md`. Each carries the
baseline frontmatter plus its per-type fields, plus a
minimal body skeleton appropriate to the type.

### `raw/` templates — multiple, one per shape

Set TBD. Working candidates: `raw-youtube`, `raw-paper`,
`raw-article`, `raw-tweet`, `raw-skill`, `raw-own-note`. The
list is itself an integrity claim — adding a template means
_"this is a valid kind of raw artifact."_ Tom signs off on
the final set.

## Commands

Startup set (ship with v1):

- **`/wiki-new-page`** — creates a page from a template.
  Argument: page type. Without this command, the frontmatter
  contract depends on Tom remembering to invoke Templater
  every time.
- **`/wiki-lint`** — health check. See _Lint_ below.

Deferred (named, spec'd later when need arises):

- **`/wiki-harvest`** — end-of-project skill.
  Reasoning-capable model required (Opus or equivalent).
  Reads project artifacts (ADRs, handoffs, filtered git
  history) and queries the wiki via qmd. Outputs a chat-only
  proposal report. No writes to `raw/` or `wiki/`.
  Real-world-testing flag from Q9.3 — needs to be tested
  whether the report gets acted on or becomes silent
  backlog.
- **`/wiki-compile`** — two-phase compile (extract concepts
  → generate pages), atomicstrata-style. Revisit when 50+
  pages exist.

## Lint

`/wiki-lint` is Tom-invoked, never on a schedule. Checks:

1. **Required frontmatter per page type** (see schema
   above).
2. **`raw_sources:` validation** — each listed file exists
   in `raw/`.
3. **`[[wikilink]]` validation** — target exists; flag stubs
   separately from broken links separately from links into
   the void.
4. **Path/type drift** — `type:` frontmatter agrees with
   subfolder path. If not, surface as re-typing proposal.
5. **Orphan check** — pages with no incoming `[[wikilink]]`.
6. **Stale `explored: false`** — pages untouched for N
   months. N: TBD.
7. **Low confidence** — pages with `confidence < threshold`.
   Threshold: TBD.
8. **Contradictions** — pages with non-empty
   `contradictedBy:`.
9. **Domain drift** — pages outside Tech / Tooling / LLM
   scope.
10. **Stub vs. page** — depends on stub definition (Q14,
    TBD).

`/wiki-lint` reads `learnings.md` to avoid re-surfacing
proposals Tom already rejected. Tom's decisions on lint
proposals are appended to `learnings.md`. Output: chat
report; optional `wiki/outputs/lint-report-YYYY-MM-DD.md` (a
legitimate `output` page).

## qmd

`qmd` is the query layer for structured wiki reads —
markdown-as-database. Available as CLI and MCP.
Index-via-query, body-on-demand. No maintained `index.md`.
Used by `/wiki-harvest`, `/wiki-lint`, and any future skill
that needs to read across pages.

## Meta-files

Per `CONTEXT.md`. At startup:

- **Dashboard** — single Dataview note in the vault.
  Authored once, rendered live by Obsidian. Not maintained.
- **`index.md`** — none. Obsidian file explorer is the
  index.
- **`hot.md`** — none. Replaced by session memory and the
  handoff pattern (kept outside the vault).
- **`log.md`** — open question. Format and trigger TBD.

## Naming and conventions

- **Filenames**: kebab-case, lowercase. CamelCase brand
  names get split (`BetterTouchTool` →
  `better-touch-tool.md`). Acronyms preserved (`MCP` →
  `mcp.md`).
- **Wiki slugs**: `<topic>.md` for concepts/entities, free
  per Tom's judgment for
  sources/SOPs/decisions/outputs/syntheses.
- **Body prose**: official brand spelling
  ("BetterTouchTool", "Keyboard Maestro"). Only the slug is
  kebab-case.
- **Language**: English in `wiki/`. Tom may write or speak
  German; the agent translates on the way in.
- **HEX colors in inline code**: `` `#4080F2` ``, never raw,
  to avoid Obsidian's `#` tag-parser.
- **Code snippets**: triple-backtick blocks with syntax  highlighting

## Integrity rules — operational reminder

Per `CONTEXT.md`. Re-stated here for the agent's convenience
when running commands:

1. Three layers, no fourth.
2. Tom is the sole curator of `raw/`.
3. `raw/` content is immutable after entry.
4. `explored: true` is Tom's gate.
5. The read test is a gate.
6. Relevance filter — no wikilinks into the void.
7. English in `wiki/`.

Any command, skill, or workflow proposal must be checked
against all seven before adoption.
