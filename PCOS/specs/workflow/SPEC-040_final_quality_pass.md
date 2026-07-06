# SPEC-040: Final Quality Pass — Explicit Checklist

## Rule ID
RULE-040

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 40

## Lock Status
**[STRENGTHENED in v8]**

## Requirement
All 11 items below must pass before metadata is generated. Each item requires a **verifiable check**.

### The 11-Item Checklist

| # | Check | Validator / Method | Spec |
|---|---|---|---|
| 1 | No organization name present | `validate_privacy.py` | SPEC-001 |
| 2 | No PAN, UAN, bank account numbers, or private ID data | `validate_privacy.py` | SPEC-002 |
| 3 | Credential disclaimer present with exact wording | `validate_disclaimer.py` | SPEC-003 |
| 4 | All [VERIFY] tags resolved or removed | `validate_meta_leakage.py` | SPEC-004 |
| 5 | No fabricated reactions or unconfirmed characterizations | Manual (Founder review) | SPEC-005 |
| 6 | No meta-leakage | `validate_meta_leakage.py` | SPEC-027 |
| 7 | No em dashes in copy or H2 titles | `validate_em_dash.py` | SPEC-028 |
| 8 | All paragraphs within 3-4 sentence cap | `validate_paragraph_length.py` | SPEC-023 |
| 9 | Exact focus keyword phrase in first 10% of body | `validate_keyword_placement.py` | SPEC-012 |
| 10 | Article body meets 2,000-word minimum | `validate_word_count.py` | SPEC-013 |
| 11 | Keyword density between 1.0% and 1.5% | `validate_keyword_density.py` | SPEC-015 |

### The v8 Strengthening
**If any item fails and is corrected, the complete corrected article text must be re-delivered per LAW-7 before proceeding.** A "now passing" report is not sufficient on its own.

## Mechanical Check
- **Validator:** `run_all_validators.py` (runs all applicable validators)
- **Template:** TMPL_final_quality_pass.md
- **Enforcement:** PROMPT_quality_pass

## Failure Consequence
**Block metadata generation.** All 11 items must pass. Each failure triggers a correction + full text re-delivery cycle.

## Dependencies
- All safety specs (SPEC-001 through SPEC-007)
- All voice specs (SPEC-023, SPEC-027, SPEC-028)
- SEO specs (SPEC-012, SPEC-013, SPEC-015)

## Override Rules
Individual checklist items can be overridden per-article by the Founder, but the Founder must explicitly acknowledge the override.
