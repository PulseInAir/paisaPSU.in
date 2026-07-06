# PROMPT: Quality Pass

## Phase
6 of 8 — Final Quality Pass

## Purpose
Run all validators against the complete article text. If anything fails, fix it and re-deliver the full corrected text.

## Applicable Specs
- SPEC-040 (Final Quality Pass — Explicit Checklist)
- SPEC-007 (Deliverable Completeness)

## Template
- TMPL_final_quality_pass.md

---

## Instructions

### Step 1: Assemble Full Article Text
Combine all approved sections into a single complete article text. This is the text that validators will run against.

### Step 2: Run All Validators
Execute `run_all_validators.py` (or run each validator individually):

```bash
python run_all_validators.py article.txt --keyword "FOCUS_KEYWORD"
```

Or run individually:
```bash
python validate_privacy.py article.txt              # Checks 1, 2 (SPEC-001, SPEC-002)
python validate_disclaimer.py article.txt           # Check 3 (SPEC-003)
python validate_meta_leakage.py article.txt         # Checks 4, 6 (SPEC-004, SPEC-027)
python validate_em_dash.py article.txt              # Check 7 (SPEC-028)
python validate_paragraph_length.py article.txt     # Check 8 (SPEC-023)
python validate_keyword_placement.py article.txt --keyword "KEYWORD"  # Check 9 (SPEC-012)
python validate_word_count.py article.txt           # Check 10 (SPEC-013)
python validate_keyword_density.py article.txt --keyword "KEYWORD"    # Check 11 (SPEC-015)
```

### Step 3: Check 5 (Manual)
Confirm with the Founder: "Are there any fabricated reactions or unconfirmed personal characterizations in the article?"

This is the only check that requires Founder input — all others are mechanical.

### Step 4: Report Results
Fill in TMPL_final_quality_pass.md with all results. Present the completed checklist.

### Step 5: Handle Failures
If ANY item fails:
1. Fix the issue
2. **Re-deliver the COMPLETE corrected article text** in the conversation (LAW-7 / SPEC-007)
3. Re-run the validators against the corrected text
4. Present updated results
5. Repeat until all 11 items pass

**A "now passing" report is NOT sufficient.** The Founder must see the actual corrected text.

### Step 6: Confirm All Pass
Only when all 11 items pass, confirm: "Final Quality Pass complete. All 11 items pass. Proceeding to metadata generation."

---

## Transition
After all items pass, load PROMPT_metadata_generation.md.

---

*Prompt: PROMPT_quality_pass.md — PCOS v1.0*
