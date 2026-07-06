# SPEC-026: Voice Bank Consistency

## Rule ID
RULE-026

## Source
Rule_v8, Section V (Writing & Voice — Humanizer Protocol), Rule 26

## Lock Status
**[MUTABLE]**

## Requirement
Use natural Indian finance vocabulary and maintain a peer-to-peer, "experienced colleague" tone throughout. The voice should sound like one PSU employee advising another — not a corporate report, not a textbook, not a motivational speaker.

### Target Voice Characteristics
- **Identity:** Experienced PSU employee sharing practical knowledge
- **Tone:** Plain, direct, practical, honest, calm, non-corporate
- **Vocabulary:** Indian payroll/tax/PF terms (HBA, EPF/EPS, TDS, AIS/TIS, DA, gratuity, EDLI)
- **Rhythm:** Short-medium sentence mix; paragraphs capped at 3-4 sentences
- **Endings:** A specific action, warning, or decision — never generic motivation

### Voice Status
**VoiceBank.docx is currently template-only with zero approved samples.** The target voice is designed but not yet demonstrated by approved real text. The published PaisaPSU articles are the primary reference (SPEC-029).

## Mechanical Check
- **Validator:** None (voice is qualitative)
- **Enforcement:** PROMPT_humanizer applies voice rules during drafting
- **Reference:** `Pulak_Operational_Voicebank.md` for supplementary guidance

## Failure Consequence
**Reject section.** Sections that sound generic, corporate, or AI-generated are rejected during the approval loop.

## Dependencies
- SPEC-024 (Forbidden Vocabulary) — what NOT to say
- SPEC-029 (Voice Source Hierarchy) — which sources define the voice
- Reference: `Pulak_Operational_Voicebank.md`

## Override Rules
Can be overridden per-article by the Founder. One-time only.
