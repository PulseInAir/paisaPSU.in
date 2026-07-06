#!/usr/bin/env python3
"""
validate_url_length.py — PCOS v1.0
Rule: SPEC-014 (75-Character URL Limit)
Pass condition: Total URL <= 75 characters
"""

import sys
import json
import argparse


BASE_URL = "https://paisapsu.in/"


def validate(slug):
    full_url = BASE_URL + slug.strip('/') + '/'
    total_length = len(full_url)
    passed = total_length <= 75

    result = {
        "validator": "URL Length",
        "rule": "SPEC-014",
        "pass": passed,
        "details": f"{total_length} characters (max 75): {full_url}",
        "violations": []
    }

    if not passed:
        result["violations"].append(
            f"URL is {total_length} characters, exceeds 75-char limit by {total_length - 75}. "
            f"Shorten slug from '{slug}' (currently {len(slug)} chars, max {75 - len(BASE_URL) - 1} chars)."
        )

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate URL length (max 75 chars)")
    parser.add_argument("--slug", required=True, help="URL slug (without base URL)")
    args = parser.parse_args()

    result = validate(args.slug)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
