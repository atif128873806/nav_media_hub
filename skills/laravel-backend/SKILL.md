---
name: laravel-backend
description: Coordinate accepted Laravel backend feature work, domain requirements, API integration, project-specific verification, and official Laravel best-practices rule selection.
---

# Laravel project implementation

Read approved domain rules, current architecture, composer.json/lock, relevant code/tests,
and repository conventions. Resolve actor/tenant ownership, lifecycle transitions, money,
timezones, atomic changes, external side effects, and idempotency from actual requirements.
Do not invent domain invariants from a generic admin checklist or reference website.

Load laravel-best-practices for the applicable official framework rules. Use actual
project-generated Boost guidance/version-matched docs when available; see
integrations/LARAVEL_BOOST.md from the workspace root. Static skills do not install MCP.

Use laravel-architecture/database-design only when structural or schema decisions warrant
them. Keep architecture proportional to domain complexity and existing conventions.
Implement accepted behavior with server-side validation/authorization, then use qa-review
and security-review for relevant checks. Do not run migrations on production without
authorization or claim sample/mock behavior is complete. Report actual tests and gaps.
