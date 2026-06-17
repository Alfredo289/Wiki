---
title: Dashboard
type: schema
date: 2026-06-10
explored: false
cssclasses:
  - dashboard
  - wide-tables
---

# Dashboard

> [!abstract] What this is
> The vault's single live view. Authored once, rendered by Dataview — never
> maintained by hand. Replaces `index.md` (see [[CONTEXT#Navigation]]).
> If a query block shows nothing, the vault is empty, not broken.

> [!todo]+ Needs Tom's gate
> Unread pages awaiting your review. This is the queue, not an archive.
> ```dataview
> TABLE WITHOUT ID
>   link(file.link, title) AS "Page",
>   type AS "Type",
>   date AS "Added"
> FROM "wiki"
> WHERE explored = false
> SORT date DESC
> ```

## Pulse

```dataviewjs
const pages = dv.pages('"wiki"');
const total = pages.length;
const unread = pages.where(p => p.explored === false).length;
const sources = pages.where(p => p.type === "source").length;
const thin = pages.where(p => p.type !== "source" && p.wiki_sources && p.wiki_sources.length === 1).length;
dv.paragraph(
  `**${total}** pages · **${unread}** awaiting gate · ` +
  `**${sources}** sources · **${thin}** thin-provenance`
);
```

> [!info]- Counts by type
> ```dataview
> TABLE WITHOUT ID type AS "Type", length(rows) AS "Count"
> FROM "wiki"
> GROUP BY type
> SORT length(rows) DESC
> ```

## Recently added

```dataview
TABLE WITHOUT ID
  link(file.link, title) AS "Page",
  type AS "Type",
  date AS "Added",
  choice(explored, "✓", "○") AS "Gated"
FROM "wiki"
SORT date DESC
LIMIT 15
```

## Freshness — what's gone quiet

```dataviewjs
const cutoff = dv.date("today").minus(dv.duration("14 days"));
const stale = dv.pages('"wiki"')
  .where(p => p.date && dv.date(p.date) < cutoff)
  .sort(p => p.date, 'asc')
  .limit(10);
if (stale.length === 0) {
  dv.paragraph("> [!success] Nothing stale — every page touched in the last 14 days.");
} else {
  dv.table(["Page", "Type", "Last touched"],
    stale.map(p => [p.file.link, p.type, p.date]));
}
```

> [!warning]- Thin-provenance pages
> A single source backs these. Add a source or justify the page.
> ```dataview
> TABLE WITHOUT ID link(file.link, title) AS "Page", wiki_sources AS "Source"
> FROM "wiki"
> WHERE type != "source" AND length(wiki_sources) = 1
> SORT date DESC
> ```

## Recent writing sessions

> [!quote] From the log
> The five most recent sessions, read live from `log.md`. The log stays the
> history of record; this only windows onto its tail.

```dataviewjs
const file = app.vault.getAbstractFileByPath("log.md");
const raw = await app.vault.cachedRead(file);
const lines = raw.split("\n")
  .map(l => l.trim())
  .filter(l => /^\d{4}-\d{2}-\d{2}\s+—/.test(l))
  .slice(-5)
  .reverse();
if (lines.length === 0) {
  dv.paragraph("_No sessions logged yet._");
} else {
  dv.table(["Date", "What changed"], lines.map(l => {
    const [date, ...rest] = l.split(" — ");
    return [date, rest.join(" — ")];
  }));
}
```

## Corrections in force

> [!danger]- Standing rules agents must not break
> Pulled from [[learnings]]. Read before any write.
> ![[learnings#Entries]]
