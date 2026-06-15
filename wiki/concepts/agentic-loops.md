---
title: "Agentic loops"
type: concept
date: 2026-05-15
explored: false
raw_sources:
  - karpathy-talk-llm-os-recording.md
  - karpathy-llm-wiki-gist.md
tags:
  - llm
  - agents
confidence: 0.7
provenanceState: extracted
---

# Agentic loops

An agentic loop is an LLM-driven process that plans, acts, observes, and replans across multiple turns without a human in each cycle. The defining property is autonomy of step selection — the model picks the next tool call, not a script.

The pattern only earns its keep when paired with a curator. Without one, the loop drifts: the model keeps producing plausible next steps long after the original task stopped mattering. Karpathy's framing in the LLM-OS talk fits here — the loop is the worker, the human is the curator, and the [[three-layer-vault]] makes that split structural rather than aspirational.

For Tom's vault, the relevant question is which loops are allowed to write where. Skills may *propose* candidates for `raw/`, but the move into `raw/` is always Tom's hand — see Integrity Rule 2. The agentic loop becomes a proposal engine, not a writer.
