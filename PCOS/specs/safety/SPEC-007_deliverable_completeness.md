# SPEC-007: Deliverable Completeness (No Assumed Implementation)

## Rule ID
RULE-007

## Source
Rule_v8, Section II (Non-Negotiable Safety & Identity), Rule 7

## Lock Status
**[LOCKED] [STRENGTHENED in v8]** — Cannot be overridden by any instruction, including the Founder's.

## Requirement
The AI must never assume that a described edit, fix, or content change has been applied to the actual live article, WordPress post, or any file outside the conversation.

**Every deliverable is an explicit, complete output:**
- A downloadable file, OR
- Fully quoted paragraph/section text the Founder can copy directly

**The Strengthened Rule (v8):**
If any mechanical check (word count, keyword density, em dash, etc.) fails and is corrected in a sandbox file, the **complete corrected article text** must be pasted back into the conversation (or delivered as an updated file) in the **same turn** the fix is made — before metadata, linking, or tracker steps proceed.

Running a check silently and reporting only "pass" is **not sufficient**. The Founder must see the text the check was actually run against.

A description of a change, or a claim that checks now pass, is never itself a deliverable.

## Mechanical Check
- **Validator:** None (this is a structural/process rule, not a content check)
- **Enforcement:** Prompt instructions in PROMPT_quality_pass and PROMPT_section_drafting
- **The test:** Did the Founder receive the actual text, or only a report about it?

## Failure Consequence
**Block proceeding.** The AI cannot move to metadata generation, tracker updates, or session close until the Founder has seen and holds the actual corrected text. Re-delivery is mandatory.

## Dependencies
- SPEC-040 (Final Quality Pass) explicitly requires re-delivery when items fail and are fixed
- Every validator's failure path routes through this rule

## Override Rules
**No override possible.** This is a LOCKED rule. Source: Article 30/382 (fixes described without text), Article 31/392 (sandbox fixes reported as passing without re-pasting corrected text).
