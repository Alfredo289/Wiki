---
title: "Dashboard"
type: schema
date: 2026-06-10
explored: false
---

# Dashboard

The vault's single live view. Authored once, rendered by Dataview — never
maintained by hand. Replaces `index.md` (see decision `no-index-md-meta-file`).
If a query block shows nothing, the vault is empty, not broken.

## Recently added

```dataview
TABLE type, date, explored
FROM "wiki"
SORT date DESC
LIMIT 15
```

## Needs Tom's gate (unread)

```dataview
LIST
FROM "wiki"
WHERE explored = false
SORT date DESC
```

## Counts by type

```dataview
TABLE length(rows) AS count
FROM "wiki"
GROUP BY type
```

## Single-source pages (review: justify or merge)

```dataview
TABLE raw_sources
FROM "wiki"
WHERE length(raw_sources) = 1
```
