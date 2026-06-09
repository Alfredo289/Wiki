---
title: "Use kebab-case for all wiki slugs"
type: decision
date: 2026-04-12
explored: false
raw_sources:
  - karpathy-llm-wiki-gist.md
  - obsidian-dataview-readme.md
tags:
  - convention
  - naming
confidence: 0.85
---

# Use kebab-case for all wiki slugs

## Context

Filenames are the public identifiers of `wiki/` pages — they appear in wikilinks, in Dataview tables, in qmd output. A single naming convention removes friction at every read and write.

## Decision

All wiki slugs are kebab-case, lowercase. CamelCase brand names get split (`BetterTouchTool` → `better-touch-tool.md`). Acronyms preserved (`MCP` → `mcp.md`). Body prose still uses official brand spelling — only the slug is normalised.

## Alternatives considered

- **snake_case.** Rejected: visually heavier in wikilinks.
- **Free-form titles as filenames.** Rejected: collides with shell autocompletion and breaks portable slugs in URLs.

## Consequences

Renaming a page is a slug-normalisation step, not a content edit. Wikilinks and `raw_sources:` references must be updated together.

Note for the test corpus: this decision page deliberately omits the `status:` field. The lint's per-type required-frontmatter check should flag the missing field for a `decision` page.
