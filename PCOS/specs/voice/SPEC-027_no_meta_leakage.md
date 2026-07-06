# SPEC-027: No Meta-Leakage

## Rule ID
RULE-027

## Source
Rule_v8, Section V (Writing & Voice — Humanizer Protocol), Rule 27

## Lock Status
**[MUTABLE]**

## Requirement
The following must **never** appear in reader-facing article copy:
- Internal outline numbers (1., 2., 3. from the drafting skeleton)
- Section labels ("Section A:", "Part 2:")
- Unresolved `[VERIFY]` tags
- `TODO` brackets
- Citation markup (`[1]`, `(Source: ...)` in academic format)
- Any other drafting scaffolding

## Mechanical Check
- **Validator:** `validate_meta_leakage.py`
- **Method:** Regex scan for: `[VERIFY]`, `TODO`, `[DRAFT]`, `[NOTE]`, `[EDIT]`, `[SOURCE]`, numbered outline patterns, citation brackets
- **Pass condition:** 0 matches
- **Scope:** Full article body text, H2 titles

## Failure Consequence
**Fail Quality Pass item.** All scaffolding must be removed. Full corrected text re-delivered per LAW-7.

## Dependencies
- SPEC-004 (No Hallucinations) — [VERIFY] tags are part of the fact-check process
- SPEC-040 (Final Quality Pass) — checklist item 6

## Override Rules
Can be overridden per-article by the Founder. One-time only.
