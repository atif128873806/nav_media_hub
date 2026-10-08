# Application placed under version control — 2026-10-07

## User instruction

Initialize a Git repository in the application root, add a sensible `.gitignore` for Laravel build
output, local databases and uploads, and make the first commit so the work has a rollback point.
Recorded as TASK-016 / DEC-012.

## Starting state

`/home/atif/nabmediahub/.git` existed but was an **empty directory**, so `git status` reported "not a
git repository" and none of the redesign, design-system, inquiry or admin work had a diff, history
or rollback point. This had been logged as the project's single largest risk in `ARCHITECTURE.md`
and the handoff notes; it is now closed.

## What was done

| Step | Detail |
| --- | --- |
| Initialise | `git init -b main` in the application root, reusing the empty `.git` directory. No existing objects, no remote. |
| Ignore rules | Extended the Laravel `.gitignore` and `.gitattributes` already present rather than replacing them. |
| Stage | `git add .` only after each rule was checked individually. |
| Commit | Root commit `0ed1dbd`, 125 files, 20,008 insertions, authored with the machine's existing Git identity (a GitHub noreply address, so no personal email entered the history). |

### Ignore policy

Added explicitly:

- `/.freebuff` — local harness state (it holds a project id), placed beside the already-ignored
  `/.codex`, `/.cursor/`, `/.idea`, `/.nova`, `/.vscode` and `/.zed` tool directories.
- `/database/*.sqlite` plus `-journal`, `-shm` and `-wal`, with a comment stating that real inquiry
  contact data must never be committed.

Already covered by files Laravel ships, and **verified rather than assumed** with
`git check-ignore -v`:

- `database/.gitignore` → `*.sqlite*`.
- Every `storage/**` directory and `bootstrap/cache/` carry Laravel's `*` + `!.gitignore` pair, which
  is what keeps compiled Blade views, sessions, cache and logs out of the repository.
- The root file covers `.env`, `*.log`, `/vendor`, `/node_modules`, `/public/build`, `/public/hot`,
  `/public/storage`, `/storage/*.key` and `/auth.json`.

Checked paths that must stay untracked: `.env`, `database/database.sqlite`, `vendor/autoload.php`,
`node_modules/.package-lock.json`, `public/build/manifest.json`, a compiled view under
`storage/framework/views/`, `storage/logs/laravel.log`, `bootstrap/cache/services.php`,
`.freebuff/project-id`, `.phpunit.result.cache` — all ignored.

`.env.example` was kept (it is the template) after confirming it holds no real values: `APP_KEY` and
the AWS keys are empty and the mail/Redis entries are the literal `null` placeholder.

### Tracked deliberately

Application code, `config/`, Blade views, `resources/css` and `resources/js`, `database/` migrations
and seeders, the scaffold tests, `composer.json`/`lock`, `package.json`/`lock`, `vite.config.js`,
`phpunit.xml`, `boost.json`, `.npmrc`, the README/AGENTS/CLAUDE pointers, the relocation-notice
folder, the Boost `.claude/skills` rules, and the six encoded portfolio films with their posters
(`public/media/portfolio/`, about 158 MB, largest single file 43.7 MB).

## The media judgement, stated plainly

The films are the site's delivered content and the application cannot be deployed without them, so
they were included; the largest file is under GitHub's 50 MB warning threshold. This is the one
choice here that is really the owner's: a clone is now roughly 158 MB and the client's footage sits
inside the repository, which matters before any public push (TASK-004's publication check). Because
this is the only commit and there is no remote, the decision is cheap to reverse in either
direction — removing the media is one `git rm --cached` plus amend, and adding it later is one more
commit. The alternative (Git LFS or keeping media in the client's own storage) was offered and is
not yet chosen.

## Verification

- `git log --oneline` shows `0ed1dbd (root-commit)` on `main`; `git status --short` is empty, so the
  tree is clean and nothing outside the ignore rules is untracked.
- The media is genuinely in the object store, not merely listed: `git cat-file -s` reports 45,799,653
  bytes for `brampton-ravine-lot.mp4` and 32,120,345 for `short-form-brand-campaign.mp4`, matching the
  files measured on disk.
- Local-only files survived untouched — `.env` and `database/database.sqlite` are unchanged, and the
  original inquiry record is intact (`leads=1`, the existing `Muhammad Arslan` row). This was checked
  because the database is ignored and `phpunit.xml` runs tests against `:memory:`.
- `GET /` still returns 200 with the running `php artisan serve` process, and no source file was
  modified by this task.

## Open and limits

No remote is configured and nothing has been pushed; publishing needs explicit authorization and the
client publication check first. `.git` holds about 168 MB of loose (unpacked) objects — `git gc`
would tidy them but cannot shrink already-compressed video. This task changed no application
behaviour, so the build, test and browser checks recorded in the other notes of this date were not
re-run; the working tree is identical to the state that was verified.
