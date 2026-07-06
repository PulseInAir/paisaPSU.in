# SPEC-003: Credential Transparency

## Rule ID
RULE-003

## Source
Rule_v8, Section II (Non-Negotiable Safety & Identity), Rule 3

## Lock Status
**[LOCKED]** — Cannot be overridden by any instruction, including the Founder's.

## Requirement
Every article must include a disclaimer using this **exact wording**:

> "I am not a SEBI-registered advisor or a CA, and views expressed are personal."

Partial disclaimers, paraphrased versions, or disclaimers missing any of the three components (SEBI, CA, personal views) fail this rule.

## Mechanical Check
- **Validator:** `validate_disclaimer.py`
- **Method:** Exact string match for the disclaimer text
- **Scope:** Full article text
- **Placement:** Must appear at least once, either within the opening two sections or the closing section (per SPEC-043)

## Failure Consequence
**Block draft.** No article proceeds past Final Quality Pass without the exact disclaimer. The violation must be corrected and the full corrected text re-delivered per LAW-7.

## Dependencies
- SPEC-043 (Disclaimer Placement) defines WHERE the disclaimer must appear

## Override Rules
**No override possible.** This is a LOCKED rule. The wording is fixed — not even the Founder may alter it per-article.
