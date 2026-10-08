# Quick start

V1.3 adds four reviewed official-source skill entries. Start with the normal file workflow
below; read UPSTREAM_SKILLS.md for optional native installation and Laravel Boost setup.

## One shared workspace

Open this extracted folder in your AI coding tool. Copy `projects/example-project` to
`projects/<slug>` or use the CLI. Set `repository.path` in the project manifest to the real
code folder; use an absolute path when the repository is external. An agent must verify
the path and confirm project identity before editing. A tool restricted to this workspace
may not be able to read the external repository; use the self-contained layout instead.

Fill `PROJECT.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `DESIGN.md`, and test commands.
Keep unknown details marked unknown. Do not substitute a reference's features for scope.

First prompt:

> Read AGENTS.md. Active project: lockwood-limo. Check its project.yaml and context index,
> then report missing material decisions before starting the requested implementation.

## Self-contained repository — easiest across coding tools

1. Put this package's `workspace/`, `skills/`, and `agents/` in your repository under
   `.ai-workspace/`. Keep `workspace.yaml` beside them.
   Also copy `integrations/`, `UPSTREAM_SKILLS.md`, `SECURITY.md`, and
   `THIRD_PARTY_NOTICES.md` beside them so setup references and notices stay available.
2. Copy `projects/example-project/` to `.ai-workspace/projects/<slug>/`.
3. Set `repository.path: ../../..` in that project's manifest: paths are relative to the
   project folder. Set the project ID/name and real stack; this path refers to repo root.
4. Copy package `AGENTS.md` to `.ai-workspace/AGENTS.md`.
5. Merge the text in `adapters/PROJECT_ENTRY.md` into the repository's existing AGENTS.md,
   substituting the slug. Preserve existing project instructions; do not overwrite them.
6. Put an equivalent explicit pointer in existing CLAUDE.md/GEMINI.md when needed.
   Do not assume a tool automatically imports or expands a pointer; verify that it reads
   the contract, project docs, and selected skill during the first task.

If you want the optional CLI here, copy `tools/` into `.ai-workspace/tools/` too and run
`python3 .ai-workspace/tools/workspace.py validate`. Merge private-file ignore patterns
into the repository's existing .gitignore using the `.ai-workspace/projects/` prefix.
Do not overwrite repository ignore rules or assume package-root patterns apply unchanged.

The self-contained copy keeps project context available with code and avoids cross-repo
access limitations. Maintain one authoritative copy of project decisions. Sync updates
intentionally rather than letting a central and local copy disagree.

## Where client material goes

| Material | Location inside the project |
| --- | --- |
| Raw WhatsApp notes, PDFs, attachments | context/inbox/ |
| Meeting transcript | context/meetings/YYYY-MM-DD-topic.md |
| Website link and what client likes | context/references/websites.md |
| Screenshots, client-owned images/files | context/assets/ |
| Source registry and processing status | context/sources.yaml |
| Short source overview | context/CONTEXT_INDEX.md |
| Approved scope and criteria | REQUIREMENTS.md |
| Accepted decisions and supersession | DECISIONS.md |
| Work items | TASKS.md |

When adding material, prompt once:

> Process the new material in this project's context/inbox using context-intake.
> Register sources, extract requirements and questions with provenance, and keep uncertain
> decisions pending. My reference websites are for ideas, not cloning.

Later:

> Active project: lockwood-limo. Build the approved booking management page.

If your tool starts a fresh session or compacts context, the entry contract tells it to
reload the project and handoff. This is file-based continuity, not shared model memory.

## Before committing

Check what is staged. `.gitignore` is a convenience, not a secret detector. Keep private
client files and secrets out of public repositories. Store only approved redacted summaries
in tracked docs. Do not use this package to expose production credentials to an AI model.

## Updating from V1.1

Use this as a fresh workspace foundation. Copy your own project docs and accepted decisions
into the new project structure deliberately. Old skill IDs `laravel`, `ui-design`, `qa`, and
`security` are now `laravel-backend`, `frontend-ui-ux`, `qa-review`, and `security-review`.
Update your manifests and run validation. Preserve client originals and existing rules.
