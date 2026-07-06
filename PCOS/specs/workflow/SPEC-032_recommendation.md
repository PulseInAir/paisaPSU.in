# SPEC-032: Recommendation — Explore Mode & Decision Delegation

## Rule ID
RULE-032

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 32

## Lock Status
**[MUTABLE]**

## Requirement
### Default Mode
Propose **ONE strong title** based on Information Gain (SPEC-009). Include a two-line justification max.

### Explore Mode
Activated **only** if the Founder explicitly asks to "explore" alternatives. Present up to **3 angles** in a single round, clearly flagged as a deviation from the default.

### Decision Delegation
If the Founder declines two full rounds without selecting one, ask once: "Do you want to decide, or should I choose?"

## Mechanical Check
- **Validator:** None (process rule)
- **Enforcement:** PROMPT_topic_selection enforces the one-recommendation default

## Failure Consequence
**Process violation.** Offering multiple options without being asked is a workflow error. The AI must default to one recommendation.

## Dependencies
- SPEC-031 (Gap Analysis) — informs which category to recommend
- SPEC-009 (Information Gain) — the quality standard for the recommendation
- SPEC-019 (Title Optimization) — title format requirements

## Override Rules
The Founder can request Explore Mode at any time. This is not an override — it's an explicit trigger built into the rule.
