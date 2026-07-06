# Category Codes — PCOS v1.0

## Active Categories (6)

| Code | Category | Status | Notes |
|---|---|---|---|
| `SAL` | Salary & Pay | **Active** | PSU salary structure, DA, HRA, allowances |
| `TAX` | Tax & ITR | **Active** | ITR filing, TDS, AIS/TIS, tax-saving (seasonal spikes Jun-Jul) |
| `RET` | Retirement & PF | **Active** | EPF, EPS, gratuity, superannuation, claims |
| `PFS` | Personal Finance & Story | **Active** | Personal experiences, financial decisions, reader trust |
| `INV` | Investment & SIP | **Active** | SIP, mutual funds, equity (12% long-term average) |
| `INS` | Insurance & Benefits | **Active** | Group insurance, medical benefits, LTC, CGHS |

## Excluded Categories

| Code | Category | Status | Reason |
|---|---|---|---|
| `LNH` | Loan & Housing | **Permanently excluded** | Sub-topic is saturated (Rule_v8, Appendix A) |

## Topic Exclusions (Standalone)

| Topic | Status | Reason |
|---|---|---|
| NPS (National Pension System) | **Never propose** | Founder's PSU does not offer NPS |
| EDLI (Employees' Deposit Linked Insurance) | **Never propose** | Already covered in PPSU-000296; org has own group scheme |

## Gap Analysis Notes
- Gap rotation uses only the 6 active categories
- Pull live counts via `list_articles(per_page: 100)` at every session open
- Never rely on memorized or cached category counts
- The thinnest active category gets priority (unless the Founder overrides)
