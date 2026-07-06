# SPEC-044: Override Hierarchy

## Rule ID
RULE-044

## Source
Rule_v8, Section VIII (Amendment Discipline), Rule 44

## Lock Status
**[MUTABLE]**

## Requirement
### Override Rules
1. **Locked rules** (Section II, and any rule marked [LOCKED]) — cannot be overridden by anyone, including the Founder
2. **Non-locked rules** — may be overridden by the Founder's explicit, session-specific instruction
3. **Session-specific overrides** apply only to that instance unless folded into Rule_v8 through a logged amendment
4. When a per-article override is used, the AI states plainly in the same turn that it is a **one-time deviation, not a new default**
5. Exception: if the amendment is being logged as a standing change (like Rule 18 in v8), it IS the new default and doesn't need restating

### The Hierarchy (repeated from MASTER_BLUEPRINT)
```
LOCKED RULES → MASTER_BLUEPRINT → Rule_v8 → Founder override → AI judgment
```

## Mechanical Check
- **Validator:** None (process rule)
- **Enforcement:** All prompts include the override hierarchy in their preamble

## Failure Consequence
**Process violation.** If the AI applies a locked-rule override, it must be corrected immediately.

## Dependencies
- All LOCKED specs (SPEC-001 through SPEC-007, SPEC-011, SPEC-045)

## Override Rules
This rule itself defines the override system. It is mutable but changes require a new Constitution version.
