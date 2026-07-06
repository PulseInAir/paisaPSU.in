# SYSTEM_ARCHITECTURE.md

## PCOS v1.0 — Technical Architecture

**Governed by:** MASTER_BLUEPRINT.md
**Constitution:** Rule_v8 (July 2026)

---

## 1. System Overview

PCOS is a file-based content operating system. It has no database, no server, no UI. It is a collection of Markdown files and Python scripts that together enforce Rule_v8 and carry project memory between AI conversations.

```
┌─────────────────────────────────────────────────┐
│                   FOUNDER                        │
│         (Approve / Reject / Decide)              │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│               AI CONVERSATION                    │
│                                                  │
│   Inputs:                                        │
│   ┌──────────────────┐                           │
│   │ MASTER_BLUEPRINT │ (always loaded)           │
│   │ PROJECT_STATE    │ (always loaded)           │
│   │ PROMPT_phase_N   │ (phase-specific)          │
│   └──────────────────┘                           │
│                                                  │
│   During Execution:                              │
│   ┌──────────────────┐                           │
│   │ SPEC files       │ (referenced by prompt)    │
│   │ TMPL files       │ (used to format output)   │
│   │ Validators       │ (run mechanically)        │
│   │ Reference files  │ (loaded on demand)        │
│   └──────────────────┘                           │
│                                                  │
│   External:                                      │
│   ┌──────────────────┐                           │
│   │ Tracker MCP      │ (article records)         │
│   │ Web Search       │ (fact verification)       │
│   └──────────────────┘                           │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│              OUTPUTS                             │
│                                                  │
│   • Article text (section by section)            │
│   • Metadata (SEO title, description, slug...)   │
│   • Tracker record updates                       │
│   • Updated PROJECT_STATE.md                     │
└─────────────────────────────────────────────────┘
```

---

## 2. Component Map

### How Components Connect

```
MASTER_BLUEPRINT.md
        │
        ├── specs/ ──────────────────┐
        │   (47 spec files)          │
        │                            ▼
        ├── templates/ ◄──── Referenced by specs
        │   (6 template files)       │
        │                            ▼
        ├── prompts/ ◄────── Load specs + templates
        │   (9 prompt files)         │
        │                            ▼
        ├── validators/ ◄─── Called by prompts
        │   (12 Python scripts)      │
        │                            │
        ├── reference/ ◄──── Consulted by prompts
        │   (5+ reference files)     │
        │                            │
        └── PROJECT_STATE.md ◄────── Updated at session close
```

### Data Flow Per Article

```
Session Open
    │
    ├── Load: MASTER_BLUEPRINT + PROJECT_STATE + PROMPT_session_open
    ├── Action: Situation audit, gap analysis (Tracker MCP)
    │
    ▼
Topic Selection
    │
    ├── Load: PROMPT_topic_selection
    ├── Reference: SPEC-020 (keyword uniqueness), category_codes.md
    ├── Action: Propose ONE title
    ├── Gate: Founder approves topic
    │
    ▼
Research Gathering
    │
    ├── Load: PROMPT_research_gathering
    ├── Reference: SPEC-033, SPEC-034, SPEC-035
    ├── Action: Personal hook, rapid-fire Q&A, fact verification
    ├── Gate: Founder confirms all facts and personal hook
    │
    ▼
Outline Approval
    │
    ├── Load: PROMPT_outline_approval
    ├── Run: validate_title.py, keyword grep on H2s
    ├── Action: Build H2 skeleton
    ├── Gate: Founder approves outline
    ├── Action: Create tracker record (Tracker MCP)
    │
    ▼
Section Writing (loop per H2)
    │
    ├── Load: PROMPT_section_drafting + PROMPT_humanizer
    ├── Reference: SPEC-038, SPEC-017 (inline linking)
    ├── Action: Write one H2, insert links, apply humanizer
    ├── Gate: Founder approves section
    ├── Repeat for each H2
    │
    ▼
Quality Pass
    │
    ├── Load: PROMPT_quality_pass
    ├── Run: run_all_validators.py
    ├── Use: TMPL_final_quality_pass.md
    ├── Action: If any validator fails, fix and re-deliver full text (LAW-7)
    ├── Gate: All 11 checklist items pass
    │
    ▼
Metadata Generation
    │
    ├── Load: PROMPT_metadata_generation
    ├── Use: TMPL_metadata_checklist.md
    ├── Run: validate_url_length.py, validate_title.py
    ├── Action: Generate SEO metadata
    ├── Gate: Founder approves metadata
    │
    ▼
Publication Close
    │
    ├── Load: PROMPT_publication_close
    ├── Action: Scoreboard tracking (Tracker MCP)
    ├── Action: Update PROJECT_STATE.md
    ├── Gate: Session complete
    │
    ▼
Done
```

