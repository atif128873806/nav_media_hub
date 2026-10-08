# Requirements

Status is explicit; read original sources for detailed behavior.

| ID | Status | Requirement and acceptance | Provenance |
| --- | --- | --- | --- |
| REQ-001 | approved | One responsive public marketing page; hero inquiry first, selected work directly afterward; private admin separate. | SRC-RULES, Goal and approved scope; SRC-HANDOFF §2 |
| REQ-002 | approved | Required name, email, service interest, short brief. Server validation, useful errors, preserved input, honest saved/failure state. Save exactly one durable lead across matching retries. | SRC-RULES, Functional rules; SRC-INQUIRY §§2–3; SRC-LARAVEL §4 |
| REQ-003 | approved | Admin login/logout, newest-first paginated inbox, full submitted detail, validated status updates. Authentication and explicit admin authorization on all lead routes. | SRC-RULES, Functional rules; SRC-INQUIRY §5; SRC-LARAVEL §3 |
| REQ-004 | approved | PHP/Laravel; maintain the existing Blade/Vite implementation and local SQLite prototype. Production runtime/database selection remains pending. | SRC-RULES, Goal; SRC-LARAVEL §§1–2; SRC-IMPLEMENTATION |
| REQ-005 | approved | Original professional composition, readable stable form, visible labels/focus, mobile usability, reduced motion, user-controlled permissioned videos with posters/fallbacks. | SRC-RULES, Design and content rules; SRC-DESIGN |
| REQ-006 | approved | Genuine client facts and approved/licensed media only; visibly mark private prototype placeholders. Final copy/services/branding require evidence. | SRC-RULES, Design and content rules; SRC-HANDOFF §§3–5 |
| REQ-007 | approved | Register this existing application in the shared AI workspace, preserve project context and actual progress. | SRC-WORKSPACE-REQUEST, user instruction dated 2026-10-07 |
| REQ-008 | deferred | Live discovery calendar or preferred shoot-date enhancement; requires explicit scope and availability decisions. | SRC-RULES, Goal; SRC-INQUIRY §7 |
| REQ-009 | proposed | Owner email notification after durable storage; owner and operating email configuration pending. | SRC-HANDOFF §5; SRC-LARAVEL §1 |
| REQ-010 | deferred | Production release after approved content/privacy/retention, host/runtime/database and admin access are resolved. | SRC-LARAVEL §6; SRC-HANDOFF §5 |

The detailed acceptance scenarios in workspace document 03 and delivery checks in this project
AGENTS.md still apply. A successful workspace validation does not complete application QA.
