# SPEC-015: Keyword Density

## Rule ID
RULE-015

## Source
Rule_v8, Section IV (Technical SEO Guardrails), Rule 15

## Lock Status
**[MUTABLE]**

## Requirement
Maintain a strict keyword density between **1.0% and 1.5%**. Density must be calculated mechanically, not estimated.

**Formula:** `(keyword occurrences × words in keyword) / total word count × 100`

This is Final Quality Pass checklist item 11 (SPEC-040).

## Mechanical Check
- **Validator:** `validate_keyword_density.py`
- **Method:** Counts exact keyword phrase occurrences (case-insensitive), calculates density
- **Pass condition:** 1.0% ≤ density ≤ 1.5%
- **Input:** Article text + focus keyword phrase

## Failure Consequence
**Fail Quality Pass item.** If density is too low, add natural keyword occurrences. If too high, remove or rephrase some. Full corrected text re-delivered per LAW-7.

## Dependencies
- SPEC-013 (Word Count) — total word count is a component of density calculation
- SPEC-040 (Final Quality Pass) — checklist item 11

## Override Rules
Can be overridden per-article by the Founder. One-time only.

## Tracker Note
Keyword Density has no dedicated tracker field. Log the calculated density in the tracker's free-text notes field at Scoreboard Tracking (SPEC-042).
