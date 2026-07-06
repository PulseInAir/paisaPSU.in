# SPEC-047: No Unverifiable Completeness Claims

## Rule ID
RULE-047

## Source
Rule_v8, Section VIII (Amendment Discipline), Rule 47

## Lock Status
**[MUTABLE]**

## Requirement
Changelog entries and rule descriptions must **never claim** that a category of failure is now fully closed. The AI must not tell the Founder that a version is:
- "Airtight"
- "Leak proof"
- "10/10"
- "Complete"
- "Fully resolved"

These are **unverifiable claims** — no system can guarantee the absence of all future failures.

### What to Say Instead
- "This version addresses the specific failures identified in Articles 30 and 31"
- "The following gaps have been closed: [specific list]"
- "No known violations remain from the audit findings"

## Mechanical Check
- **Validator:** None (applies to changelog/meta-text, not article content)
- **Enforcement:** Prompt instruction — the AI's own output must not make completeness claims

## Failure Consequence
**No content block.** This is a meta-discipline rule about how the AI describes its own work. Violations are corrected conversationally.

## Dependencies
- None (standalone governance rule)

## Override Rules
Can be overridden by the Founder. One-time only.
