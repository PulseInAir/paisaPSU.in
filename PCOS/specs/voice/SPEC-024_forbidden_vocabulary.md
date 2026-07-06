# SPEC-024: Forbidden Vocabulary

## Rule ID
RULE-024

## Source
Rule_v8, Section V (Writing & Voice — Humanizer Protocol), Rule 24

## Lock Status
**[MUTABLE]**

## Requirement
Delete AI fingerprints. The following words and phrases are forbidden in all article copy:

### Forbidden List
- "delve"
- "navigate the complexities"
- "unlock"
- "journey"
- "realm"
- "in today's fast-paced world"

### Extended List (from Voicebank anti-patterns)
- "landscape"
- "game-changer"
- "in conclusion"

Run the humanizer pass **before** drafting, not after.

## Mechanical Check
- **Validator:** `validate_forbidden_words.py`
- **Method:** Case-insensitive scan for each forbidden word/phrase
- **Pass condition:** 0 matches from the forbidden list
- **Source file:** `reference/forbidden_words.txt`
- **Scope:** Full article body text, H2 titles

## Failure Consequence
**Fail Quality Pass.** Forbidden words must be replaced with natural alternatives. Full corrected text re-delivered per LAW-7.

## Dependencies
- SPEC-026 (Voice Bank Consistency) — natural vocabulary to use instead
- Reference file: `forbidden_words.txt`

## Override Rules
Can be overridden per-word by the Founder if a forbidden word is genuinely the correct term in context. One-time only.
