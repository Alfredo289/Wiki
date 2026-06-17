---
title: Build plugins – Codex
type: source
date: 2026-06-15
explored: true
tags:
  - codex
  - openai
  - plugins
  - agent-tooling
confidence: 0.8
raw_sources:
  - Build plugins – Codex.md
source_url: https://developers.openai.com/codex/plugins/build
source_type: article
fetched: 2026-06-15
---

# Build plugins – Codex

## Argument

Codex plugins are the primary unit of workflow distribution — they bundle skills, MCP servers, lifecycle hooks, and app integrations into a single installable package. The marketplace JSON catalog is the distribution layer, supporting repo-scoped, personal, and eventually public sources. The hooks trust model (untrusted by default) reflects a deliberate security boundary.

## Key claims

- **Plugin structure:** `.codex-plugin/plugin.json` manifest; `skills/`, `hooks/`, `.mcp.json`, `.app.json` sit at the plugin root (not inside `.codex-plugin/`)
- **Marketplace paths:** repo at `$REPO_ROOT/.agents/plugins/marketplace.json`; personal at `~/.agents/plugins/marketplace.json`
- **Install cache:** `~/.codex/plugins/cache/$MARKETPLACE/$PLUGIN/$VERSION/`; local plugins use version `local`
- **Fastest scaffold:** `@plugin-creator` built-in skill generates manifest + local marketplace entry
- **MCP bundling:** plugin's `.mcp.json` adds servers; user overrides per-plugin MCP policy in `config.toml` under `plugins.<plugin>.mcp_servers.<server>`
- **Hooks untrusted by default:** Codex skips plugin-bundled hooks until user reviews and trusts the current definition
- **Hook env vars:** `PLUGIN_ROOT`, `PLUGIN_DATA` (also `CLAUDE_PLUGIN_ROOT`, `CLAUDE_PLUGIN_DATA` for compatibility)
- **Marketplace sources:** GitHub shorthand (`owner/repo`), HTTP/SSH Git URLs, or local paths; `--ref` pins Git ref; `--sparse PATH` for subdirectory checkout
- **Workspace sharing:** local plugins shareable within ChatGPT workspace (not public); admins can disable via `features.plugin_sharing = false` in `requirements.toml`
- **Official public Plugin Directory:** coming soon — no self-serve publishing yet

## Counter-arguments

- No public registry yet — distribution limited to repo/personal marketplaces or workspace sharing
- Local plugin install requires Codex restart after changes; no hot-reload
- Plugin hooks need explicit user trust review, adding friction for hook-heavy plugins

## Data gaps

- Plugin versioning lifecycle beyond the `version` string in manifest
- Auth flow details for `.app.json` integrations
- Whether Git ref pinning (`--ref`) governs update behavior on `marketplace upgrade`
