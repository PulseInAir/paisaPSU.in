# PROMPT: Topic Selection

## Phase
2 of 8 — Topic Recommendation

## Purpose
Propose one strong article topic based on Information Gain and category gap analysis.

## Applicable Specs
- SPEC-032 (Recommendation — Explore Mode & Decision Delegation)
- SPEC-009 (Information Gain)
- SPEC-008 (Synthesize + Augment)
- SPEC-019 (Title Optimization)
- SPEC-020 (Keyword Uniqueness)

---

## Instructions

### Default Mode: ONE Recommendation
Based on the gap analysis from Session Open:
1. Identify the thinnest category (or most timely topic given the Founder's situation audit)
2. Propose **exactly ONE** article title with:
   - A two-line justification (max)
   - The proposed focus keyword
   - The Information Gain angle ("What this adds that current search results lack")
3. Verify the keyword hasn't been used before (SPEC-020)

### Title Requirements (SPEC-019)
The proposed title must contain:
- A number (e.g., "5 Hidden...", "7 Real...")
- A Power Word from: Hidden, Real, Actually, Truth, Warning, Mistake, Trap, Secret, Revealed, Alert, Free, Exposed, Critical, Essential, Proven
- A positive or negative sentiment word

### Explore Mode (SPEC-032)
Activated ONLY if the Founder explicitly asks to "explore" alternatives.
- Present up to 3 angles in a single round
- Clearly flag this as a deviation from the default
- Return to default one-recommendation mode after this round

### Decision Delegation (SPEC-032)
If the Founder declines two full rounds:
- Ask once: "Do you want to decide, or should I choose?"
- If delegated, make the choice and state it plainly

### Approval Gate
The Founder must explicitly approve the topic and keyword before proceeding to research gathering.

---

## What the Founder Sees
- One title recommendation with brief justification
- The proposed focus keyword
- What makes this article different from existing search results

---

## Transition
After topic approval, load PROMPT_research_gathering.md.

---

*Prompt: PROMPT_topic_selection.md — PCOS v1.0*
