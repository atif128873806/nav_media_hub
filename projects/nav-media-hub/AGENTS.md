# AGENTS.md — Nav Media Hub

This file is the operating guide for any coding agent working on the **Nav Media Hub** project. It applies to the one-page creative agency demo and its private inquiry admin panel. It is not a guide for the Gossips Beauty salon or any other client.

## Mandatory start and recovery procedure

At the beginning of **every work session, new task, or resumed task after context compaction**, read this entire `AGENTS.md` first. Then:

1. Inspect the mapped application at /home/atif/nabmediahub and the current user request. Check existing code and changes before editing.
2. Locate the Nav Media Hub documents listed below, either beside this file or under `docs/`. Read the documents relevant to the task **before** planning or coding. Read the Laravel architecture document before any setup or backend work. Read the handoff document for any task that changes scope, copy, assets, data handling or launch behavior.
3. Reconstruct the current goal and decisions from the documents, the latest user instructions and actual project state. Do not treat a compacted conversation summary as the only source of truth.
4. If a needed document is missing, ask the user for it instead of inventing its contents. If a material requirement is unclear or documents conflict, identify the exact conflict and ask the user; continue independent work that is unaffected.
5. Before finishing, record what changed, what was verified, and any open client decision. Keep documentation synchronized if an approved decision changes the specification.

These steps apply again after **every** compaction, even if you remember reading the files earlier.

## Documents: read by task

| Task | Read first |
| --- | --- |
| Competitor research, design references, positioning | `Nav_Media_Hub_01_Global_Reference_Audit.md` and `Nav_Media_Hub_Competitor_Research_Brief.md` |
| Colors, typography, layout, responsive UI, video gallery | `Nav_Media_Hub_02_Design_and_Page_Blueprint.md`, then `Nav_Media_Hub_01_Global_Reference_Audit.md` |
| Inquiry form, validation, lead storage, admin panel, consultation or shoot requests | `Nav_Media_Hub_03_Inquiry_and_Booking_Spec.md`, then `Nav_Media_Hub_04_Content_and_Handoff.md` |
| Laravel setup, PHP version, routes, database, auth, media delivery, testing, deployment | `Nav_Media_Hub_05_Laravel_Technical_Plan.md`, then document 03 for the affected workflow |
| Client copy, portfolio media, permissions, acceptance testing, deployment | `Nav_Media_Hub_04_Content_and_Handoff.md`, plus the relevant design/workflow document |
| New feature or architecture decision | All five numbered documents, current user instructions and existing code |

Exact filenames are part of the handoff. Do not silently substitute unrelated project files. If the documents are placed under `docs/`, use those copies and avoid keeping conflicting duplicates.

## Goal and approved scope

Create **one public page** for Nav Media Hub, a Canada-based creative production/marketing business, with a prominent **project inquiry form in the hero**. Show selected, client-approved videos immediately after the hero. A **separate authenticated admin interface** must receive and display real submissions. The website should convey cinematic automotive, real estate and social content only to the extent the client confirms those services and supplies usable work.

The initial demo scope is the working form, persistent lead record, selected portfolio, responsive page and private lead admin. **A live discovery-call calendar is researched but not yet approved.** A preferred filming date is a request, not an automatically confirmed shoot. Do not add payments, packages, subscriptions, a CRM or scheduling integration based on assumption. **PHP and Laravel are approved.** Follow document 05 for the recommended Blade-first implementation and the PHP/Laravel compatibility check. Production database, hosting and deployment credentials remain unconfirmed; do not present a recommendation as a client decision.

## Design and content rules

- Follow the design blueprint and actual client assets. **Do not create a generic agency template or an obvious AI-generated design.** Use a deliberate editorial/cinematic composition with strong typography, restrained detail and a clear inquiry path.
- **Do not add AI-style icons, emoji icons, fake 3D symbols, random gradients, glowing cards, stock illustrations or decorative badges.** If a meaningful control needs an icon, use a simple consistent UI symbol with a clear purpose.
- The documented charcoal, warm-light and ember palette is **provisional**. Inspect the original logo and approved footage before finalizing the brand colors. Keep the hero form on a stable, readable surface; never place inputs or essential copy on changing footage without sufficient protection.
- Use only Nav Media Hub media, licensed assets or clearly marked temporary placeholders in a private prototype. Do not scrape the Instagram avatar as a production logo. Never copy competitor text, layouts pixel-for-pixel, imagery, logos, prices, reviews or claims.
- Do not invent clients, project outcomes, testimonials, awards, follower counts, timelines, service areas, turnaround, response promises or prices. Mark unapproved copy as draft and ask the user for a material missing business fact.
- Provide accessible labels, keyboard focus, clear form errors and success states, usable mobile layouts, video posters/fallbacks and user-controlled playback. Respect reduced-motion preferences.

## Functional rules

- The form must save **one durable lead** and give honest success/failure feedback. A failed notification email must not erase or hide a saved lead. Preserve user input on retry and prevent duplicate submission.
- Only authorized admins may see inquiry contact details or change status. Never expose leads through public routes or browser-only storage. Do not commit credentials, tokens or personal inquiry data.
- Keep lead status separate from booking status if consultations are later approved. A project inquiry or preferred shoot date must never be labeled as a confirmed appointment.
- If a live calendar is approved, use real availability, account for time zones and conflicts, and reconcile confirmed bookings with the admin lead. Follow document 03 and the client's specific scheduling decisions.

## Working with gaps

Look in the relevant project document first, then inspect existing code and approved assets. If a material answer is still absent, ask the user a focused question and state which decision depends on it. Examples: active services, priority audience, exact service area, portfolio permissions, logo, consultation availability, or public contact details. Make routine implementation choices within the approved stack using sound engineering judgment; do not block progress for minor details.

The current user request overrides a provisional document recommendation. If a new approved decision changes the plan, update the relevant document and tell the user what changed. Keep the public site to one page unless the user changes the scope; the private admin interface is separate.

## Delivery checks

Before reporting completion, verify the specific affected path end to end. At minimum for the demo: submit on desktop and mobile, confirm one accurate record in protected admin, verify signed-out access is blocked, exercise validation/error states, and open/pause each portfolio video with a usable poster/fallback. Report the evidence and any remaining asset or client decision plainly.

## Workspace is the authoritative home

These full project rules and the six handoff documents under this project's docs/ are the
single maintained source of Nav Media Hub instructions and specifications. The application's
AGENTS.md and CLAUDE.md are startup pointers, not separate rulebooks. The application's
old handoff folder is a relocation notice. Archived intake copies retain historical evidence
and must not be edited or treated as current specifications.

Active project: nav-media-hub. Code root: /home/atif/nabmediahub.
Workspace root: /home/atif/nav_mediaHub_workspace_project.
At startup read the workspace root AGENTS.md, workspace.yaml, USER_RULES.md, WORKFLOW.md
and this project's manifest, overview, requirements, decisions, tasks, context index/sources
and memory/HANDOFF.md. Use workspace routing to load only relevant skills. Check actual
code and tool access before relying on memory. Update central tasks and handoff before
finishing. If this workspace is inaccessible, ask for the correct location rather than
creating another instruction copy or inventing the missing requirements.

The existing composer.json already includes Laravel Boost; inspect its actual state before
repeating setup. Do not overwrite this project contract with generated bootstrap guidance.
The code, environment, dependencies and runtime lead database stay in the application root.
Never copy credentials, logs, sessions or inquiry contact data into the workspace.
