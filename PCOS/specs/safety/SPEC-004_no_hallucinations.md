# SPEC-004: No Hallucinations

## Rule ID
RULE-004

## Source
Rule_v8, Section II (Non-Negotiable Safety & Identity), Rule 4

## Lock Status
**[LOCKED]** — Cannot be overridden by any instruction, including the Founder's.

## Requirement
Every factual claim must be verified against primary sources before drafting. If a rule changed or a number is uncertain, flag it with a `[VERIFY]` tag. Never guess.

All `[VERIFY]` tags must be resolved or removed before the Final Quality Pass is complete.

**URLs are factual claims** — any URL intended for use as a link (internal or external) must be verified with the same rigor as a statistic (per SPEC-017).

## Mechanical Check
- **Validator:** `validate_meta_leakage.py` (checks for unresolved `[VERIFY]` tags)
- **Manual verification:** Fact verification is done via web search during PROMPT_research_gathering and PROMPT_section_drafting phases — this cannot be fully automated
- **Scope:** Full article text

## Failure Consequence
**Block draft.** Unresolved `[VERIFY]` tags block the Final Quality Pass. The AI must resolve each tag (verify or remove with justification) and re-deliver full corrected text per LAW-7.

## Dependencies
- SPEC-035 (Fact Verification) defines the verification process
- SPEC-017 (Linking) extends this rule to URLs
- SPEC-027 (No Meta-Leakage) overlaps on the `[VERIFY]` tag detection

## Override Rules
**No override possible.** This is a LOCKED rule. No factual claim ships unverified.
