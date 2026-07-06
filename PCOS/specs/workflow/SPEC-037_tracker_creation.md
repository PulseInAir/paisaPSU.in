# SPEC-037: Tracker Record Creation

## Rule ID
RULE-037

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 37

## Lock Status
**[MUTABLE]**

## Requirement
Create a tracker record via PaisaPSU Article Tracker MCP (`create_article`) **immediately after topic and title are confirmed**. Confirm stored values with `get_article`.

### Required Fields (from ARTICLE_TRACKER_FIELDS)
1. Article title
2. Primary keyword
3. Article category (from the 6 active categories)
4. Article status (set to "Outlining" at creation)
5. Planned publication date (if known)

### Verification
After `create_article`, immediately call `get_article` to confirm the stored values match what was intended.

## Mechanical Check
- **Validator:** None (MCP operation, not content check)
- **Enforcement:** PROMPT_outline_approval (post-approval step)
- **Fallback:** If MCP unavailable, log the record in PROJECT_STATE.md for next session

## Failure Consequence
**No content block.** Tracker failure doesn't stop drafting, but the record must be created before publication close.

## Dependencies
- SPEC-036 (H2 Outline Gate) — topic and title are confirmed at this gate
- SPEC-042 (Scoreboard Tracking) — uses the record created here

## Override Rules
Can be overridden by the Founder. One-time only.
