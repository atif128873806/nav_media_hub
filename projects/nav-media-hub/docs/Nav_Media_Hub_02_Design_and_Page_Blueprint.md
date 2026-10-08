# Nav Media Hub — 02 Design and one-page blueprint

**Status:** Proposed design direction for client review, 24 September 2026. PHP/Laravel is approved for development; this design is framework-independent.  
**Scope anchor:** One public marketing page with a hero inquiry form, selected content videos and a separate protected admin interface. Consultation scheduling is a decision in document 03.

## Design concept: editorial cinema with a clear inquiry panel

The site should feel like a working film portfolio, not a generic marketing template. Borrow the **principles** observed in [Rafhin Visuals](https://www.rafhin.com/) (strong film-led typography), [Revline](https://revline.studio/) (disciplined near-black/warm-light palette), and [ByHadeed](https://byhadeed.com/) (editorial narrative). Nav's original footage, brand mark and service promise must define the actual identity. Protect readability with a warm opaque form panel against any cinematic media.

### Provisional palette

| Token | Value | Intended use | Constraint |
| --- | --- | --- | --- |
| Ink | `#101112` | Hero and footer backgrounds; primary text on light surfaces | Main dark canvas. |
| Charcoal | `#191B1B` | Secondary dark surfaces | Subtle section changes, not a wall of identical black. |
| Paper | `#F5F2EC` | Form panel and private-admin surface only (superseded: see the 2026-10-07 note below) | Normal paper text uses Ink. Not used as a full section surface. |
| Stone | `#D7D0C5` | Fine rules, secondary decorative surfaces | Not for small text on Paper. |
| Muted light | `#9A9B98` | Secondary text on Ink only | Check every combination in final layout. |
| Ember | `#D6634F` | Restrained CTA or detail accent on Ink | Approx. 5.18:1 against Ink; approx. 3.26:1 against Paper, so do **not** use as small text on Paper. Button text on Ember uses Ink. |

**Superseded in part — 2026-10-07 (DEC-010, SRC-RETHEME).** The page no longer alternates dark and light section surfaces. The site is implemented as one continuous warm dark canvas (a page-level tonal gradient with transparent sections) so no boundary is a light/dark inversion; Paper survives only as the inquiry panel and the private-admin surface, which this document requires for form readability. The charcoal/ember accent family below is retained, re-tuned for a single canvas. Token values as implemented are recorded in the project DESIGN.md. The section order in this document is unchanged and still authoritative.

This is a **placeholder brand system**, not an assertion that the Instagram logo uses these colors. Swap the accent to a color supported by the original logo. Keep one accent, not multiple gradients. Ink/Paper contrast is approximately 16.9:1. Verify overlays using real video frames. [W3C guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum) explains the 4.5:1 normal-text minimum at WCAG AA.

### Type and composition

- Use one expressive editorial display family for major headlines and a highly legible sans for navigation, form labels and body. The exact licensed/web-safe font pair is to be approved after seeing the logo.
- Desktop content width: up to ~1240px within 32–48px side margins. Hero: roughly 55% story/media and 45% form, with a stable readable text block. Breakpoints are governed by content, not a device list; at narrow widths everything becomes one column.
- Hero title: approximately 64–80px desktop and 36–44px mobile, with no more than three short lines where possible. Body text: approximately 16–18px, comfortable line length. Small overlines can be uppercase but must not carry essential meaning alone.
- Square or modestly rounded media frames, editorial rules and numeric section labels may add rhythm. Avoid stock camera icons, invented award badges, glass cards, neon glows and decorative AI motifs.
- Use a single primary button style and a quiet secondary text/link style. Clearly visible keyboard focus and input error states are part of the design.

## Information architecture and exact section order

| Order / anchor | What the visitor sees | Purpose / behavior | Source needed |
| --- | --- | --- | --- |
| 0. Header | Logo, Work, Services, Process, Contact; “Start a project” CTA | Anchor links; compact mobile menu; CTA scrolls/focuses hero form. | Logo. |
| 1. Hero `#contact` | A precise benefit-led headline, approved location/service line, a strong approved poster or restrained motion frame, and inquiry form with “Tell us about your project” | Show what Nav does and allow submission immediately. All field labels visible; no text laid directly on a changing frame without an opaque layer. | Hero video/poster, approved offer, form destination. |
| 2. Selected work `#work` | 3–6 curated project entries, with first row showing an automotive and a property example if both are strong and approved | Poster, project title, category, deliverable and play action; no empty placeholders in final. Portrait reels keep their crop; wide films remain wide. | Original videos, thumbnails, client approval, names. |
| 3. Services `#services` | Three or four plain-language offers | Each has who it is for, tangible output, one CTA that preselects interest in the hero form. Avoid claiming unavailable services. | Exact offer list. |
| 4. Process `#process` | Brief → Plan → Shoot/Edit → Deliver, only if true | Explain what happens after inquiry and which stage requires a quote/date confirmation. | Real workflow and response expectation. |
| 5. Proof | One attributable testimonial or a small approved client/project strip | Give confidence without unsupported metrics. Omit if no permission. | Approved quote/logos. |
| 6. FAQ | Four to six concise answers: service area, project types, timing, revisions, pricing approach, shoot-date approval | Remove booking uncertainty. No invented fixed rates or delivery promises. | Client answers. |
| 7. Closing CTA | Short prompt, “Start a project” and optional “Book a discovery call” | Returns to form or verified availability, as decided in doc 03. | Booking decision. |
| 8. Footer | Contact, approved location/service area, Instagram, privacy link | Genuine, usable contact path. | Approved details and privacy copy. |

**Provisional headline options, subject to client approval:** “Visual stories worth stopping for.” / “Make your next project impossible to overlook.” Supporting line should name the actual service and geography, e.g., cinematic video and social content for automotive, real estate and brands in the confirmed service area. Do not publish a guess as fact.

## Hero layout and interactions

**Desktop (roughly ≥ 900px):** header above a two-column hero. Left: overline, headline, short description, unobstructed showreel/selected still with “Watch our work.” Right: Paper form panel with visible title, fields, privacy note and solid CTA. The form should start within the first viewport at common laptop sizes; its submit button may require a small scroll depending on height. Avoid shrinking controls simply to fit.

**Mobile:** logo/menu → headline and short description → full-width Paper form → optional hero media/poster. The Selected Work section follows. The form is the main action, and a motion-heavy media asset must not delay it. Anchor jumps should account for sticky header and keyboard.

**Portfolio:** no silent autoplay inside every card. Use sharp posters and play on explicit action; display a meaningful label, duration if known, and close/pause controls. If a short hero loop is chosen after real-media review, it must be muted, have a static poster and a pause control. W3C's [pause/stop/hide guidance](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide) applies to auto-start motion lasting more than five seconds. Google's [video performance guidance](https://web.dev/learn/performance/video-performance) supports poster and restrained preload to avoid downloading every video immediately.

## Interface states to design

- Header: default, scrolled, mobile menu open, keyboard focus.
- Form: pristine, focus, invalid, submitting, success, retryable server error, rate-limited/spam response. Preserve entered details on failure.
- Media: poster, loading, playing, paused, unavailable fallback. Portfolio page must work even if a third-party video fails.
- Consultation CTA, if enabled: availability loading, no slots, selected slot, confirmed, changed/cancelled, booking service unavailable.
- Admin visual baseline: login, empty inbox, populated list, lead detail, status update, no-access/expired-session. Admin specifics in doc 03.

## Quality bar for review

Desktop and mobile should reveal the offer and action quickly, show true work within one scroll after the hero, and maintain legibility with video playing or blocked. Check keyboard navigation, focus, labels, error announcements, responsive crops and reduced-motion. Use client-owned or licensed media only. Design should look deliberate when all video is paused, slow or unavailable.

## Decisions awaiting real client material

The final accent, logo placement, hero frame, service ordering, exact headline, testimonials and any claim such as “4+ years” require approval. Do not fabricate brand history, project outcomes, clients, awards or delivery timelines. Document 04 lists the assets and wording needed to finish them.
