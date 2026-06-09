---
title: "Three-layer vault"
type: concept
date: 2026-05-15
explored: false
raw_sources:
  - karpathy-llm-wiki-gist.md
  - tom-voice-memo-vault-three-layers.md
  - karpathy-talk-llm-os-recording.md
tags:
  - vault
  - architecture
confidence: 0.85
provenanceState: merged
---

# Three-layer vault

A personal knowledge vault organised as three explicit layers: a raw substrate of human-curated artifacts, a compiled wiki layer written by an agent against the substrate, and a schema layer that holds the rules both depend on.

The split is what makes provenance auditable. Every claim in the wiki traces back to a named artifact in `raw/`; every rule the agent obeys is stated in the schema. Removing any layer collapses the architecture into the "single notes folder" that erodes over time.

The model originates with Karpathy's [[karpathy-llm-wiki-gist]] notes and was adopted in this vault via [[adopt-three-layer-vault]]. It is operationally tied to [[agentic-loops]] — the loop writes the wiki, the human curates raw, the schema disciplines both.
