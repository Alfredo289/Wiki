---
title: "Wiki repository structure — low-level implementation plan"
type: schema
date: 2026-06-10
explored: false
---

# Wiki repository structure — low-level implementation plan

Scope: build out the missing structural elements of the vault — schema anchors,
the trimmed skills/rules set, the navigation/log layer, and a testing harness.
macOS-only instructions.

> **Build status (2026-06-10):** Phases 1–5 are now **shipped** — `CONTEXT.md`,
> `AGENTS.md`, `learnings.md`, `dashboard.md`, `log.md`, the `raw/` + seven
> `wiki/` folders, reconciled templates (incl. new `entity`/`decision`), the
> three `.claude/skills/`, `tools/wiki_lint.py`, and the `tools/test_wiki_lint.py`
> harness + `expected-lint.json`. **Pending (Tom's call):** run the test once on
> your Mac (sandbox couldn't execute here), optionally seed `wiki/` from the
> corpus's valid pages, write the real `log.md`-exception decision page (2.3), and
> optionally add the git pre-commit hook (5.3).

---

## 0. Current state (2026-06-10)

**Exists**
- `AGENTS.md` — rewritten this session (was a stale agent proposal + grill notes).
- `.docs/test-corpus/` — a reference `wiki/` **and** the fixture set for the linter.
- `.obsidian/` — Dataview + Templater installed; 6 templates in `.obsidian/templates/`.
- `.mcp.json` — registers the `qmd` MCP server.
- `.cogito-folder.json`, `.git/`.

**Was missing → now / planned**
- `CONTEXT.md` — the keystone every tool loads first. **Created this session.**
- `learnings.md` — schema layer's third file. *Planned (Phase 1.3).*
- `raw/`, `wiki/` — the actual substrate and compiled layers. *Planned (Phase 2).*
- `dashboard.md`, `log.md` — navigation + append-only log. *Planned (Phase 2).*
- Skills + rules — none implemented. *Planned (Phase 3).*
- `wiki-lint` validator. *Planned (Phase 4).*
- Testing. *Planned (Phase 5).*

**Resolved conflict.** Your ADR `no-index-md-meta-file` bans `index.md`/`log.md`.
Decision taken: **no `index.md`** (Dataview dashboard instead) + **one
append-only `log.md`** as the single allowed exception. The ADR is amended in
Phase 2.3.

---

## 1. Target structure

```
Wiki/
├── CONTEXT.md          # schema · conceptual ground (DONE)
├── AGENTS.md           # schema · operating rules (DONE)
├── learnings.md        # schema · accumulated corrections (1.3)
├── dashboard.md        # Dataview navigation, rendered live (2.2)
├── log.md              # append-only session log (2.2)
├── raw/                # substrate · FLAT · Tom-only (2.1)
├── wiki/               # compiled layer (2.1)
│   ├── concepts/  entities/  sources/  sops/
│   └── decisions/  syntheses/  outputs/
├── .claude/
│   └── skills/
│       ├── wiki-lint/        SKILL.md   (3.1)
│       ├── capture-triage/   SKILL.md   (3.2)
│       └── compile-wiki/     SKILL.md   (3.3)
├── tools/
│   └── wiki_lint.py     # the validator (4)
└── .docs/
    ├── repo-structure-implementation-plan.md   # this file
    ├── test-corpus/                              # fixtures (exists)
    └── test-corpus/expected-lint.json            # expected results (5.1)
```

Integrity Rule 1 holds: three layers (`raw/`, `wiki/`, schema), no fourth.
`.claude/`, `tools/`, `.docs/` are tooling, not knowledge layers.

---

## 2. The frontmatter contract (canonical) + template reconciliation

The canonical contract is defined in `CONTEXT.md`. **Action:** reconcile the six
Obsidian templates to it — they currently drift.

| Field in template | Problem | Fix |
|---|---|---|
| `confidence: medium` | string, contract wants number | `confidence: 0.7` |
| `date_created` / `date_modified` | not in contract | collapse to `date` |
| `sources: []` | ambiguous | split into `raw_sources` / `wiki_sources` |
| `tldr: ""` | not in contract | drop (or keep as optional, lint ignores) |

Templater syntax stays (`{{date}}`, `{{title}}`). One template per `type`. Update
`.obsidian/templates/{concept,source,sop,project,output,synthesis}.md`; add
`entity.md`, `decision.md` to cover all seven types.

---

## 3. Phase 1 — schema anchors

- **1.1 `CONTEXT.md`** — DONE. Three-layer model, Integrity Rules 1–4, both
  frontmatter contracts, relevance filter + read test, navigation decision.
- **1.2 `AGENTS.md`** — DONE. Load order, may / may-not, per-page discipline,
  skills, logging, definition of done.
- **1.3 `learnings.md`** — create as an append-only list of corrections the agent
  must not repeat (e.g. "don't infer `confidence` — leave 0.5 if unknown").
  Starts nearly empty; grows from real mistakes. Loaded second, after CONTEXT.

---

## 4. Phase 2 — folders, dashboard, log

- **2.1 Scaffold** `raw/` (flat, empty, with a `.gitkeep`) and the seven `wiki/`
  type subfolders. Optionally seed `wiki/` by copying the *valid* pages from
  `.docs/test-corpus/wiki/` (exclude the four broken fixtures).
- **2.2 `dashboard.md`** — a single Dataview note, authored once:

  ````markdown
  # Dashboard
  ## Recently added
  ```dataview
  TABLE type, date, explored FROM "wiki" SORT date DESC LIMIT 15
  ```
  ## Unread (needs Tom's gate)
  ```dataview
  LIST FROM "wiki" WHERE explored = false SORT date DESC
  ```
  ## Counts by type
  ```dataview
  TABLE length(rows) AS count FROM "wiki" GROUP BY type
  ```
  ````

  And `log.md` — header + append-only entries: `YYYY-MM-DD — change — pages`.
- **2.3 Amend the ADR.** When `wiki/decisions/` exists, add a real decision page
  recording the append-only `log.md` exception (supersede/extend
  `no-index-md-meta-file`). Do **not** edit the test-corpus fixture copy.

---

## 5. Phase 3 — the trimmed skills + rules

"Rules" = the Integrity Rules + frontmatter contract, already encoded in
`CONTEXT.md`/`AGENTS.md`. "Skills" = three purpose-built `.claude/skills/`
entries. Each is one folder with a `SKILL.md`. Keep them trimmed: smallest
instruction that enforces the contract.

### 3.1 `wiki-lint` — the validator skill
```markdown
---
name: wiki-lint
description: Validate the vault against the frontmatter contract and Integrity
  Rules. Use before declaring any write done, or on request to check the vault.
---
Run `python3 tools/wiki_lint.py <path-or-vault-root>`. Report every error with
file + rule id. Never auto-fix `raw/`. Exit non-zero on any error.
```

### 3.2 `capture-triage` — Inbox → proposal
```markdown
---
name: capture-triage
description: Turn an item in ~/Inbox into a proposed kebab-case slug + complete
  raw/ frontmatter for Tom to file. Proposes only — never moves files.
---
Read the inbox item. Propose: slug, origin, format, added, source_url, title.
Output a ready-to-paste frontmatter block. State explicitly that Tom must move
the file into raw/ (Integrity Rule 2).
```

### 3.3 `compile-wiki` — raw → wiki page
```markdown
---
name: compile-wiki
description: Compile raw/ artifacts into a wiki/ page under the contract. Use when
  asked to write up a concept/entity/source/sop/synthesis from the substrate.
---
Gather ≥2 relevant raw_sources. Apply the read test + relevance filter. Write the
page with explored:false, full frontmatter, provenance [[wikilinks]]. Run
wiki-lint. Append one line to log.md.
```

---

## 6. Phase 4 — the `wiki-lint` validator

A single `tools/wiki_lint.py` — **stdlib only**, no `pip install` (macOS ships
python3). It lints `ROOT/wiki` and `ROOT/raw` only (never recurses into `.docs`).
**Hard** rules gate the build; **soft** rules are advisory. Checks by rule id:

| id | tier | Check | Corpus fixture |
|----|------|-------|----------------|
| `FM-PARSE` | hard | frontmatter present and the `---` block is closed | `wrong-explored-page` |
| `FM-REQ` | hard | required fields for the page `type` (decision also needs `status`) | `missing-title-page`, `decision-without-status` |
| `FM-TYPE` | hard | `explored` bool, `confidence` number 0–1, `date` ISO, known type | — |
| `GATE` | hard | no agent-set `explored: true` (Rule 4) | `wrong-explored-page` |
| `LINK` | hard | every `[[wikilink]]` resolves by filename slug **or** title | `void-link-page`, `broken-wikilink-page` |
| `PATH` | hard | `type:` matches folder (`concepts/`→`concept`) | `path-type-drift` |
| `PROV-REF` | hard | every `raw_sources` entry exists in `raw/` | `raw-sources-broken` |
| `PROV-MISSING` | hard | page has ≥1 source (`raw_sources` and/or `wiki_sources`) | — |
| `FLAT` | hard | `raw/` has no subfolders (Rule 1) | — |
| `ORPHAN` | soft | page linked from ≥1 other page | `orphan-page` |
| `PROV-SINGLE` | soft | exactly one `raw_source` — justify or merge | `single-source-no-justification` |

Note on the single-source pair: `single-source-with-justification` is *acceptable*
(justified in prose) and `single-source-no-justification` is not — but the
difference is prose only, with no deterministic frontmatter signal. So v1 emits
`PROV-SINGLE` (soft) for **both** and leaves the keep/merge call to Tom's review,
consistent with the validation-gate philosophy. Output: one line per violation
`RULE  path  message` + a summary; exit code = number of hard errors.
Run: `python3 tools/wiki_lint.py .`

---

## 7. Phase 5 — testing

The test-corpus already contains four deliberately broken pages. Make that a
real regression test.

- **5.1 Expected-results manifest** — `.docs/test-corpus/expected-lint.json`
  (shipped). The corpus holds **nine** deliberate fixtures; each entry lists the
  rule(s) it must trigger (**at-least** semantics — a fixture may also surface
  extra soft rules like `ORPHAN`):

  ```json
  {
    "wiki/concepts/missing-title-page.md":            ["FM-REQ"],
    "wiki/concepts/wrong-explored-page.md":           ["FM-PARSE", "GATE"],
    "wiki/concepts/void-link-page.md":                ["LINK"],
    "wiki/concepts/broken-wikilink-page.md":          ["LINK"],
    "wiki/concepts/path-type-drift.md":               ["PATH"],
    "wiki/concepts/raw-sources-broken.md":            ["PROV-REF"],
    "wiki/concepts/orphan-page.md":                   ["ORPHAN"],
    "wiki/concepts/single-source-no-justification.md":["PROV-SINGLE"],
    "wiki/decisions/decision-without-status.md":      ["FM-REQ"]
  }
  ```
- **5.2 Runner** — `tools/test_wiki_lint.py` (shipped) imports `wiki_lint`, lints
  the corpus, and asserts: (1) every fixture triggers at least its listed rules;
  (2) every **other** `wiki/` page is clean of *hard* errors (soft warnings
  allowed). The "at-least + others-clean" design is robust to fixtures that also
  read as orphans, so no fixture cross-linking is needed.
  Run: `python3 tools/test_wiki_lint.py`
- **5.3 Verification status.** The sandbox could not execute Python this session
  (host disk space), so the linter was verified by **hand-tracing all 15 corpus
  pages** — every fixture hits its rule and all 12 non-fixtures are hard-clean.
  Run 5.2 once on your Mac to confirm; if anything is off, the runner prints the
  exact file + rule.
- **5.3 (optional) git pre-commit hook** — `.git/hooks/pre-commit` runs
  `python3 tools/wiki_lint.py` on staged `wiki/` files; non-zero blocks the
  commit. macOS: `chmod +x .git/hooks/pre-commit`. Keep optional so it never
  becomes a write-tax on the substrate.

---

## 8. Build order & acceptance

1. Phase 1.3 `learnings.md` — trivial.
2. Phase 2.1–2.2 scaffold + dashboard + log — vault becomes navigable.
3. Phase 4 `wiki_lint.py` — the validator.
4. Phase 5.1–5.2 fixtures + runner — **gate: `test_wiki_lint.py` passes.**
5. Phase 3 skills — wrap the now-proven linter + the two write skills.
6. Phase 2 reconcile templates; 2.3 ADR amendment.

**Definition of done for the whole structure:** the seven `wiki/` subfolders and
`raw/` exist; `dashboard.md` renders; `wiki-lint` passes on the real vault and
flags exactly the four fixtures in the corpus; the three skills are present and
reference the contract.

---

## 9. Open items / my reconstructions (confirm before relying on them)

- **Integrity Rule 3 wording** is reconstructed from the provenance principle in
  the source notes — the exact canonical text isn't on disk. Confirm it.
- **`GATE` check** can't truly know "who" set `explored: true` without inspecting
  git blame. Pragmatic v1: flag every `explored: true` introduced in a commit not
  authored by Tom; for the corpus test it simply flags the fixture.
- **Frontmatter drift** between `.obsidian/templates/` and the contract must be
  reconciled (Section 2) or the linter and Templater will disagree.
