# Version-matched Next.js guidance

The former https://github.com/vercel-labs/next-skills repository now directs users to
https://github.com/vercel/next.js/tree/canary/skills. Its next-best-practices reference
knowledge is now distributed with framework docs rather than as that standalone skill.
Source README inspected 2026-10-04 at revision c522619e45aa3492fd2bfc916b308b275eff7798.

Therefore V1.3 bundles Vercel React performance/composition procedures and retains a thin
project-specific Next.js integration procedure. It does not ship a stale next-best-practices
skill or a generic Cache Components migration. Inspect actual installed Next.js version,
local docs, and supported workflow first. Do not install canary dependencies or upgrade
an application merely to obtain AI instructions.

Official guide: https://nextjs.org/docs/app/guides/ai-agents
Merge any generated agent-doc pointers with existing workspace/project rules. Consult
the matching version's documentation for RSC, caching, actions, and routing semantics.
