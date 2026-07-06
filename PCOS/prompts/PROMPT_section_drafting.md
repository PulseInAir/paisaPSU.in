# PROMPT: Section Drafting

## Phase
5 of 8 — Section-by-Section Writing with Inline Linking

## Purpose
Write the article one H2 section at a time, with humanizer applied during drafting and links inserted in real time.

## Applicable Specs
- SPEC-038 (Section Writing — Links Drafted In Real Time)
- SPEC-039 (Approval Loop)
- SPEC-017 (Internal and External Linking)
- SPEC-005 (No Fabricated Reactions)
- SPEC-007 (Deliverable Completeness)

## Co-load
- PROMPT_humanizer.md (apply during drafting, not after)

## Template
- TMPL_section_draft.md

---

## Instructions

### For Each H2 Section:

**1. Draft the Section**
- Use the Founder's rough notes and research from Phase 3
- Apply PROMPT_humanizer rules DURING writing (not as a post-pass)
- Write complete, polished text — ready for the Founder to copy into WordPress
- Minimum effort per section: enough depth to contribute to the 2,000-word total

**2. Insert Links in Real Time (SPEC-017)**
As you write each H2:
- If this section naturally references another PaisaPSU article topic → insert an internal link
- If this section references an external authoritative fact → insert an external DoFollow link
- **Verify every link** via web_search or web_fetch before presenting the section
- A URL is a factual claim (LAW-4) — treat it with the same rigor as a statistic

If no link naturally fits this section, note it and move on. At least one internal + one external link must exist somewhere in the full article by the end.

If no H2 naturally supports a link, add one during the opening section by default.

**3. Quality Checks Per Section**
Before presenting, verify:
- [ ] No em dashes (—)
- [ ] No [VERIFY] tags, TODO brackets, or outline numbers
- [ ] All paragraphs ≤ 4 sentences
- [ ] No forbidden vocabulary (SPEC-024)
- [ ] No fabricated reactions (SPEC-005)
- [ ] Links verified (if any)

**4. Present the Section**
Deliver the complete section text in the conversation. The Founder must see the actual text (LAW-7).

**5. Wait for Approval (SPEC-039)**
Do NOT write the next section until the Founder explicitly approves.

Valid approval signals:
- Pasting the next H2 title
- "ok", "good", "approved", "next"
- Any clear affirmative

**6. Repeat for Each H2**

### Image Revision (SPEC-046)
If the Founder rejects a proposed image idea at any point, generate a replacement mapped to the same section.

### Decision Revision (SPEC-046)
If the Founder wants to reopen the topic decision after drafting has begun, treat it as a fresh restart from PROMPT_topic_selection.md.

---

## Transition
After all sections are approved, load PROMPT_quality_pass.md.

---

*Prompt: PROMPT_section_drafting.md — PCOS v1.0*
