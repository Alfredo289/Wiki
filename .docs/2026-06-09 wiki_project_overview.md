---
name: wiki-project-overview
description: Karpathy-3-Layer-Vault in ~/Documents/Wiki/. Schema (CONTEXT.md + AGENTS.md) und vier Commands jetzt aligned. Templates und learnings.md sind die letzten v1-Blocker.
metadata:
  type: project
---

# Wiki Project Overview

**Vault:** `/Users/tomsaenger/Documents/Wiki/`
**Modell:** Andrej Karpathys 3-Layer LLM-Wiki — raw/ (human-curated, immutable) → wiki/ (compiled, 7 Page-Types) → Schema (CONTEXT.md, AGENTS.md, learnings.md).
**Sprache:** Deutsch in Konversation, Englisch in wiki/. Vault-interne Slugs kebab-case.

## Aktueller Stand (2026-06-09)

**Schema:** aligned. CONTEXT.md (konzeptionelle Grundlage, 7 Integrity Rules, Read Test, Relevance Filter, named Frontmatter, Meta-File-Stance) und AGENTS.md (volle Frontmatter-Tabelle, Template-Liste, Command-Liste, 10 Lint-Checks, Naming-Konventionen) widerspruchsfrei.

**Commands:** vier Dateien unter `commands/` neu geschrieben — `/wiki-ingest`, `/wiki-query`, `/wiki-lint`, `/wiki-explore`. Strikte Read-Write-Trennung implementiert. Details: [[wiki-handoff-v5-commands-refactor]].

**Templates:** noch nicht. `.obsidian/templates/` enthält 7 Pre-Grilling-Templates mit Frontmatter-Drift (`tldr`, `date_created`/`date_modified`, `sources`, `confidence: medium`). Refactor steht aus (Phase 2.1). Blocker für Command-Ausführung, weil Commands *durch* Templates schreiben.

**learnings.md:** existiert noch nicht. Format TBD. Wird von `/wiki-lint` ab Tag 1 gelesen.

**Testkorpus:** vorhanden unter `.test-corpus/` (versteckt). 12 raw + 21 wiki + 10 dokumentierte Verstöße + Negativ-Kontrolle.

## qmd

MCP gewired in `.mcp.json`. Einzige Read-Schicht über wiki/ in den neuen Commands. Verfügbarkeit nicht extern verifiziert — falls qmd selbst nicht implementiert ist, brechen `/wiki-lint`, `/wiki-query`, `/wiki-explore` (und teilweise `/wiki-ingest`). Klärungsbedarf.

## Offene Entscheidungen vor v1

Drei in Session 4→5 pragmatisch getroffen, brauchen Sign-off:
1. Stale-Schwelle = 6 Monate
2. Check 7 prüft via Git-Historie
3. `/wiki-learn` als hypothetischer Begleit-Command zu `/wiki-lint`

Sechs aus Original-Audit offen:
- confidence/provenanceState — behalten/droppen
- /wiki-new-page Verhalten
- Stub-Definition
- raw-* Template-Set
- entity-Felder (current_state, last_checked)
- learnings.md-Format

## Source of Truth

`CONTEXT.md` (Vault-Root) für konzeptionelle Grundlage. Bei Konflikten gewinnt CONTEXT.md über AGENTS.md (AGENTS.md Z. 3).

## Bezüge

- [[wiki-handoff-v5-commands-refactor]] — aktueller Handover
- [[wiki-handoff-v4-agents-draft]] — Audit-Trail, AGENTS.md-Draft-Stand
- [[wiki-handoff-v3-grilling]], [[wiki-handoff-v2-grilling]], [[wiki-handoff-v1-architecture]] — Audit-Trail älterer Sessions
