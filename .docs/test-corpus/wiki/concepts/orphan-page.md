---
title: "Retrieval-augmented generation"
type: concept
date: 2026-04-17
explored: false
raw_sources:
  - karpathy-talk-llm-os-recording.md
  - obsidian-dataview-readme.md
tags:
  - llm
  - retrieval
confidence: 0.7
---

# Retrieval-augmented generation

A pattern that pairs an LLM with a retrieval step over a document store. The model's answer is conditioned on retrieved passages rather than on parametric memory alone. Lower hallucination rate when the store is well-curated; higher latency.

For Tom's vault, RAG is the read-time companion to the write-time three-layer split: the agent reads `raw/` and the compiled `wiki/`, retrieves relevant pages by frontmatter and wikilinks, and answers conditioned on what it found.

This page is deliberately not linked from any other page in the test corpus — orphan check should flag it.
