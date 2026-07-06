# SPEC-046: Image and Decision Revision Protocols

## Rule ID
RULE-046

## Source
Rule_v8, Section VIII (Amendment Discipline), Rule 46

## Lock Status
**[MUTABLE]**

## Requirement
### Image Revision
If the Founder rejects a proposed image idea, generate a **replacement mapped to the same section**. Do not drop the image requirement — iterate until accepted.

### Decision Revision
If the Founder wants to reopen a topic decision after drafting has already begun, treat it as a **fresh Recommendation step restart** (SPEC-032), not a silent pivot mid-draft.

This means:
1. Acknowledge the pivot explicitly
2. Return to SPEC-032 (topic recommendation)
3. The existing draft work is abandoned or saved in PROJECT_STATE.md
4. A new outline and tracker record may be needed

## Mechanical Check
- **Validator:** None (process rule)
- **Enforcement:** PROMPT_section_drafting (image revision), PROMPT_topic_selection (decision revision)

## Failure Consequence
**Process violation.** Silent pivots or dropped image requirements are workflow errors.

## Dependencies
- SPEC-018 (Media Count) — image requirements
- SPEC-032 (Recommendation) — topic selection restart

## Override Rules
Can be overridden by the Founder. One-time only.
