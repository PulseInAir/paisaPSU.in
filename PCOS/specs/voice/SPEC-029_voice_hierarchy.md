# SPEC-029: Voice Source Hierarchy

## Rule ID
RULE-029

## Source
Rule_v8, Section V (Writing & Voice — Humanizer Protocol), Rule 29

## Lock Status
**[MUTABLE]**

## Requirement
The voice reference hierarchy for PaisaPSU articles:

1. **Primary (most reliable):** Published PaisaPSU articles on paisapsu.in
2. **Supplementary only:** `Pulak_Operational_Voicebank.md`

The published articles are the ground truth for Pulak's authentic voice. The Voicebank document may be consulted for supplementary guidance but does not override the demonstrated voice in published work.

### Current Status
- Published articles: Available at paisapsu.in (cannot be web-fetched by AI)
- VoiceBank.docx: Template-only, zero approved samples
- Pulak_Operational_Voicebank.md: Populated profile, but designed voice (not demonstrated)

## Mechanical Check
- **Validator:** None (hierarchy is a process rule)
- **Enforcement:** Prompt instruction in PROMPT_humanizer

## Failure Consequence
**No direct block.** If the AI writes in a voice that contradicts published articles, the Founder catches it during the section approval loop.

## Dependencies
- SPEC-026 (Voice Bank Consistency) — the target voice characteristics

## Override Rules
Can be overridden per-article by the Founder. One-time only.
