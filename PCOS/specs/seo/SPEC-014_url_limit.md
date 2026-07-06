# SPEC-014: 75-Character URL Limit

## Rule ID
RULE-014

## Source
Rule_v8, Section IV (Technical SEO Guardrails), Rule 14

## Lock Status
**[MUTABLE]**

## Requirement
The total URL — including `https://paisapsu.in/` — must be **75 characters or less**. The slug must include the focus keyword.

**Calculation:** `https://paisapsu.in/` = 21 characters, leaving 54 characters for the slug.

## Mechanical Check
- **Validator:** `validate_url_length.py`
- **Method:** Concatenates base URL + slug, counts total characters
- **Pass condition:** ≤ 75 characters total
- **Input:** Slug string

## Failure Consequence
**Fail metadata check.** Slug must be shortened while retaining the focus keyword. Iterate privately until passing (per SPEC-041).

## Dependencies
- SPEC-012 (Keyword Placement) — slug must contain the focus keyword
- SPEC-041 (Metadata Checklist) — slug is generated at this step

## Override Rules
Can be overridden per-article by the Founder. One-time only.
