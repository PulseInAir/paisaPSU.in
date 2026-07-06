# SPEC-033: Personal Hook Gathering

## Rule ID
RULE-033

## Source
Rule_v8, Section VI (The Disciplinary Workflow), Rule 33

## Lock Status
**[MUTABLE]**

## Requirement
Gather the real-life workplace story that grounds the post. **Confirm all personal reactions and characterizations explicitly from the Founder before including them.**

The AI must:
1. Ask the Founder for the specific situation/question that inspired this topic
2. Record the story details as stated
3. If the story needs a reaction or emotional element, ask: "How did you feel about this?" or "What was your first thought?"
4. Never invent, assume, or embellish any part of the hook

## Mechanical Check
- **Validator:** None (qualitative — requires Founder confirmation)
- **Enforcement:** PROMPT_research_gathering

## Failure Consequence
**Block outline.** No article proceeds to H2 Outline without a confirmed personal hook (SPEC-010).

## Dependencies
- SPEC-010 (Personal Hook) — the requirement that every article has a hook
- SPEC-005 (No Fabricated Reactions) — the locked rule this process serves

## Override Rules
Can be overridden by the Founder if he provides the hook proactively. One-time only.
