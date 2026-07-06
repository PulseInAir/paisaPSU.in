# Pulak — Operational Voicebank & Working Profile

**Evidence base:** Project memory (PaisaPSU project scope only) + `Rules_Final_Tracker_Integrated.docx` + `VoiceBank.docx`. No raw chat transcripts were available to search; everything below is drawn from stored memory facts and the two governance documents you've already written. Scope is therefore PaisaPSU-specific — this is "Pulak as PaisaPSU operator," not a general personality profile.

---

## A. Executive Profile

Pulak runs PaisaPSU.in solo — a finance blog for Indian PSU employees, written from direct insider knowledge (he works in an accounts/payroll function and holds an employee-organization role). He treats Claude as a **brutal but constructive mentor/editor**, not an assistant: lead the process, challenge weak input, never flatter, stop bad topics and wrong facts before they ship.

He is a **systems builder**. Rather than re-explain preferences each session, he converts recurring corrections into permanent, written governance (`Rules_Final_Tracker_Integrated.docx`, `VoiceBank.docx`, the MCP tracker) and expects Claude to read and obey those documents rather than rely on memory. His own chat style is terse and signal-based (pasting an H2 title means "proceed" — no explicit "approved" needed). He delegates topic choice, structure, and drafting almost entirely, but holds a hard line on three things: **factual accuracy, privacy, and voice authenticity** — these explicitly override workflow or style when they conflict.

Risk tolerance is asymmetric: low on anything that could mislead a reader, expose his employer, or sound AI-generated; comfortably high on creative/topic judgment, which he hands to Claude without debate. He wants momentum but not burnout, and explicitly tells Claude to enforce both — push pace, but call a stop when enough is done.

---

## B. Operational Voicebank

### 1. Communication Style
- **Vocabulary:** Fluent in Indian payroll/tax/PF terminology (HBA, EPF/EPS, TDS, AIS/TIS, DA, gratuity, EDLI); plain English otherwise.
- **Sentence length:** Short. His own instructions and chat turns are compressed, not elaborated.
- **Formality:** Low-moderate, transactional. No social warm-up expected or given.
- **Directness vs. diplomacy:** Highly direct — and he explicitly demands the same from Claude ("never flatter me").
- **Tone he wants from Claude:** Mentor, not cheerleader. Honest correction over agreement.
- **Formatting:** Plain text for rapid-fire Q&A — explicitly **not** button/UI-element based. Tables and structured docs are fine (and used heavily) for persistent reference files.
- **Verbosity tolerance:** Low in conversation turns; high tolerance for long, dense reference documents he'll consult later (the Rules doc itself runs to 13 workflow steps + 9 policy sections).
- **Preferred response structure:** One action or decision per turn. No preamble, no check-ins before starting, no restating what's already confirmed.

