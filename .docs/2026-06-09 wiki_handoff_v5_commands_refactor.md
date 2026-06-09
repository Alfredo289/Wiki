---
name: wiki-handoff-v5-commands-refactor
description: Session 4→5 handover. Vier Commands neu geschrieben (ingest, query, lint, explore). Testkorpus aufgebaut. Drei Entscheidungen ohne expliziten Sign-off getroffen. Templates + learnings.md + E2E-Test stehen noch aus.
metadata:
  type: project
---

# Wiki Handoff v5 — Commands-Refactor, Session 4 → 5

**Datum:** 2026-06-09
**Vorgängerstand:** [[wiki-handoff-v4-agents-draft]]
**Vault:** `/Users/tomsaenger/Documents/Wiki/`

## Was in dieser Session passiert ist

Audit der Schema-Files (CONTEXT.md, AGENTS.md) ergab: konzeptionell aligned, aber operative Lücken (Read Test und Relevance Filter als reine Norm). Zoom-out zeigte den eigentlichen Blocker: die Dateien in `commands/` und `templates/` waren **Pre-Grilling-Artefakte**, die das neue Schema vielfach verletzten. Damit wurde Tooling-Refactor zum Hauptweg für v1.

Sequenz:

1. **Phase 0** — Testkorpus unter `.test-corpus/` aufgebaut (12 raw-Artefakte, 21 wiki-Pages über alle 7 Page-Types, 10 gezielte Verstöße + 1 Negativ-Kontrolle, Mapping in `EXPECTED-VIOLATIONS.md`).
2. **Phase 1.1** — Drift-Audit kartografierte alle 11 Pre-Grilling-Dateien. Verdict: 4× delete, 7× rewrite, 0× keep.
3. **Phase 2.2** — vier Commands iterativ neu geschrieben, ein Command pro Schritt, jeweils mit explizitem Verstoß-Mapping gegen die getroffenen Entscheidungen aus CONTEXT.md/AGENTS.md.

## Stand der vier Commands (jetzt aligned)

**`/wiki-ingest`** — Autoscan (kein Argument). Ingest-Menge = `raw/`-Dateien minus alle Filenames in `raw_sources:`-Frontmattern. Pro Artefakt eine `source`-Page Pflicht, `concept`/`entity` nur bei erfülltem Relevance Filter. Schreibt durch `wiki-<type>.md`-Templates. Niemals nach `raw/`. Setzt immer `explored: false`. Stubs werden nicht erzeugt; verworfene Kandidaten landen im Chat-Report.

**`/wiki-query`** — qmd als einziger Read-Pfad. **Read Test als operativer Gate**: Default ist Chat-Antwort; persistierte Page nur wenn der Test passt. Persistenz-Pfad: `wiki/syntheses/<slug>.md`, `type: synthesis`, `wiki_sources:` (nicht `raw_sources:`), `explored: false`. Kein-Wissen-erfunden-Regel: jede Behauptung braucht Wikilink-Zitat. `explored: false`-Pages werden in der Antwort als provisorische Evidenz markiert.

**`/wiki-lint`** — read-only ohne Ausnahme. Alle 10 Checks aus AGENTS.md §Lint, jeder explizit an Integrity Rule oder named Frontmatter-Feld geknüpft. Liest `learnings.md` vor jedem Lauf. Output: Chat-Report; optional `wiki/outputs/lint-report-YYYY-MM-DD.md` nur auf explizite Zustimmung.

**`/wiki-explore`** — read-only Proposal-Command. Identifiziert Lücken in einer wiki/-Page, durchsucht Web, liefert pro Lücke 1–3 Quellen-Kandidaten plus passendes `raw-*`-Template. Schreibt nichts. Tom kuratiert in `raw/`; `/wiki-ingest` macht den Rest.

Vorher: alle vier schrieben `wiki/index.md` und/oder `wiki/log.md`. `/wiki-explore` und `/wiki-ingest` schrieben direkt in `raw/`. `/wiki-query` benutzte `type: output` für Cross-Page-Antworten. `/wiki-lint` machte "fix automatically where possible".

## Gemeinsame Regeln (jetzt einheitlich in allen vier Commands)

