# Nav Media Hub — 03 Inquiry, consultation booking and admin specification

**Status:** Product specification for design and coding in PHP/Laravel; booking provider remains undecided. See `Nav_Media_Hub_05_Laravel_Technical_Plan.md` for implementation.  
**Important scope distinction:** The original client request confirmed a **one-page demo with a working hero form and submissions visible in admin**. The newer request asks us to research booking. A live consultation calendar is a proposed addition until the client explicitly approves it. A filming date is a project commitment and must be requested, then confirmed by Nav.

## 1. Name the three actions accurately

| Action | Meaning | Public wording | Result |
| --- | --- | --- | --- |
| Project inquiry | Visitor describes a possible production project | “Start a project” / “Tell us about your project” | New lead in admin; no appointment or shoot date promised. **Confirmed demo scope.** |
| Discovery consultation | Short call to discuss goals, rough scope and next steps | “Book a discovery call” only when real slots are available; otherwise “Request a call” | Confirmed calendar event or a pending call request. **Approval needed for live scheduling.** |
| Filming/shoot date | On-location/studio production requiring scope, crew, logistics and commercial agreement | “Preferred shoot date” / “Request a shoot” | Date preference recorded; Nav confirms it separately after review. **Never auto-label as booked.** |

The competitor patterns support this separation: [Revline](https://revline.studio/) offers both a project form and a distinct discovery-call link; [Lemonlight](https://www.lemonlight.com/lets-talk-video/) describes a submission followed by a discovery-call choice; [ByHadeed](https://byhadeed.com/) asks for a brief and then quotes the work. These are observed flows, not a reason to imply Nav already offers every one of them.

## 2. Recommended visitor journey

### A. Form-only demo, the baseline

1. Visitor opens the one public page, sees offer + labeled form in the hero.
2. Visitor enters required name, email, service interest and short project description. Phone, company, desired timeframe, city and preferred shoot date can be optional, depending on the client. Keep the visible hero form short; use a single optional “Anything else?” field rather than many mandatory questions.
3. Submission validates on client and server, saves exactly one lead, then returns a clear confirmation: “We received your project inquiry.” Only show a response-time promise if approved.
4. Owner opens authenticated admin, sees the lead newest first, reviews details and updates status.
5. A notification email may be sent, but lead storage is the source of truth. A failed email does not turn a successful stored submission into an apparent failure.

### B. Optional discovery-call booking

After a successful inquiry, offer “Choose a time for a discovery call” if approved. Let the visitor leave with the inquiry safely saved. If a calendar integration is live, choose a real free slot and collect only information missing from the lead. On actual provider confirmation, link the booking to the lead, show date, time, time zone, meeting method and reschedule/cancel route. If no live calendar exists, ask for preferred contact times and call it **a request**, not a confirmed booking.

An alternative “Book a call” button in the header can first collect a brief and then show scheduling, so the admin has one lead record. Avoid sending people to an external calendar with no way to reconcile a booked call to the inquiry inbox.

### C. Optional shoot-date request

Ask for location, preferred date/date range, service type, estimated outputs and any deadline. Show “date requested; we will confirm after reviewing scope and availability.” Nav may follow up with a quote and confirmed slot. Never expose raw crew calendars or imply a shoot is secured from one field selection.

## 3. Hero form specification

| Field | Requirement | Reason and behavior |
| --- | --- | --- |
| Name | Required | Trim whitespace; sensible length cap; preserve on validation error. |
| Email | Required | Format check and server validation; primary follow-up address. |
| Service interest | Required | Choices only from client-approved services, plus “Not sure yet.” Do not force a visitor to misclassify the project. |
| Project description | Required, short | Ask “What are you looking to create?” with a reasonable length cap and a plain example. |
| Phone | Optional by default | Make required only if the client commits to a phone-first follow-up. |
| Company/brand | Optional | Useful for B2B follow-up, but not essential to send. |
| City / shoot location | Optional, conditional | Ask when the visitor seeks on-location filming. |
| Timeframe / preferred date | Optional | A preference, never calendar confirmation. |
| Budget range | Optional, decision pending | Include only if client wants it and can explain ranges; “Not sure” must be possible. |
| Privacy acknowledgement | Concise and accessible | Say why details are collected, where the privacy notice is, and who will reply. Avoid pre-checked marketing consent. |

Use a proper success state and a single clearly named CTA. Disable repeated submission while pending; on retry, avoid duplicate records through a unique request identifier or equivalent server-side handling. Sanitize and validate incoming data, restrict submission rates, use spam controls that do not block legitimate visitors unnecessarily, and avoid placing personal data in analytics or public URLs.

## 4. Consultation scheduler requirements if approved

The scheduling provider or a future custom implementation should define:

- One clear meeting type to start: proposed 15–30 minute discovery call; **duration requires client approval**.
- Owner and connected calendar; weekly availability; exception dates/holidays; minimum notice; maximum advance window; buffer before/after; daily booking limit.
- Conflict checks against the actual busy calendar and, when relevant, each co-host. Hold/confirm slots atomically or rely on the calendar provider's authoritative reservation. If a slot disappears at confirmation, offer another slot without losing the brief.
- Visitor and owner time zones displayed explicitly. Store an unambiguous timestamp and the visitor-facing zone; show a clear local time in confirmation.
- Meeting method chosen by the client: video, phone or in-person. Do not invent a video link when none exists.
- Confirmation to both parties; change/cancel route; reminder policy and what happens on cancellation or no-show. Keep a booking state distinct from lead state.
- Failure handling: calendar unavailable, authorization expired, no slots, duplicate callback, user closes the scheduler, confirmation email fails. A saved inquiry remains visible in admin throughout.

[Google Calendar's official guide](https://support.google.com/calendar/answer/10729749?hl=en-ie) documents duration, availability/time zone, minimum lead time, buffers, daily limits, conflict checks, booking-form fields, confirmation and reminders. Its [overview](https://support.google.com/calendar/answer/11608416?hl=en) states a booking page can be linked or embedded and blocks busy times. [Calendly's routing-form guide](https://calendly.com/help/how-to-create-a-routing-form) documents answer-based routing and website embedding, but feature availability depends on plan. These are product-capability examples, **not** a booking-provider selection or a guarantee that all features are free.

## 5. Admin panel information and states

**Minimum for the confirmed demo:** authenticated owner login, lead list (newest first), full detail view, status update and logout. List columns: received time, name, service, email/phone summary, status. Detail: all form fields, source page, submitted time and any owner notes. Search/filter and export are useful later, not prerequisites unless client asks.

| Lead status | Meaning |
| --- | --- |
| New | Successfully saved; no review yet. |
| Reviewed | Owner saw the inquiry. |
| Contacted | Owner reached out. |
| Proposal sent | Quote/proposal sent, if workflow needs this. |
| Closed | Resolved or not proceeding; reason can be recorded privately. |

**If consultations are enabled**, add a separate booking status: `Pending request` (only when no live slot confirmed), `Scheduled`, `Rescheduled`, `Cancelled`, `Completed`, `No-show`. Store provider event ID if applicable, UTC start/end, time zone, meeting method, lead reference and last provider sync. Status names in the UI should be human-readable. A booking can be cancelled while the lead remains open. A lead can exist without any booking. Keep an activity timestamp/history for changes that staff need to explain.

**Access and handling:** Only authorized admin users view contact data. Sessions expire. Validate every mutation on the server, prevent unauthenticated data reads and avoid showing full inquiry content in notification subject lines. Define deletion/retention with the client before launch. Do not hard-code admin credentials in a demo or use browser storage as the lead database.

## 6. Acceptance scenarios

1. Submit a valid inquiry on desktop and mobile: one record appears in admin with matching data and time.
2. Submit missing/invalid fields: exact field errors appear; other values remain; no lead is created.
3. Slow network/server failure: the user sees a retry path; no false “received” success; a retried success creates one record.
4. Admin logged out cannot open list/details; logged in can update status; bad input cannot alter another lead.
5. If live booking is enabled, two simultaneous visitors cannot both confirm the same slot; the second receives a fresh choice.
6. A time zone difference is displayed clearly and the stored instant corresponds to the selected local slot.
7. Closing the booking step after submitting still leaves the project inquiry in admin.
8. Cancellation/reschedule updates the booking display without silently deleting the lead.
9. If a preferred shoot date is submitted, both the visitor and owner see “requested,” not “confirmed.”

## 7. Decisions before implementation

| Decision | Recommended default for the demo | Needs client answer |
| --- | --- | --- |
| Live appointment scheduling? | No; build the confirmed form/admin first | Yes. If included, choose provider after tech selection. |
| Consultation duration/owner/availability | Leave configurable, do not invent | Yes. |
| Shoot request in form? | Optional date/location fields only if actively offered | Yes. |
| Notifications | Optional owner email; database remains authoritative | Yes. |
| Price/payment | No online payment or automatic shoot confirmation | Yes if business requests them later. |
| Lead retention, staff access and response target | Define before production launch | Yes. |
