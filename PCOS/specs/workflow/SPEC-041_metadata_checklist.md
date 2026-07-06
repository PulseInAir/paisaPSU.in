# SPEC-041: Metadata Checklist

## Rule ID
RULE-041

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 41

## Lock Status
**[MUTABLE]**

## Requirement
After the Final Quality Pass (SPEC-040) completes with all items passing, generate the following metadata:

| Field | Requirements | Validator |
|---|---|---|
| **SEO Title** | Focus keyword in first 50 chars; number + power word + sentiment | `validate_title.py` |
| **Meta Description** | 120–160 characters; contains focus keyword | Length check |
| **URL Slug** | Contains focus keyword; total URL ≤ 75 chars | `validate_url_length.py` |
| **Featured Image Idea** | One dynamic, article-specific image; specify which H2 it represents | Manual |
| **Alt Text** | Carries exact focus keyword phrase | Manual check |
| **Tags** | Real, search-relevant terms; not just the primary keyword | Manual |

### Iteration Rule
Do not present any field that fails its own mechanical check. **Iterate privately** until every field passes, then present the complete metadata block.

## Mechanical Check
- **Validators:** `validate_title.py`, `validate_url_length.py`
- **Template:** TMPL_metadata_checklist.md
- **Enforcement:** PROMPT_metadata_generation

## Failure Consequence
**Iterate privately.** The Founder should only see passing metadata. If the Founder rejects a field, revise and re-present.

## Dependencies
- SPEC-040 (Final Quality Pass) — must complete before metadata generation
- SPEC-012 (Keyword Placement) — keyword requirements for title, slug, description
- SPEC-018 (Media Count) — image idea format
- SPEC-019 (Title Optimization) — title format requirements

## Override Rules
Can be overridden per-field by the Founder. One-time only.
