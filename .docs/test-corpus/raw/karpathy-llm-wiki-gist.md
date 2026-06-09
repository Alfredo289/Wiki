---
title: "Andrej Karpathy — Notes on the LLM-Wiki idea (gist)"
origin: external
format: md
added: 2026-05-12
source_url: https://gist.github.com/karpathy/llm-wiki-notes
---

Karpathy outlines a three-layer model for a personal knowledge vault built around LLMs: a raw substrate of curated artifacts, a compiled wiki layer the model writes against the substrate, and a schema layer that holds the rules. The pitch is that LLMs are bad at remembering and good at compiling — so the human curates, the model compiles, and the schema keeps both honest.

He emphasises that the wiki layer is for the human to read, not for the model to use as scratch memory. A page exists if a person wants to open it months later. Otherwise the content stays in the substrate or doesn't get written at all. Provenance from compiled claims back to raw artifacts is non-negotiable — without it the wiki drifts into hallucination by accretion.

The note ends with an open question on validation: how does the human signal "yes, I read this and it matches my understanding" without that step becoming a chore? Karpathy floats a single boolean field per page, flipped only by the human.
