# CONTEXT.md — Wiki

This file is loaded first by every agent session working in `~/Documents/Wiki`. It defines the vault's architecture and the vocabulary the agent and Tom share. Operational rules and frontmatter live in `AGENTS.md`; this file is the conceptual ground under it.

## What this vault is

A personal knowledge vault following Andrej Karpathy's three-layer LLM-Wiki model. The vault holds compiled, long-lived domain knowledge — things that stay true after any specific project ends. Project-bound documents live with the project, not here.

## The three layers

1. **Raw sources — `raw/`.** One flat folder containing every curated source artifact: anything Tom decided was worth keeping. No subfolders. Origin (own vs. external) and format (md, pdf, image, audio) are recorded in each file's frontmatter, not in the directory structure. The agent does not edit content after intake.
2. **The wiki — `wiki/`.** Compiled markdown pages the agent writes and maintains by reading `raw/`. Organised into one subfolder per page type: `concepts/`, `entities/`, `sources/`, `sops/`, `decisions/`, `outputs/`, `syntheses/`. Page type is the path; topic is the filename. Tom reads; the agent writes; Tom validates.
3. **The schema.** The rulebook. Loaded first. Co-evolves with the vault. Schema files live at the vault root by definition; `AGENTS.md` enumerates which root-level files belong to the schema. Currently: `CONTEXT.md`, `AGENTS.md`, and `learnings.md` — an append-only log of Tom's decisions on agent proposals surfaced by the wiki-lint maintenance command (e.g. re-typing a page), loaded by the agent only when running wiki-lint, not on every session. New schema files are added only when an integrity rule or downstream tool genuinely requires one (see *Meta-files*). Hidden tooling directories (`.obsidian/`, `.claude/`, `.cursor/`) are tool config, not part of the schema and not part of the conceptual model.

## `raw/` — human-curated, agent-immutable

Two rules govern `raw/`, together:

1. **Tom is the sole curator.** Every artifact in `raw/` enters because Tom decided it was worth keeping. The agent never writes to `raw/` — not via ingest, not via harvest, not via promotion from projects, not via any future skill. Skills may *propose* candidates to Tom (in chat, in a report), but the move into `raw/` is always Tom's hand. This is what makes the validation gate downstream actually mean something: every `wiki/` claim traces back to a human-curated artifact.
2. **Content is immutable after entry.** Filesystem placement (renaming for the slug convention) is allowed. In-file edits are not. If new information arrives on the same topic, it enters as a new `raw/` artifact and the compiled `wiki/` page is updated to reflect both.

Together: `raw/` is the human-curated, agent-immutable substrate. Anything that would erode either rule is a breach of the architecture, not a clever workflow.

## Validation gate

Every `wiki/` page has an `explored` field. The agent always writes `explored: false`. Only Tom flips it to `true`, and only after reading the page and confirming it matches his understanding. Untrusted pages are still useful — they exist, they're linkable, they're searchable — but no downstream wiki page should treat an `explored: false` claim as load-bearing without a human checkpoint.

## The read test

Before creating or substantially expanding a `wiki/` page, the agent applies one test:

> *If Tom opens this page in 6 months — does he want to read it, or is it just agent context that he never looks at again?*

If the honest answer is the second, the content does not become a wiki page. It can stay as an annotation in `raw/`, a section inside a larger page, or nothing at all. The wiki is for Tom, not for the agent's working memory.

## Relevance filter

A `wiki/` page exists only if at least one is true: two or more `raw/` sources touch the topic, **or** the topic is explicitly Tom-relevant (current work, recurring interest, stated curiosity). Single-source mentions become stubs, not pages. The agent never writes `[[wikilinks]]` to pages that do not exist and were not justified by this rule.

## The seven page types

These are the categories the agent uses when compiling `raw/` into `wiki/`. They are kinds-of-page, not topics; a single raw artifact may produce more than one.

