---
title: "Tree-of-thoughts reasoning"
type: concept
date: 2026-05-06
explored: false
raw_sources:
  - karpathy-talk-llm-os-recording.md
tags:
  - llm
  - reasoning
confidence: 0.55
---

# Tree-of-thoughts reasoning

A prompting pattern that asks the model to explore multiple branches of reasoning at each step and select the most promising one before continuing. Generalises chain-of-thought from a single linear trace to a search over partial reasoning trees.

The technique appears briefly in the Karpathy LLM-OS talk recording. Tradeoffs against simpler chain-of-thought: more tokens per answer, sometimes more brittle when the branching factor outruns the model's evaluation ability.

This page rests on a single raw source and the body contains no Tom-relevance hook — not a current interest, not tied to vault work, not a stated recurring topic. The relevance filter should flag it: with only one raw source and no justification, this should be a stub or a section in a larger page, not its own wiki page.
