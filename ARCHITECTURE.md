# AI Workspace architecture

## Delivered V1.3

The file contract is the control plane. An existing coding AI reads project rules,
sources, and selected skills, then operates its available tools. A small Python CLI
scaffolds project copies, validates manifests/pointers/source integrity, and can copy four
reviewed native skill entries to an explicitly chosen directory. Markdown holds context and
provenance; YAML holds compact metadata; JSON Schema documents machine contracts.

Repository mapping supports external code folders or a self-contained `.ai-workspace/`
inside a project repo. Source evidence stays distinct from accepted requirements.
Raw client material does not control execution. Real permission enforcement belongs to
the AI tool/host. No model service or connected integrations are included.

## Proposed application architecture — future decision

The UI should provide an editor/chat center with projects/files, context, and a lower
terminal/tests/Git/activity panel. A local executor would mediate project filesystem and
tool operations, with explicit execution policy and audit events. A context service would
index sources and trace summaries to evidence; a router would select skill manifests.
Provider adapters would translate the shared contract to each actual executor.

Do not preselect a multi-service stack, database/vector store, queue, model provider, or
daemon protocol until actual requirements justify it. Laravel is preferred for client
backend work; that preference does not require Laravel for every workspace component.
Future work needs threat modeling, auth, repository isolation, source retention, and
safe execution tests. Build features only after testing the file workflow on real projects.
