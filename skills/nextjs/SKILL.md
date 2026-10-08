---
name: nextjs
description: Coordinate Next.js project-specific frontend integration, data contracts, routes, and actual configured checks; load official specialist guidance for performance/composition rather than duplicating it.
---

# Next.js project integration

Inspect package/lockfile, existing router, actual frontend conventions, accepted requirements,
and data contracts. Read integrations/NEXTJS_GUIDANCE.md from the workspace root. Match API
behavior to installed-version docs. Preserve the project's router and existing data layer.

For material React performance, use vercel-react-best-practices. For real component API
complexity, use vercel-composition-patterns. For original brand/layout, use frontend-ui-ux;
for a rules-based interface review, use web-design-guidelines. Do not load all on every task.

Keep backend authorization/secrets on the server. Integrate approved API contracts and
handle missing/loading/error states and recoverable updates. Do not invent functionality,
testimonials, or stats. Run actual configured build/type/lint checks and relevant flow tests.
Read the reviewed source detail instead of repeating generic optimization instructions here.
