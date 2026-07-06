# SPEC-009: Information Gain

## Rule ID
RULE-009

## Source
Rule_v8, Section III (Content Philosophy: E-E-A-T & Originality), Rule 9

## Lock Status
**[MUTABLE]** — Can be overridden by the Founder's explicit session-specific instruction.

## Requirement
Every post must provide a detail, insight, or synthesis that current search results lack. If no original insight can be added, **reject the topic**.

**Information Gain sources for PaisaPSU:**
- First-hand PSU workplace experience (payroll, HR, accounts)
- Real (anonymized) colleague situations
- Informal tax-filing practice observations
- Calculation mechanics that generic articles get wrong
- Date-scoped regulatory specifics that generic articles omit

## Mechanical Check
- **Validator:** None (qualitative judgment)
- **Enforcement:** Prompt instruction in PROMPT_topic_selection
- **The AI must state:** "The information gain for this article is: [specific insight]" before proceeding to outline

## Failure Consequence
**Reject topic.** The AI proposes a replacement. If no replacement meets the standard, the session pivots to content maintenance or gap analysis.

## Dependencies
- SPEC-008 (Synthesize + Augment) — the broader synthesis requirement
- SPEC-031 (Gap Analysis) — identifies where information gain is most needed

## Override Rules
Can be overridden per-article by the Founder's explicit instruction. Override is one-time only.
