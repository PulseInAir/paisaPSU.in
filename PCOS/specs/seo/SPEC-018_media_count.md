# SPEC-018: Media Count — Default Is One Image

## Rule ID
RULE-018

## Source
Rule_v8, Section IV (Technical SEO Guardrails), Rule 18

## Lock Status
**[NEW] [CHANGED DEFAULT in v8]**

## Requirement
- Default: **one featured image** per article
- The image must be **dynamic and tailored** to that specific article's content and tone — not a generic template reused across articles
- The image idea must specify **which section/H2 it best represents**
- **Alt Text must carry the exact focus keyword phrase**
- If the Founder wants more than one image, that is his call per-article (no exception needed)
- Claude cannot verify whether the image has been embedded in WordPress — this is **Founder-confirmed**, not AI-verified
- Logged in the tracker's notes field at Scoreboard Tracking (SPEC-042)

## Mechanical Check
- **Validator:** None (image embedding is WordPress-side, not in article text)
- **Enforcement:** Prompt instruction in PROMPT_metadata_generation
- **Tracker:** Media count logged in notes field (no dedicated tracker field)

## Failure Consequence
**No block** — the image idea and alt text are generated at metadata step. Whether it's actually embedded is the Founder's responsibility.

## Dependencies
- SPEC-041 (Metadata Checklist) — image idea and alt text are part of the metadata output
- SPEC-042 (Scoreboard Tracking) — media count logged in notes

## Override Rules
The Founder can request more images at any time. This is not an exception — it's an explicit right (per v8 change from 4-image default).

## Source Note
v7 required 4 dynamic images by default. Article 31/392 session: Pulak explicitly directed 1-image workflow. This is the standing default.
