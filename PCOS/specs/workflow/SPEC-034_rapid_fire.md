# SPEC-034: Rapid-Fire Questioning

## Rule ID
RULE-034

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 34

## Lock Status
**[MUTABLE]**

## Requirement
Ask more questions than feels necessary. **Depth over speed.** Run as plain text, not buttons. Reuse earlier answers instead of re-asking.

### Session Efficiency Note
Rapid-fire questions should be answered in **one batched message** wherever possible, not one at a time across multiple turns. Long threads cost more per turn since the full conversation history is reprocessed each time, so batching answers reduces both the number of turns and the cumulative cost of the session.

This is a **usage-efficiency practice for the Founder**, not a content-quality rule, and does not change what this rule requires of the AI.

## Mechanical Check
- **Validator:** None (process rule)
- **Enforcement:** PROMPT_research_gathering

## Failure Consequence
**No direct block.** Insufficient questioning leads to thin content that fails the 2000-word minimum (SPEC-013) or lacks Information Gain (SPEC-009).

## Dependencies
- SPEC-013 (Word Count) — questions must gather enough material for 2000+ words
- SPEC-009 (Information Gain) — questions must uncover the proprietary angle

## Override Rules
The Founder can signal "enough" at any time. The AI should comply but note if it believes more detail is needed.
