# Public page redesign and theme pivot — 2026-10-07

## User instructions (two, same session)

1. **Redesign to competitor-grade quality:** audit the current design in the actual files, rebuild
   the UI to a high professional standard (hierarchy, typography, spacing, consistent design
   system, responsive), add smooth tasteful animation and a distinctive visual concept, preserve
   all existing content and behaviour, and avoid new dependencies unless necessary and explained.
2. **Theme and motion polish:** the abrupt switch from black sections to white sections looks
   jarring. Choose a premium, cohesive palette applied consistently so there are no harsh
   black-to-white transitions, and raise the animation quality to competitor level.

Both are user-approved scope. Neither changes the product requirements (REQ-001–REQ-010), the
inquiry workflow, the admin workflow, or any published copy.

## What changed

| Area | File | Change |
| --- | --- | --- |
| Design system | `app resources/css/app.css` | Rebuilt: colour/type/space/easing tokens, unified button, frame and card primitives, harmonised private-admin block. All previous admin selectors preserved. |
| Concept | `app resources/views/home.blade.php` | "Contact sheet": sheets numbered 01–06, crop-mark frame chrome on all media, timecode-style duration badges, tabular indices. All copy, the six-film loop, service rows, process steps, FAQ and closing CTA retained. |
| Layout | `app resources/views/layouts/public.blade.php` | Wordmark/footer markup, pre-paint `js` flag, scroll-progress element. |
| Motion | `app resources/js/app.js` | Staggered IntersectionObserver reveals, masked headline line reveal, media settle, rAF-throttled paint-only header state, scroll-progress hairline, `aria-busy` on submit. |
| Theme | `app resources/css/app.css` | One continuous warm dark canvas (page-level tonal gradient, transparent sections) replacing alternating dark/light section surfaces. |
| Dependencies | `app package.json` | Two build-time devDependencies, self-hosted at build time: `@fontsource/instrument-serif`, `@fontsource-variable/inter`. No runtime or CDN requests. |
| Docs | `memory/HANDOFF.md`, `TASKS.md` | Session records (TASK-013, TASK-014). |

## Why the fonts were added

The previous stack (`Iowan Old Style`, Baskerville, Palatino, Georgia / `Helvetica Neue`,
Helvetica, Arial) resolved to a Times clone and an Arial clone on the target machine, which was
measured with `fc-list` rather than assumed. No display serif was available locally. Shipped
build-time fonts were therefore necessary for the requested standard; nothing is fetched at
runtime.

## Verification performed

`npm run build` exits 0; `php artisan test` passes; `composer validate` valid. Every class used by
a Blade view was scripted against the built stylesheet. Contrast measured programmatically for
each text/canvas pair. Browser review at 1440, 1280, 960, 800 and 390 widths with console and
overflow checks. Inquiry flow re-verified end to end twice (valid save, invalid rejection with
preserved input, guest redirect); test leads were deleted afterwards.

## Limits

Layout aesthetics were reviewed in Chromium at the widths above; no other browser or device was
tested. Captions and publication permission remain owner-review items (TASK-004). Native video
controls are unchanged. No automated tests were added, so inquiry/admin flows remain manually
verified. At the time the application was not under version control, so this work had no diff or
rollback point. That was corrected later the same day: the repository was initialised with a root
commit `0ed1dbd`, which contains this redesign and retheme as part of its baseline (DEC-012).