- **Concept.** An idea, theory, model, or pattern. Explains *what something is* and *why it matters*. Example: a page on "agentic loops."
- **Entity.** A specific thing in the world — a tool, library, person, organisation, product. Inventory of facts, links, install notes, current state. Example: a page on Raycast.
- **Source.** A summary of one external artifact. One source → one source page. Captures the artifact's argument, its key claims, and Tom's reaction. Example: a page on the Karpathy LLM-Wiki gist.
- **SOP.** A standard operating procedure. A repeatable how-to Tom expects to run again. Example: "How to ingest a YouTube transcript."
- **Decision.** An architectural or policy choice with rationale, alternatives, and consequences. ADR-shaped. Example: this vault's three-layer decision.
- **Output.** A finished artifact a project produced — a published article, a talk's slide deck, a one-pager, a finalised memo — that survives the project's end because its content stays useful. The artifact itself is wiki content; the project that birthed it is not.
- **Synthesis.** The wiki's own answer to a question Tom asked it, drawn across multiple `wiki/` pages. Provenance traces back to other wiki pages rather than to a single `raw/` source. A synthesis is a permanent type, not just a birth state — it may later seed a concept page without being deleted.

## Language

Compiled `wiki/` pages are written in English for shareability and searchability. Tom may write or speak in German; the agent translates on the way in.

## Named frontmatter

Frontmatter is the contract every downstream tool (`wiki-lint`, `wiki-harvest`, qmd queries) depends on. Most fields are operational and live in `AGENTS.md`. The fields named here are load-bearing for the architecture itself — without them, an integrity rule or a page-type definition cannot be enforced or queried. Full schema, defaults, and validation belong in `AGENTS.md`. Templates (one per `raw/` shape, one per `wiki/` page type) are the enforcement mechanism: producing valid frontmatter is the default path, not an act of discipline.

- **`explored:` (every `wiki/` page).** Boolean. The validation gate. Agent always writes `false`; only Tom flips to `true`.
- **`type:` (every `wiki/` page).** One of the seven page types. Path encodes type for humans; this field makes type queryable for tools. Frontmatter follows path — re-typing means both move together.
- **`raw_sources:` (every `wiki/` page).** List of `raw/` artifact filenames the page rests on. Makes the relevance filter ("no wikilinks into the void", "2+ sources or Tom-relevance") auditable. May be empty only for `synthesis` pages (which trace to other `wiki/` pages instead) and for explicitly Tom-relevant single-source stubs.
- **`origin:` and `format:` (every `raw/` artifact).** Origin: own | external. Format: md | pdf | image | audio | …. Replaces the subfolders that flat-`raw/` deliberately removed.
- **`source_url:` (every `source` page).** Live link to the external artifact the page summarises. Required because a source page without a back-link is not auditable as a summary.

## Meta-files

The vault leans on Obsidian's native views (file explorer, search, graph, backlinks, tag pane, Dataview blocks rendered inside a note) and qmd queries for almost all *what's in here?* needs. A standalone meta-file at vault root or in `wiki/` is justified only when no view, query, or pane can produce the same signal — and even then, it is written by an explicit command, never as a side-effect of other operations.

The failure mode this rule exists to prevent: every workflow ends with *"and then update `hot.md`, `index.md`, `log.md`."* That tax is what killed the previous vault. Meta-files exist to give Tom feedback, not to give the agent housekeeping.

Concretely, at vault startup:

- **Dashboard** — a single note with Dataview query blocks (recent pages, counts by type, pages with `explored: false`). Authored once, rendered live by Obsidian. Not maintained.
- **`index.md`** — none. Obsidian's file explorer is the index. Revisit only if scale forces it.
- **`hot.md`** — none. The session-memory and handoff pattern (kept outside the vault) replaces it.
- **`log.md`** — optional, append-only, written only by commands that explicitly choose to log. Never required reading.

## Integrity rules

The architecture rests on these. Any new workflow, skill, or directory proposal must be checked against all of them before being adopted. Implicit rules get violated by clever workflows; named rules don't. Violating any one of them is a breach of the architecture, not a clever workflow — no matter what the proposal does afterward, the integrity is already damaged.

1. **Three layers, no fourth.** Any new directory at vault root must be either schema (named in `AGENTS.md`) or tool config (hidden directory). No fourth conceptual layer.
2. **Tom is the sole curator of `raw/`.** Agents propose; Tom's hand moves the file. No exceptions, no skills, no "convenience writes."
3. **`raw/` content is immutable after entry.** Filesystem placement only; no in-file edits.
4. **`explored: true` is Tom's gate.** The agent never sets it.
5. **The read test is a gate, not a guideline.** Pages that fail it don't get created.
6. **Relevance filter — no wikilinks into the void.** No page exists without two raw sources or explicit Tom-relevance.
7. **English in `wiki/`.** Single-language compiled output.
