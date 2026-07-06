# SPEC-017: Internal and External Linking — Drafted In, Not Retrofitted

## Rule ID
RULE-017

## Source
Rule_v8, Section IV (Technical SEO Guardrails), Rule 17

## Lock Status
**[NEW] [STRENGTHENED in v8]**

## Requirement
- Link to at least **one internal PaisaPSU article** and at least **one authoritative primary source** (DoFollow)
- Linking is part of **Section Writing** (SPEC-038), not a separate late-stage step
- As each H2 is drafted, if that H2 naturally references another PaisaPSU article's topic or an external authoritative fact, the link is inserted at that moment
- Links must be **verified live** via web_search or web_fetch before the section is presented as complete
- If no H2 naturally supports a link, add one link during the What Changed / opening section by default
- **A URL is a factual claim** under LAW-4 and must be verified with the same rigor as a statistic

## Mechanical Check
- **Validator:** None (link verification requires live web access, not static analysis)
- **Enforcement:** Prompt instruction in PROMPT_section_drafting
- **Verification:** Each link is web-searched/fetched during drafting to confirm it resolves and is relevant

## Failure Consequence
**Block section approval.** A section containing an unverified link cannot be approved. A section with no link when one naturally fits should have the link added before moving on.

## Dependencies
- SPEC-004 (No Hallucinations) — URLs are factual claims
- SPEC-035 (Fact Verification) — link verification follows the same standard
- SPEC-038 (Section Writing) — where linking happens in real time

## Override Rules
Can be overridden per-article by the Founder. One-time only.

## Source Note
Article 30/382: fabricated URL nearly shipped. Article 31/392: linking was correctly verified but handled as a full separate step after Quality Pass, requiring the user to ask why it was missing.
