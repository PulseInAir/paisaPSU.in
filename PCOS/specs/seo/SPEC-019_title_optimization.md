# SPEC-019: Title Optimization

## Rule ID
RULE-019

## Source
Rule_v8, Section IV (Technical SEO Guardrails), Rule 19

## Lock Status
**[MUTABLE]**

## Requirement
Every title must include all three elements:
1. **A number** (e.g., "5 Hidden...", "7 Real...")
2. **A Power Word** from the approved list
3. **A positive or negative sentiment word**

### Approved Power Word List
Hidden, Real, Actually, Truth, Warning, Mistake, Trap, Secret, Revealed, Alert, Free, Exposed, Critical, Essential, Proven

## Mechanical Check
- **Validator:** `validate_title.py`
- **Method:** Checks for: (a) at least one digit/number word, (b) at least one word from the power word list, (c) at least one sentiment word (from a curated positive/negative sentiment list)
- **Pass condition:** All three elements present
- **Timing:** Checked at H2 Outline Gate (SPEC-036) and again at Final Quality Pass (SPEC-040)

## Failure Consequence
**Block outline approval.** Title must be revised to include all three elements before proceeding.

## Dependencies
- SPEC-036 (H2 Outline Gate) — first enforcement point
- SPEC-012 (Keyword Placement) — keyword must also be in the title

## Override Rules
Can be overridden per-article by the Founder. One-time only.
