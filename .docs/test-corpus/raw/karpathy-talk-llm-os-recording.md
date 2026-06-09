---
title: "Karpathy — 'LLM as an Operating System' talk, recording"
origin: external
format: video
added: 2026-02-10
source_url: https://www.youtube.com/watch?v=karpathy-llm-os
---

One-hour conference talk. Karpathy frames the LLM as the kernel of a new computing stack: context window as RAM, tool calls as system calls, the file system as long-term storage. The argument that maps directly into Tom's vault: the wiki is the user-space file system; the LLM kernel reads and writes against it via well-defined contracts (frontmatter, qmd queries).

The talk also lands the point about agentic loops — that an LLM left running on its own veers off without a curator. Karpathy uses the same framing Tom adopted for `raw/`: the human is the curator, the loop is the worker.
