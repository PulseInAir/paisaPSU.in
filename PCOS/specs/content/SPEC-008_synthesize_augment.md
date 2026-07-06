# SPEC-008: The Synthesize + Augment Rule

## Rule ID
RULE-008

## Source
Rule_v8, Section III (Content Philosophy: E-E-A-T & Originality), Rule 8

## Lock Status
**[MUTABLE]** — Can be overridden by the Founder's explicit session-specific instruction.

## Requirement
Never just "rewrite" existing articles. Every PaisaPSU article must combine multiple sources and add proprietary analysis from a PSU accountant's perspective. The article must synthesize information in a way that no single existing source provides.

**The test:** If the article could have been written by someone who only read the top 3 Google results, it fails this rule.

## Mechanical Check
- **Validator:** None (this is a qualitative judgment)
- **Enforcement:** Prompt instruction in PROMPT_topic_selection and PROMPT_research_gathering
- **Gate:** The AI must identify what proprietary angle the article adds before outlining begins

## Failure Consequence
**Reject topic.** If no original synthesis or PSU-insider perspective can be added, the topic is rejected and a new one is proposed (per SPEC-009).

## Dependencies
- SPEC-009 (Information Gain) — the specific "what's new" test
- SPEC-010 (Personal Hook) — the experience-based angle that enables synthesis

## Override Rules
Can be overridden per-article by the Founder's explicit instruction. Override is one-time only unless logged as amendment.
