# Design context

Canonical guidance: workspace document 02, followed by workspace document 01. This file records
what the application actually implements, so it can be checked against the code.

## Implemented direction (2026-10-07)

The public page uses a **contact-sheet editorial concept**: sheets numbered 01–07 running down the
page, crop-mark corner ticks and a metadata bar on media frames, timecode-style duration badges,
mono indices, and hairline rules as a printed-sheet grid. Per DEC-014/015 the type and section
devices follow the live reference studio site (SRC-RAFHIN-LANGUAGE), whose measured values are
recorded in `context/2026-10-07-rafhin-design-language.md`. Section order is: header; hero with
inquiry form; **showcase rail**; **client strip**; **expertise grid**; process; FAQ; **closing
statement**; footer. Mobile order puts the form before hero media.

Per DEC-010 the site sits on **one continuous warm dark canvas** — a single page-level tonal
gradient with all public sections transparent — so no section boundary is a light/dark inversion.
This supersedes the "bright editorial section" use of Paper in document 02. Paper is retained only
as the surface of the inquiry form panel and the private admin, which document 02 requires so the
form stays readable against media.

## Tokens as implemented

| Token | Value | Use |
| --- | --- | --- |
| `--canvas-1` … `--canvas-3` | `#0b0c0c`, `#101212`, `#151817` | Warm near-black stops of the page gradient. |
| `--canvas-4` / `--canvas-warm` | `#121110` / `#1a1310` | Warm close of the gradient; footer surface. |
| `--on-ink` / `--on-ink-soft` / `--on-ink-mute` | `#f3f0e9` / `#b3b1a9` / `#8a8982` | Text ramp on the dark canvas (measured 15.7–17.2 : 1 / 8.3–9.1 : 1 / 5.1–5.6 : 1). |
| `--paper` | `#f5f2ec` | Inquiry panel and private admin only. |
| `--ember` | `#d6634f` | Single accent; 4.9–5.4 : 1 on the canvas. |
| `--ember-deep` | `#9c4433` | Accent for small text on the light panel (5.7 : 1). |

Type (DEC-014): **Archivo** for display, UI and body — 900 display, 800 nav and buttons, 700
eyebrows, 400 body; **Instrument Serif** for the italic accent line only; **Azeret Mono** for numbers,
timecodes and meta. All three are self-hosted build-time assets through the `@fontsource` pattern
(DEC-009) and the only remaining `font-family: var(--font-display)` rule in the stylesheet is that
italic accent. The heading device is one shape everywhere: eyebrow (10 px / 700 / 0.22em / 38 % white),
serif italic line, heavy uppercase line (900, `letter-spacing: -0.045em`, line-height 0.88, italic at
0.58em — 0.92em in the hero and 0.8em in the closing statement). Nav and buttons are 11 px / 800 /
uppercase on pill radii; the wordmark is uppercase Archivo with a mono sub-label. Fluid scale from a
2.4–5.4rem section display (7.5rem in the closing statement) down to a 0.62rem label.

Sections as implemented: the **showcase rail** (inactive `flex: 1 1 0`, open tile
`calc(var(--rail-h) * 0.5625)` so it is a true 9:16 at any width, 0.38 s flex curve, caption and
`is-previewing` clip only on the open tile, height `clamp(400px, 44vw, 640px)`); the **client strip**
(landscape tiles opening to `clamp(220px, 26vw, 380px)`, a duplicate-set CSS marquee on ≤800 px); the
**expertise grid** (four ruled columns, accent mono index, 900 uppercase name, items resting at
`opacity: .8` and coming forward 4 px); and the **closing statement** (photograph behind a dark pass
and ember radial wash, photograph travelling 40 px as the section crosses the viewport, 120 px
uppercase line over a pill inquiry button). Only one film is in flight and previews load on pointer
devices alone (DEC-015).

Section labels ("sheet" numbers 01–06) are the ember number plus the uppercase label text: no
leading rule and no text decoration. The `overline` class name doubles as a Tailwind utility that
drew a line above the label, which is reset in the shared rule (DEC-011).

The hero's film frame previews its own footage: the still holds the first paint and stays as the
fallback, and the clip fades in over it only while the frame is hovered or keyboard-focused,
stopping on leave, on leaving the viewport or under reduced motion (DEC-013). The hero is
otherwise a still composition, so the headline and form always sit on stable surfaces.

Motion: masked line-by-line headline reveal, and the same mask drives every section title (each
title line is a block, so line breaks never depend on JavaScript); the rail's flex expansion with
its caption revealed on open and only the open tile's clip loaded; the client strip's marquee;
staggered section reveals on an expo curve; the closing photograph's 40 px scroll travel; and a
scroll-progress hairline. All animation is transform, opacity, flex-basis or `background-size` only;
scroll work is rAF-throttled and paint-only. Reveals hide content only after JS registers the
observers, so the page reads fully without JavaScript — the rail is six working links and the strips
are legible as stills — and `prefers-reduced-motion` removes the hidden states, the previews, the
marquee and the section transitions entirely.

## Still open

Final active services, service area/geography, logo, contact details, privacy wording and genuine
proof remain unapproved; the wordmark is still a text placeholder. Portfolio captions were inferred
from filenames and footage and need owner review before public launch (TASK-004). References supply
principles only — no competitor copy, layout or asset is reused.
