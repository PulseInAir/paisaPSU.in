#!/usr/bin/env python3
"""
validate_privacy.py — PCOS v1.0
Rules: SPEC-001 (Org Anonymity), SPEC-002 (Strict Privacy), SPEC-006 (Case Anonymization)
Pass condition: No organizational names, PAN, UAN, bank account numbers, or PII patterns found
"""

import sys
import re
import json


# PII patterns
PII_PATTERNS = [
    # PAN format: 5 letters + 4 digits + 1 letter (e.g., ABCDE1234F)
    (r'\b[A-Z]{5}\d{4}[A-Z]\b', 'PAN number pattern'),
    # UAN format: 12 digits
    (r'\b\d{12}\b', 'Possible UAN (12-digit number)'),
    # Aadhaar format: 4-4-4 digits
    (r'\b\d{4}\s?\d{4}\s?\d{4}\b', 'Possible Aadhaar pattern'),
    # Bank account: 9-18 consecutive digits (common Indian bank account lengths)
    (r'\b\d{9,18}\b', 'Possible bank account number'),
    # IFSC code
    (r'\b[A-Z]{4}0[A-Z0-9]{6}\b', 'IFSC code pattern'),
]

# Words/phrases that suggest organizational identification
# These are examples — the Founder should customize this list
ORG_PATTERNS = [
    # Common PSU identifiers that might leak
    # (intentionally generic to avoid naming any specific org)
    (r'\b(?:my company|our company|the company)\b', 'Company reference (use "my organization" or "my PSU")'),
]


def validate(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')
    violations = []

    # Check PII patterns
    for pattern, name in PII_PATTERNS:
        for i, line in enumerate(lines, 1):
            # Skip if the pattern is within a clearly illustrative context
            matches = re.finditer(pattern, line)
            for match in matches:
                # Don't flag years (4 digits) or common non-PII numbers
                matched_text = match.group()
                if len(matched_text) <= 4:
                    continue
                # Don't flag numbers in monetary context (Rs. 50000, etc.)
                before = line[:match.start()].strip()
                if before.endswith(('Rs.', 'Rs', 'INR', '$', 'rupees')):
                    continue
                # Don't flag article IDs like PPSU-000296
                if re.match(r'PPSU-\d+', matched_text):
                    continue

                context = line.strip()[:80]
                violations.append(f"Line {i}: {name} detected: \"{context}\"")

    # Check organizational name patterns
    for pattern, name in ORG_PATTERNS:
        for i, line in enumerate(lines, 1):
            matches = re.finditer(pattern, line, re.IGNORECASE)
            for match in matches:
                context = line.strip()[:80]
                violations.append(f"Line {i}: {name}: \"{context}\"")

    passed = len(violations) == 0

    result = {
        "validator": "Privacy Check",
        "rule": "SPEC-001, SPEC-002, SPEC-006",
        "pass": passed,
        "details": "No organizational names or PII found" if passed else f"{len(violations)} potential privacy issue(s)",
        "violations": violations
    }

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_privacy.py <article_file>")
        sys.exit(1)

    result = validate(sys.argv[1])
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["pass"] else 1)
