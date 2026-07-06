#!/usr/bin/env python3
"""
validate_keyword_density.py — PCOS v1.0
Rule: SPEC-015 (Keyword Density)
Pass condition: 1.0% <= density <= 1.5%
"""

import sys
import re
import json
import argparse


def count_words(text):
    """Count words in article text."""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[([^\]]+)\]\(.*?\)', r'\1', text)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\*{1,3}', '', text)
    text = re.sub(r'_{1,3}', '', text)
    words = [w for w in text.split() if w.strip()]
    return len(words)


def count_keyword_occurrences(text, keyword):
    """Count exact phrase occurrences of the keyword (case-insensitive)."""
    # Clean text for counting
    text_clean = re.sub(r'<[^>]+>', '', text)
    text_clean = re.sub(r'\*{1,3}', '', text_clean)
    text_clean = re.sub(r'_{1,3}', '', text_clean)

    pattern = re.escape(keyword)
    matches = re.findall(pattern, text_clean, re.IGNORECASE)
    return len(matches)


def validate(filepath, keyword):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    total_words = count_words(text)
    keyword_occurrences = count_keyword_occurrences(text, keyword)
    keyword_word_count = len(keyword.split())

    if total_words == 0:
        density = 0
    else:
        density = (keyword_occurrences * keyword_word_count) / total_words * 100

    passed = 1.0 <= density <= 1.5

    result = {
        "validator": "Keyword Density",
        "rule": "SPEC-015",
        "pass": passed,
        "details": f"{density:.2f}% ({keyword_occurrences} occurrences of '{keyword}' in {total_words:,} words)",
        "violations": []
    }

    if density < 1.0:
        result["violations"].append(f"Density {density:.2f}% is below 1.0% minimum. Add ~{int((1.0 * total_words / (keyword_word_count * 100)) - keyword_occurrences)} more occurrences.")
    elif density > 1.5:
        result["violations"].append(f"Density {density:.2f}% exceeds 1.5% maximum. Remove ~{int(keyword_occurrences - (1.5 * total_words / (keyword_word_count * 100)))} occurrences.")

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate keyword density (1.0-1.5%)")
    parser.add_argument("filepath", help="Path to article text file")
    parser.add_argument("--keyword", required=True, help="Focus keyword phrase")
    args = parser.parse_args()

    result = validate(args.filepath, args.keyword)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
