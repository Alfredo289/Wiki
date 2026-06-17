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
- **Don't write `raw/` on your own.** Tom curates `raw/`. The only agent write is
  the `wiki-capture-triage` skill, and only when Tom invokes it (Integrity Rule 2).
- **`~/Inbox/` is not part of this vault.** Never reference it or route captures
  through it. Captures come from Tom filling `raw/clippings/`, or from
  `wiki-capture-triage` writing a conversation note there.
- **`explored` is always `false` from you** (Integrity Rule 4). No exceptions.
- **Write the vault in English only.** Every `raw/` and `wiki/` file is written in
  English, regardless of the conversation language.
