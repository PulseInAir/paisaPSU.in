# SPEC-016: Subheadings with Focus Keyword

## Rule ID
RULE-016

## Source
Rule_v8, Section IV (Technical SEO Guardrails), Rule 16

## Lock Status
**[MUTABLE]**

## Requirement
At least **2 of the H2 headings** must carry the exact focus keyword phrase or a tight variant. Confirmed by mechanical grep at the outline gate (SPEC-036).

## Mechanical Check
- **Validator:** Grep scan during PROMPT_outline_approval
- **Method:** Case-insensitive exact-match search for the keyword phrase in all H2 headings
- **Pass condition:** ≥ 2 H2 headings contain the keyword
- **Timing:** Checked at the H2 Outline gate, not at Final Quality Pass

## Failure Consequence
**Block outline approval.** H2 headings must be revised to include the keyword before proceeding to section writing.

## Dependencies
- SPEC-036 (H2 Outline Gate) — where this check is enforced
- SPEC-012 (Keyword Placement) — broader keyword placement requirements

## Override Rules
Can be overridden per-article by the Founder. One-time only.
