# SPEC-031: Gap Analysis

## Rule ID
RULE-031

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 31

## Lock Status
**[MUTABLE]**

## Requirement
Pull a live tracker list via PaisaPSU Article Tracker MCP (`list_articles`, `per_page: 100`). **Never rely on memory-stored category counts.**

Analyze the distribution across the 6 active categories:
- SAL: Salary & Pay
- TAX: Tax & ITR
- RET: Retirement & PF
- PFS: Personal Finance & Story
- INV: Investment & SIP
- INS: Insurance & Benefits

**Loan & Housing is permanently excluded from gap rotation.**

Identify which category is thinnest and would benefit most from a new article.

## Mechanical Check
- **Validator:** None (requires live MCP data)
- **Enforcement:** PROMPT_session_open executes this as mandatory Step 2
- **Fallback:** If MCP is unavailable, note in PROJECT_STATE.md and use last known counts

## Failure Consequence
**Process violation.** Topic selection without gap analysis may lead to category imbalance.

## Dependencies
- SPEC-030 (Situation Audit) — must complete before gap analysis
- SPEC-020 (Keyword Uniqueness) — tracker data also used for keyword deduplication

## Override Rules
Can be overridden by the Founder if he has a specific topic in mind regardless of gaps. One-time only.
