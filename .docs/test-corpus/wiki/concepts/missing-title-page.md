---
type: concept
date: 2026-05-11
explored: false
raw_sources:
  - karpathy-llm-wiki-gist.md
  - tom-voice-memo-vault-three-layers.md
tags:
  - vault
  - validation
confidence: 0.6
---

# Validation gate

The single explicit human signal that distinguishes an agent-written page Tom has read and trusts from one he has not. Implemented as the `explored:` boolean in the frontmatter contract — agent always writes `false`, only Tom flips to `true`.

Related to [[three-layer-vault]] and [[hallucination-by-accretion]].

Note for the test corpus: this page deliberately omits the `title:` field in frontmatter. The lint's required-frontmatter check should flag the missing field.
