# SPEC-012: Focus Keyword Placement

## Rule ID
RULE-012

## Source
Rule_v8, Section IV (Technical SEO Guardrails), Rule 12

## Lock Status
**[MUTABLE]**

## Requirement
The primary keyword must appear as an **exact, contiguous phrase** in all four locations:
1. **SEO Title** — within the first 50 characters
2. **Meta Description** — within 120–160 characters total
3. **URL slug** — exact keyword (hyphenated)
4. **First 10% of article body** — exact phrase present

Confirm with an exact-string search before the Final Quality Pass.

## Mechanical Check
- **Validator:** `validate_keyword_placement.py`
- **Method:** Takes article text + keyword + metadata as input; checks all four placements
- **Scope:** Article body (first 10%), SEO title, meta description, slug

## Failure Consequence
**Fail Quality Pass item.** The missing placement must be corrected and full text re-delivered per LAW-7.

## Dependencies
- SPEC-041 (Metadata Checklist) — generates SEO title, meta description, slug
- SPEC-015 (Keyword Density) — overall keyword frequency

## Override Rules
Can be overridden per-article by the Founder. One-time only.
