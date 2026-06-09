---
title: "Raycast"
type: entity
date: 2026-05-21
explored: false
raw_sources:
  - raycast-screenshot-window-tile.md
  - tom-keyboard-maestro-macro-export.md
tags:
  - macos
  - launcher
confidence: 0.8
---

# Raycast

A macOS launcher and command palette. Replaces Spotlight for file and app launch, and acts as a host for scripts, snippets, and extensions. Tom uses it as the daily-driver entry point for almost every workflow that starts at the keyboard.

Current state (May 2026): built-in window-tiling commands are good enough that the third-party tilers (Magnet, Rectangle Pro) no longer earn their slot — see the screenshot capture in `raw/`. The launcher still cohabits with [[keyboard-maestro]] for macros that need text expansion or palettes deeper than two levels.

Relevant to Tom's vault as the front door for capture: the [[capture-to-inbox]] SOP runs through a Raycast script command that hands artifacts to `~/Inbox/` for curation.
