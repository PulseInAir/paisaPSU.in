# SPEC-011: Honest Returns

## Rule ID
RULE-011

## Source
Rule_v8, Section III (Content Philosophy: E-E-A-T & Originality), Rule 11

## Lock Status
**[LOCKED]** — Cannot be overridden by any instruction, including the Founder's.

## Requirement
- Use a realistic **12% long-term equity average** for all investment calculations
- Never promise "guaranteed" returns
- Never use language implying certainty of investment outcomes
- All return projections must be clearly labeled as projections, not guarantees

## Mechanical Check
- **Validator:** `validate_forbidden_words.py` includes "guaranteed returns" and "guaranteed profit" in its pattern list
- **Manual verification:** The AI must verify any calculation using return assumptions during PROMPT_section_drafting
- **Scope:** Full article text, particularly in Investment & SIP (INV) category articles

## Failure Consequence
**Block draft.** Return claims that promise guarantees or use unrealistic projections must be corrected. Full corrected text re-delivered per LAW-7.

## Dependencies
- SPEC-004 (No Hallucinations) — return figures are factual claims subject to the same verification standard

## Override Rules
**No override possible.** This is a LOCKED rule.
