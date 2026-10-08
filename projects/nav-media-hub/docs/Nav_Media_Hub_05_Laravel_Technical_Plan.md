# Nav Media Hub — 05 Laravel technical plan

**Prepared:** 24 September 2026  
**Decision:** PHP and Laravel are approved by the project owner.  
**Purpose:** A buildable handoff for the one-page site, its hero inquiry form, client video portfolio and private lead admin. This document does not authorize a live scheduler or production deployment.

## 1. Read this with the product documents

Start with `AGENTS.md`. Use document 02 for layout, document 03 for inquiry/admin behavior, and document 04 for approved content, assets and remaining business decisions. Document 01 and the competitor brief explain the design references. If a technical suggestion here conflicts with an approved client requirement, record and resolve the discrepancy before implementation.

| Decision | Status | Development direction |
| --- | --- | --- |
| PHP + Laravel | **Approved** | Build a single Laravel application for public page and protected admin. |
| Laravel major / PHP runtime | **Conditional** | Prefer Laravel 13 if local and eventual host run supported PHP >=8.3. If hosting is fixed at PHP 8.2, use supported Laravel 12 and record the reason. Check installed runtime and host before pinning versions. |
| Rendering | **Recommended implementation** | Blade templates with Vite-built CSS and small progressive JavaScript; keep the public page server-rendered. Avoid adding a separate SPA, Inertia, Livewire or API purely for a small demo. |
| Database | **Recommended, not client-approved** | MySQL or MariaDB if available in the actual hosting environment; SQLite can be used locally. Confirm production database before deployment; use migrations to keep both environments in sync. |
| Portfolio storage | **Recommended, depends on file sizes and host** | Store client-approved media through a configured public media disk or delivery host; store only metadata/URLs needed for the page. Do not put large master video files in Git. |
| Email and queue | **Optional** | Persist lead first; add owner notification after email/account details are supplied. If queued, configure a real worker and failure monitoring before relying on it. |
| Live appointments | **Unapproved** | Implement only inquiry form and lead admin. Record a preferred shoot date as a request if the client approves that field. |
| Hosting/domain | **Unconfirmed** | Do not assume shared hosting, VPS, provider, credentials or domain cutover. |

Laravel's current official release information lists Laravel 13 with PHP 8.3 minimum and Laravel 12 with PHP 8.2 minimum; 12 is in security-fix support into February 2027. Verify compatibility against the server before initializing the project. [Official release notes](https://laravel.com/docs/13.x/releases) and [deployment requirements](https://laravel.com/docs/13.x/deployment).

## 2. Recommended Laravel application shape

One Laravel repository, one server-rendered public URL (`/`), and protected `/admin` views. Keep the admin compact and custom to the chosen editorial design; do not ship unrelated starter-kit pages or public registration. Use Laravel's existing session authentication facilities, server validation, migrations and HTTP tests. If a starter kit is installed to speed up authentication, remove/disable public registration and unused account flows and confirm what it actually generated. Laravel supports session authentication and route protection. [Official authentication docs](https://laravel.com/docs/13.x/authentication).

```text
app/
  Http/Controllers/HomeController.php
  Http/Controllers/InquiryController.php
  Http/Controllers/Admin/InquiryController.php
  Http/Controllers/Auth/AdminSessionController.php
  Http/Requests/StoreInquiryRequest.php
  Models/Inquiry.php
  Models/User.php
  Policies/InquiryPolicy.php  # if multiple roles/users require policy checks
config/nav.php                 # approved service options and contact details
database/migrations/           # inquiry table and auth-related tables
resources/views/home.blade.php
resources/views/admin/         # login, inbox, detail
resources/views/components/    # form, media card, feedback states
resources/css/ and resources/js/
routes/web.php
tests/Feature/               # meaningful form/auth/status behavior
```

