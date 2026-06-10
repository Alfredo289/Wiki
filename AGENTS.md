Sehr guter Ansatz. Wenn du eine Obsidian-Wiki nutzt, ist „alles indizieren“ oft genau der richtige Schritt, aber nur mit sauberer Pipeline, sonst wird es schnell unbrauchbar.

## Pragmatisches Zielbild

* **Rohdaten rein** (automatisiert, unverändert)
* **Indexierung darüber** (Metadaten, Tags, Volltext)
* **Kuratierte Wissensebene getrennt** (deine echten Notizen)

So vermeidest du Chaos.

## Empfohlene Struktur in Obsidian

* `inbox`  
    * ungefilterte Imports (Webseiten, RSS, PDFs)
* `raw`  
    * bereinigte, stabile Quellenkopien
* `raw/assets/`  
    * deine Synthesen, Evergreen Notes
* `index.md; log.md; registry.md`  
    * MOCs, Register, Suchseiten

## Was du konkret für „gesamte Datenbank indizieren“ brauchst

* Einheitliches Frontmatter in **allen** importierten Dateien:
    * `title`, `url`, `source_name`, `captured`, `language`, `type`, `status`, `tags`
* Ein fester Status-Flow:
    * `inbox -> reviewed -> synthesized`
* Ein globaler Tag-Standard:
    * tagging anhand des Arts und des Inhaltes der Seite


## Technischer Weg (einfach und robust)

* Web-Content immer zuerst als Markdown speichern
* URL-Cleanup direkt beim Import (Tracking-Parameter raus)
* Pro Quelle eine eigene Source-Note mit RSS/Domain
* Dann automatisiert:
    * Volltextsuche (Obsidian Search)
    * Property-basierte Filter (Dataview/Query)
    * zentrale Index-Notizen (MOC)

## Minimaler Start in 30 Minuten

* 1 Template für Web-Importe (haben wir schon vorbereitet)
* 1 Template für Quellen
* 2 Indexseiten:
    * `Index Quellen.md`
    * `Index Themen.md`
* Danach alle neuen Web-Dokumente strikt nur noch über diese Pipeline aufnehmen

Wenn du willst, erstelle ich dir jetzt direkt die beiden Index-Dateien (`Index Quellen.md` + `Index Themen.md`) als copy-paste-Version, passend zu deinem RSS/Web-Workflow.



---
Found live contradiction. Stop before editing — this is the grill.

**On disk now:**

**The conflict.** Your `CONTEXT.md` (the doc every agent loads first, the "conceptual ground") says, verbatim:

> `raw/` — **One flat folder** containing every curated source artifact. **No subfolders.** Origin and format are recorded in **frontmatter, not the directory structure.**

Plus integrity rule #1: _"Three layers, no fourth."_

Your instruction now puts `clippings/` +  **inside** `raw/`. That is subfolders in `raw/`. Direct breach of the flat-`raw/` decision.

Two things are tangled here, separate them:

**1. AGENTS.md is the wrong structure entirely.** It currently shows — the agent's old proposal. That's the _"wie sie sie uns gezeigt haben"_ you're rejecting. It matches neither CONTEXT.md nor your new instruction. Whole file needs rewrite to your model. Agreed?

**2. What IS their fuckup/`?** This decides whether your flat-`raw/` rule survives or dies:

- **(A) Single drop-zone.** `clippings/` = where the Web Clipper dumps _all_ tool-imports regardless of format; `assets/` = its attachment sidecar. One operational folder, not one-per-format. Format still lives in frontmatter. Flat-`raw/` rule bends, doesn't break — amend it to _"no conceptual subfolders; tool-import drop-zones allowed."_
- **(B) Web-specific folder.** Then PDFs get `raw/pdfs/`, audio gets `raw/audio/`… = format-as-folder. That **reverses** CONTEXT.md's explicit choice (format in frontmatter). Bigger decision, likely an ADR.

**Recommend (A).** Keeps your three-layer model intact, just admits the clipper needs a physical target Obsidian can't fake with frontmatter.

Which — A or B? And confirm I rewrite AGENTS.md to your structure, not the old one.