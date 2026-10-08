# Project memory

- Workspace ID: nav-media-hub; code root: /home/atif/nabmediahub (SRC-WORKSPACE-REQUEST).
- Baseline: one public page, hero inquiry, persistent lead, separate protected admin (SRC-RULES).
- Stack exists: Laravel 13/Blade/Vite/local SQLite; source inventory in ARCHITECTURE.md (SRC-IMPLEMENTATION).
- Final media, brand, services/geography, contact and privacy/retention remain pending (SRC-HANDOFF).
- Calendar is unapproved; inquiry never confirms a shoot (SRC-RULES / SRC-INQUIRY).
- Workspace docs/ handoff documents remain authoritative; context/inbox holds dated source archives.
- Prior build/syntax/migration checks were reported in the earlier development chat. They were not
  repeated as part of registration; functional inquiry/admin acceptance is still pending.
- Read TASKS.md and memory/HANDOFF.md before resuming. Check current tools/runtime/Git/preview afresh.

DEC-007 makes this workspace AGENTS.md and docs/ authoritative. Code-folder instructions are startup pointers only. See latest handoff and SRC-CONSOLIDATION. Temporary .py helpers were migration/validation tools, not Laravel runtime code.


Portfolio update: six user-supplied videos integrated as optimized first-party site media, about 158 MB total. User reports Hostinger Premium and has chosen not to use R2 initially (DEC-008). See `context/2026-10-07-portfolio-website.md`; Hostinger account specifics and public-launch content review remain open.

Public presentation was redesigned on 2026-10-07 (DEC-009, contact-sheet concept, self-hosted fonts)
and rethemed to a single continuous dark canvas (DEC-010, supersedes the bright Paper section in
document 02). Paper now survives only as the inquiry panel and admin surface. Evidence and limits:
context/2026-10-07-redesign-and-retheme.md; session records in memory/HANDOFF.md and TASKS.md
(TASK-013, TASK-014).

Section labels were simplified and the simpler sections were animated further on 2026-10-07
(DEC-011: no leading dash or line on the label — the line came from the `overline` class name
colliding with a Tailwind utility — plus masked section-title lines, a curtain reveal on film
frames, per-row scroll drift, hover focus dimming, and staggered service rows with a sweeping
hover wash). Evidence and limits: context/2026-10-07-label-cleanup-and-work-motion.md; session
records in TASK-015 and memory/HANDOFF.md.

The application is under version control as of 2026-10-07 (DEC-012, TASK-016): Git repository on
branch `main` with root commit `0ed1dbd` as the baseline, including the redesign, retheme, label
cleanup, motion work and the six portfolio films. Build output, dependencies, `.env`, logs,
framework caches, harness state and the SQLite database (which holds a real inquiry record) are
ignored; no remote exists and nothing has been pushed. Evidence and limits:
context/2026-10-07-version-control.md.

The hero film previews inside its own contact-sheet frame as of 2026-10-07 (DEC-013, TASK-017): the
still keeps the first paint and the clip is fetched only on hover or keyboard focus. The user's
original full-bleed hero background proposal was advised against and not built, for the rules and
cost reasons recorded in context/2026-10-07-hero-film-preview.md. That change is uncommitted; the
baseline commit is still `0ed1dbd`.

As of 2026-10-07 the public page follows the design language of the live reference studio site
(DEC-014/015, TASK-018), which was measured in a browser rather than judged from screenshots:
Archivo is the house face for display, UI and body, Instrument Serif survives only as the italic
accent line, Azeret Mono carries numbers and meta, and every section heading is built from the same
eyebrow / italic / heavy-uppercase device. The work grid is the expanding portrait showcase rail, a
new client strip marquees on small screens, the service rows became a four-column ruled expertise
grid, and the closing statement is a photograph with a scrubbed parallax. No runtime library was
added — the behaviour is CSS plus IntersectionObserver and rAF — only one film is ever in flight,
previews load on pointer devices alone, and no competitor wordmark, copy, logo, client name or asset
is reused. The reference declares `IvyPresto Display` but never loads it, so that face should not be
chased again. Evidence, deliberate deviations and limits:
context/2026-10-07-rafhin-design-language.md.
