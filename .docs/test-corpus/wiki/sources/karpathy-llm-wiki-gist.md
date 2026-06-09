---
title: "Karpathy — LLM-Wiki notes (gist)"
type: source
date: 2026-05-13
explored: false
raw_sources:
  - karpathy-llm-wiki-gist.md
source_url: https://gist.github.com/karpathy/llm-wiki-notes
source_type: notes
fetched: 2026-05-12
tags:
  - vault
  - llm
confidence: 0.9
---

# Karpathy — LLM-Wiki notes (gist)

## Argument

A personal knowledge vault should be built as three layers: a curated raw substrate, a compiled wiki written by the LLM against that substrate, and a schema that holds the rules. LLMs compile well and remember poorly; humans curate well and compile poorly. The architecture matches each side to what it is good at.

## Key claims

- The compiled wiki is for humans to read, not for the model to use as scratch memory.
- A page exists only if a person will want to open it months later (the read test).
- Provenance from compiled claims back to raw artifacts is non-negotiable.
- Validation needs a single explicit human signal — a boolean per page, flipped only by the human.

## Tom's reaction

This is the spine of the [[three-layer-vault]] adoption. The validation gate landed as the `explored:` field; the read test became Integrity Rule 5. The open question Karpathy ends on — how to keep validation from becoming a chore — is the design pressure behind the `/wiki-lint` command rather than scheduled scans.
