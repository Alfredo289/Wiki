---
title: "Model Context Protocol — Specification snapshot, March 2026"
origin: external
format: pdf
added: 2026-03-18
source_url: https://modelcontextprotocol.io/spec
---

PDF companion stub. The artifact is the .pdf next to this file; this note captures the metadata.

The March 2026 spec consolidates the three transport modes (stdio, SSE, streamable HTTP) and pins the JSON-RPC 2.0 envelope. Resources, tools, and prompts remain the three primitive object types. New in this revision: a `roots` capability that lets a host advertise the filesystem boundaries an MCP server is allowed to touch — relevant for any vault-bound server (qmd, wiki-lint).

Notable for Tom: the spec is now explicit that tool descriptions are part of the prompt surface area and should be treated as untrusted input by the host model. This shifts some of the prompt-injection burden from server authors to host implementers.
