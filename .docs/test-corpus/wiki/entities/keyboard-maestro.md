---
title: "Keyboard Maestro"
type: entity
date: 2026-05-31
explored: false
raw_sources:
  - tom-keyboard-maestro-macro-export.md
tags:
  - macos
  - automation
confidence: 0.75
---

# Keyboard Maestro

A macOS automation tool centred on hotkey-triggered macros. Strong at text expansion, conditional palettes, and gluing together GUI apps that lack scripting interfaces. Cohabits with [[raycast]] in Tom's setup — Raycast for launch, Keyboard Maestro for macros with branching logic.

Tom-relevance is explicit and current: the "capture to inbox" palette that feeds the vault is built in Keyboard Maestro (see the export in `raw/`). The macros deliberately stop at `~/Inbox/` rather than writing into `raw/` — Integrity Rule 2 means the move into the vault is a deliberate human step, not a macro side-effect. This page exists as a single-source stub because of that direct relevance to Tom's vault workflow.

Linked from [[capture-to-inbox]].
