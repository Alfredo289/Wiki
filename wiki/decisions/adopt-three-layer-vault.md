---
title: "Adopt the three-layer vault architecture"
type: decision
date: 2026-04-30
explored: false
raw_sources:
  - karpathy-llm-wiki-gist.md
  - tom-voice-memo-vault-three-layers.md
status: active
tags:
  - architecture
  - adr
confidence: 0.9
---

# Adopt the three-layer vault architecture

## Status

Active.

## Context

The previous vault collapsed under meta-file tax — every workflow ended with "and now update `index.md`, `hot.md`, `log.md`". Reads stayed shallow; writes got duplicated. The vault stopped earning Tom's time.

## Decision

Adopt the [[three-layer-vault]] model from Karpathy's [[karpathy-llm-wiki-gist]]: `raw/` as immutable, human-curated substrate; `wiki/` as compiled output written by the agent and validated by Tom; schema files (CONTEXT.md, AGENTS.md, learnings.md) as the rulebook.

## Alternatives considered

- **Flat notes folder, no agent involvement.** Rejected: this is what failed last time.
- **Single-layer agent-managed vault.** Rejected: erases the validation gate. No way to tell which claims Tom has read.
- **Project-local knowledge, no central vault.** Rejected: domain knowledge that survives projects has nowhere to live.

## Consequences

- The `explored:` field becomes load-bearing — without Tom flipping it, no downstream tool can treat a page as trusted.
- Meta-files are banned by default. The dashboard becomes a Dataview note (see [[no-index-md-meta-file]]).
- Agent autonomy in `raw/` is forbidden by Integrity Rule 2. Skills may propose; only Tom writes.
