---
title: "Vault one-pager — three-layer model (May 2026)"
type: output
date: 2026-05-25
explored: false
raw_sources:
  - karpathy-llm-wiki-gist.md
  - tom-voice-memo-vault-three-layers.md
tags:
  - onepager
  - share
confidence: 0.85
---

# Vault one-pager — three-layer model

A shareable one-page summary Tom wrote to explain the vault's shape to a colleague. Survives the conversation because the content is reusable — every time someone asks "how do you organise notes with an LLM in the loop?", this is the answer.

## The three layers

- **`raw/`** — every artifact Tom decided was worth keeping. Flat folder. Origin and format in frontmatter. Human-curated, agent-immutable.
- **`wiki/`** — compiled markdown pages the agent writes against `raw/`. Seven page types: concept, entity, source, SOP, decision, output, synthesis.
- **Schema** — the rulebook (CONTEXT.md, AGENTS.md, learnings.md). Loaded first by every agent session.

## Why this shape

LLMs compile well and remember poorly; humans curate well and compile poorly. The architecture matches each side to what it is good at. The validation gate — a single `explored:` boolean per page, only flipped by Tom — keeps the wiki honest.

Companion to [[three-layer-vault]] and [[adopt-three-layer-vault]].
