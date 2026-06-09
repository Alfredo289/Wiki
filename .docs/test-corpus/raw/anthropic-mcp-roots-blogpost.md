---
title: "Anthropic blog — MCP roots and the boundary problem"
origin: external
format: url
added: 2026-03-22
source_url: https://www.anthropic.com/news/mcp-roots
---

Short post from Anthropic walking through the motivation for the `roots` capability added to MCP. The framing: an MCP server (filesystem, qmd, vault-lint) shouldn't be trusted with the entire user disk just because it needs *some* of it. Roots let the host declare which directories the server may touch.

For Tom's vault, the relevant beat is that a wiki-bound MCP server can declare `~/Documents/Wiki` as its single root and refuse anything outside it — without the host needing to police each call.

The post also flags that roots are advisory until enforced by the host runtime. Servers should still defensively validate paths.
