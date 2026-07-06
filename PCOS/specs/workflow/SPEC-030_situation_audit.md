# SPEC-030: Situation Audit

## Rule ID
RULE-030

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 30

## Lock Status
**[MUTABLE]**

## Requirement
At the start of every content session, the AI must ask:
1. **What is the current month?** (for seasonal relevance — tax season, ITR deadlines, etc.)
2. **Are there any urgent PSU finance issues?** (policy changes, notifications, deadline reminders)

This keeps content relevant to live financial situations and **must not be skipped**.

## Mechanical Check
- **Validator:** None (process step, not content check)
- **Enforcement:** PROMPT_session_open makes this the mandatory first action

## Failure Consequence
**Process violation.** If skipped, the AI must return to this step before proceeding to topic selection.

## Dependencies
- This is Step 1 of the workflow — everything else depends on it

## Override Rules
Can be overridden by the Founder if he provides the information proactively. One-time only.
