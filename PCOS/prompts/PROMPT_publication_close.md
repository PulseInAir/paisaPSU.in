# PROMPT: Publication Close

## Phase
8 of 8 — Scoreboard Tracking + Session Close

## Purpose
Close out all tracker checklist items, record publication, and update PROJECT_STATE.md.

## Applicable Specs
- SPEC-042 (Scoreboard Tracking)
- SPEC-037 (Tracker Record — update)

## Template
- TMPL_tracker_record.md

---

## Instructions

### Step 1: Wait for Publication Confirmation
The Founder must provide:
- The live WordPress URL
- The WordPress post ID (from admin edit URL)

**Do NOT assume** the publication date is "today" just because a URL is provided.
**Do NOT attempt** to web_fetch the live paisapsu.in URL to verify.

### Step 2: Close Tracker Checklist Items (SPEC-042)
Close each applicable item individually via `set_article_checklist_item`:
- Research completed ✓
- Outline approved ✓
- Draft completed ✓
- Fact-check completed ✓
- Authenticity check completed ✓
- Final review completed ✓
- SEO completed ✓
- Featured image completed (Founder-confirmed) ✓
- Internal links added ✓
- External sources added ✓

After each write, verify with `get_article`.

### Step 3: Record Publication
```
record_article_publication(
  id: ...,
  wordpress_post_id: "...",
  wordpress_post_url: "...",
  actual_publication_date: "..." (from Founder, not assumed)
)
```
Verify with `get_article`.

### Step 4: Log Notes
In the tracker's free-text notes field, record:
- Keyword Density: ____%
- Media Count: 1 (or custom)
- Tags: tag1, tag2, ...

### Step 5: Update PROJECT_STATE.md
Record:
- Article completed (title, ID, URL)
- Current category distribution (updated)
- Next recommended action
- Any pending items or open decisions

### Step 6: Session Complete
Confirm to the Founder: "Session complete. [Article Title] is published and tracked. PROJECT_STATE.md updated."

---

## Fallback: Tracker MCP Unavailable
If MCP is unreachable:
1. State plainly that tracker operations are blocked
2. Log ALL pending operations in PROJECT_STATE.md with exact values
3. Execute them at the start of the next session

---

## Fallback: Founder Doesn't Publish This Session
If the article is approved but not yet published:
1. Update article status to "Ready" in tracker
2. Note in PROJECT_STATE.md: "Article ready, awaiting publication"
3. Publication close will complete in the next session when the URL is provided

---

*Prompt: PROMPT_publication_close.md — PCOS v1.0*
