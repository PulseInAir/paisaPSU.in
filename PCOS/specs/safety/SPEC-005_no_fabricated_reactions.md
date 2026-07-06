# SPEC-005: No Fabricated Reactions

## Rule ID
RULE-005

## Source
Rule_v8, Section II (Non-Negotiable Safety & Identity), Rule 5

## Lock Status
**[LOCKED]** — Cannot be overridden by any instruction, including the Founder's.

## Requirement
Personal reactions, internal states, or characterizations not explicitly stated by the Founder (Pulak) must never be invented to fill a narrative gap. If a section needs a personal reaction, the AI must ask first and wait for the Founder's explicit confirmation before including it.

This applies to:
- Emotional reactions ("I was shocked when...")
- Internal thoughts ("I immediately realized...")
- Characterizations of colleagues or situations
- Any attribution of feeling, motivation, or judgment to the Founder

## Mechanical Check
- **Validator:** None (this cannot be mechanically verified)
- **Enforcement:** Prompt instruction in PROMPT_research_gathering and PROMPT_section_drafting
- **Gate:** Founder reviews each section and can reject fabricated reactions

## Failure Consequence
**Reject section.** The AI must remove the fabricated reaction and either ask the Founder for the real reaction or rewrite the section without one. Full corrected text re-delivered per LAW-7.

## Dependencies
- SPEC-033 (Personal Hook Gather) — the process for collecting authentic reactions
- SPEC-010 (Personal Hook) — the hook must be confirmed by the Founder

## Override Rules
**No override possible.** This is a LOCKED rule. Source: Audit of Article 29 — invented reactions added without author confirmation.
