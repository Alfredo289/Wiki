---
title: "Capture an artifact to ~/Inbox"
type: sop
date: 2026-06-01
explored: false
raw_sources:
  - tom-keyboard-maestro-macro-export.md
  - raycast-screenshot-window-tile.md
tools:
  - "[[raycast]]"
  - "[[keyboard-maestro]]"
tags:
  - capture
  - workflow
confidence: 0.8
---

# Capture an artifact to `~/Inbox`

The capture step that precedes any move into `raw/`. The SOP deliberately stops at `~/Inbox/` — Integrity Rule 2 requires the move into the vault to be Tom's own deliberate action.

## When to run

Whenever a URL, selection, screenshot, or voice memo crosses the "worth keeping" threshold. The bar is intentionally low at this stage; triage happens later.

## Steps

1. **URL or selected text** — trigger the [[raycast]] script command "Capture to Inbox". It saves a timestamped `.md` stub under `~/Inbox/` with `source_url` pre-filled.
2. **Screenshot of frontmost window** — trigger the [[keyboard-maestro]] macro `⌃⌥⌘S`. It writes a `.png` plus a sibling `.md` companion carrying `origin: own`, `format: image`, `added: <today>`.
3. **Voice memo** — record into the macOS Voice Memos app, then drop the `.m4a` into `~/Inbox/`. Whisper-transcribe locally before triage.

## After capture

Nothing is in the vault yet. Triage during the next session: rename to the kebab-case slug, fill any missing frontmatter, then move into `raw/` by hand. Skills may suggest candidates, but only Tom moves files.
