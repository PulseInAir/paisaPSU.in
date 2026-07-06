#!/usr/bin/env python3
"""
validate_disclaimer.py — PCOS v1.0
Rule: SPEC-003 (Credential Transparency)
Pass condition: Exact disclaimer wording found at least once
"""

import sys
import json


EXACT_DISCLAIMER = "I am not a SEBI-registered advisor or a CA, and views expressed are personal."


def validate(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Check for exact disclaimer text
    found = EXACT_DISCLAIMER in text

    # Also check for common partial versions to give helpful feedback
    partial_checks = []
    if not found:
        if "SEBI" in text and "CA" in text and "personal" in text:
            partial_checks.append("Found SEBI, CA, and personal references but wording doesn't match exactly")
        if "not a SEBI" in text:
            partial_checks.append("Found partial match: 'not a SEBI'")
        if "views expressed are personal" in text:
            partial_checks.append("Found partial match: 'views expressed are personal'")

    result = {
        "validator": "Disclaimer Present",
        "rule": "SPEC-003",
        "pass": found,
        "details": "Exact disclaimer wording found" if found else "Exact disclaimer wording NOT found",
        "violations": []
    }

    if not found:
        result["violations"].append(
            f"Missing exact disclaimer. Required text: \"{EXACT_DISCLAIMER}\""
        )
        if partial_checks:
            result["violations"].extend(partial_checks)

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_disclaimer.py <article_file>")
        sys.exit(1)

    result = validate(sys.argv[1])
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
