# Portfolio website and Hostinger direction — 2026-10-07

## User-approved direction

The user asked for a professional real portfolio website using the supplied local videos, taking competitor references into account while improving the design, and reported having Hostinger Premium hosting. User prefers hosting the video files with the website and not using R2 for the initial portfolio. This supersedes the earlier R2 delivery proposal (DEC-006); see DEC-008.

## Supplied media and site exports

Source files supplied in `/home/atif/Downloads/` (preserved unchanged):

- `Brampton ravine lot_v2.mp4` → `brampton-ravine-lot.mp4`
- `Car Video.mp4` → `subaru-555.mp4`
- `August_Golf NewTrend_v2.mp4` → `august-golf-newtrend.mp4`
- `New Project 361 [0D1CD89].mp4` → `short-form-brand-campaign.mp4`
- `NAV02.mp4` → `education-hub.mp4`
- `New Project 368 [6CCD531].mp4` → `restaurant-stories.mp4`

Web-ready H.264 MP4s and local JPG posters are in the code project's `public/media/portfolio/`. Approximate combined delivery size: 158 MB, compared with roughly 930 MiB for the supplied originals. Outputs are normalized portrait 1080×1920, 30 fps, fast-start. The home page now presents six poster-led video cards after the inquiry hero. Working project captions were inferred from filenames/visible footage and require owner review.

Footage review identified real-estate walkthrough, Subaru track film, golf, mixed local-brand content, education promotion, and restaurant/food footage. Integration follows the user’s direct instruction; exact client publication permissions should be confirmed before public production launch.

## Implementation and verification

- Updated Laravel Blade home page, project configuration, public metadata and CSS while retaining the existing inquiry-first hero and established palette. Competitor work is inspiration only; no competitor assets or copy were copied.
- `npm run build`, `php artisan view:cache`, and `php artisan route:list --except-vendor` succeeded. No automated tests were run.
- Browser preview reviewed at responsive widths; portfolio posters/cards render. Native video controls are present. Playback interaction and full form/admin acceptance remain unverified.
- Hostinger has not been accessed; nothing has been uploaded or deployed. Current official plan limits vary by plan/region/account; check the user's own hPanel. Confirm PHP 8.3+ for this Laravel 13 project and the account's disk/database/domain details before deployment.

## Sources / limits

- User instruction in this conversation: approved integration of supplied videos and reports Hostinger Premium.
- Hostinger plan limits: https://www.hostinger.com/support/6976044-parameters-and-limits-of-hosting-plans-in-hostinger/
- Hostinger PHP version selection: https://support.hostinger.com/en/articles/1575755-how-to-change-the-php-version-of-your-hosting-plan
- Prior competitor audit: `context/references/2026-10-07-live-competitor-audit.md`.
- The source filenames and footage content do not establish official campaign names or client publication rights.
