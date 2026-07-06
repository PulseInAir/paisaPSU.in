# Template: Final Quality Pass Checklist

**Article Title:** _______________
**Focus Keyword:** _______________
**Date:** _______________

---

## Quality Pass Results

| # | Check | Result | Details |
|---|---|---|---|
| 1 | No organization name present (SPEC-001) | ☐ PASS / ☐ FAIL | |
| 2 | No PAN, UAN, bank account numbers, or private ID data (SPEC-002) | ☐ PASS / ☐ FAIL | |
| 3 | Credential disclaimer present with exact wording (SPEC-003) | ☐ PASS / ☐ FAIL | |
| 4 | All [VERIFY] tags resolved or removed (SPEC-004) | ☐ PASS / ☐ FAIL | |
| 5 | No fabricated reactions or unconfirmed characterizations (SPEC-005) | ☐ PASS / ☐ FAIL | Founder-verified |
| 6 | No meta-leakage (SPEC-027) | ☐ PASS / ☐ FAIL | |
| 7 | No em dashes (—) in copy or H2 titles (SPEC-028) | ☐ PASS / ☐ FAIL | |
| 8 | All paragraphs within 3-4 sentence cap (SPEC-023) | ☐ PASS / ☐ FAIL | |
| 9 | Exact focus keyword phrase in first 10% of body (SPEC-012) | ☐ PASS / ☐ FAIL | |
| 10 | Article body meets 2,000-word minimum (SPEC-013) | ☐ PASS / ☐ FAIL | Word count: ___ |
| 11 | Keyword density between 1.0% and 1.5% (SPEC-015) | ☐ PASS / ☐ FAIL | Density: ___% |

---

## Validator Command
```bash
python run_all_validators.py article.txt --keyword "FOCUS_KEYWORD_HERE"
```

## Result Summary
- **Passed:** ___/11
- **Failed:** ___/11
- **Action Required:** _______________

## If Any Item Failed
Per LAW-7 (SPEC-007): The complete corrected article text must be re-delivered before proceeding to metadata generation. A "now passing" report alone is not sufficient.

---

*Template: TMPL_final_quality_pass.md — PCOS v1.0*
