# Decisions

| ID | Status | Decision | Evidence / limits |
| --- | --- | --- | --- |
| DEC-001 | approved | PHP/Laravel for the application. | SRC-RULES, Goal; SRC-LARAVEL §1. No production host is selected. |
| DEC-002 | approved | Inquiry and private lead admin are baseline; booking is a separate decision. | SRC-RULES, Goal and Functional rules; SRC-INQUIRY §1. |
| DEC-003 | approved | Register `nav-media-hub` in the shared workspace and map the existing code directory. | SRC-WORKSPACE-REQUEST, 2026-10-07; reversible configuration choice under the user's setup request. |
| DEC-004 | proposed | Final charcoal/paper/ember identity and specific headline/service copy. | SRC-DESIGN, Provisional palette and final section. Implemented draft is not client branding approval. |
| DEC-005 | proposed | Production MySQL/MariaDB or another hosting-compatible database. | SRC-LARAVEL §1. SQLite is the existing local implementation, not a production commitment. |

Observed implementation choices: Laravel 13, Blade, Vite, local SQLite, custom session auth
plus an admin boolean, config-based portfolio metadata. See ARCHITECTURE.md. Preserve these
unless an authorized task warrants change; their presence does not imply a client chose
every technical detail. No previous approved decision is superseded by workspace setup.

DEC-006 — **superseded**: earlier proposal to use R2 for portfolio delivery. Superseded by DEC-008.


DEC-007 — **approved**, user instruction dated 2026-10-07 (SRC-CONSOLIDATION, User instruction):
all maintained Nav Media Hub rules and handoff specifications live in the AI workspace
project. The application retains startup pointers and code. This supersedes DEC-003's initial
split-authority layout and earlier statements that application-local documents were canonical.
Project product scope remains unchanged. R2 delivery was later superseded by DEC-008.


DEC-008 — **approved**, user instruction dated 2026-10-07 (SRC-PORTFOLIO-WEBSITE): integrate the six supplied portfolio videos as optimized files served with the website; the user reports having Hostinger Premium hosting and prefers not to use R2 for this initial portfolio. Do not upload/deploy to Hostinger without a separate explicit launch instruction. Confirm exact hPanel plan limits, PHP 8.3+ compatibility, database and domain before deployment.

DEC-009 — **approved**, user instruction dated 2026-10-07 (SRC-REDESIGN): the public page adopts a
"contact sheet" editorial concept (numbered sheets, crop-mark frame chrome, timecode-style
badges) over a rebuilt design system, with two self-hosted build-time font packages
(`@fontsource/instrument-serif` for display, `@fontsource-variable/inter` for UI) because the
previous stack resolved to fallback clones on the target machine. Content, inquiry behaviour and
the private admin are unchanged; document 02's section order still applies.

DEC-010 — **approved**, user instruction dated 2026-10-07 (SRC-RETHEME): the public site uses one
continuous warm dark canvas (a single page-level tonal gradient with transparent sections)
instead of alternating dark and light section surfaces. This **supersedes** the "bright editorial
section" use of Paper in document 02 and the corresponding statement in DESIGN.md. Paper remains
the surface for the inquiry form panel and the private admin, which document 02 requires for form
readability. The ember/charcoal palette family from document 02 is retained, re-tuned for a single
dark canvas.

DEC-011 — **approved**, user instruction dated 2026-10-07 (SRC-LABEL-MOTION): the section label is
reduced to the ember sheet number plus the uppercase label text. The leading dash and the line
above the label are removed. The line above came from the class name `overline` doubling as a
Tailwind 4 utility (Tailwind scans Blade sources and generated `text-decoration-line: overline`),
so the shared `.overline` rule now resets the decoration; the change therefore applies to all six
sheet labels and to nothing else, since `.overline` is not used in the private admin. The same
instruction lifts the simpler sections with higher-level motion: masked line-by-line section
titles, a curtain reveal over each film poster, alternating per-row scroll drift in the work grid,
hover focus dimming, and staggered service rows with a sweeping hover wash. Motion stays
transform/opacity only, keeps the existing `html.motion-ready` fail-safe and reduced-motion
exemption, and adds no dependency. "Section 03 (the work)" was ambiguous between the films grid and
the services list, so both were treated as in scope.

