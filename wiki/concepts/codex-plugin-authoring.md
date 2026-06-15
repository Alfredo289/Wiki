---
title: "Codex plugin authoring"
type: concept
date: 2026-06-15
explored: false
tags: [codex, plugins, agent-tooling, reference]
confidence: 0.8
wiki_sources: ["codex-plugin-build-docs"]
provenanceState: single
---

# Codex plugin authoring

How to create, package, and distribute plugins for [[openai-codex]]. A plugin bundles skills, MCP servers, lifecycle hooks, and app integrations into a single installable unit distributed via JSON marketplace catalogs.

*Single-source provenance — justified because this is an official reference guide Tom keeps for active use.*

## Key ideas

### Plugin structure

```
my-plugin/
  .codex-plugin/
    plugin.json       ← manifest (only thing in here)
  skills/             ← SKILL.md files
  hooks/
    hooks.json        ← lifecycle hooks
  .mcp.json           ← MCP server definitions
  .app.json           ← app/connector integrations
  assets/             ← icons, screenshots
```

### Fastest path: `@plugin-creator`

Ask `@plugin-creator` in Codex. It scaffolds `plugin.json` and generates a local marketplace entry for testing.

### Minimal manifest

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "What it does",
  "skills": "./skills/"
}
```

Use kebab-case for `name` — it's the plugin identifier and component namespace.

### Marketplace distribution

| Scope | Path |
|---|---|
| Repo | `$REPO_ROOT/.agents/plugins/marketplace.json` |
| Personal | `~/.agents/plugins/marketplace.json` |
| Legacy compat | `$REPO_ROOT/.claude-plugin/marketplace.json` |

Add via CLI instead of editing `config.toml` by hand:

```bash
codex plugin marketplace add owner/repo
codex plugin marketplace add owner/repo --ref main
codex plugin marketplace add ./local-marketplace-root
codex plugin marketplace add https://github.com/example/plugins.git --sparse .agents/plugins
```

Manage marketplaces:

```bash
codex plugin marketplace list
codex plugin marketplace upgrade [name]
codex plugin marketplace remove name
```

### Marketplace JSON format

```json
{
  "name": "my-marketplace",
  "interface": { "displayName": "My Plugins" },
  "plugins": [
    {
      "name": "my-plugin",
      "source": { "source": "local", "path": "./plugins/my-plugin" },
      "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
      "category": "Productivity"
    }
  ]
}
```

- `source.path` is relative to marketplace root, must start with `./`
- `policy.installation` values: `AVAILABLE`, `INSTALLED_BY_DEFAULT`, `NOT_AVAILABLE`
- For Git-backed plugins: use `"source": "url"` (repo root) or `"source": "git-subdir"` (subdirectory) with `url`, `path`, `ref`

Install cache lands at `~/.codex/plugins/cache/$MARKETPLACE/$PLUGIN/$VERSION/` (local = version `local`).

### MCP server bundling

Point `mcpServers` in manifest at `.mcp.json`:

```json
{ "docs": { "command": "docs-mcp", "args": ["--stdio"] } }
```

User overrides per-plugin MCP policy in `config.toml`:

```toml
[plugins."my-plugin".mcp_servers.docs]
enabled = true
default_tools_approval_mode = "prompt"
enabled_tools = ["search"]
```

### Lifecycle hooks

Default hook file: `hooks/hooks.json`. Or point `hooks` in manifest at one or more paths / inline objects.

**Hooks are untrusted by default.** Codex skips plugin-bundled hooks until user reviews and trusts the current definition.

Hook commands receive: `PLUGIN_ROOT`, `PLUGIN_DATA` (and `CLAUDE_PLUGIN_ROOT`, `CLAUDE_PLUGIN_DATA` for compatibility).

```json
{
  "hooks": {
    "SessionStart": [
      { "hooks": [{ "type": "command", "command": "python3 ${PLUGIN_ROOT}/hooks/session_start.py" }] }
    ]
  }
}
```

### Local install workflow (repo)

```bash
mkdir -p ./plugins
cp -R /path/to/my-plugin ./plugins/my-plugin
# add entry to $REPO_ROOT/.agents/plugins/marketplace.json
# restart Codex
```

### Workspace sharing

From Codex app → Plugins → Created by you → Share. Stays within workspace/org boundary. Admins disable via `requirements.toml`:

```toml
features.plugin_sharing = false
```

## How it connects

- [[openai-codex]] — the platform these plugins extend
- [[codex-plugin-build-docs]] — source page (official docs)
- MCP server bundling inside plugins mirrors how Claude Code uses `.mcp.json` at repo root — same convention, different scope

## Counter-arguments

- No public Plugin Directory yet — all distribution is repo/personal/workspace
- Hook trust gate adds friction; hooks-heavy plugins require extra user action
- Restart required after local plugin changes (no hot-reload)

## Data gaps

- Plugin versioning lifecycle (semver enforcement, update behavior with `--ref`)
- Auth flow for `.app.json` integrations
