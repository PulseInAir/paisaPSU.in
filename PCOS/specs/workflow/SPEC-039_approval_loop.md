# SPEC-039: Approval Loop

## Rule ID
RULE-039

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 39

## Lock Status
**[MUTABLE]**

## Requirement
Move to the next section **only after explicit approval** from the Founder.

### Valid Approval Signals
- Pasting the next H2 title (implicit "approved, continue")
- Single-word confirmations ("ok", "good", "approved", "next")
- Any clear affirmative signal

### Not Valid Approval Signals
- Silence (the AI must not proceed without a signal)
- Ambiguous responses (the AI should ask for clarification)

## Mechanical Check
- **Validator:** None (conversational process rule)
- **Enforcement:** PROMPT_section_drafting — the AI must wait for approval before writing the next H2

## Failure Consequence
**Process violation.** Writing ahead without approval wastes tokens and may produce content the Founder doesn't want.

## Dependencies
- SPEC-038 (Section Writing) — what is being approved
- SPEC-036 (H2 Outline Gate) — the approved outline defines the section sequence

## Override Rules
Can be overridden by the Founder if he explicitly says "write all remaining sections" or similar batch instruction. One-time only.
