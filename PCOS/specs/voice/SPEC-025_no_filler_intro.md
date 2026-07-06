# SPEC-025: The No-Filler Intro

## Rule ID
RULE-025

## Source
Rule_v8, Section V (Writing & Voice — Humanizer Protocol), Rule 25

## Lock Status
**[MUTABLE]**

## Requirement
Answer the main question early in the article. Never start with filler phrases like:
- "In this article, we will discuss..."
- "Let's explore..."
- "Today we'll look at..."
- Any variation that delays the value to the reader

The personal hook (SPEC-010) should lead directly into the core answer, not into a meta-description of what the article will cover.

## Mechanical Check
- **Validator:** `validate_forbidden_words.py` includes filler intro patterns
- **Manual review:** The AI checks the opening paragraph during PROMPT_section_drafting
- **Scope:** First 2 paragraphs of article body

## Failure Consequence
**Reject intro section.** Rewrite to lead with value. No separate block — caught during section approval loop.

## Dependencies
- SPEC-010 (Personal Hook) — the hook is the intro, not filler
- SPEC-024 (Forbidden Vocabulary) — overlapping forbidden patterns

## Override Rules
Can be overridden per-article by the Founder. One-time only.
