---
title: "Vault architecture — overview synthesis"
type: synthesis
date: 2026-06-02
explored: false
raw_sources: []
wiki_sources:
  - three-layer-vault
  - agentic-loops
  - adopt-three-layer-vault
  - no-index-md-meta-file
  - karpathy-llm-wiki-gist
  - capture-to-inbox
  - raycast
  - obsidian-dataview
tags:
  - synthesis
  - architecture
confidence: 0.8
provenanceState: merged
---

# Vault architecture — overview synthesis

A synthesis page drawing across the architecture material the vault has accumulated. Provenance traces to other `wiki/` pages, not to `raw/`.

## The shape

The vault is a [[three-layer-vault]]: an immutable curated substrate (`raw/`), a compiled wiki the agent writes (`wiki/`), and a schema layer that holds the rules. The shape comes from [[karpathy-llm-wiki-gist]] and was formally adopted in [[adopt-three-layer-vault]].

## The disciplines

Two disciplines hold the architecture together:

- **Curation discipline** — Tom is the sole curator of `raw/`. The capture pipeline ([[capture-to-inbox]], using [[raycast]] and [[keyboard-maestro]]) deliberately stops at `~/Inbox/`. Skills propose; only Tom moves files.
- **Compilation discipline** — the agent writes `wiki/` pages that pass the read test and the relevance filter, and ships them with `explored: false`. Tom flips the boolean only after reading.

## The view layer

[[obsidian-dataview]] renders the dashboard live. No maintained `index.md` (see [[no-index-md-meta-file]]). Tools that cannot call Dataview parse the frontmatter contract directly.

## The loop

[[agentic-loops]] are allowed as proposal engines, never as writers into `raw/`. The split between proposer and curator is the structural form of Integrity Rule 2.
