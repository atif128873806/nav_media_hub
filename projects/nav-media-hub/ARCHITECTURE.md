# Existing architecture

Application root: `/home/atif/nabmediahub`. Dependency lock reports `laravel/framework` v13.33.0
and `laravel/boost` v2.10.0. `composer.json` requires PHP ^8.3. These are file observations, not a
current host runtime check.

Blade renders the public page and custom admin views. Vite builds CSS and a small JavaScript file;
there is no separate frontend application. `config/nav.php` holds the visitor service options and
the **six configured portfolio projects** (title, category, deliverable, duration, orientation,
`src`, `poster`), with the encoded films and posters served from `public/media/portfolio/`. Local
SQLite is used; production database and host are open.

| Responsibility | Application paths |
| --- | --- |
| Public render | routes/web.php; app/Http/Controllers/HomeController.php; resources/views/home.blade.php |
| Public layout/shell | resources/views/layouts/public.blade.php |
| Presentation system | resources/css/app.css (design tokens, canvas gradient, components, motion); resources/js/app.js (menu, reveals, header state, scroll progress) |
| Self-hosted type | build-time devDependencies `@fontsource/instrument-serif`, `@fontsource-variable/inter`, emitted into `public/build/assets/` |
| Portfolio media | public/media/portfolio/ (six H.264 portrait encodes + posters); masters stay outside `public/` |
| Inquiry save/retry | app/Http/Controllers/InquiryController.php; app/Models/Inquiry.php; inquiry migration |
| Admin auth/access | app/Http/Controllers/Admin/AdminSessionController.php; app/Http/Middleware/EnsureAdmin.php; bootstrap/app.php |
| Inbox/detail/status | app/Http/Controllers/Admin/InquiryController.php; resources/views/admin/inquiries/ |
| Private admin provisioning | app/Console/Commands/CreateAdmin.php; hidden password prompt; no default credential |

Public POST is CSRF protected and throttled. The server fingerprints normalized fields and uses a
unique submission key; admin routes use auth plus admin middleware. Existing tests are Laravel
scaffold examples, not inquiry/admin coverage, so the flows are manually verified rather than
regression-guarded. No live scheduler, mail delivery, payments or public lead API is configured.
No deployment has occurred and no R2/Stream delivery is configured (DEC-008 keeps initial media
site-hosted).

**The application is now under version control.** `/home/atif/nabmediahub` is a Git repository on
branch `main`; the baseline is the root commit `0ed1dbd` dated 2026-10-07 (125 files), which
includes the public page, its design system and motion, the inquiry form, the private admin, the
migrations and tests, the project rule pointers, and the six encoded portfolio films with their
posters. Previously `.git` was an empty directory, so nothing recorded here had a diff or rollback
point; that risk is closed.

Tracked: application code, config, Blade views, `resources/css` and `resources/js`, migrations,
scaffold tests, root project files and `public/media/portfolio/`. Ignored as local-only: `vendor/`,
`node_modules/`, `/public/build` and other build output, framework caches and compiled views (the
`.gitignore` files Laravel ships inside `storage/`, `bootstrap/cache/` and `database/`),
`storage/*.key`, `*.log`, `.env`, `/.freebuff`, and the local SQLite database — `database/.gitignore`
covers `*.sqlite*` and the root `.gitignore` repeats it explicitly, because that file holds a real
inquiry record. **There is no remote and nothing has been pushed**, so the tracked films are local
only; if the repository is ever published, confirm the client's publication permission first
(TASK-004) and expect a clone of roughly 158 MB of media.

Run application commands from the application root. See live technical plan document 05.