- CONTEXT.md zuerst, dann AGENTS.md, dann learnings.md.
- qmd ist die einzige Read-Schicht über wiki/.
- Templates sind das Frontmatter-Enforcement — kein Hand-Roll.
- Kein Command schreibt nach raw/. Niemals.
- Kein Command schreibt wiki/index.md oder wiki/log.md.
- `explored: false` ist Standard für jede erzeugte oder substantiell veränderte Page.

## Drei Entscheidungen ohne expliziten Sign-off — Tom muss bestätigen oder kippen

1. **Stale-Schwelle = 6 Monate** in `/wiki-lint` Check 6. Begründung: konsistent mit dem Read-Test-Zeitfenster (CONTEXT.md). Alternativen: 3 oder 12.
2. **Check 7 (`explored: true` vom Agent) prüft über Git-Historie**. Bricht, wenn Tom Commits mit "Tom" co-authored anlegt. Alternative: Check droppen.
3. **`/wiki-learn` als hypothetischer Command erwähnt** in `/wiki-lint` für das Schreiben in `learnings.md`. `/wiki-lint` schreibt es selbst nicht. Alternative: `/wiki-lint` schreibt direkt mit per-Eintrag-Bestätigung.

## Testkorpus — scharfgeschaltet, bereit für E2E

`.test-corpus/` ist versteckt (Obsidian ignoriert), enthält:

- 12 raw-Artefakte über alle Origin/Format-Kombinationen
- 21 wiki-Pages über alle 7 Page-Types
- 10 dokumentierte Verstöße (1 broken, 2 void/relevance, 1 orphan, 1 falsch-explored, 1 raw_sources-broken, 1 path/type-drift, 2 single-source, 1 missing title, 1 decision ohne status)
- 1 Negativ-Kontrolle (single source MIT Tom-Relevanz — Lint darf NICHT meckern)
- Mapping in `.test-corpus/EXPECTED-VIOLATIONS.md`

Jeder Command hat ein Test-Profil gegen den Korpus (siehe Chat-Report 2026-06-09).

## Was noch fehlt für v1

- **Phase 2.1 — Templates** (`.obsidian/templates/wiki-<type>.md` × 7, plus N `raw-*`-Templates). Ohne sie können die Commands nicht laufen — sie schreiben *durch* die Templates.
- **Phase 2.3 — learnings.md initialisieren**. Format-Vorschlag: Append-only Markdown, datierte Einträge, eine Zeile pro Decision: `- 2026-06-09 — wiki/concepts/foo.md — proposal: retype to entity — Tom: rejected (reason: ...)`. Endgültige Form Toms Entscheidung.
- **Phase 3 — End-to-End-Test** gegen den Testkorpus.

Sechs weitere v1-Punchlist-Punkte aus dem Original-Audit bleiben offen: `confidence`/`provenanceState`-Status, `/wiki-new-page`-Verhalten (existiert aktuell gar nicht als Datei), Stub-Definition, `raw-*`-Template-Set, `entity`-Felder (`current_state`/`last_checked`), `learnings.md`-Format. Die meisten beim Templates-Refactor mit-entscheidbar.

## Architektur-Bilanz

Die vier Commands realisieren jetzt eine saubere Strikt-Read-Write-Trennung:

- **raw/** — write nur durch Tom
- **wiki/** — write durch `/wiki-ingest` (compile aus raw/) und `/wiki-query` (synthesis aus wiki/), beide durch Templates, beide setzen `explored: false`
- **`/wiki-lint`** und **`/wiki-explore`** — read-only, liefern Proposals

Damit ist der Validation Gate (CONTEXT.md Z. 19) durch Tooling operativ, nicht nur normativ.

## Methoden-Memo

Eingeführter Iterations-Loop pro Command: (1) Datei lesen, (2) Verstöße gegen ausschließlich bereits getroffene Entscheidungen explizit auflisten mit Zeilen-/Section-Verweisen, (3) Entwurf vorstellen, (4) Tom-Sign-off einholen, (5) schreiben, (6) Testbarkeit gegen `.test-corpus/` explizit darlegen. Wert: macht jeden Refactor-Schritt einzeln auditierbar und verhindert "kreatives" Hinzufügen von Entscheidungen, die nicht im Schema stehen.

## Bezüge

- [[wiki-project-overview]] — Source of Truth
- [[wiki-handoff-v4-agents-draft]] — vorheriger Stand (AGENTS.md-Draft)
- `.test-corpus/EXPECTED-VIOLATIONS.md` — Test-Mapping
