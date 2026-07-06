# SPEC-036: H2 Outline — Approval Gate

## Rule ID
RULE-036

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 36

## Lock Status
**[MUTABLE]**

## Requirement
Create the structural skeleton of the article. Before presenting for approval, verify mechanically:

1. At least **2 H2 headings** contain the exact focus keyword phrase (SPEC-016)
2. The **article title** contains a number, Power Word, and sentiment word (SPEC-019)
3. Titles only — **no appended explainer text** after H2 titles

The outline is presented as a list of H2 headings. No body text, no descriptions, no annotations.

### Session-Split Checkpoint
This is the recommended break point for long articles. After H2 Outline approval, the session can be split:
- Save progress to PROJECT_STATE.md
- Start a new conversation for section writing
- The tracker record (SPEC-037) preserves all approved state

## Mechanical Check
- **Validator:** Grep scan for keyword in H2s + `validate_title.py` for title
- **Enforcement:** PROMPT_outline_approval
- **Template:** TMPL_article_outline.md

## Failure Consequence
**Block section writing.** The outline must pass both mechanical checks before any section is drafted.

## Dependencies
- SPEC-016 (Subheadings with Focus Keyword) — the H2 keyword requirement
- SPEC-019 (Title Optimization) — the title format requirement
- SPEC-037 (Tracker Record Creation) — happens immediately after outline approval

## Override Rules
Can be overridden per-article by the Founder. One-time only.
