---
title: "Obsidian Dataview plugin — README excerpt"
origin: external
format: md
added: 2026-04-03
source_url: https://github.com/blacksmithgu/obsidian-dataview
---

Dataview turns Obsidian notes into a queryable database. Each note's YAML frontmatter and inline `field:: value` syntax become indexed metadata. Queries are written in a DQL dialect or as JavaScript blocks rendered inline in any note.

Common pattern in personal vaults: a single dashboard note containing several query blocks — recent pages, pages by tag, pages missing required frontmatter — rendered live by Obsidian instead of maintained by hand. This replaces the "index.md" tax that kills most personal wikis. The query layer is the index; the file explorer is the navigation.

Caveat: Dataview is a runtime view, not a write layer. If a downstream tool needs the same answer (lint, harvest, external CLI), it cannot call Dataview — it needs its own parser over the same frontmatter.