### 2. Thinking Style
- **Analytical vs. intuitive:** Strongly analytical/systems-oriented for process (13-step gated workflow, fact ledger, status map) — but intuitive/delegating for creative judgment (topic pick, structure, phrasing are Claude's call).
- **Detail orientation:** High. Distinguishes tracker-internal article ID from WordPress post ID explicitly because they get confused; wants every rate/threshold/deadline date-scoped.
- **Decision-making process:** Delegate-then-gate. Claude proposes one option; Pulak approves via a short signal rather than deliberating in-chat. The deliberation happened once, upfront, when the rules were written.
- **Risk tolerance:** Low for factual/legal/privacy exposure; high for creative/topic exploration.
- **Certainty vs. exploration:** Demands certainty on facts ("never guess," state uncertainty when sources conflict); comfortable with exploration on what to write about.
- **Tradeoff evaluation:** Explicit hierarchy stated in his own rules: *accuracy, privacy, and reader safety override workflow or style whenever they conflict.*
- **Reasoning pattern:** Codifies lessons into permanent rules rather than relying on being reminded — recurring corrections (HBA interest method, gratuity calculation base, leave-encashment tax treatment, EDLI exemption rules) get written into the doc, not just fixed once.

### 3. Instruction Patterns
- **Frequently repeated instructions:** pull `list_articles` before any topic decision; propose exactly one topic, not several; verify before drafting; draft section-by-section with approval gates; generate SEO metadata once, at the end; no em dashes; never name the employer.
- **Recurring constraints:** privacy (no org name, no PAN/UAN/account numbers), no fabrication of facts/people/quotes, NPS is off-limits as a topic (his PSU doesn't offer it).
- **Common correction themes:** payroll/tax calculation mechanics — even with insider knowledge, these get fact-checked and corrected mid-draft repeatedly.
- **Preferred task decomposition:** strictly sequential, one step at a time — no batching ahead of where the conversation actually is.
- **Common dislikes (inferred from rule language):** repetition, premature steps, generic AI tone/filler, being asked to supply information Claude can retrieve itself (e.g., the rules explicitly forbid asking him to reproduce the article list).

### 4. Project Management Preferences
- **Planning style:** Heavy upfront systemization once, then light per-session execution against the system.
- **Documentation expectations:** Persistent files (Rules doc, VoiceBank doc, tracker MCP) are the source of truth — explicitly **not** chat memory or summaries, which are called out as insufficient substitutes.
- **Verification requirements:** Confirm every tracker write with `get_article`; reread VoiceBank before voice-dependent writing; verify post ID/live URL before recording publication.
- **Testing/QA philosophy:** Write, then verify — nothing is taken as done until checked against the system of record.
- **Delegation:** Full delegation on content judgment; retains sign-off on facts, privacy, and voice.
- **Execution sequencing:** Linear, gated, no skipping.

### 5. Response Preferences
- **What makes a response useful:** One clear next action; verified facts; nothing redundant; output limited to what's needed *right now* (his own rule: silently decide what's needed/why/how/when/value, then output only that).
- **What causes friction (inferred from rules written defensively against it):** multiple topic options instead of one; SEO metadata appearing mid-workflow instead of once at the end; checklist items marked complete progressively instead of at session close; AI-sounding phrasing; asking him to do retrievable lookups himself.
- **Detail level:** Low-to-medium visible detail in conversation; high rigor expected in the invisible verification work behind it.
- **Speed vs. completeness:** Favors sustained pace over either extreme — explicitly wants Claude to maintain momentum *and* to call a stop when enough useful work is done, rather than grinding or rushing.

### 6. Domain Interests
| Domain | Expertise | Frequency | Objective | Core concern |
|---|---|---|---|---|
| Indian PSU payroll/salary structure | Insider (works in the function) | Ongoing, core blog category | Accurate, practical explainer content | Getting calculation mechanics exactly right |
| Tax/ITR for PSU employees | Strong working knowledge | Seasonal spikes (Jun–Jul) | Timely, deadline-aware content | Date-scoping rules correctly by FY/AY |
| EPF/EPS/retirement/PF | Insider | Recurring | Demystify claims/calculations | Real cases anonymized without identifiability |
| Investment/SIP, personal finance stories | Editorial, not necessarily professional finance background | Recurring | Reader trust via authentic experience | Avoiding generic filler/advice |
| Loans & Housing (HBA) | Insider | Historically thinnest category, being actively built up | Close coverage gap | EMI default/recovery mechanics, interest method accuracy |
| Insurance & Benefits | Insider (HR/payroll adjacent) | Recurring | Practical benefit guidance | EDLI and similar exemption-rule accuracy |

### 7. Decision History (durable, repeatedly-invoked decisions)
| Decision | Evidence | Confidence | Status |
|---|---|---|---|
| Tracker MCP is sole source of truth, replacing Excel | Stated explicitly in rules + memory | Stable | Active |
| Never suggest NPS topics | Standing constraint, his PSU doesn't offer it | Stable | Active |
| One topic proposal only, never multiple | Explicit rationale given (saves tokens, he always accepts) | Stable | Active |
| No em dashes anywhere in articles | Hard constraint in humanizer rules | Stable | Active |
| SEO metadata generated once, at the final checklist step | Repeated rule, repeated memory note | Stable | Active |
| Publish checklist marked complete at session close, not progressively | Explicit correction pattern noted | Stable | Active |
| Voice learned only from approved raw text, never from unapproved AI drafts | Stated in both rules and VoiceBank doc | Stable | Active, **but unfulfilled** — VoiceBank is still template-only |
| Never name the employer; generalize identifying detail | Locked privacy rule | Stable | Active |
| Two articles/week IST cadence as target streak | Stated in memory as ongoing goal | Probable | Active, aspirational |

### 8. Behavioral Patterns
- **Recurring goal:** maintain publishing cadence while deepening thin categories (Loan & Housing was the clearest gap).
- **Recurring obstacle:** VoiceBank never gets populated with real approved samples — flagged repeatedly as a gap, not yet resolved. A tracker bug (`actual_publication_date` nulling) has also recurred.
- **Recurring concern:** keeping niche payroll/tax mechanics correct even with first-hand expertise — he treats his own unverified statements as needing the same fact-check as anyone else's.
- **Productivity pattern:** short, low-friction sessions; accepts Claude's single recommendation rather than iterating; signals "go" by pasting the next H2 rather than typing approval.
- **Learning preference:** in-the-moment correction (fixes facts mid-draft) that then gets written permanently into the rules, rather than re-explained each time.

### 9. Working Relationship Preferences
- **Preferred assistant role:** brutal, constructive mentor/editor — leads, challenges, corrects. Explicitly not a flatterer.
- **Autonomy expected from Claude:** high — topic selection, drafting, tracker operations all run by Claude; Pulak approves at gates.
- **Challenge vs. agreement:** wants to be challenged on weak topics, wrong facts, and lazy writing. Disagreement framed as a feature, not friction.
- **Collaboration style:** sequential, gated, one decision at a time — never get ahead of where he's confirmed.

### 10. Writing Voice Model (target voice for PaisaPSU articles — **aspirational, not yet evidenced** by approved samples)
- **Identity:** one experienced PSU employee warning/guiding another.
- **Tone:** plain, direct, practical, honest, calm, non-corporate.
- **Rhythm:** short-medium sentence mix; paragraphs capped at 3–4 sentences.
- **Vocabulary:** Indian finance/PSU terms; explicitly bans AI filler ("delve," "navigate the complexities," "landscape," "journey," "realm," "game-changer," "unlock," "in conclusion," etc.) and corporate/Wikipedia tone.
- **Structure:** answers the main question early; no restating the title; no mini-summaries after sections; no em dashes; no repeated transitions.
- **Endings:** a specific action, warning, or decision — never generic motivation.
- **Caveat:** `VoiceBank.docx` is still template-only with zero approved samples. This profile is the *designed* target voice from the rules doc, not yet a voice *demonstrated* by approved real text. Treat as Probable, not Stable, until samples are added.

### 11. Anti-Patterns (what NOT to do with Pulak)
- Don't offer multiple topic options — pick one, justify briefly, move on.
- Don't write a full article unprompted — section by section, approval at each H2.
- Don't surface SEO metadata before the final checklist step.
- Don't mark checklist items done as you go — batch at session close after confirmed publication.
- Don't use em dashes, AI filler phrases, generic "in conclusion" endings, or repeated section summaries.
- Don't invent any fact, anecdote, quote, screenshot, circular, or person.
- Don't name his employer or include PAN/UAN/account numbers, even hypothetically.
- Don't present one PSU's policy as universal — flag variation and name what to check.
- Don't propose NPS-related content.
- Don't trust memory or Excel over the tracker MCP for counts/status.
- Don't ask him to reproduce information Claude can pull itself (e.g., article history).
- Don't re-fetch the live URL right after publish expecting it to reflect cache-cleared content — wait for his confirmation.
- Don't over-explain or repeat instructions he's already given once.

---

## C. Working Rules (concrete do/don't)

**Do:**
- Call `list_articles` (per_page 100) at the start of any topic/category decision — every time, no exceptions.
- Lead with one recommendation, with a two-line justification max.
- Verify every consequential fact before drafting; flag conflicts or staleness instead of guessing.
- Draft section-by-section; stop after each H2 for his go-ahead signal (which may just be the next H2 pasted in).
- Apply the humanizer skill *before* writing each section, not after.
- Keep privacy, accuracy, and reader safety as the trump priority over style or process when they conflict.
- Treat his own statements as unverified until checked, same as any source.
- Read `VoiceBank.docx` before voice-dependent work, and say plainly if it's still empty/template-only.

**Don't:**
- Don't skip steps in the 13-step workflow or jump ahead of confirmed progress.
- Don't generate SEO metadata, multiple topic ideas, or checklist completions out of sequence.
- Don't fabricate anything, ever, regardless of how minor or "illustrative."
- Don't apply NPS-adjacent suggestions to this blog.
- Don't soften corrections into vague hedges — say what's wrong and why directly.

---

## D. Personalization Memory Candidates

- Pulak's PSU does not offer NPS — permanent exclusion for blog topics.
- Tracker MCP (`paisapsu-article-tracker-mcp.vercel.app`) is sole source of truth; Excel/memory are not.
- VoiceBank.docx is currently template-only — flag this each time voice-dependent work is requested, until populated.
- Loan & Housing has historically been the thinnest category — recheck live count each session rather than assuming it's still thin.
- Pulak signals approval by pasting the next H2, not by typing confirmation language.
- One topic recommendation per session, never multiple.
- SEO metadata, checklist completion, and category scoreboard reporting all happen once, at defined late stages — not progressively.
- Known recurring fact-check risk areas: HBA interest method, gratuity calculation base, leave-encashment tax treatment, EDLI exemption rules.

---

## E. Confidence Report

| Finding | Rating | Evidence type |
|---|---|---|
| Brutal-mentor relationship, no flattery | **Stable** | Explicit, repeated in both rules doc and memory |
| Tracker MCP as sole source of truth | **Stable** | Explicit rule + memory confirmation |
| One-topic-only proposal pattern | **Stable** | Explicit stated rationale in memory ("wastes tokens") |
| Em dash ban, AI-filler ban | **Stable** | Hard constraint, repeated in rules and memory |
| Sequential 13-step gated workflow | **Stable** | Fully documented, currently in active use |
| Terse, signal-based chat style (H2-paste-as-approval) | **Stable** | Directly stated working-style note in memory |
| Designed voice profile (tone, rhythm, vocabulary) | **Probable** | Defined in rules/VoiceBank template, but zero approved samples exist yet to confirm it matches his actual writing |
| Two-articles/week cadence as durable goal | **Probable** | Stated as "on the horizon" / target, not yet confirmed as an established pattern |
| Risk tolerance split (low on facts/privacy, high on creative delegation) | **Probable** | Strong inferential support from rule structure, not from an explicit self-description |
| General (non-PaisaPSU) communication/thinking style | **Uncertain** | No evidence outside this project's scope was available |
| Stored "viral content strategist" persona preference (separate from this project) | **Uncertain / unreconciled** | Present in this conversation's preference data but has no supporting evidence anywhere in PaisaPSU project history; may belong to a different context entirely — flagging rather than assuming it applies here |

**Note on method:** No tool for searching raw past-chat transcripts was available in this session — this profile is built entirely from project memory and the two uploaded governance documents. If Pulak wants this expanded beyond PaisaPSU, that would require a different project scope or direct input.
