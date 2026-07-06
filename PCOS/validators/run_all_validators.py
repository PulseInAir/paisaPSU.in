#!/usr/bin/env python3
"""
run_all_validators.py — PCOS v1.0
Master runner: executes all validators and reports consolidated pass/fail.
Rule: SPEC-040 (Final Quality Pass)

Usage:
    python run_all_validators.py article.txt --keyword "focus keyword" [--title "Article Title"] [--slug "url-slug"]
"""

import sys
import os
import json
import argparse

# Import validators from the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

import validate_word_count
import validate_keyword_density
import validate_em_dash
import validate_paragraph_length
import validate_forbidden_words
import validate_url_length
import validate_keyword_placement
import validate_meta_leakage
import validate_privacy
import validate_disclaimer
import validate_title


def print_table(results):
    """Print a formatted results table."""
    print()
    print("=" * 80)
    print(f"{'Validator':<30} {'Result':<8} {'Details'}")
    print("=" * 80)

    for r in results:
        status = "PASS" if r["pass"] else "FAIL"
        marker = "  " if r["pass"] else ">>"
        print(f"{marker} {r['validator']:<28} {status:<8} {r['details'][:40]}")

    print("=" * 80)

    passed = sum(1 for r in results if r["pass"])
    failed = sum(1 for r in results if not r["pass"])
    total = len(results)

    if failed == 0:
        print(f"\nRESULT: {passed}/{total} PASSED — ALL CLEAR")
    else:
        print(f"\nRESULT: {passed}/{total} PASSED — {failed} FAILURE(S)")
        print("\nFailed checks:")
        for r in results:
            if not r["pass"]:
                print(f"  - {r['validator']}: {r['details']}")
                for v in r.get("violations", []):
                    print(f"    > {v}")

    print()


def main():
    parser = argparse.ArgumentParser(
        description="PCOS v1.0 — Run all validators against an article"
    )
    parser.add_argument("filepath", help="Path to article text file")
    parser.add_argument("--keyword", required=True, help="Focus keyword phrase")
    parser.add_argument("--title", default=None, help="Article title (for title validation)")
    parser.add_argument("--slug", default=None, help="URL slug (for URL length validation)")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--reference-dir", default=None, help="Path to reference directory")
    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        print(f"Error: File not found: {args.filepath}")
        sys.exit(1)

    results = []

    # 1. Privacy Check (SPEC-001, SPEC-002, SPEC-006)
    results.append(validate_privacy.validate(args.filepath))

    # 2. Disclaimer Check (SPEC-003)
    results.append(validate_disclaimer.validate(args.filepath))

    # 3. Meta Leakage / [VERIFY] tags (SPEC-004, SPEC-027)
    results.append(validate_meta_leakage.validate(args.filepath))

    # 4. Em Dash Check (SPEC-028)
    results.append(validate_em_dash.validate(args.filepath))

    # 5. Paragraph Length (SPEC-023)
    results.append(validate_paragraph_length.validate(args.filepath))

    # 6. Forbidden Words (SPEC-024, SPEC-025, SPEC-011)
    results.append(validate_forbidden_words.validate(args.filepath, args.reference_dir))

    # 7. Keyword in First 10% (SPEC-012)
    results.append(validate_keyword_placement.validate(args.filepath, args.keyword))

    # 8. Word Count (SPEC-013)
    results.append(validate_word_count.validate(args.filepath))

    # 9. Keyword Density (SPEC-015)
    results.append(validate_keyword_density.validate(args.filepath, args.keyword))

    # 10. Title Check (SPEC-019) — if title provided
    if args.title:
        results.append(validate_title.validate(args.title))
    else:
        results.append({
            "validator": "Title Check",
            "rule": "SPEC-019",
            "pass": None,
            "details": "SKIPPED (no --title provided)",
            "violations": []
        })

    # 11. URL Length (SPEC-014) — if slug provided
    if args.slug:
        results.append(validate_url_length.validate(args.slug))
    else:
        results.append({
            "validator": "URL Length",
            "rule": "SPEC-014",
            "pass": None,
            "details": "SKIPPED (no --slug provided)",
            "violations": []
        })

    # Output
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print_table(results)

    # Exit code
    failures = [r for r in results if r["pass"] is False]
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
