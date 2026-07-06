#!/usr/bin/env python3
"""
validate_keyword_placement.py — PCOS v1.0
Rule: SPEC-012 (Focus Keyword Placement)
Pass condition: Keyword found in first 10% of article body
"""

import sys
import re
import json
import argparse


def count_words(text):
    words = [w for w in text.split() if w.strip()]
    return len(words)


def validate(filepath, keyword):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Clean text
    clean_text = re.sub(r'<[^>]+>', '', text)
    clean_text = re.sub(r'^#{1,6}\s+', '', clean_text, flags=re.MULTILINE)

    total_words = count_words(clean_text)
    ten_percent_words = max(int(total_words * 0.1), 50)  # At least 50 words

    # Get the first 10% of words
    words = clean_text.split()
    first_ten_percent = ' '.join(words[:ten_percent_words])

    # Search for keyword in first 10%
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    match = pattern.search(first_ten_percent)

    if match:
        # Calculate position as percentage
        words_before = len(first_ten_percent[:match.start()].split())
        position_pct = (words_before / total_words) * 100 if total_words > 0 else 0
        passed = True
        details = f"Found at position {position_pct:.1f}% (word ~{words_before} of {total_words:,})"
    else:
        passed = False
        # Check if keyword exists anywhere
        full_match = pattern.search(clean_text)
        if full_match:
            words_before = len(clean_text[:full_match.start()].split())
            position_pct = (words_before / total_words) * 100 if total_words > 0 else 0
            details = f"Not in first 10%. First occurrence at {position_pct:.1f}% (word ~{words_before})"
        else:
            details = f"Keyword '{keyword}' not found anywhere in the article"

    result = {
        "validator": "Keyword in First 10%",
        "rule": "SPEC-012",
        "pass": passed,
        "details": details,
        "violations": [] if passed else [f"Focus keyword '{keyword}' must appear in the first 10% of the article body"]
    }

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate keyword placement in first 10%")
    parser.add_argument("filepath", help="Path to article text file")
    parser.add_argument("--keyword", required=True, help="Focus keyword phrase")
    args = parser.parse_args()

    result = validate(args.filepath, args.keyword)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
