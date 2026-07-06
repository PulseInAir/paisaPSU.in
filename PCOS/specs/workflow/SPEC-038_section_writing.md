# SPEC-038: Section Writing — Links Drafted In Real Time

## Rule ID
RULE-038

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 38

## Lock Status
**[STRENGTHENED in v8]**

## Requirement
Expand **one H2 at a time** using rough notes from the Founder. For each section:

1. **Apply the humanizer pass during drafting** (PROMPT_humanizer) — not after
2. **Insert links in real time** (SPEC-017): if the H2 naturally references another PaisaPSU article or an external fact, insert the link now, verify it live, and include it in the section text
3. **No internal scaffolding**: no outline numbers, no `TODO` brackets, no `[VERIFY]` tags in the delivered text
4. **Deliver as explicit text** in the conversation for the Founder to review

### What the Founder Sees
A complete, polished section of article text — ready to copy into WordPress. Not a draft, not a skeleton, not a summary.

## Mechanical Check
- **Validator:** None per-section (validators run at Final Quality Pass on full article)
- **Enforcement:** PROMPT_section_drafting + PROMPT_humanizer
- **Template:** TMPL_section_draft.md

## Failure Consequence
**Reject section.** The section must be rewritten before the Founder can approve and move to the next H2.

## Dependencies
- SPEC-017 (Linking) — inline linking during writing
- SPEC-039 (Approval Loop) — section approval before next H2
- SPEC-023 through SPEC-029 — voice rules applied during drafting

## Override Rules
Can be overridden per-section by the Founder. One-time only.
