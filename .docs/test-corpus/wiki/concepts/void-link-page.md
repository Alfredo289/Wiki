---
title: "Prompt caching"
type: concept
date: 2026-05-19
explored: false
raw_sources:
  - karpathy-talk-llm-os-recording.md
  - mcp-spec-snapshot-2026-03.md
tags:
  - llm
  - performance
confidence: 0.65
---

# Prompt caching

A provider-side optimisation where stable prefixes of a prompt (system message, large tool definitions, retrieved documents) are cached across requests so the model does not re-process them token-by-token. Brings latency and cost down for any agent loop with a stable scaffold and a changing tail.

For Tom's vault: the schema files (`CONTEXT.md`, `AGENTS.md`) are exactly the kind of stable prefix that benefits from caching when an agent session does many small operations.

Related: [[zukunfts-konzept]] (a target that does not exist and was not justified by the relevance filter — a deliberate void link for the test corpus). The link target is neither a current Tom-interest nor backed by two raw sources; it should be flagged as a wikilink into the void.
