# Section label cleanup and work-section motion — 2026-10-07

## User instruction

Two changes to the delivered public page, with constraints: remove the hyphen/dash sign on the
section label and the line above that label (checking the attached reference picture first), and
make the simpler-looking sections, "for example section 03 (the work)", more creative with
high-level animation. Keep the current design and behaviour intact, add no new dependencies unless
necessary, and verify the sections still render across all frames.

The attached reference picture was measured rather than eyeballed: it is a 349×64 crop containing a
grey rule at **x 36–61, y 39** (exactly `1.6rem`, the `.overline::before` element) and a hairline at
**y 32 spanning the `02` and the label text**. Those are the two marks to remove. The crop is
archived at `assets/label-reference-2026-10-07.png`.

## What the second mark actually was

The hairline above the label was not a deliberate rule. `class="overline"` is also a **Tailwind 4
utility name**, and Tailwind scans Blade sources for candidate class names, so the built stylesheet
contained `.overline{text-decoration-line:overline}` — a decorative line drawn above the label text.
It did not exist in `resources/css/app.css`, which is why it was invisible to a stylesheet search.

## What changed

| Area | File | Change |
| --- | --- | --- |
| Label | `app resources/css/app.css` | `.overline` gains `text-decoration: none` (which resets the generated `overline` utility) and loses the `::before` rule; the two motion rules that animated that rule are removed. The sheet number and label text are unchanged. |
| Labels (scope) | `app resources/views/home.blade.php` | None needed. The change is on the shared `.overline` element, so all six sheets stay consistent. `.overline` is used nowhere else in the application, so the private admin is unaffected. |
| Section titles | `app resources/css/app.css`, `app resources/views/home.blade.php` | New `.title-line` device: each title line is its own block (so a line break never depends on JavaScript) and rises from behind a mask, staggered by `--line`, when its section arrives. Applied to the work, services, process, FAQ and closing titles — the hero keeps its existing `.line` device. |
| Work grid | `app resources/css/app.css`, `app resources/views/home.blade.php`, `app resources/js/app.js` | A canvas-coloured curtain is parked over each poster and is drawn back as the film arrives (the poster now waits at full opacity instead of fading), the frame rule for hover focus dims the films that are not hovered, and a single rAF pass alternates a small scroll-linked vertical drift between grid rows. |
| Services list | `app resources/css/app.css`, `app resources/views/home.blade.php` | The single block fade becomes three staggered rows that arrive from the left, plus a warm ember wash that sweeps across a row on hover or keyboard focus (implemented as an animated `background-size` so no stacking or z-index assumptions are needed). |

## Constraints honoured

No dependency was added or changed (`package.json` untouched). No published copy, section order,
form field, route, controller, model or admin view was touched. Motion remains transform/opacity
(or `background-size`) only, the hidden states are still applied only under `html.motion-ready`
(which JavaScript sets only when reduced motion is not requested), and the reduced-motion block is
unchanged. The pre-existing single scroll listener pattern was extended rather than replaced.

## Ambiguity recorded

"Section 03 (the work)" can mean either the films grid (`#work`, whose label reads
"02 Selected work · 06 films", the label shown in the reference picture) or the services list
(`#services`, whose label reads "03 The work, in a few frames"). Both readings were treated as in
scope, since the instruction says "some sections look too simple, for example …" and "in a few
frames". The film grid received the larger treatment.

## Verification performed

- `npm run build` exits 0; `php artisan test` 2 passed; no PHP file was touched, so the
  pre-existing `pint` findings on `bootstrap/app.php` and `routes/web.php` are unchanged.
- Computed style in Chromium confirms `text-decoration-line: none` and a `::before` content of
  `none` on all six labels, and a close-up of the work label matches the reference crop with both
  marks gone.
- Work grid: all six films reveal with the curtain settled off-frame (`translateY(-101%)`), drift
  offsets alternate per row at ≤11px and return to zero as a row crosses the viewport centre, and a
  forced covering state showed the parked curtain reading as a canvas panel rather than a visible
  plate.
- Viewports 1440, 1280, 960 (grid/breakpoint checks), 800, 390 and 360: no horizontal overflow on
  any of them, two columns at 390, one track at 360, and drift correctly disabled on the
  single-column layout.
- Fail-safe re-checked with `motion-ready` removed: zero hidden reveals, zero covered frames and
  zero shifted title lines.
- Console clean apart from the Laravel Boost browser logger; `/admin/login` still returns 200 and
  guest `/admin` still redirects.

## Limits

Judged in headless Chromium at the widths above; no other browser or device was tested, and hover
states were verified by rule inspection and a forced-state preview rather than a real pointer.
Reveal timing in the browser panel can lag when the tab is not painting frames, which is an
instrumentation artefact rather than page behaviour. No automated test was added, so the film
grid and services list remain manually verified only. At the time of writing the application had no
version control; it was initialised later the same day with a root commit `0ed1dbd` that contains
this change as part of the baseline (DEC-012).
