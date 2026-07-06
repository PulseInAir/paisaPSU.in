#!/usr/bin/env python3
"""
validate_forbidden_words.py — PCOS v1.0
Rule: SPEC-024 (Forbidden Vocabulary) + SPEC-025 (No-Filler Intro) + SPEC-011 (Honest Returns)
Pass condition: 0 matches from the forbidden list
"""

import sys
import re
import json
import os


# Default forbidden words/phrases if reference file not found
DEFAULT_FORBIDDEN = [
    # AI fingerprints (SPEC-024)
    "delve",
    "navigate the complexities",
    "unlock",
    "journey",
    "realm",
    "in today's fast-paced world",
    "landscape",
    "game-changer",
    "in conclusion",
    # Filler intro patterns (SPEC-025)
    "in this article, we will discuss",
    "in this article, we will explore",
    "in this article, we'll",
    "let's explore",
    "today we'll look at",
    "let's dive in",
    "let's dive into",
    # Honest returns (SPEC-011)
    "guaranteed returns",
    "guaranteed profit",
    "guaranteed income",
]


def load_forbidden_words(reference_dir=None):
    """Load forbidden words from reference file or use defaults."""
    if reference_dir:
        filepath = os.path.join(reference_dir, 'forbidden_words.txt')
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                words = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                return words
    return DEFAULT_FORBIDDEN


def validate(filepath, reference_dir=None):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    forbidden = load_forbidden_words(reference_dir)
    violations = []

    for phrase in forbidden:
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        matches = pattern.finditer(text)
        for match in matches:
            # Find line number
            line_num = text[:match.start()].count('\n') + 1
            context = text[max(0, match.start()-20):match.end()+20].replace('\n', ' ')
            violations.append(f"Line {line_num}: Found \"{phrase}\" in: \"...{context}...\"")

    passed = len(violations) == 0

    result = {
        "validator": "Forbidden Words",
        "rule": "SPEC-024, SPEC-025, SPEC-011",
        "pass": passed,
        "details": f"{len(violations)} AI fingerprint(s) found" if violations else "0 AI fingerprints found",
        "violations": violations
    }

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_forbidden_words.py <article_file> [--reference-dir <path>]")
        sys.exit(1)

    ref_dir = None
    if '--reference-dir' in sys.argv:
        idx = sys.argv.index('--reference-dir')
        if idx + 1 < len(sys.argv):
            ref_dir = sys.argv[idx + 1]

    result = validate(sys.argv[1], ref_dir)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
