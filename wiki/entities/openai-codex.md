---
title: "OpenAI Codex"
type: entity
date: 2026-06-15
explored: false
tags: [codex, openai, coding-agent]
confidence: 0.8
wiki_sources: ["codex-plugin-build-docs"]
---

# OpenAI Codex

OpenAI's cloud-hosted coding agent. Runs sandboxed coding tasks asynchronously; extensible via plugins that bundle skills, MCP servers, lifecycle hooks, and app integrations. Tom uses Codex actively.

## Current state

- Plugin system available: create via `@plugin-creator` skill or manual scaffold
- Distribution via JSON marketplace catalogs — repo-scoped, personal, or workspace-shared
- MCP servers bundleable inside plugins; user controls per-plugin policy via `config.toml`
- Official public Plugin Directory announced as coming soon

## Tom-relevance

Tom uses Codex as a primary coding agent. The `.agents/` directory convention (`$REPO_ROOT/.agents/plugins/marketplace.json`) is an emerging industry standard that Codex follows. Writing and distributing Codex plugins is how Tom packages reusable workflows.

See [[codex-plugin-authoring]] for the how-to guide.

## Related

- [[codex-plugin-authoring]] — how to create and distribute Codex plugins
