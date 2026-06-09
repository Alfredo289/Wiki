---
title: "Tool-call introspection"
type: concept
date: 2026-05-22
explored: false
raw_sources:
  - nicht-da.md
tags:
  - llm
  - tooling
confidence: 0.5
---

# Tool-call introspection

The practice of letting a model inspect, summarise, or critique its own tool calls before committing to them. Sits between a pure agentic loop (which executes blindly) and a fully scripted pipeline (which forbids autonomy). Useful when the cost of a wrong call is high enough to pay for the extra reasoning turn.

Related to [[agentic-loops]] and [[context-engineering]].

This page lists `raw_sources: [nicht-da.md]` — a file that does not exist in `raw/`. The lint's `raw_sources` validation step should flag the missing referent.
