# Skill contract

Each `skills/<id>/` has SKILL.md (procedure with name/description frontmatter) and
skill.yaml (routing metadata). Optional `references/` provide task-specific detail.
The package supplies file-based procedures, not connected tools. Four adapted official-source
entries can also be installed in a supported native skill directory. A package copy does
not automatically install them on another machine; see UPSTREAM_SKILLS.md.

The agent resolves project and intent, discovers candidate metadata, loads relevant
instructions, checks actual tools and authorization, executes, verifies, and records state.
Recommended companions are advisory. Task-specific scope and accepted decisions prevail.
Use progressive disclosure: load core project docs and selected skills, then relevant
evidence/detail on demand. A future router may consume the same manifests; no autonomous
router is implemented here. See workspace/schemas/skill.schema.json.
