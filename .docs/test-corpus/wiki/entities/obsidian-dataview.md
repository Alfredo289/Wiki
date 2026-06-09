---
title: "Obsidian Dataview"
type: entity
date: 2026-04-08
explored: false
raw_sources:
  - obsidian-dataview-readme.md
tags:
  - obsidian
  - query
confidence: 0.7
---

# Obsidian Dataview

An Obsidian plugin that exposes a note's YAML frontmatter and inline `field:: value` syntax as a queryable database. Queries render live inside any note via DQL or JavaScript blocks.

Tom-relevance: Dataview is the runtime view layer for the vault's dashboard note — recent pages, counts by type, pages with `explored: false`. It replaces the maintained `index.md` that killed the previous vault. The decision to lean on it is recorded in [[no-index-md-meta-file]].

Caveat that matters operationally: Dataview is read-only and Obsidian-bound. The external CLI (`qmd`) and any wiki-lint tool cannot call Dataview — they need their own parser over the same frontmatter contract. The plugin is a view, not a source of truth.
