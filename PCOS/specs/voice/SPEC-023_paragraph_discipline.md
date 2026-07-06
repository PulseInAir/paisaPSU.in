# SPEC-023: Paragraph Discipline

## Rule ID
RULE-023

## Source
Rule_v8, Section V (Writing & Voice — Humanizer Protocol), Rule 23

## Lock Status
**[MUTABLE]**

## Requirement
Maximum **3-4 sentences per paragraph**. Enforced mechanically via bash/Python sentence count before presenting any section as complete.

## Mechanical Check
- **Validator:** `validate_paragraph_length.py`
- **Method:** Split text into paragraphs, count sentences per paragraph using period/exclamation/question mark delimiters (accounting for abbreviations like "Dr.", "Mr.", "Rs.", "etc.")
- **Pass condition:** Every paragraph has ≤ 4 sentences
- **Scope:** Full article body text

## Failure Consequence
**Fail Quality Pass item.** Long paragraphs must be split. Full corrected text re-delivered per LAW-7.

## Dependencies
- SPEC-040 (Final Quality Pass) — checklist item 7

## Override Rules
Can be overridden per-article by the Founder. One-time only.