---

## 3. Full Folder Structure (Detailed)

```
PCOS/
│
├── MASTER_BLUEPRINT.md
├── SYSTEM_ARCHITECTURE.md              ← This file
├── PROJECT_STATE.md
│
├── specs/
│   │
│   ├── safety/
│   │   ├── SPEC-001_org_anonymity.md
│   │   ├── SPEC-002_strict_privacy.md
│   │   ├── SPEC-003_credential_transparency.md
│   │   ├── SPEC-004_no_hallucinations.md
│   │   ├── SPEC-005_no_fabricated_reactions.md
│   │   ├── SPEC-006_case_anonymization.md
│   │   └── SPEC-007_deliverable_completeness.md
│   │
│   ├── content/
│   │   ├── SPEC-008_synthesize_augment.md
│   │   ├── SPEC-009_information_gain.md
│   │   ├── SPEC-010_personal_hook.md
│   │   └── SPEC-011_honest_returns.md
│   │
│   ├── seo/
│   │   ├── SPEC-012_keyword_placement.md
│   │   ├── SPEC-013_word_count.md
│   │   ├── SPEC-014_url_limit.md
│   │   ├── SPEC-015_keyword_density.md
│   │   ├── SPEC-016_subheadings_keyword.md
│   │   ├── SPEC-017_linking.md
│   │   ├── SPEC-018_media_count.md
│   │   ├── SPEC-019_title_optimization.md
│   │   ├── SPEC-020_keyword_uniqueness.md
│   │   ├── SPEC-021_toc.md
│   │   └── SPEC-022_tags.md
│   │
│   ├── voice/
│   │   ├── SPEC-023_paragraph_discipline.md
│   │   ├── SPEC-024_forbidden_vocabulary.md
│   │   ├── SPEC-025_no_filler_intro.md
│   │   ├── SPEC-026_voice_bank.md
│   │   ├── SPEC-027_no_meta_leakage.md
│   │   ├── SPEC-028_em_dash_prohibition.md
│   │   └── SPEC-029_voice_hierarchy.md
│   │
│   ├── workflow/
│   │   ├── SPEC-030_situation_audit.md
│   │   ├── SPEC-031_gap_analysis.md
│   │   ├── SPEC-032_recommendation.md
│   │   ├── SPEC-033_personal_hook_gather.md
│   │   ├── SPEC-034_rapid_fire.md
│   │   ├── SPEC-035_fact_verification.md
│   │   ├── SPEC-036_h2_outline_gate.md
│   │   ├── SPEC-037_tracker_creation.md
│   │   ├── SPEC-038_section_writing.md
│   │   ├── SPEC-039_approval_loop.md
│   │   ├── SPEC-040_final_quality_pass.md
│   │   ├── SPEC-041_metadata_checklist.md
│   │   └── SPEC-042_scoreboard_tracking.md
│   │
│   └── governance/
│       ├── SPEC-043_disclaimer_placement.md
│       ├── SPEC-044_override_hierarchy.md
│       ├── SPEC-045_account_preference_isolation.md
│       ├── SPEC-046_image_revision_protocol.md
│       └── SPEC-047_no_unverifiable_claims.md
│
├── templates/
│   ├── TMPL_metadata_checklist.md
│   ├── TMPL_final_quality_pass.md
│   ├── TMPL_article_outline.md
│   ├── TMPL_session_handoff.md
│   ├── TMPL_tracker_record.md
│   └── TMPL_section_draft.md
│
├── prompts/
│   ├── PROMPT_session_open.md
│   ├── PROMPT_topic_selection.md
│   ├── PROMPT_research_gathering.md
│   ├── PROMPT_outline_approval.md
│   ├── PROMPT_section_drafting.md
│   ├── PROMPT_quality_pass.md
│   ├── PROMPT_metadata_generation.md
│   ├── PROMPT_publication_close.md
│   └── PROMPT_humanizer.md
│
├── validators/
│   ├── validate_word_count.py
│   ├── validate_keyword_density.py
│   ├── validate_em_dash.py
│   ├── validate_paragraph_length.py
│   ├── validate_forbidden_words.py
│   ├── validate_url_length.py
│   ├── validate_keyword_placement.py
│   ├── validate_meta_leakage.py
│   ├── validate_privacy.py
│   ├── validate_disclaimer.py
│   ├── validate_title.py
│   └── run_all_validators.py
│
├── reference/
│   ├── Rule_v8.md
│   ├── Pulak_Operational_Voicebank.md    ← Symlink or copy from parent
│   ├── power_words.txt
│   ├── forbidden_words.txt
│   ├── category_codes.md
│   └── tracker_api_reference.md
│
└── logs/
    └── session_log_template.md
```

