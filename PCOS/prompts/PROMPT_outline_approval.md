# PROMPT: Outline Approval

## Phase
4 of 8 — H2 Outline Gate + Tracker Record Creation

## Purpose
Build the structural skeleton, verify it mechanically, get approval, and create the tracker record.

## Applicable Specs
- SPEC-036 (H2 Outline Gate)
- SPEC-016 (Subheadings with Focus Keyword)
- SPEC-019 (Title Optimization)
- SPEC-037 (Tracker Record Creation)

## Template
- TMPL_article_outline.md

---

## Instructions

### Step 1: Build the H2 Outline
Create a list of H2 headings based on the research gathered. Rules:
- **Titles only** — no appended explainer text
- Structure should support 2,000+ words (SPEC-013)
- The personal hook should map to the opening section
- Include a natural closing section (action/warning/decision, not generic motivation)

### Step 2: Mechanical Verification
Before presenting the outline, verify:

**Check 1: Keyword in H2s (SPEC-016)**
```
Grep: At least 2 H2 headings contain the exact focus keyword phrase
```
If fewer than 2, revise H2 headings before presenting.

**Check 2: Title Optimization (SPEC-019)**
```
Title must contain: (a) a number, (b) a Power Word, (c) a sentiment word
```
Run `validate_title.py` or verify manually.

### Step 3: Present for Approval
Present:
- The article title
- The list of H2 headings (titles only)
- Confirmation that both mechanical checks pass

**Wait for explicit approval.** Do not proceed to writing without it.

### Step 4: Create Tracker Record (SPEC-037)
Immediately after approval:
```
create_article(
  title: "...",
  primary_keyword: "...",
  category: "...",
  status: "Outlining"
)
```
Then verify:
```
get_article(id: ...)
```
Confirm stored values match. Report the article ID to the Founder.

### Session-Split Checkpoint
This is the recommended break point for long articles. If the session is getting long:
- Save all progress to PROJECT_STATE.md
- The Founder can continue section writing in a new conversation
- Use TMPL_session_handoff.md for the transition

---

## Transition
After outline approval and tracker creation, load PROMPT_section_drafting.md + PROMPT_humanizer.md.

---

*Prompt: PROMPT_outline_approval.md — PCOS v1.0*
