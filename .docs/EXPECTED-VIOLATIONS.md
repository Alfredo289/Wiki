# EXPECTED-VIOLATIONS.md

Catalogue of deliberately seeded defects in this test corpus. Each row maps a file to the violation it carries and to the lint check / integrity rule that should catch it. Used to score `/wiki-lint` and any future schema-validation tooling against ground truth.

The negative control (row 8) is included on purpose: it must **not** be flagged.

| # | File (relative to `.test-corpus/`) | Violation | Should be flagged by |
|---|---|---|---|
| 1 | `wiki/concepts/broken-wikilink-page.md` | Contains `[[nicht-existent]]` — link target is a page that does not exist and is not justified anywhere | Lint check 3 — `[[wikilink]]` validation (broken link branch) |
| 2 | `wiki/concepts/void-link-page.md` | Contains `[[zukunfts-konzept]]` — target does not exist and is not justified by the relevance filter | Lint check 3 — `[[wikilink]]` validation (link-into-the-void branch). Integrity Rule 6 — Relevance filter, no wikilinks into the void |
| 3 | `wiki/concepts/orphan-page.md` | No incoming `[[wikilink]]` from any other page in the corpus | Lint check 5 — Orphan check |
| 4 | `wiki/concepts/wrong-explored-page.md` | `explored: true` written by an agent | Integrity Rule 4 — `explored: true` is Tom's gate. (No dedicated lint check listed today; should be added or covered by required-frontmatter semantics + an "explored set without human signal" rule) |
| 5 | `wiki/concepts/raw-sources-broken.md` | `raw_sources: [nicht-da.md]` — referenced file is absent from `raw/` | Lint check 2 — `raw_sources:` validation |
| 6 | `wiki/concepts/path-type-drift.md` | Filed under `wiki/concepts/` but frontmatter `type: entity` | Lint check 4 — Path/type drift |
| 7 | `wiki/concepts/single-source-no-justification.md` | Only one `raw_sources:` entry and no Tom-relevance hook in the body | Lint check 10 — Stub vs. page (relevance filter branch). Integrity Rule 6 — Relevance filter |
| 8 | `wiki/concepts/single-source-with-justification.md` | **Negative control — must NOT be flagged.** One `raw_sources:` entry, but body contains explicit Tom-relevance justification block | Lint must remain silent on this file under the single-source-stub exception in CONTEXT.md §"Named frontmatter" — `raw_sources` |
| 9 | `wiki/concepts/missing-title-page.md` | Frontmatter omits the required `title:` field | Lint check 1 — Required frontmatter per page type (baseline) |
| 10 | `wiki/decisions/decision-without-status.md` | `decision`-type page omits the required `status:` field | Lint check 1 — Required frontmatter per page type (per-type, decision) |

## Notes for the lint author

- Row 1 (broken) and row 2 (void) are intentionally distinct: a broken link targets *anything* that does not exist; a void link is the subset where the target was also never justifiable under the relevance filter. AGENTS.md §Lint check 3 says to flag the three categories separately — broken, void, stub.
- Row 4 cannot be detected from the file content alone — it requires either (a) a git/history check that no human commit flipped the bit, or (b) the lint being run by an agent that knows it should never see `explored: true` on a page it just wrote. The corpus seeds the violation; how the lint detects it is a downstream design question.
- Row 7 vs row 8 is the most subtle pair. Both have a single `raw_sources:` entry. The differentiator is the presence of an explicit Tom-relevance block in the body of row 8 ("**Tom-relevance (single-source stub justification):** ..."). Any heuristic the lint uses must distinguish these two cases.
