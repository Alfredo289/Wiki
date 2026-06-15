---
name: capture-triage
description: >
  Turn an item sitting in ~/Inbox into a proposed kebab-case slug and complete
  raw/ frontmatter for Tom to file. Use when triaging captures. Proposes only —
  never moves or writes files into raw/ (Integrity Rule 2).
---

# capture-triage

You prepare a capture for filing. You do **not** file it. The move into `raw/`
is Tom's hand (Integrity Rule 2).

## Steps

1. Read the inbox item (text, transcript, image companion `.md`, etc.).
2. Propose a **kebab-case** slug (lowercase, hyphens; acronyms kept; brands split,
   e.g. `BetterTouchTool` → `better-touch-tool`).
3. Produce a ready-to-paste `raw/` frontmatter block:

   ```yaml
   ---
   title: "<concise title>"
   origin: own | external
   format: md | image | audio | video | pdf
   added: <YYYY-MM-DD>
   source_url: "<url if origin: external>"
   ---
   ```
4. State plainly: *"Move `<slug>.<ext>` into `raw/` yourself — I won't."*

## Never

- Write to `raw/`. Move files. Set `explored`. Invent a `source_url`.
