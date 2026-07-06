# SPEC-022: Tags

## Rule ID
RULE-022

## Source
Rule_v8, Section IV (Technical SEO Guardrails), Rule 22

## Lock Status
**[MUTABLE]**

## Requirement
Every article must have a generated set of WordPress tags produced at the Metadata Checklist step (SPEC-041). Tags must:
- Reflect **real, search-relevant terms**
- Be **distinct from** simply repeating the primary keyword alone
- Cover related search queries a PSU employee might use

## Mechanical Check
- **Validator:** None (qualitative — tag relevance is a judgment call)
- **Enforcement:** Prompt instruction in PROMPT_metadata_generation
- **Tracker:** Tags have no dedicated tracker field. Log in the tracker's free-text notes field at Scoreboard Tracking (SPEC-042)

## Failure Consequence
**No block** — tags are generated at metadata step and included in the deliverable. If missing, the metadata checklist is incomplete.

## Dependencies
- SPEC-041 (Metadata Checklist) — tags are one of the generated fields
- SPEC-042 (Scoreboard Tracking) — tags logged in notes field

## Override Rules
Can be overridden per-article by the Founder. One-time only.
