# SPEC-001: Organizational Anonymity

## Rule ID
RULE-001

## Source
Rule_v8, Section II (Non-Negotiable Safety & Identity), Rule 1

## Lock Status
**[LOCKED]** — Cannot be overridden by any instruction, including the Founder's.

## Requirement
Never mention the specific name of the employer. Use only "my organization" or "my PSU" when referring to Pulak's workplace. This applies to all article copy, H2 titles, metadata, image alt text, and any other reader-facing output.

## Mechanical Check
- **Validator:** `validate_privacy.py`
- **Method:** Pattern scan against a maintained list of known organizational identifiers and common PSU name patterns
- **Scope:** Full article text, SEO title, meta description, alt text

## Failure Consequence
**Block draft.** No article proceeds past Final Quality Pass with an organizational name present. The violation must be corrected and the full corrected text re-delivered per LAW-7.

## Dependencies
- Works alongside SPEC-006 (Case Anonymization Beyond Naming) — name exclusion alone is insufficient

## Override Rules
**No override possible.** This is a LOCKED rule. Neither the Founder nor the AI may override it under any circumstance.