DEC-012 — **approved**, user instruction dated 2026-10-07 (SRC-VERSION-CONTROL): the application at
`/home/atif/nabmediahub` is placed under Git on branch `main`, with the current state recorded as
the root commit `0ed1dbd`, so the work has a diff and rollback point where before there was none
(the `.git` directory was empty). Excluded from the repository as local-only: build output
(`/public/build`, Vite manifests), dependencies (`vendor/`, `node_modules/`), framework caches and
compiled views, `.env`, `*.log`, `storage/*.key`, the `/.freebuff` harness state, and the local
SQLite database, which contains a real inquiry record and must never be committed. Tracked
deliberately: the six encoded portfolio films and posters, because the site serves them directly —
if the repository is later published, TASK-004's publication check applies first. **No remote is
configured and nothing has been pushed**; pushing is a separate, explicitly authorized decision.

DEC-013 — **approved**, user instruction dated 2026-10-07 (SRC-HERO-PREVIEW): motion is added to the
hero by previewing the Subaru 555 film **inside its existing contact-sheet frame**, not by making it
the full-bleed background of the hero. The full-bleed proposal was considered and deliberately not
built, for four recorded reasons — AGENTS.md and document 02 forbid essential copy on changing
footage without an opaque layer (and document 01 logged that exact legibility failure on a
competitor); an auto-starting 36-second loop would owe a pause control under REQ-005; the 25.1 MB
portrait file is about 136× the 184 KB still that currently holds the first paint, against document
05's guidance not to auto-download video at load; and a 9:16 master cropped to a wide hero cannot
reproduce the chosen wide still. In the approved design the still remains the first paint and the
designed fallback, the clip is fetched only on hover or keyboard focus, and it stops on leave, on
leaving the viewport and under reduced motion. Content, copy, layout, the inquiry form and the admin
are unchanged, and no dependency was added.

DEC-014 — **approved**, user instruction dated 2026-10-07 (SRC-RAFHIN-LANGUAGE): the site's type
system follows the live reference, measured in a browser rather than judged from screenshots. One
house face — **Archivo** (variable) — now carries display, UI and body at 900/800/700/400, with
**Instrument Serif** kept for the italic accent line and **Azeret Mono** for numbers, timecodes and
meta, and every public section heading uses the same three-part device (eyebrow, serif italic line,
heavy uppercase line). The typefaces were installed as build-time devDependencies through the
existing `@fontsource` pattern (DEC-009); the now-unused Inter import was removed, so the change adds
no runtime dependency and no request to a third party. The same faces apply to the private admin,
which was previously serif, so the whole product reads as one type system. Recorded measurement: the
reference declares `IvyPresto Display` in its font URL but **never loads it** (a width probe matched a
deliberate no-such-font fallback exactly), so its italic accents are a generic serif fallback and our
Instrument Serif italic is genuinely better than what the reference renders. Nobody should revisit
this face. Their crimson accent, 12 px radius and palette were not adopted; ours stay per DEC-010.

DEC-015 — **approved**, user instruction dated 2026-10-07 (SRC-RAFHIN-LANGUAGE): the reference's
signature section behaviour was rebuilt with the project's own means, not by importing theirs. The
work grid is now the expanding portrait showcase rail (inactive `flex: 1 1 0` against an open tile of
`calc(var(--rail-h) * 0.5625)`, which is a true 9:16 at every width, on the reference's 0.38 s flex
curve, with the caption revealed only on the open tile); a new client strip applies the same device in
landscape and marquees on small screens; the service rows became the four-column ruled expertise grid
whose items rest at `opacity: .8`; and the closing statement is a photograph behind a dark pass and
ember wash with a scrubbed 40 px parallax. **No GSAP or other runtime library was added** — expansion,
scrims and the marquee are CSS, and activation, hash routing, preview states and parallax are
`IntersectionObserver`, `matchMedia` and rAF passes in `app.js`, as in DEC-011/013. Three engineering
limits are part of the decision: only **one film is in flight** (the open tile's clip waits 300 ms for
the pointer to settle and its source is released when the tile closes, because our masters are
25–44 MB where the reference's clips are small, and their own 50 ms debounce demonstrably queues
several); **previews are loaded only on pointer devices** (`(hover: hover) and (pointer: fine)`), so
touch devices see stills rather than a 25 MB autoplay; and the mobile film rail is a scroll-snap strip
rather than the reference's rAF marquee — the marquee is reproduced instead on the client strip, which
is the section whose reference is that rail. Clicking a tile opens an in-page `<dialog>` player with
sound, with the film file kept as the tile's `href` so the no-JS path still works. No competitor
wordmark, slogan, copy, logo, client name, media asset, accent or full-screen composition is reused,
and our section copy remains our own. The closing background uses the clean `posters/subaru-555.jpg`
frame because three of the six posters carry burned-in caption or brand text and cannot hold hero
scale.
