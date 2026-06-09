---
title: "No maintained index.md — use Dataview dashboard instead"
type: decision
date: 2026-05-02
explored: false
raw_sources:
  - obsidian-dataview-readme.md
  - tom-voice-memo-vault-three-layers.md
status: active
supersedes: []
tags:
  - meta
  - dashboard
confidence: 0.85
---

# No maintained index.md — use Dataview dashboard instead

## Status

Active.

## Context

Maintained meta-files (index, hot, log) were the proximate cause of the previous vault's collapse. Every command grew a tail of "and update the index", and the tail eventually exceeded the work.

## Decision

No `index.md` at vault root. Navigation uses Obsidian's file explorer; cross-cutting views use a single dashboard note with [[obsidian-dataview]] query blocks (recent pages, counts by type, pages with `explored: false`). The dashboard is authored once and rendered live — never maintained by hand.

## Alternatives considered

- **Maintained `index.md`.** Rejected: the failure mode that motivated this whole rework.
- **Auto-generated `index.md` written by an agent.** Rejected: still a write tax, still a stale artifact between runs. Dataview is live; an auto-generated file is not.
- **No dashboard at all.** Rejected: Tom wants the "what's new" signal somewhere.

## Consequences

- Tools that cannot call Dataview (`qmd`, `/wiki-lint`) must parse frontmatter themselves. The contract is the only shared source of truth.
- Adding a new meta-file requires explicit decision-page justification — never a side-effect of another workflow.
