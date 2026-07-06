#!/usr/bin/env python3
"""
validate_em_dash.py — PCOS v1.0
Rule: SPEC-028 (Em Dash Prohibition)
Pass condition: 0 em dashes found
"""

import sys
import json


def validate(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')
    violations = []

    for i, line in enumerate(lines, 1):
        # Check for em dash (U+2014)
        if '\u2014' in line:
            count = line.count('\u2014')
            violations.append(f"Line {i}: {count} em dash(es) found: \"{line.strip()[:80]}...\"")

    em_dash_count = text.count('\u2014')

    result = {
        "validator": "Em Dash Check",
        "rule": "SPEC-028",
        "pass": em_dash_count == 0,
        "details": f"{em_dash_count} em dash(es) found",
        "violations": violations
    }

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_em_dash.py <article_file>")
        sys.exit(1)

    result = validate(sys.argv[1])
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
