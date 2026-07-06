# SPEC-042: Scoreboard Tracking

## Rule ID
RULE-042

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 42

## Lock Status
**[MUTABLE]**

## Requirement
At session close, after publication is confirmed:

1. **Close all applicable tracker checklist items** individually via `set_article_checklist_item`
2. **Verify** each write with `get_article` after the operation
3. **Record publication** via `record_article_publication` once the live URL is confirmed
4. **Do not assume** the actual publication date is "today" just because the Founder supplied a live URL
5. **Do not attempt** to `web_fetch` the live paisapsu.in URL to self-verify publication details

### Fields Without Dedicated Tracker Fields
These must be logged in the tracker's **free-text notes field**:
- Media Count (SPEC-018)
- Tags (SPEC-022)
- Keyword Density (SPEC-015)

## Mechanical Check
- **Validator:** None (MCP operation)
- **Enforcement:** PROMPT_publication_close
- **Template:** TMPL_tracker_record.md

## Failure Consequence
**No content block.** Tracker operations can be deferred to next session if MCP is unavailable (logged in PROJECT_STATE.md).

## Dependencies
- SPEC-037 (Tracker Record Creation) — the record that gets updated
- SPEC-040 (Final Quality Pass) — must complete before scoreboard

## Override Rules
Can be overridden by the Founder. One-time only.
