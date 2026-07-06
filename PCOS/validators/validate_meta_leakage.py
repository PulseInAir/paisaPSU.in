#!/usr/bin/env python3
"""
validate_meta_leakage.py — PCOS v1.0
Rule: SPEC-027 (No Meta-Leakage) + SPEC-004 (No Hallucinations — [VERIFY] tags)
Pass condition: 0 matches of drafting scaffolding
"""

import sys
import re
import json


# Patterns that indicate drafting scaffolding
LEAKAGE_PATTERNS = [
    (r'\[VERIFY\]', '[VERIFY] tag'),
    (r'\[TODO\]', '[TODO] tag'),
    (r'\[DRAFT\]', '[DRAFT] tag'),
    (r'\[NOTE\]', '[NOTE] tag'),
    (r'\[EDIT\]', '[EDIT] tag'),
    (r'\[SOURCE\]', '[SOURCE] tag'),
    (r'\[INSERT\]', '[INSERT] tag'),
    (r'\[UPDATE\]', '[UPDATE] tag'),
    (r'\[CHECK\]', '[CHECK] tag'),
    (r'\[TBD\]', '[TBD] tag'),
    (r'TODO:', 'TODO: marker'),
    (r'FIXME:', 'FIXME: marker'),
    (r'XXX:', 'XXX: marker'),
]


def validate(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')
    violations = []

    for pattern, name in LEAKAGE_PATTERNS:
        for i, line in enumerate(lines, 1):
            matches = re.finditer(pattern, line, re.IGNORECASE)
            for match in matches:
                context = line.strip()[:80]
                violations.append(f"Line {i}: {name} found: \"{context}\"")

    passed = len(violations) == 0

    result = {
        "validator": "Meta Leakage",
        "rule": "SPEC-027, SPEC-004",
        "pass": passed,
        "details": f"No drafting scaffolding found" if passed else f"{len(violations)} leak(s) found",
        "violations": violations
    }

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_meta_leakage.py <article_file>")
        sys.exit(1)

    result = validate(sys.argv[1])
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
