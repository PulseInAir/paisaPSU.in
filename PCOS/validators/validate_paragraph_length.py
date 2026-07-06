#!/usr/bin/env python3
"""
validate_paragraph_length.py — PCOS v1.0
Rule: SPEC-023 (Paragraph Discipline)
Pass condition: Every paragraph has <= 4 sentences
"""

import sys
import re
import json


# Common abbreviations that end with a period but don't end a sentence
ABBREVIATIONS = {
    'mr.', 'mrs.', 'ms.', 'dr.', 'prof.', 'sr.', 'jr.',
    'vs.', 'etc.', 'inc.', 'ltd.', 'govt.', 'dept.',
    'rs.', 'no.', 'nos.', 'approx.', 'est.', 'min.', 'max.',
    'jan.', 'feb.', 'mar.', 'apr.', 'jun.', 'jul.', 'aug.',
    'sep.', 'oct.', 'nov.', 'dec.',
    'i.e.', 'e.g.', 'viz.', 'fig.', 'ref.',
}


def count_sentences(paragraph):
    """Count sentences in a paragraph, accounting for abbreviations."""
    text = paragraph.strip()
    if not text:
        return 0

    # Replace known abbreviations with placeholders
    for abbr in ABBREVIATIONS:
        text = re.sub(re.escape(abbr), abbr.replace('.', '<DOT>'), text, flags=re.IGNORECASE)

    # Replace decimal numbers (e.g., 12.5%, Rs.500)
    text = re.sub(r'(\d)\.(\d)', r'\1<DOT>\2', text)

    # Count sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    return len(sentences)


def validate(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split into paragraphs (double newline or blank line)
    paragraphs = re.split(r'\n\s*\n', text)
    violations = []

    for i, para in enumerate(paragraphs, 1):
        para = para.strip()
        # Skip markdown headers, empty lines, lists, tables, code blocks
        if not para or para.startswith('#') or para.startswith('|') or para.startswith('```'):
            continue
        # Skip short lines (likely list items or metadata)
        if len(para) < 30:
            continue

        sentence_count = count_sentences(para)
        if sentence_count > 4:
            preview = para[:100].replace('\n', ' ')
            violations.append(f"Paragraph {i}: {sentence_count} sentences (max 4). Preview: \"{preview}...\"")

    passed = len(violations) == 0

    result = {
        "validator": "Paragraph Length",
        "rule": "SPEC-023",
        "pass": passed,
        "details": f"{len(violations)} paragraph(s) exceed 4-sentence limit" if violations else "All paragraphs within limit",
        "violations": violations
    }

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_paragraph_length.py <article_file>")
        sys.exit(1)

    result = validate(sys.argv[1])
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
