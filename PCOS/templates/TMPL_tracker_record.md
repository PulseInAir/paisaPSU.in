# Template: Tracker Record

Use this template to create and verify a tracker record via PaisaPSU Article Tracker MCP.

---

## Fields to Set at Record Creation (SPEC-037)

| # | Field | Value | Status |
|---|---|---|---|
| 1 | Article ID | (auto-generated) | — |
| 2 | Article title | _______________ | |
| 3 | Primary keyword | _______________ | |
| 4 | Article category | _______________ | |
| 5 | Article status | Outlining | |
| 6 | Planned publication date | _______________ | |
| 7 | Created date | (auto) | — |

---

## Fields to Update During Workflow

| # | Field | When to Update | Value |
|---|---|---|---|
| 8 | Article status | At each phase change | Outlining → Drafting → Reviewing → Ready → Published |
| 9 | Research completed | After SPEC-035 | ☐ |
| 10 | Outline approved | After SPEC-036 | ☐ |
| 11 | Draft completed | After all sections approved | ☐ |
| 12 | Fact-check completed | After SPEC-035 | ☐ |
| 13 | Authenticity check completed | After SPEC-005 review | ☐ |
| 14 | Final review completed | After SPEC-040 | ☐ |
| 15 | SEO completed | After SPEC-041 | ☐ |
| 16 | Featured image completed | Founder-confirmed | ☐ |
| 17 | Internal links added | After SPEC-017 | ☐ |
| 18 | External sources added | After SPEC-017 | ☐ |

---

## Fields to Set at Publication Close (SPEC-042)

| # | Field | Value |
|---|---|---|
| 19 | Actual publication date | _______________ (do NOT assume "today") |
| 20 | WordPress post ID | _______________ (from admin URL) |
| 21 | WordPress post URL | _______________ |
| 22 | Last updated date | (auto) |

---

## Notes Field (for fields without dedicated tracker columns)

```
Keyword Density: ____%
Media Count: 1 (default) / ___ (custom)
Tags: tag1, tag2, tag3, tag4, tag5
```

---

## Verification
After every MCP write operation, call `get_article` to confirm stored values match.

---

*Template: TMPL_tracker_record.md — PCOS v1.0*
