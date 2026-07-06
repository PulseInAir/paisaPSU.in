# SPEC-035: Fact Verification

## Rule ID
RULE-035

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 35

## Lock Status
**[MUTABLE]**

## Requirement
Search and verify **all factual and regulatory claims** against primary sources before drafting begins. Flag any unverified claim with `[VERIFY]`.

This includes:
- Tax rates, thresholds, and deadlines (date-scoped by FY/AY)
- EPF/EPS contribution rates and limits
- Gratuity calculation formulas and caps
- HBA interest methods and recovery rules
- Any government notification, circular, or policy reference
- **URLs intended for use as links** (per SPEC-017) — verify before the section referencing it is drafted

### Known Recurring Fact-Check Risk Areas
- HBA interest method
- Gratuity calculation base
- Leave encashment tax treatment
- EDLI exemption rules

## Mechanical Check
- **Validator:** `validate_meta_leakage.py` catches unresolved `[VERIFY]` tags
- **Manual verification:** Web search against primary sources (income tax department, EPFO, etc.)
- **Enforcement:** PROMPT_research_gathering

## Failure Consequence
**Block drafting.** Unverified claims cannot appear in draft text. All `[VERIFY]` tags must be resolved before Quality Pass.

## Dependencies
- SPEC-004 (No Hallucinations) — the locked law this process serves
- SPEC-017 (Linking) — URL verification is part of fact verification
- SPEC-027 (No Meta-Leakage) — [VERIFY] tags must not appear in final copy

## Override Rules
Can be overridden per-claim by the Founder if he personally confirms a fact from his workplace knowledge. The Founder's own statements are still treated as unverified until checked (per Voicebank working rules).
