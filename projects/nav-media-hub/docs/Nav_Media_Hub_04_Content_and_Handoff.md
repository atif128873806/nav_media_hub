# Nav Media Hub — 04 Content inventory and coding handoff

**Prepared:** 24 September 2026  
**Purpose:** Give the future development session one place for approved scope, content dependencies, open decisions and testable outcomes. PHP/Laravel is approved; use `Nav_Media_Hub_05_Laravel_Technical_Plan.md` for the implementation plan. Hosting remains undecided.

## 1. Read order and source of truth

1. `Nav_Media_Hub_01_Global_Reference_Audit.md` — observed websites, inspiration and limits of the evidence.
2. `Nav_Media_Hub_02_Design_and_Page_Blueprint.md` — selected visual direction, page order, responsive behavior and states.
3. `Nav_Media_Hub_03_Inquiry_and_Booking_Spec.md` — form, lead admin, optional consultation scheduler and shoot requests.
4. This document — assets, unanswered business questions and acceptance criteria.
5. `Nav_Media_Hub_05_Laravel_Technical_Plan.md` — approved framework, recommended implementation, data contract and technical gates.
6. Earlier `Nav_Media_Hub_Competitor_Research_Brief.md` — first local audit; the numbered documents expand it.

If a client-approved requirement differs from a provisional idea here, record the decision before implementing. Treat competitor sites as evidence and inspiration, never as content to copy. The current project is **Nav Media Hub**, a creative production / marketing business, not a salon appointment website.

## 2. Confirmed baseline and proposed additions

| Item | Status | Delivery expectation |
| --- | --- | --- |
| One public page | Confirmed from client brief | Responsive marketing page with hero form and selected videos. |
| Hero inquiry form | Confirmed | Stores a real submission and shows success/error. |
| Admin panel | Confirmed | Authorized owner can view and manage submissions. It is a private interface, not another public marketing page. |
| Portfolio | Confirmed in principle | Use the client's own approved videos and posters; exact projects pending. |
| Live discovery-call calendar | Researched, not confirmed | Add only after client approves duration, owner and availability. |
| Shoot date requests | Possible form enhancement | Store a preference; Nav confirms separately. |
| Payments, packages, subscriptions, full CRM, campaign analytics | Outside stated demo | Add only with explicit new requirements. |

## 3. Content and media inventory to request

| Asset / answer | Minimum usable submission | Where used / why |
| --- | --- | --- |
| Brand mark | Original vector or high-resolution transparent PNG; light/dark variants if available | Header, footer, share image. A small Instagram avatar is insufficient to establish exact brand colors. |
| Brand guide | Colors, fonts, tone, any do/don't rules | Refines provisional palette and type in doc 02. |
| Hero film or still | Approved short film master or one striking landscape still + poster rights | First screen; still must work when playback is disabled. |
| Portfolio projects | 3–6 approved videos; title, client/industry, location if public, deliverable, publish permission | Selected Work. Include portrait and wide masters where available. Do not publish confidential projects. |
| Poster/stills | One intentional cover frame per video, preferably supplied as image | Fast gallery and clear focus before video plays. |
| Current offers | Exact names and what is included; flag inactive services | Hero copy, service cards and form selection. |
| Priority market | Main buyer segment and actual shooting geography | Specific headline, examples and FAQ. |
| Claims | Written approval for years active, notable clients, testimonials and response/delivery times | Avoid invented proof or unapproved promises. |
| Contact | Public email, phone if desired, Instagram URL, office/service area wording | Footer and replies. |
| Lead owner | Who receives leads and who needs admin access | Admin access and any notifications. |
| Privacy wording | Client-approved notice and desired retention period | Form and footer; avoid inventing a legal policy. |
| Consultation rules, if approved | Owner, call type/duration, time zone, weekly availability, booking limits and meeting method | Accurate scheduling. |

**Media handling direction:** obtain originals from the client; create responsive encodes and poster images later in the selected stack. Preserve intentional framing for 9:16 social reels versus wide property/brand films. Do not embed Instagram as the only video source for the portfolio; an Instagram link may supplement an owned, permissioned asset. Set clear accessible play labels and meaningful fallback when media cannot load.

## 4. Copy skeleton for approval

