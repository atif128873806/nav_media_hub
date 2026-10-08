# Official Laravel Boost — setup in a real application

Source: https://laravel.com/framework/docs/12.x/boost
Repository reviewed: https://github.com/laravel/boost
Reviewed 2026-10-04. Check the matching installed Laravel/PHP versions and Composer
compatibility before installing; the current upstream branch is not proof of a compatible
stable release for every old application.

The workspace bundles static official Laravel best-practices guidance with portable
command rendering. It does not install the Composer package or an MCP server in your
client apps. Boost generates package-aware guidance/skills from the actual application;
that setup belongs inside each real Laravel repository.

## Setup workflow

1. Inspect composer.json/lock, PHP/Laravel versions, existing AGENTS.md/CLAUDE.md/GEMINI.md,
   local development commands, and repository status. Preserve your custom instructions.
2. Within an authorized development checkout, follow official installation guidance:

```bash
composer require laravel/boost --dev
php artisan boost:install
```

Use the project's existing container/Sail command prefixes if applicable. Let Composer
resolve an appropriate stable compatible release; do not force a framework upgrade.
Review generated files and merge instruction blocks with your existing workspace entry.
The interactive setup selects coding agents and available guideline/skill/MCP features.
Verify the actual configuration before claiming a connection is working.

3. Select skills for installed packages such as Livewire, Inertia, Tailwind, or Pest only
   when detected/relevant. Do not put every Laravel package skill in every app.
4. Load project-generated rules and version-matched docs for concrete API questions.
   Keep workspace requirements, reference policy, original visual direction, and accepted
   decisions authoritative. Use one version of overlapping specialist guidance per task.
5. Re-run `php artisan boost:update` deliberately after relevant package/guidance updates,
   then review the resulting diff. Do not overwrite user rules to fix a conflict.

No Boost package installation or application/MCP connectivity was performed while producing
this workspace, because no actual Laravel application repository was supplied.
