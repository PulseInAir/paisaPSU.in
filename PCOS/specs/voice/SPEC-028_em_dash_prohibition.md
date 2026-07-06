# SPEC-028: Em Dash Prohibition

## Rule ID
RULE-028

## Source
Rule_v8, Section V (Writing & Voice — Humanizer Protocol), Rule 28

## Lock Status
**[MUTABLE]** (but treated as hard constraint in practice)

## Requirement
Em dashes (—) are **hard-prohibited** in all article copy and H2 titles. Run a bash scan before presenting any section. **Zero occurrences is the only passing result.**

This includes:
- Standard em dash: `—` (U+2014)
- Two-hyphen substitutes: `--`
- En dash used as em dash: `–` (U+2013) in em-dash context

## Mechanical Check
- **Validator:** `validate_em_dash.py`
- **Method:** Scan for Unicode character U+2014 (em dash) and optionally U+2013 (en dash)
- **Pass condition:** 0 occurrences of em dash
- **Scope:** Full article body text, H2 titles, SEO title

## Failure Consequence
**Fail Quality Pass item.** All em dashes must be replaced (typically with commas, periods, or restructured sentences). Full corrected text re-delivered per LAW-7.

## Dependencies
- SPEC-040 (Final Quality Pass) — checklist item 7
- PROMPT_humanizer — applies this check during drafting, not just at quality pass

## Override Rules
Technically mutable, but has never been overridden and is treated as a hard constraint in practice.