| Placement | Draft direction | Approval needed |
| --- | --- | --- |
| Hero overline | “Cinematic content · [approved service area]” | Actual geography. |
| Hero headline | “Visual stories worth stopping for.” | Client tone and priority segment. |
| Hero support | “We create film, photography and social content that helps [approved audience] show their work at its best.” | Which deliverables are offered now; avoid outcome guarantees. |
| Form title | “Tell us about your project” | Match actual follow-up process. |
| Submit CTA | “Send project inquiry” | Makes the immediate result clear. |
| Success | “Your inquiry has been received. [Approved follow-up expectation].” | Time and channel, if promised. |
| Services | “Real Estate Media,” “Automotive Content,” “Social Video,” etc. | Final names and inclusions. |
| Consultation CTA | “Book a discovery call” only for live calendar; “Request a call” otherwise | Scheduling decision. |

No copied competitor language, synthetic testimonials or generic stock visuals. If client media is missing during a private prototype, use clearly marked temporary placeholders and remove them before presenting it as finished work.

## 5. Decisions to take to the client

1. Which service is the priority on the homepage: property, automotive, general brand production, or an even split?
2. What exact cities/regions can the team shoot in, and is remote editing offered beyond those regions?
3. Which services are currently sold (video, photography, drone, social strategy/management, ads or automation)?
4. Which three projects may be featured publicly, and can Nav provide original files and publication permission?
5. Is the goal simply to receive a brief, or should visitors book a **confirmed discovery call** as part of this demo?
6. If calls are bookable: who hosts, what duration and hours, which time zone and conferencing/phone method?
7. Can visitors request a preferred shoot date? Who confirms date, quote and logistics?
8. What approved contact details and response expectation should appear? Who needs protected admin access?
9. Should the owner get email alerts, and how long should inquiries be kept?
10. Does the client have an existing logo guide and privacy notice? Which existing domain/hosting credentials will be used only after demo approval?

These answers improve copy and workflow. The **form/admin baseline can be prototyped** with a provisional layout and clearly marked demo content while business decisions are pending. Do not present a guessed offer as approved.

## 6. Implementation sequence in Laravel

1. Check PHP/Laravel compatibility and hosting constraints in document 05; collect client-approved assets and answers above.
2. Translate doc 02 into responsive page sections and all specified states using the actual brand mark and media.
3. Build the real form → persistent record → authenticated admin vertical slice; verify from browser to inbox.
4. Add curated work with correct video framing, poster/fallback and user-controlled playback.
5. Add consultation scheduling only if approved, then test data linkage, calendar conflicts and failure paths from doc 03.
6. Review copy, privacy text, media permissions, mobile usability, accessibility and launch configuration before domain cutover.

## 7. Definition of done for the client demo

- A new visitor understands the offer and can find a working inquiry form immediately.
- Selected work displays correct project metadata; every video opens, pauses and has a poster/fallback. No broken embed is required to understand the page.
- Valid form submission produces **one** durable lead; successful and failed states are unambiguous. No lead details appear publicly.
- Protected admin shows the exact submitted details, timestamp, status and a usable empty state; a signed-out visitor cannot read the data.
- Mobile layout retains readable hero/form, reachable controls and correctly cropped poster frames. Keyboard focus, labels, error messages and reduced-motion behavior are checked.
- Any consultation booking is described accurately as either a confirmed slot or a pending request. A preferred shoot date is never automatically confirmed.
- A client review can identify exactly which remaining assets and decisions prevent final launch.

## References

- Research: [Rafhin](https://www.rafhin.com/), [Revline](https://revline.studio/), [ByHadeed](https://byhadeed.com/), [Vidico form](https://vidico.com/contact/), [Lemonlight scheduling path](https://www.lemonlight.com/lets-talk-video/).
- Scheduling capabilities and constraints: [Google Calendar appointment schedule documentation](https://support.google.com/calendar/answer/10729749?hl=en-ie) and [Calendly routing documentation](https://calendly.com/help/how-to-create-a-routing-form).
- Web quality: [W3C contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum), [W3C motion](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide), [web.dev video performance](https://web.dev/learn/performance/video-performance).


## 8. Portfolio update — 7 October 2026

The user reports real client portfolio material and existing Cloudflare R2. The supplied
screenshot shows three separate attachments of 184 MB, 99 MB and 243 MB. The user states
the Drive-linked clips are 30–40 seconds; sizes of those linked clips and durations of the
separate attachments have not been verified. Actual video inspection, poster frames, final
project labels and publication permission remain pending. R2 web exports/custom domain are
a recommendation (DEC-006), not an approved upload. Evidence is registered centrally as
SRC-CONSOLIDATION and SRC-PORTFOLIO-SCREENSHOT.
