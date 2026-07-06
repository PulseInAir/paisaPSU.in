# SPEC-006: Case Anonymization Beyond Naming

## Rule ID
RULE-006

## Source
Rule_v8, Section II (Non-Negotiable Safety & Identity), Rule 6

## Lock Status
**[LOCKED]** — Cannot be overridden by any instruction, including the Founder's.

## Requirement
When citing a real colleague situation in an article, strip **all** identifying specifics — not just the name. This includes:
- Approximate timing ("last month," "in March")
- Department name or function
- Grade or pay level
- Seniority markers ("senior manager," "joined 20 years ago")
- Any combination of details that could narrow identification to a specific person in a small office

The name exclusion alone is insufficient. The test is: could a colleague in the same organization read this and identify the person? If yes, it fails.

## Mechanical Check
- **Validator:** `validate_privacy.py` (partial — scans for grade/department patterns)
- **Manual verification:** The AI must flag any real-person case study for the Founder's review during PROMPT_section_drafting
- **Scope:** Full article text

## Failure Consequence
**Block draft.** Identifiable cases must be further anonymized or removed. Full corrected text re-delivered per LAW-7.

## Dependencies
- Works alongside SPEC-001 (Org Anonymity) and SPEC-002 (Strict Privacy)
- SPEC-033 (Personal Hook Gather) — cases are collected during this phase

## Override Rules
**No override possible.** This is a LOCKED rule. Source: Small-office identifiability risk.
