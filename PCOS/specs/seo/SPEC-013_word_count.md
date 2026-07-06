# SPEC-013: Minimum Word Count

## Rule ID
RULE-013

## Source
Rule_v8, Section IV (Technical SEO Guardrails), Rule 13

## Lock Status
**[MUTABLE]**

## Requirement
Every article must be a minimum of **2,000 words**. Word count must be verified by tool (bash/Python `wc`) before the Final Quality Pass — not estimated.

If the article falls short, the Rapid-Fire Q&A (SPEC-034) must gather enough detail to support this floor. If expansion is needed after the quality pass, the corrected full text must be delivered per LAW-7.

## Mechanical Check
- **Validator:** `validate_word_count.py`
- **Method:** Counts words in article text (excluding metadata, HTML tags, markdown syntax)
- **Pass condition:** ≥ 2,000 words
- **Scope:** Full article body text

## Failure Consequence
**Fail Quality Pass item.** Article must be expanded. Full corrected text re-delivered per LAW-7.

## Dependencies
- SPEC-034 (Rapid-Fire Questioning) — gathers enough material to support word count
- SPEC-040 (Final Quality Pass) — checklist item 9

## Override Rules
Can be overridden per-article by the Founder. One-time only.
