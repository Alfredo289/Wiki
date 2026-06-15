#!/usr/bin/env python3
"""Regression test for wiki-lint against the .docs/test-corpus fixtures.

Run from the vault root (macOS):
    python3 tools/test_wiki_lint.py

Asserts two things:
  1. every fixture in expected-lint.json triggers AT LEAST its listed rules;
  2. every other wiki/ page is clean of HARD errors.
Exit 0 = pass, 1 = fail (with a per-line diff of what went wrong).
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # vault root
CORPUS = os.path.join(ROOT, ".docs", "test-corpus")
MANIFEST = os.path.join(CORPUS, "expected-lint.json")

sys.path.insert(0, HERE)
import wiki_lint  # noqa: E402


def main():
    if not os.path.isdir(CORPUS):
        print(f"FAIL — test corpus not found at {CORPUS}")
        return 1

    with open(MANIFEST, encoding="utf-8") as fh:
        expected = {k: v for k, v in json.load(fh).items() if not k.startswith("_")}

    results = wiki_lint.lint(CORPUS)
    got = {rel: [r for r, _ in vs] for rel, vs in results.items()}
    failures = []

    # 1. each fixture triggers at least its listed rules
    for rel, rules in expected.items():
        have = got.get(rel, [])
        for rule in rules:
            if rule not in have:
                failures.append(f"[missing]    {rel}: expected {rule}, got {have or 'none'}")

    # 2. non-fixture wiki pages have no HARD violations
    for rel, rules in sorted(got.items()):
        if rel in expected or not rel.startswith("wiki/"):
            continue
        hard = [r for r in rules if r in wiki_lint.HARD]
        if hard:
            failures.append(f"[unexpected] {rel}: hard errors {hard}")

    if failures:
        print("FAIL")
        for f in failures:
            print("  " + f)
        return 1

    clean = sum(1 for rel, rules in got.items()
                if rel.startswith("wiki/") and rel not in expected
                and not [r for r in rules if r in wiki_lint.HARD])
    print(f"PASS — {len(expected)} fixtures flagged correctly; "
          f"{clean} other wiki pages clean of hard errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
