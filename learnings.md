---
title: "learnings — accumulated corrections for agents"
type: schema
date: 2026-06-10
explored: false
---

# learnings.md

Append-only list of corrections an agent must not repeat. Loaded **second**,
after `CONTEXT.md` and before `AGENTS.md`. Keep each entry one or two lines:
the mistake, then the rule that replaces it. Never delete entries; supersede them.

## Entries

- **Don't invent `confidence`.** If you cannot justify a number, write `0.5` and
  say so in the body — never guess high.
- **Don't resolve a wikilink you haven't checked.** Every `[[link]]` must point at
  a real page slug or a real page title; otherwise leave it as plain text.
- **Don't touch `raw/`.** Propose a slug + frontmatter; stop. The move is Tom's
  (Integrity Rule 2).
- **`explored` is always `false` from you** (Integrity Rule 4). No exceptions.
