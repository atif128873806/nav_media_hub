# 2026-10-07 — Matching the live reference design language

User instruction (SRC-RAFHIN-LANGUAGE): study **https://www.rafhin.com/** in a browser, not from the
supplied screenshots, identify the typefaces and weights, and rebuild five numbered sections of the
public page on the same design language — with the explicit constraints to verify the real live
behaviour before implementing, keep every existing site behaviour working, and add no new
dependencies unless the reference site already uses them. No competitor branding, copy, slogans,
project names or assets may be reused.

## What the reference actually does (measured live, 2026-10-07)

Read from the live page, its stylesheets and its script (`/styles/base/tokens.css`,
`/styles/pages/home.css` — 20,427 chars, `/scripts/pages/home.js` — 11,002 chars), by computed-style
probes in Chromium rather than by eye.

- **Type.** `Archivo` (variable) for everything: 900 for display, 800 for nav and buttons, 700 for
  eyebrows, 400 for body. `Azeret Mono` 400/500 for the mission statement. `IvyPresto Display` is
  declared in the Google Fonts URL but **does not load** — a width probe against a deliberate
  no-such-font fallback returned identical metrics (306.8 px), so every "serif italic" accent on their
  site renders in a generic `serif` fallback. We therefore did **not** chase that face: our
  Instrument Serif italic accent is a genuinely rendering italic where theirs is a fallback.
- **Scale.** Section display 86.4 px / 900 / tracking −4.15 px (−0.048em) with a serif italic accent
  line at 48.96 px (0.567× of the bold line); hero 79.2 px bold against 72 px italic (0.91×); closing
  statement 120 px / 900 / −6 px with a 110 px italic (0.92×); eyebrow 10 px / 700 / 2.2 px / 38 %
  white; nav and buttons 11 px / 800 / 1.32 px, uppercase; body 14 px.
- **Palette.** `--black:#050505`, `--white:#f5f5f5`, accent `#cc2255`, radius 12 px, buttons pill
  (100 px). Their accent is crimson; ours is ember, and the palette was not adopted.
- **Rails (their signature sections).** `.showcase-rail` is a flex row, `gap: 6px`, height
  `clamp(480px, 36vw, 680px)`, `padding: 0 48px`, `overflow: hidden`. Two mechanisms exist: the
  landscape rail keeps inactive tiles at a fixed `clamp(72px, 6vw, 110px)` and lets the active tile
  `flex: 1 1 auto`; the portrait rail (`--vert`, height 640 px) gives every tile `flex: 1 1 0` and the
  active tile `flex: 0 0 360px` — exactly 640 × 9/16, a true portrait frame. Expansion animates
  `flex-basis` and `flex-grow` on `0.38s cubic-bezier(.25, 1, .5, 1)`. Tile content is
  `opacity: 0; translateY(8px)` until the tile is active; stills sit at
  `saturate(.6) brightness(.5)` and the active tile at `saturate(1) brightness(.8)`; a two-axis scrim
  (`rgba(0,0,0,.06→.12→.45)` vertical plus 55 %→8 %→55 % horizontal) holds the caption. Their script
  starts at index 2, loads the active clip only through an IntersectionObserver with
  `rootMargin: '0px 0px 400px 0px'`, plays the active tile, pauses it when the rail leaves the
  viewport, and switches on a 50 ms-debounced `pointerenter` or a click. On ≤768 px the portrait rail
  becomes a JS-cloned, rAF-marqueed track at 0.3 px per frame (≈18 px/s) with items fixed at 236×420,
  pausing on touch and resuming after 2 s.
- **Expertise and closing statement.** `.exp-grid` is four ruled columns (`border-top: 1px
  rgba(245,245,245,.5)`) whose items **rest at `opacity: .8`** and come to 1 with
  `translateX(4px)`; accent index, 900 uppercase name, one plain line of description. The closing
  section is a photograph behind a dark pass plus a crimson radial wash, centred eyebrow, a
  near-full-size italic line above a 120 px uppercase line, and a pill button; the photograph is
  scrubbed 40 px with GSAP ScrollTrigger.
- **Implementation.** GSAP 3.12.5 + ScrollTrigger from cdnjs, plus their own `nav.js`, `loader.js`,
  `home.js`. Breakpoints 1024 / 768 / 480 and `prefers-reduced-motion: reduce`.

## What was built

1. **Type system.** One house face for display, UI and body — `Archivo Variable` — with
   `Instrument Serif` reserved for the italic accent line and `Azeret Mono` for numbers, timecodes
   and meta. The heading device is now consistent everywhere: eyebrow, serif italic accent line,
   heavy uppercase line (`.title-line > em` / `.title-line > span`, `letter-spacing: -0.045em`,
   line-height 0.88, italic at 0.58em — 0.92em in the hero, 0.8em in the closing statement). Nav and
   buttons are 11 px / 800 / uppercase; buttons are pills; the wordmark is uppercase Archivo with a
   mono sub-label. Applied site-wide **including the private admin**, which was previously serif.
   Only one `font-family: var(--font-display)` rule remains in the stylesheet — the italic accent.
2. **Showcase rail (`#work`).** The six-film grid was rebuilt as the portrait rail: height
   `clamp(400px, 44vw, 640px)`, `gap: 6px`, whole-pixel gutter padding, inactive `flex: 1 1 0`, active
   `flex: 0 0 calc(var(--rail-h) * 0.5625)` so the open tile is a true 9:16 at every width, the same
   0.38 s curve, per-tile scrim, radial field behind the caption, and the number / title / category /
   duration / "watch the film" block revealed only on the open tile. Each tile is a real link to its
   film file, so the rail is six working films without scripting.
