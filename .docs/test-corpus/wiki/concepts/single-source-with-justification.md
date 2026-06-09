---
title: "MCP roots capability"
type: concept
date: 2026-03-25
explored: false
raw_sources:
  - anthropic-mcp-roots-blogpost.md
tags:
  - mcp
  - security
confidence: 0.8
---

# MCP roots capability

A capability in the Model Context Protocol that lets a host advertise filesystem boundaries an MCP server is allowed to touch. Replaces the prior default of "the server sees whatever path the host hands it" with an explicit, server-checkable boundary.

**Tom-relevance (single-source stub justification):** this is directly load-bearing for the vault's MCP servers. The wiki-bound qmd server and the lint MCP both need to declare `~/Documents/Wiki` as their single root and refuse any path outside it. Without roots, a misconfigured host can hand the server arbitrary filesystem paths and the integrity boundary of the vault leaks out at the protocol layer. This is a current implementation concern for Tom's vault tooling, not an abstract interest — it earns its single-source page under the relevance filter's "explicitly Tom-relevant" branch.

Related: [[agentic-loops]] (the loops that consume the protocol), [[obsidian-dataview]] (a sibling read-only view, but Obsidian-bound, not MCP).
