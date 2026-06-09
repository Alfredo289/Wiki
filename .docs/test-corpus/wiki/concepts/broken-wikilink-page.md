---
title: "Context engineering"
type: concept
date: 2026-05-18
explored: false
raw_sources:
  - karpathy-talk-llm-os-recording.md
  - anthropic-mcp-roots-blogpost.md
tags:
  - llm
  - context
confidence: 0.6
---

# Context engineering

The discipline of choosing what an LLM sees on a given turn — prompts, retrieved snippets, tool outputs, prior turns — and what it does not. The framing replaces "prompt engineering" once the system holds enough state that selecting context is the dominant lever.

Adjacent to [[agentic-loops]] (which depend on context selection between steps) and [[nicht-existent]] (a deliberate broken wikilink target for the test corpus).

The relevant constraint for Tom's vault is the MCP roots capability — see the related raw artifact. A wiki-bound MCP server with roots set to `~/Documents/Wiki` controls exactly what enters the context window from the vault.