3. **Client strip (`#brands`, new).** The same body of work read as sectors: shallow landscape tiles,
   the active one opening to `clamp(220px, 26vw, 380px)` with its caption revealed, and on ≤800 px the
   duplicate-set marquee (CSS keyframe, 90 s, `calc(-50% + 3px)` so the loop is seamless, paused on
   hover or press) — the small-screen treatment the reference gives its own client rail.
4. **Expertise (`#services`).** The three service rows became the four-column ruled grid: accent mono
   index, 900 uppercase name, one line of plain description, items resting at `opacity: .8` and coming
   forward with `translateX(4px)`, each linking back to the film that shows it. 2 columns at ≤800 px,
   1 at ≤560 px.
5. **Closing statement (`.closing`).** One photograph behind the section with a dark pass and an
   ember radial wash, centred eyebrow, italic "have a story" above a 120 px "TO TELL?", and a pill
   inquiry button. The photograph travels 40 px as the section crosses the viewport (a rAF pass
   writing one custom property, the CSS-only equivalent of their scrubbed timeline).

Sheet numbering moved to 01–07 (hero, work, brands, expertise, process, FAQ, closing) and `#brands`
was added to the primary navigation.

## Constraints, and where we deliberately differ

- **No new runtime dependency.** GSAP was not added. Expansion, scrims, reveals and the marquee are
  CSS; activation, hash routing, previews and parallax are `IntersectionObserver`, `matchMedia` and
  rAF passes in the existing `app.js`, matching the discipline of DEC-009/011/013. Two **build-time**
  font devDependencies were added (`@fontsource-variable/archivo`, `@fontsource/azeret-mono`) because
  item 1 names the typefaces explicitly and this is the approved self-hosting pattern; the now-unused
  `@fontsource-variable/inter` import was removed and the package can be dropped.
- **One film in flight.** The reference autoplays the open tile's clip on desktop. Their clips are
  small; ours are 25–44 MB. So the tile opens immediately, the clip waits 300 ms for the pointer to
  settle, and closing a tile releases its source — a sweep along the rail cannot queue six films. The
  measured effect of the reference's own 50 ms debounce was exactly that hazard.
- **Previews on pointer devices only.** Films autoplay on `(hover: hover) and (pointer: fine)`;
  touch devices see stills. On a phone a 25 MB autoplay is not a design nicety.
- **Mobile film rail is a swipe strip, not a marquee** (documented deviation). The reference clones
  its portrait rail into an rAF marquee at ≤768 px. Ours becomes a horizontal scroll-snap strip with
  every caption visible and every film reachable; a marquee of six playable films on a phone is worse
  to use and worse to pay for. The marquee behaviour *is* reproduced on our site — on the client
  strip, which is the section whose reference is that rail.
- **The film player.** Clicking a tile no longer leaves the site to a raw MP4: where `<dialog>` is
  available the film opens in an in-page player with sound, dismissed by Escape, the close button or
  the backdrop. The tile's `href` is still the file, so the no-JS path is unchanged.
- **Not copied:** no competitor wordmark, slogan, copy, logo, client name or media; their crimson
  accent, radius and full-screen hero composition were not taken; the section headings keep our own
  words ("made to be / remembered", "made for / brands", "what we / do best", "have a story / to
  tell?"), and the closing background is our own film still.
- **Assets.** Of the six posters, three carry burned-in caption or brand text and are unusable at
  hero scale; the closing statement uses the clean `posters/subaru-555.jpg` frame after the
  restaurant poster was rejected on exactly that ground.

## Verification

- `npm run build` exit 0; `php artisan test` 2 passed. The built CSS carries the reduced-motion rules
  (`showcase-media video{display:none}`, `brands-track{animation:none}`,
  `showcase-item,.brand-tile{transition:none}`).
- Measured at 1440 in Chromium: section display 86.4 px / 900 / −3.888 px against the reference's
  86.4 / 900 / −4.15; italic accent 50.1 px against 48.96; hero 88 / 81 px against 79.2 / 72; closing
  120 px with a 76.8 px italic against 120 / 110; eyebrow 9.92 px / 700 / 2.18 px / 38 % against
  10 / 700 / 2.2 / 38 %; rail 634 px tall with a 356.4 px open tile (0.5625 exactly) and 189 px
  slivers against 640 / 360 / 188. All three Archivo, Azeret Mono and Instrument Serif faces report
  loaded.
- Rail behaviour: only the open tile carries a source; a hover that settles for 300 ms loads and
  plays that one film (`readyState 4`, advancing `currentTime`) while the previous tile's source is
  released; the player opened the right film at 377×731 with sound; the close button released the
  source (`src: null`, `readyState 0`).
- Hit areas and cross-links: brand tiles and expertise links set the hash and open the matching frame
  in the rail (education-hub → index 4, subaru-555 → index 1).
- Breakpoints 1440 / 1024 / 800 / 560 / 390: no horizontal overflow at any width; the rail is an
  expanding rail above 800 px and a snap strip below it; the marquee track measures 3546 px for two
  1770 px sets and is translating; expertise is 4 / 4 / 2 / 1 / 1 columns.
- Fail-safe: with `js` and `motion-ready` removed, every `.reveal` stays visible (the only elements
  below full opacity are the four expertise items at their intended 0.8), the rail shows its stills
  and the client strip shows every caption. Console clean throughout.
- Not verified live: `prefers-reduced-motion` cannot be emulated in the browser panel, so that path
  rests on code plus built-CSS inspection, and real keyboard focus still cannot be produced there
  (the panel reports no `focus`/`focusin` for `.focus()` calls), so focus-driven activation was
  exercised by calling the same code path directly.
