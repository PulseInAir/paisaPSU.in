# Tracker API Reference — PCOS v1.0

## PaisaPSU Article Tracker MCP

**Base:** `paisapsu-article-tracker-mcp.vercel.app`
**Type:** MCP (Model Context Protocol) server
**Status:** Sole source of truth for all article records

---

## Endpoints Used by PCOS

### list_articles
**When:** Session Open (SPEC-031 — Gap Analysis)
**Parameters:** `per_page: 100`
**Returns:** All article records with fields: ID, title, keyword, category, status, dates, checklist items
**Used for:** Category count, keyword uniqueness check, gap analysis

### create_article
**When:** After topic/title confirmation (SPEC-037 — Tracker Record Creation)
**Parameters:** title, primary_keyword, category, status ("Outlining"), planned_publication_date
**Returns:** New article record with auto-generated ID
**Follow-up:** Immediately call `get_article` to verify stored values

### get_article
**When:** After any write operation (SPEC-042 — Scoreboard Tracking)
**Parameters:** article ID
**Returns:** Full article record
**Used for:** Verification that stored values match intended values

### set_article_checklist_item
**When:** Publication Close (SPEC-042 — Scoreboard Tracking)
**Parameters:** article ID, checklist item name, value (boolean)
**Used for:** Closing individual checklist items (research, outline, draft, etc.)

### record_article_publication
**When:** After Founder confirms live URL (SPEC-042 — Scoreboard Tracking)
**Parameters:** article ID, wordpress_post_id, wordpress_post_url, actual_publication_date
**Important:**
- Do NOT assume publication date is "today"
- Do NOT web_fetch the live URL to verify
- actual_publication_date comes from the Founder

---

## Fields Without Dedicated Tracker Columns
These are logged in the free-text **notes** field:
- Keyword Density (from SPEC-015)
- Media Count (from SPEC-018)
- Tags (from SPEC-022)

---

## Fallback When MCP Is Unavailable
1. State plainly that tracker operations are blocked
2. Continue content work without tracker writes
3. Log ALL pending operations in PROJECT_STATE.md with exact values
4. Execute at start of next session where MCP is accessible

---

## Authentication
Application password stored separately. Never included in PCOS files or article text.

---

*Reference: tracker_api_reference.md — PCOS v1.0*
