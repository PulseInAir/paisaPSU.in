# SPEC-020: Keyword Uniqueness

## Rule ID
RULE-020

## Source
Rule_v8, Section IV (Technical SEO Guardrails), Rule 20

## Lock Status
**[MUTABLE]**

## Requirement
The focus keyword must not have been used as a primary keyword in any previously published PaisaPSU article. Confirm against the live tracker at session open.

## Mechanical Check
- **Validator:** None (requires live tracker data)
- **Enforcement:** Prompt instruction in PROMPT_session_open and PROMPT_topic_selection
- **Method:** Pull `list_articles` (per_page: 100) from Tracker MCP and search for keyword matches
- **Timing:** Checked at session open before any topic is confirmed

## Failure Consequence
**Reject keyword.** A new keyword must be proposed. This is caught early — before outlining begins.

## Dependencies
- SPEC-031 (Gap Analysis) — the tracker pull that provides the keyword history
- SPEC-037 (Tracker Record Creation) — the new keyword is recorded

## Override Rules
Can be overridden per-article by the Founder if he intentionally wants to revisit a keyword (e.g., for an update post). One-time only.
