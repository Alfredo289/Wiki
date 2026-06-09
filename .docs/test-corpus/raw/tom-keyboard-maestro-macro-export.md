---
title: "Keyboard Maestro — macro export for the 'capture to raw' palette"
origin: own
format: md
added: 2026-05-30
---

Export of the Keyboard Maestro group Tom uses to drop the macOS share-sheet target into a single hotkey palette. Three macros: capture URL, capture selected text, capture frontmost-window screenshot. All three land the artifact under `~/Inbox/` for Tom to triage by hand before any move into `raw/`.

The macros deliberately stop at `~/Inbox/`. None of them write to the vault directly — Integrity Rule 2 ("Tom is the sole curator of raw/") means the move must be a deliberate, human-initiated step.
