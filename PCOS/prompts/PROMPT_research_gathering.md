# PROMPT: Research Gathering

## Phase
3 of 8 — Personal Hook + Rapid-Fire Q&A + Fact Verification

## Purpose
Gather all the raw material needed to write the article: the personal hook, detailed answers from the Founder, and verified facts.

## Applicable Specs
- SPEC-033 (Personal Hook Gathering)
- SPEC-034 (Rapid-Fire Questioning)
- SPEC-035 (Fact Verification)
- SPEC-010 (Personal Hook)
- SPEC-005 (No Fabricated Reactions)

---

## Instructions

### Step 1: Personal Hook (SPEC-033)
Ask the Founder:
- "What's the real-life situation or question from your workplace that connects to this topic?"
- "How did this come up? Was it a colleague's question, something from your tax practice, or a personal experience?"

If the story needs emotional/reaction detail:
- Ask explicitly: "How did you feel about this?" or "What was your first thought?"
- **Never invent or assume a reaction** (LAW-5 / SPEC-005)

Record the hook as stated. Confirm it back to the Founder.

### Step 2: Rapid-Fire Questions (SPEC-034)
Ask more questions than feels necessary. Depth over speed.

**Run as plain text, not buttons.**

Typical questions (adapt to the topic):
- What specific numbers/dates/thresholds apply?
- Have you seen colleagues get this wrong? How?
- What's the most common misconception?
- What would you tell a new colleague asking about this?
- Are there recent rule changes that affect this?
- What's the worst-case scenario if someone ignores this?

**Reuse earlier answers.** Don't re-ask what the Founder already provided.

**Session Efficiency Note:** Suggest the Founder batch answers into one message to reduce turns and token cost.

### Step 3: Fact Verification (SPEC-035)
Before drafting begins:
1. Search and verify all factual/regulatory claims against primary sources
2. Verify any URLs intended for linking (SPEC-017)
3. Flag any unverified claim with [VERIFY]
4. Present a brief fact summary to the Founder

**Known risk areas** (verify with extra care):
- HBA interest method
- Gratuity calculation base
- Leave encashment tax treatment
- EDLI exemption rules
- Any rate/threshold/deadline: date-scope it by FY/AY

---

## Approval Gate
The Founder confirms:
- The personal hook is accurate
- The gathered information is sufficient
- Any flagged [VERIFY] items are resolved or acknowledged

---

## Transition
After research is complete, load PROMPT_outline_approval.md.

---

*Prompt: PROMPT_research_gathering.md — PCOS v1.0*