These are suggested responsibilities, not a command to create empty files. A small controller and form request can suffice. Avoid an admin CMS or third-party admin framework unless complexity actually warrants it. The content portfolio can initially be a reviewed config/data file and Blade partials: admin only needs to manage submitted leads for this demo.

## 3. Route and permission contract

| Route | Method | Access | Behavior |
| --- | --- | --- | --- |
| `/` | GET | Public | Single marketing page with form and selected work. |
| `/inquiries` | POST | Public, throttled, CSRF-protected | Validate and create one inquiry; show field errors or an honest confirmation. Standard HTML POST/redirect is sufficient. |
| `/admin/login` | GET / POST | Guest | Custom login, rate-limited credential attempt. No registration link. |
| `/admin/logout` | POST | Authenticated admin | End session; CSRF-protected. |
| `/admin` | GET | Authenticated authorized admin | Newest-first paginated inquiries, empty state. |
| `/admin/inquiries/{inquiry}` | GET | Authenticated authorized admin | Full inquiry detail and owner notes if implemented. |
| `/admin/inquiries/{inquiry}/status` | PATCH | Authenticated authorized admin | Validate status against allowed list and persist. |

Use the `web` middleware group for session and CSRF handling. Require **both** authentication and an explicit authorization rule for every admin data route; knowing `/admin` is insufficient authorization. Implement a limited admin account provisioned privately by a safe command or secure setup step. Do not enable visitor self-registration or put a default admin password in code or documentation. Regenerate the session on login and invalidate it on logout using Laravel's authentication flow. Restrict login attempts and keep CSRF on forms. Never expose an inquiry JSON feed or unprotected file export.

## 4. Inquiry data contract and processing

Start with one `inquiries` table and the normal users/auth tables. Draft columns below are a migration plan; optional public fields should be shown only when approved in document 03/04.

| Column | Type / rule | Meaning |
| --- | --- | --- |
| `id` | Primary key | Internal reference. |
| `submission_key` | UUID/string, unique | Client-generated request token for deduplicating retries. |
| `request_fingerprint` | String, server-computed | Compare the normalized submitted fields when a key is replayed; do not include secrets. |
| `name` | String, required | Visitor name. |
| `email` | String, required | Reply address. |
| `service_interest` | String, required | Approved service option or “Not sure yet.” |
| `project_description` | Text, required | Short project brief. |
| `phone`, `company`, `city` | Nullable strings | Save only if collected in the approved form. |
| `preferred_date`, `timeframe` | Nullable date/string | Preference only; never confirmed booking. |
| `status` | String/enum-backed application value, default `new` | Allowed lead states in document 03. |
| `admin_notes` | Nullable text | Private; only if needed for the demo. |
| `source_page` | String, default `/` | Submission origin, no personal details in URLs. |
| `created_at`, `updated_at` | Laravel timestamps | Time of receipt and last change, shown in the admin's selected zone. |

Validate with `StoreInquiryRequest` (required fields, type, maximum length, email format, allowed service choices). Escape user content in Blade; do not render submitted HTML. Do not accept `status`, `admin_notes`, or admin-owned fields from the public request. Form submission sequence: validate → insert the inquiry with unique `submission_key` → redirect to an accessible success state → optionally send notification after successful persistence. On a repeated key, return the previously successful result only if the payload matches its original fingerprint; if it differs, return a conflict/validation error. Implement the consistency check atomically around the unique index to handle near-simultaneous requests. This avoids duplicate leads and misleading success when a retry races the first request. The form must retain ordinary input on validation or server failure.

Apply a modest rate limit to public submissions and login, plus a hidden spam trap or adaptive protection if spam becomes real. Avoid depending on browser-only validation. Store as little personal data as necessary; do not include full briefs or email addresses in analytics events, query strings or verbose application logs. The database is the lead source of truth even if mail fails.

## 5. Media and page delivery

