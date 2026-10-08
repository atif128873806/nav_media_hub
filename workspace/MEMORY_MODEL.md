# Portable memory

| Layer | Files | Allowed content |
| --- | --- | --- |
| Global | workspace/USER_RULES.md | Stable cross-project preferences |
| Project | PROJECT.md, REQUIREMENTS.md, DECISIONS.md | Scope and authoritative decisions |
| Project summary | memory/PROJECT_MEMORY.md | Compact sourced facts and navigation |
| Task recovery | memory/HANDOFF.md, TASKS.md | Goal, progress, checks, blockers, next action |
| Evidence | context/ | Original client material and source-linked summaries |

Keep one canonical location per fact; link rather than duplicate full requirements.
MEMORY.md is an entry pointer to the project's memory folder for legacy consumers.
Never place another client's data, secrets, unsourced approval, or verbose logs in memory.
After interruptions verify the handoff against repository state; it may be stale.
Models do not automatically share chat histories. Portability comes from the same files
being available to the current tool. Context loading remains the agent's responsibility.
