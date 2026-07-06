# SPEC-002: Strict Privacy

## Rule ID
RULE-002

## Source
Rule_v8, Section II (Non-Negotiable Safety & Identity), Rule 2

## Lock Status
**[LOCKED]** — Cannot be overridden by any instruction, including the Founder's.

## Requirement
Never ask for or include PAN, UAN, bank account numbers, or any private identification numbers in any article, metadata, or conversation output intended for publication. This includes hypothetical examples using real-looking number formats.

## Mechanical Check
- **Validator:** `validate_privacy.py`
- **Method:** Regex scan for PAN format (`[A-Z]{5}[0-9]{4}[A-Z]`), UAN format (`\d{12}`), bank account patterns (`\d{9,18}`), and Aadhaar-like patterns
- **Scope:** Full article text, all metadata fields

## Failure Consequence
**Block draft.** No article proceeds past Final Quality Pass with PII present. The violation must be corrected and the full corrected text re-delivered per LAW-7.

## Dependencies
- Works alongside SPEC-001 (Org Anonymity) and SPEC-006 (Case Anonymization)

## Override Rules
**No override possible.** This is a LOCKED rule.