---

## 4. Component Interaction Rules

### Loading Rules
1. **Always loaded:** MASTER_BLUEPRINT.md + PROJECT_STATE.md
2. **Phase-loaded:** One PROMPT file per workflow phase
3. **On-demand:** Specs, templates, reference files — loaded only when the current prompt references them
4. **Execution-time:** Validators — run only when a prompt explicitly calls for them

### Dependency Rules
1. No prompt may reference a spec that doesn't exist
2. No template may include fields not defined in a spec
3. No validator may check a condition not defined in a spec
4. All dependencies are forward-declared in the prompt's header

### File Modification Rules
1. `MASTER_BLUEPRINT.md` — **Never modified** after approval. New version = new platform version.
2. `specs/` — Modified only when Rule_v8 is amended to a new version (v9, v10...)
3. `templates/` — Modified when output format changes. Must stay compatible with specs.
4. `prompts/` — Modified to improve workflow. Must stay compatible with specs and templates.
5. `validators/` — Modified to fix bugs or improve accuracy. Must match their spec's requirements exactly.
6. `reference/` — Read-only after initial population. Updated only for new Constitution versions.
7. `PROJECT_STATE.md` — Updated every session. This is the only file that changes regularly.
8. `logs/` — Append-only. Each session creates a new log file.

---

## 5. External System Integration

### PaisaPSU Article Tracker MCP
- **Base URL:** `paisapsu-article-tracker-mcp.vercel.app`
- **Authentication:** Application password (stored separately, never in PCOS files)
- **Used by:** PROMPT_session_open (gap analysis), PROMPT_outline_approval (record creation), PROMPT_publication_close (scoreboard)
- **Fallback:** If unavailable, log operations in PROJECT_STATE.md for next session

### WordPress
- **Integration:** Manual only (no MCP connector)
- **Post IDs:** Retrieved manually from admin edit URL pattern
- **Publication confirmation:** Founder provides live URL; AI does not web_fetch paisapsu.in URLs

### Web Search / Web Fetch
- **Used by:** PROMPT_research_gathering (fact verification), PROMPT_section_drafting (link verification)
- **Rule:** URLs are factual claims under LAW-4 and must be verified with the same rigor as statistics

---

## 6. Validator Architecture

### Design Principles
- Each validator is a standalone Python script
- Input: article text file (plain text or Markdown)
- Output: JSON with `pass` (boolean), `details` (string), `violations` (list)
- No external dependencies beyond Python standard library
- Can run in AI sandbox, local terminal, or CI pipeline

### Master Runner
`run_all_validators.py` orchestrates all validators:
1. Reads the article text file
2. Accepts the focus keyword as a parameter
3. Runs each validator in sequence
4. Outputs a consolidated pass/fail table
5. Returns exit code 0 if all pass, 1 if any fail

### Example Usage
```bash
python run_all_validators.py article.txt --keyword "psu employee salary structure"
```

### Output Format
```
╔════════════════════════════════╦════════╦══════════════════════════════╗
║ Validator                      ║ Result ║ Details                      ║
╠════════════════════════════════╬════════╬══════════════════════════════╣
║ Word Count (≥2000)             ║ PASS   ║ 2,347 words                  ║
║ Keyword Density (1.0-1.5%)     ║ PASS   ║ 1.23% (29 occurrences)       ║
║ Em Dash Check                  ║ PASS   ║ 0 em dashes found            ║
║ Paragraph Length (≤4 sent.)    ║ FAIL   ║ Para 7: 5 sentences          ║
║ Forbidden Words                ║ PASS   ║ 0 AI fingerprints found      ║
║ URL Length (≤75 chars)         ║ PASS   ║ 62 characters                ║
║ Keyword in First 10%           ║ PASS   ║ Found at position 3.2%       ║
║ Meta Leakage                   ║ PASS   ║ No [VERIFY]/TODO found       ║
║ Privacy Check                  ║ PASS   ║ No org names or PII found    ║
║ Disclaimer Present             ║ PASS   ║ Exact wording found          ║
║ Title Check                    ║ PASS   ║ Number + Power Word + Sent.  ║
╚════════════════════════════════╩════════╩══════════════════════════════╝

RESULT: 10/11 PASSED — 1 FAILURE (Paragraph Length)
```

---

*PCOS v1.0 — System Architecture*
*Governed by: MASTER_BLUEPRINT.md*
