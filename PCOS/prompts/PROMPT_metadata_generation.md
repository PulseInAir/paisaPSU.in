# PROMPT: Metadata Generation

## Phase
7 of 8 — SEO Metadata + Tags

## Purpose
Generate all SEO metadata fields. Iterate privately until every field passes its check, then present once.

## Applicable Specs
- SPEC-041 (Metadata Checklist)
- SPEC-012 (Focus Keyword Placement)
- SPEC-014 (75-Character URL Limit)
- SPEC-018 (Media Count — Default One Image)
- SPEC-019 (Title Optimization)
- SPEC-022 (Tags)

## Template
- TMPL_metadata_checklist.md

---

## Instructions

### Step 1: Generate All Fields
Using the approved article and focus keyword, generate:

**SEO Title**
- Focus keyword in first 50 characters
- Contains a number + Power Word + sentiment word (SPEC-019)
- Run `validate_title.py` before presenting

**Meta Description**
- 120–160 characters total
- Contains the focus keyword
- Compelling summary that drives clicks

**URL Slug**
- Contains the focus keyword (hyphenated)
- Total URL (`https://paisapsu.in/` + slug) ≤ 75 characters
- Run `validate_url_length.py` before presenting

**Featured Image Idea** (SPEC-018)
- ONE image (default)
- Dynamic and tailored to this article — not a generic template
- Specify which H2 section it represents
- Describe the style/tone

**Alt Text**
- Carries the exact focus keyword phrase

**Tags** (SPEC-022)
- 4-6 real, search-relevant WordPress tags
- Distinct from just repeating the primary keyword
- Cover related queries a PSU employee might search

### Step 2: Iterate Privately
Do NOT present any field that fails its check. Revise internally until all fields pass. The Founder should only see the final, passing version.

### Step 3: Present
Fill in TMPL_metadata_checklist.md and present the complete metadata block.

### Step 4: Approval
Wait for the Founder to approve the metadata. If any field is rejected, revise and re-present.

---

## Transition
After metadata approval, load PROMPT_publication_close.md.

---

*Prompt: PROMPT_metadata_generation.md — PCOS v1.0*
