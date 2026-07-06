# SPEC-021: Table of Contents

## Rule ID
RULE-021

## Source
Rule_v8, Section IV (Technical SEO Guardrails), Rule 21

## Lock Status
**[MUTABLE]**

## Requirement
Use a Table of Contents plugin in WordPress to break down article text and enable Jump-To site-links for H2 subheadings.

This is a WordPress-side configuration, not an article-text rule. The AI's responsibility is to ensure H2 headings are structured properly for TOC generation.

## Mechanical Check
- **Validator:** None (WordPress plugin responsibility)
- **Enforcement:** Article structure (proper H2 hierarchy) is verified during PROMPT_outline_approval

## Failure Consequence
**No block on article.** If TOC is missing on the live site, it's a WordPress configuration issue, not a content issue.

## Dependencies
- SPEC-036 (H2 Outline Gate) — ensures proper H2 structure

## Override Rules
Can be overridden per-article by the Founder. One-time only.
