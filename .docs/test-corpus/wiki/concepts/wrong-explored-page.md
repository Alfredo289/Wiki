---
title: "Hallucination by accretion"
type: concept
date: 2026-05-08
explored: true
raw_sources:
  - karpathy-llm-wiki-gist.md
  - tom-voice-memo-vault-three-layers.md
tags:
  - llm
  - vault
confidence: 0.75
---

# Hallucination by accretion

The failure mode where an agent-written knowledge base degrades over time as small unverified claims accumulate and start citing each other. Each individual claim looks plausible; the lattice as a whole is unanchored.

The defence is the validation gate — a single explicit human signal per page (the `explored:` boolean) plus mandatory provenance from compiled claims back to raw artifacts. See [[three-layer-vault]] for the structural form.

Note for the test corpus: this page has `explored: true` set by an agent, simulating an Integrity Rule 4 violation. The frontmatter is otherwise valid; the lint should catch the gate breach specifically.