Render the page sections in document 02's order: header, hero/form, selected work immediately after hero, services, process, approved proof if any, FAQ, closing CTA, footer. Use source filenames, captions, categories and framing approved in document 04. Build `<video>` sources or a controlled viewer with poster images and explicit playback controls; preserve portrait reels versus wide films. Provide a readable unavailable state and respect reduced motion. Do not auto-download every video at initial load; preload cautiously and serve appropriately compressed variants. If client files are not yet supplied, use visibly labeled temporary private-demo media, not unlicensed scraped Instagram uploads. Laravel's filesystem abstraction supports local and S3-compatible media disks when a production choice is made. [Official filesystem docs](https://laravel.com/docs/13.x/filesystem).

Use semantic markup, real form labels, visible focus, field-specific error messages, sufficient contrast and responsive crops. The palette remains provisional until original logo and footage are approved. Keep HTML metadata and the public contact data accurate; add privacy wording only when approved. The design document determines aesthetic choices, not Laravel starter-kit defaults.

## 6. Environment and deployment gate

Before coding: check `php -v`, required extensions, Composer, Node/build tool and actual hosting/runtime compatibility. Then choose supported Laravel version, record it in `composer.json`/lockfile, and select the available production database. Do not build around an assumed Hostinger/shared/VPS setup simply because other projects use it.

Before launch: keep `.env` outside version control; set a unique `APP_KEY`; set `APP_ENV=production`, `APP_DEBUG=false`, correct `APP_URL`, database and mail/storage settings; serve the Laravel `public/` directory as the web root; ensure `storage/` and `bootstrap/cache/` are writable only as needed; use HTTPS and secure session cookies; back up the lead database; build Vite assets; run migrations through an approved deployment procedure; run Laravel's production optimization steps. If mail uses a queue, a running worker/restart process and failed-job review are required. Obtain client signoff for privacy notice, lead retention, admin access and domain cutover before a public production launch. [Official deployment guide](https://laravel.com/docs/13.x/deployment).

No live calendar, payment processor, self-service staff provisioning, CRM or analytics dashboard is in the demo build. If approved later, extend the schema with a separate bookings table/status and use document 03's real availability and time-zone rules.

## 7. Coding order and focused verification

1. Create the Laravel project on a verified PHP version; choose Blade/Vite and configure local development database. Keep `AGENTS.md` in repository root and numbered docs in `docs/`.
2. Add the inquiry migration/model, request validation and public submission route. Complete the form → durable record path first.
3. Build admin login and authorization, newest-first list, detail and status mutation. Verify signed-out and unauthorized access cannot read lead data.
4. Build the one-page design and integrate approved video/poster files, then mobile and accessibility states.
5. Add optional notification only when owner email and operating method are confirmed; verify saved leads survive mail failure.
6. Run `php artisan test` for substantive feature cases: valid submission; invalid submission preserves input; duplicate retry creates one record; admin route access and status validation. Manually inspect responsive page, video fallback and keyboard interactions. Laravel's [HTTP testing guide](https://laravel.com/docs/13.x/http-tests) documents request and session assertions.

**Demo acceptance:** a visitor submits a valid hero form, sees a truthful confirmation, and the owner finds exactly one matching record in the protected admin. An invalid submission stores none; a retry does not duplicate; a signed-out visitor cannot inspect any inquiry. The page has working, permissioned work samples and the deliberate visual structure in document 02.

## 8. Outstanding answers (do not quietly assume)

- Actual deployment host, PHP version and database availability: determine Laravel major and production database before lock-in.
- Approved logo and media files/rights, services, priority audience, locations, contact details and privacy notice: determine publishable copy and visual identity.
- Owner's admin account/email, whether notifications are needed, and retention period: determine provisioning, mail configuration and lead handling.
- Whether confirmed call booking or optional preferred shoot-date fields are wanted: decide separately from the already approved inquiry flow.

These answers are gates only for the specific dependent decision. Build the form/admin demo with clearly marked provisional content while waiting; never present guessed business facts as approved.
