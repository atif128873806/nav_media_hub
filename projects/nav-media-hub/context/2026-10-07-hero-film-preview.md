# Hero film preview — 2026-10-07

## User request and the advice given

The user proposed making the Subaru 555 film (the footage the hero still is taken from) the
**full-bleed background of the entire hero section**, with a dark overlay if needed, no new
dependencies, and asked for an opinion **before** any change.

I advised against the full-bleed version and gave four reasons grounded in the project's own rules
and the actual file:

1. **It contradicts the specification.** AGENTS.md forbids placing essential copy on changing
   footage without sufficient protection, and document 02's hero row requires an opaque layer. The
   reference audit had already logged precisely this failure on a competitor — "the moving hero
   sometimes made small copy less legible" — and the small overline (#8a8982, 5.1:1 on a flat
   canvas) degrades over bright frames.
2. **An auto-starting 36-second loop obliges a pause control** under REQ-005 and document 02
   (pause/stop/hide beyond five seconds), so "background video" would add UI and change existing
   behaviour.
3. **First-paint cost rises about 136×.** The film is 1080×1920, 35.8 s, **25.1 MB at 5.6 Mbps**;
   the hero still that currently holds the first paint is **184 KB** with `fetchpriority="high"`.
   Document 05 says not to auto-download video at initial load.
4. **The geometry fights the idea.** A 9:16 source cropped to a wide hero with `object-fit: cover`
   shows roughly a third of the frame's height, and because the camera pans, a live crop cannot
   reproduce the deliberately chosen wide still. The hero would also show the same footage twice,
   or lose the contact-sheet frame that anchors sheet 01 and feeds `#work`.

The user chose the recommended alternative.

## What was implemented

The film now previews **inside the existing hero frame**, with the still still holding the first
paint. Three files changed, 94 insertions:

| File | Change |
| --- | --- |
| `app resources/views/home.blade.php` | `data-hero-preview` on the hero-frame link, and a `<video muted loop playsinline preload="none" aria-hidden="true" disablepictureinpicture>` with one MP4 source, layered above the `<img>` and below the scrim, ticks, play glyph and metadata bars. |
| `app resources/css/app.css` | `.hero-frame video` is absolutely positioned over the still, transparent by default, with `object-position: center 48%` to match the still's crop; `.hero-frame.is-previewing video { opacity: 1 }`; the hover push-in now covers the video as well as the still; the reduced-motion block hides the video entirely. |
| `app resources/js/app.js` | A preview controller: `pointerenter`/`focusin` start it, `pointerleave`/`focusout` stop it, an IntersectionObserver stops it below 25% visibility, and a `prefers-reduced-motion` change stops it. The `is-previewing` class is only added by the video's own `playing` event, so the still never flashes black, and a refused `play()` simply leaves the still in place. |

Design intent: the still keeps the deliberate first paint and the designed fallback; motion arrives
only on expressed interest (hover or keyboard focus), so nothing downloads at load, no pause control
is owed for an auto-starting loop, the headline and form still sit on stable surfaces, and the
contact-sheet frame plus its link to `#film-subaru-555` are untouched.

## Verification

- `npm run build` exits 0; `php artisan test` 2 passed; the reduced-motion rule (`hero-frame video
  { display: none }`) and the `is-previewing` rule are both present in the built stylesheet.
- **No video is fetched at load**: with the page freshly loaded, the media element reported
  `paused: true`, `readyState: 0`, `networkState: 1` and no `.mp4` in performance resource timing —
  the poster (184 KB) remains the first paint exactly as before. The request appears only after the
  first interaction: the network capture then logs `GET /media/portfolio/subaru-555.mp4 → 200
  (Media)`.
- **Playback works and looks right**: after the interaction the element reported `paused: false`,
  `readyState: 4`, a `currentTime` that keeps advancing (2.35 s and climbing), the `is-previewing`
  class present, and a screenshot showed live footage in the frame with the scrim, crop ticks,
  "SELECTED FILM / 02 · SUBARU 555", "AUTOMOTIVE", "VIEW THE FILM" and the play glyph all intact
  over it.
- **Every stop path holds**: pointer leave, focus out, and scrolling the hero off-screen all ended
  with `paused: true` and the class removed; the clip did not resume on its own when scrolled back
  without hover. Resting state returns to `video opacity 0.000` with the still visible.
- **No layout change**: the frame measures 619×348 at 1440 and 335×251 at 390 both before and after
  the change (the video is absolutely positioned and contributes no size), zero horizontal overflow
  at either width, and the mobile hero keeps its form-first order. Console clean apart from the
  Boost browser logger.

## Limits

- Hover was exercised by dispatching the same pointer event the handler listens for rather than by
  moving a physical pointer, and **real keyboard focus could not be produced in the browser panel at
  all**: `element.focus()` moved `document.activeElement` to the link but the browser delivered no
  `focus` or `focusin` event, which is the same window-not-OS-focused condition that stops
  `:focus-visible` from matching in this panel. The focus path was therefore verified by firing the
  matching event type; the only unverified link is the browser's own focus-event delivery, which is
  standard behaviour.
- `prefers-reduced-motion` could not be emulated with the available tooling, so that path rests on
  code and built-CSS inspection plus the fail-safe argument, not on a live reduced-motion run.
- The 25.1 MB clip is fetched in full on first hover, unchanged from the work-grid behaviour for the
  same file (one URL, so a browser serves both from cache). A shorter, lighter hero encode is still
  the better answer if the preview ever feels heavy.
- Judged in headless Chromium only. This change is **uncommitted** at the time of writing; the
  initial baseline commit remains `0ed1dbd`.
