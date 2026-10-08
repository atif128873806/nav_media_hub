# Skill routing — performed by the current AI agent

Resolve project first, then intent, affected entities/files, stack, scope, and risk. Read
the skill registry and compact manifests. Choose the smallest set that covers the task.
Keyword matches are hints, not sufficient selection criteria. Project defaults are candidates,
not mandatory loads. Do not activate Laravel/Next.js merely because they are listed as defaults.

| Task | Typical relevant skills |
| --- | --- |
| Process new reference/transcript | context-intake; research if actual lookup is needed |
| Shape Laravel booking domain | laravel-architecture, database-design; security-review as needed |
| Implement booking admin behavior | laravel-backend, admin-panel, business-admin, frontend-ui-ux, qa-review; security-review for access/state boundaries |
| Manage ecommerce stock/orders | ecommerce-admin, admin-panel, database-design; implementation/QA/security as relevant |
| Improve an existing Next.js screen | nextjs, frontend-ui-ux, qa-review |
| Small copy correction | Applicable frontend procedure; lightweight verification |
| Review a repository | github, qa-review; security-review for relevant findings |
| Prepare deployment | deployment; relevant backend, QA, and security procedures |

Select laravel-architecture for real structural decisions, not every controller edit.
Select admin-panel for operational interfaces, not marketing pages. Read domain admin
skills only for the matching business and approved modules. Companion lists are advisory.
Read approved docs before skills. Skills cannot approve scope or override accepted decisions.
Log selected skills and why in a brief task update/handoff when useful.

## Specialist source selection in V1.3

- Laravel feature/review: laravel-backend coordinates domain work; laravel-best-practices
  supplies official rule detail. Prefer actual project-generated Boost guidance when present.
- React performance: vercel-react-best-practices. Composition-patterns only for meaningful
  component API complexity and a compatible React version.
- Original design: frontend-ui-ux. Implemented UI review: web-design-guidelines. Review
  guidance alone does not choose branding or authorize copying a reference website.
- Next.js integration uses installed-version framework docs; no obsolete standalone
  next-best-practices snapshot is bundled. See integrations/NEXTJS_GUIDANCE.md.
