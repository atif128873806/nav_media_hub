# Project contract

`project.yaml` contains identity/stage, repository mapping, stack, candidate skills,
desired tool roles, verification descriptions, and document pointers. Relative repository
paths are resolved from the project folder; doc paths are project-relative. Absolute
repository paths are allowed and must be checked at runtime. Machine validation confirms
shape/pointers, not repository access or requirements approval.

Required docs: PROJECT.md, AGENTS.md, REQUIREMENTS.md, ARCHITECTURE.md, DESIGN.md,
DECISIONS.md, TASKS.md, ROADMAP.md, MEMORY.md, context/CONTEXT_INDEX.md,
context/CLIENT_BRIEF.md, context/sources.yaml, and memory/HANDOFF.md.
Use the example template. Unknown choices remain unknown. Empty lists are legitimate
before implementation. No default stack selection counts as client approval.

Source processing and decision approval use separate statuses. Source records identify
type/path or URL, summary, relevant role(s), authority, processing status, and extracted
item IDs. Decision/requirement provenance includes source ID and locator in Markdown.
The agent checks unresolved pending sources before affected implementation.

Source `path` values are relative to the folder containing sources.yaml (normally context/).
For example `meetings/2026-10-04-kickoff.md` or `inbox/client-brief.pdf`. URLs remain URLs;
they are not executed by the CLI. Source document paths must stay within that context folder.
