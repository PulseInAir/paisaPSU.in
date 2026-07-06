# SPEC-043: Credential Transparency — Placement

## Rule ID
RULE-043

## Source
Rule_v8, Section VIII (Amendment Discipline), Rule 43

## Lock Status
**[MUTABLE]**

## Requirement
The exact-wording disclaimer (SPEC-003) must appear at least once, either:
- Within the **opening two sections** of the article, OR
- In the **closing section** of the article

## Mechanical Check
- **Validator:** `validate_disclaimer.py` (checks for presence; placement is a secondary check)
- **Enforcement:** PROMPT_section_drafting — the AI should place the disclaimer during the opening or closing section

## Failure Consequence
**Fail Quality Pass.** Disclaimer must be repositioned. Full corrected text re-delivered per LAW-7.

## Dependencies
- SPEC-003 (Credential Transparency) — the locked rule defining the exact wording

## Override Rules
Can be overridden per-article by the Founder regarding placement (but not wording). One-time only.
