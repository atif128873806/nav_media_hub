# Using the official-source skills

The package contains four adapted entries backed by reviewed official source:

| Entry | Purpose | Contents |
| --- | --- | --- |
| vercel-react-best-practices | React/Next.js performance | Original Vercel index, rules, and compiled guide |
| vercel-composition-patterns | Reusable React component architecture | Original Vercel composition rules; React version gate |
| web-design-guidelines | Accessibility and interface review | Original Vercel entry plus pinned interface rule snapshot |
| laravel-best-practices | Laravel engineering | Original official rules/templates plus six rendered Markdown companions |

Use the workspace normally: its agent contract selects relevant manifests and their entry
files. You do not need native installation for this file-based path. Native installation
may help your coding tool discover these four without you specifying them manually.

## Optional native installation on your machine

Run inside the extracted workspace, with tools/requirements.txt installed:

```bash
python3 tools/workspace.py install-skills --destination /absolute/path/to/your/agent/skills
```

Choose the actual directory supported by your coding tool or use its documented installer.
The helper copies only these four reviewed entries, including all referenced resources.
It verifies source checksums, refuses existing target names, and does not execute scripts,
fetch network content, connect MCP, or install language dependencies. You can select a subset:

```bash
python3 tools/workspace.py install-skills --destination /absolute/path/to/your/agent/skills --skill laravel-best-practices
```

After installation, open a fresh task and verify the tool identifies the entry and reads
its relevant rules. Use an explicit skill request if discovery does not occur. Native
installation paths and host capabilities differ across coding tools.

For a project-contained `.ai-workspace/`, copy the complete skills/ tree, including nested
references, agents metadata, and provenance. Keep workspace/upstream-lock.yaml and policy.
Copy tools/ too if you want validation/installation there. Original upstream entry bytes are preserved as SOURCE_SKILL.md to prevent duplicate native
discovery; the outer adapted SKILL.md is the only native entry for each imported skill.

## Laravel and Next.js

Read integrations/LARAVEL_BOOST.md to install official package-aware Boost guidance in each
actual Laravel application. The static Laravel skill is available immediately; the Composer
package/MCP server was not installed in any client app. For Next.js, the old standalone
next-best-practices skill has moved to version-matched framework docs; see the integration note.

Source versions are pinned for reproducibility. Update deliberately with a reviewed diff
and refreshed hashes. The interface-review snapshot is dated, not claimed to be the latest
on every future task. Preserve project requirements and original visual direction.
