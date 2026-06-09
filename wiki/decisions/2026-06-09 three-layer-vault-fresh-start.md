---
title: Three-layer vault, fresh start
type: decision
status: active
date: 2026-06-09
explored: false
raw_sources: []
---

# Three-layer vault, fresh start

## Context

A previous personal knowledge vault (`~/Documents/Tech/`, here called the *old vault*) carried a 422-line `CLAUDE.md` that encoded multi-phase workflows for ingest, save, lint, compile and more. Every operation ended in *"and then update `hot.md`, `index.md`, `log.md`."* The result was friction on every action and no compounding value: small inputs were impossible without ceremony. The vault was abandoned.

Two parallel implementations were reviewed during planning: `green-dalii/obsidian-llm-wiki` (fully automated, no curation gate, schema inside `wiki/`) and `atomicstrata/llm-wiki-compiler` (CLI + MCP, two-phase compile, candidate review queue, epistemic frontmatter). Neither was adopted; both informed the design negatively or as reference.

## Decision

Build a fresh vault at `~/Documents/Wiki/` following Andrej Karpathy's three-layer LLM-Wiki model, hardened by named integrity rules and a thin schema layer:

1. **`raw/`** — flat folder. Human-curated. Agent-immutable.
2. **`wiki/`** — compiled markdown pages in subfolders per page type (`concepts/`, `entities/`, `sources/`, `sops/`, `decisions/`, `outputs/`, `syntheses/`). Type is path; topic is filename.
3. **Schema** — root-level files (`CONTEXT.md`, `AGENTS.md`, `learnings.md`). Enumerated by `AGENTS.md`. Hidden tooling dirs (`.obsidian/`, `.claude/`) are tool config, not schema.

The schema layer is governed by seven named integrity rules (three layers / Tom sole curator of `raw/` / `raw/` immutable / `explored:` gate / read test / relevance filter / English in `wiki/`). Any new workflow, skill or directory proposal is checked against all seven before adoption.

The compiled layer carries optional epistemic metadata (`confidence: 0.0–1.0`, `provenanceState`, `contradictedBy`) lifted from `atomicstrata/llm-wiki-compiler`. Validation is human-only: the agent always writes `explored: false`; only Tom flips to `true`.

No agent-maintained meta-files at startup. Obsidian's native views (file explorer, search, graph, backlinks, tags, Dataview-in-note) and qmd queries cover almost all *what's in here?* needs. A standalone meta-file is justified only when no view or query produces the same signal, and even then it is written by an explicit command, never as a side-effect.

## Alternatives considered

- **Continue the old `Tech/` vault.** Rejected — operationally too expensive, mandatory meta-file updates on every action, multi-page composition meta-grammars stacked on top of page types.
- **Adopt `green-dalii/obsidian-llm-wiki`.** Rejected — auto-ingest writes to `sources/` without a curation gate, no validation gate on output, schema lives inside `wiki/`. Violates Integrity Rules 2, 4 and 1.
- **Adopt `atomicstrata/llm-wiki-compiler`.** Rejected as a dependency — its candidate-review-queue trust model is structurally different from the `explored:` gate (cleaner wiki, bigger backlog problem, untrusted pages hidden from Obsidian search). Kept as a reference for two-phase compile patterns, epistemic metadata and prompt-budget defence.
- **Promote project files into the wiki.** Rejected — project files stay in projects. End-of-project knowledge extraction handled by a future `wiki-harvest` skill that emits a chat-only proposal report; the move into `raw/` remains Tom's hand.

## Consequences

- Curation is the bottleneck by design. Throughput is lower than an auto-ingest setup; trust per page is higher.
- The seven page types compose freely. No prescribed multi-page composition rules (e.g. *"a skill file becomes entity + concept + SOPs"*).
- `index.md` and `hot.md` are not maintained at startup. The dashboard is a single Dataview note, authored once, rendered live.
- The `explored:` gate creates a population of untrusted-but-present pages in Obsidian search and graph. Downstream consumers (qmd queries, `wiki-lint`, future skills) must respect the flag.
- Templates (Templater + Web Clipper, `.obsidian/templates/`) are the enforcement mechanism for the frontmatter contract. Multiple `raw/` templates (one per shape) and seven `wiki/` templates (one per page type).
- The overhead budget is watched: the old vault's 422-line schema is the cautionary baseline. `CONTEXT.md` ended planning at ~90 lines; `AGENTS.md` targets <150.
