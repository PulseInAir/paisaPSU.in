#!/usr/bin/env python3
"""
validate_title.py — PCOS v1.0
Rule: SPEC-019 (Title Optimization)
Pass condition: Title contains (a) a number, (b) a Power Word, (c) a sentiment word
"""

import sys
import re
import json
import argparse


POWER_WORDS = [
    "hidden", "real", "actually", "truth", "warning",
    "mistake", "trap", "secret", "revealed", "alert",
    "free", "exposed", "critical", "essential", "proven"
]

POSITIVE_SENTIMENT = [
    "best", "top", "smart", "safe", "secure", "powerful",
    "effective", "proven", "essential", "critical", "free",
    "easy", "simple", "important", "right", "good", "great",
    "amazing", "incredible", "true", "correct", "strong"
]

NEGATIVE_SENTIMENT = [
    "worst", "bad", "wrong", "dangerous", "risky", "hidden",
    "mistake", "trap", "warning", "alert", "avoid", "never",
    "fail", "loss", "scam", "fraud", "fake", "exposed",
    "shocking", "terrible", "horror", "painful", "costly"
]

ALL_SENTIMENT = POSITIVE_SENTIMENT + NEGATIVE_SENTIMENT


def validate(title):
    title_lower = title.lower()
    words = re.findall(r'\b\w+\b', title_lower)

    # Check 1: Contains a number
    has_number = bool(re.search(r'\d+', title))

    # Check 2: Contains a Power Word
    found_power_words = [pw for pw in POWER_WORDS if pw in words]
    has_power_word = len(found_power_words) > 0

    # Check 3: Contains a sentiment word
    found_sentiment = [sw for sw in ALL_SENTIMENT if sw in words]
    has_sentiment = len(found_sentiment) > 0

    passed = has_number and has_power_word and has_sentiment

    details_parts = []
    if has_number:
        details_parts.append("Number: YES")
    else:
        details_parts.append("Number: MISSING")
    if has_power_word:
        details_parts.append(f"Power Word: {', '.join(found_power_words)}")
    else:
        details_parts.append("Power Word: MISSING")
    if has_sentiment:
        details_parts.append(f"Sentiment: {', '.join(found_sentiment[:3])}")
    else:
        details_parts.append("Sentiment: MISSING")

    violations = []
    if not has_number:
        violations.append("Title must contain a number (e.g., '5 Hidden...', '7 Real...')")
    if not has_power_word:
        violations.append(f"Title must contain a Power Word from: {', '.join(POWER_WORDS)}")
    if not has_sentiment:
        violations.append("Title must contain a positive or negative sentiment word")

    result = {
        "validator": "Title Check",
        "rule": "SPEC-019",
        "pass": passed,
        "details": " | ".join(details_parts),
        "violations": violations,
        "title_analyzed": title
    }

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate title optimization")
    parser.add_argument("--title", required=True, help="Article title to validate")
    args = parser.parse_args()

    result = validate(args.title)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
