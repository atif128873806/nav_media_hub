# Atif AI Workspace — Final V1.3

A reusable, provider-independent workspace for Laravel development, frontend design,
client work, QA, research, and deployment preparation.

This release is a **working instruction and project-context foundation**. It includes
Markdown guidance, validated YAML manifests, JSON schemas, project templates, and a local
validation/scaffolding CLI. It does not include an editor UI, model runtime, autonomous
router, background daemon, automatic transcript extraction, or connected integrations.
An AI tool follows the rules when it can access the files and loads the entry contract.
YAML metadata does not itself make an AI tool automatically execute a skill.

## Start using it

1. Extract this folder and open it in your coding tool.
2. Ask the tool: “Read AGENTS.md and QUICKSTART.md. Set up my project using
   projects/example-project. My code is in [repository path].”
3. Fill the project overview, repository mapping, requirements, and commands. Defaults
   are starting preferences, not proof that a client approved a feature or technology.
4. Put transcripts, notes, PDFs, screenshots, and links under the project's `context/`.
   Ask the AI to process the material using the context-intake skill once.
5. Give ordinary task prompts. The startup contract directs the AI to the right sources.

See `QUICKSTART.md` for both a shared workspace and the recommended self-contained
project-repository layout. Native instruction discovery differs across tools; verify
file loading in your tool. `CLAUDE.md` and `GEMINI.md` provide explicit entry pointers.
Chat interfaces need the extracted files attached/made available; a ZIP alone may not
be readable by a particular client. Secrets should never be attached.

## Contents

| Location | Purpose |
| --- | --- |
| AGENTS.md | Startup, recovery, reference rules, task completion |
| workspace/ | Authority, source intake, routing, memory, tool policies |
| skills/ | 14 workspace procedures and 4 official-source skills with routing manifests |
| projects/example-project/ | Editable project template and context folders |
| projects/ai-workspace/ | This workspace's requirements, decisions, roadmap |
| tools/workspace.py | Validate files or create a project template locally |
| workspace/schemas/ | Machine-readable manifest contracts |
| examples/ | Reference and transcript examples with traceable decisions |
| adapters/ | Entry text for use in an external project repository |

## Client references

References supply selected ideas. The agent must distinguish visual/structure/UX/feature
references from accepted requirements, retain evidence, and implement an original result.
New transcript statements remain pending until their meaning and authority are established.
Approved decisions explicitly identify which older decisions they supersede.

## Optional CLI

Python 3.10+ is sufficient for the script; install the two validation dependencies using
`python3 -m pip install -r tools/requirements.txt` inside a virtual environment if needed.

```bash
python3 tools/workspace.py validate
python3 tools/workspace.py new-project lockwood-limo --name "Lockwood Limo"
```

The CLI validates structure and manifests; it does not prove that an AI followed the rules
or that your application works. Validate and test application changes separately.

## New in V1.3

Selected official-source skills are bundled with complete rule files, scope/version entry
instructions, provenance, reviewed source revisions, and integrity checks. The native-copy
helper can install those four into a directory you explicitly select, without a network
fetch or overwriting existing skills. Read UPSTREAM_SKILLS.md. Laravel Boost itself must
be installed separately in a real Laravel application; no app repository was supplied.
