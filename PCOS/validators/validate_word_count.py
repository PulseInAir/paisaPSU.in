#!/usr/bin/env python3
"""
validate_word_count.py — PCOS v1.0
Rule: SPEC-013 (Minimum Word Count)
Pass condition: >= 2,000 words
"""

import sys
import re
import json


def count_words(text):
    """Count words in article text, excluding markdown syntax and HTML tags."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove markdown image/link syntax
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[([^\]]+)\]\(.*?\)', r'\1', text)
    # Remove markdown headers (#)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove markdown bold/italic markers
    text = re.sub(r'\*{1,3}', '', text)
    text = re.sub(r'_{1,3}', '', text)
    # Split on whitespace and count non-empty tokens
    words = [w for w in text.split() if w.strip()]
    return len(words)


def validate(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    word_count = count_words(text)
    passed = word_count >= 2000

    result = {
        "validator": "Word Count",
        "rule": "SPEC-013",
        "pass": passed,
        "details": f"{word_count:,} words {'(PASS: >= 2,000)' if passed else '(FAIL: < 2,000)'}",
        "violations": [] if passed else [f"Article has {word_count:,} words, needs at least 2,000"]
    }

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_word_count.py <article_file>")
        sys.exit(1)

    result = validate(sys.argv[1])
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
