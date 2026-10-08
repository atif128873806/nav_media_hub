---
name: laravel-architecture
description: Use when shaping a Laravel domain, backend structure, module boundaries,
  API contracts, queues, or a substantial refactor; scale patterns to project complexity.
---

# Laravel Architecture

Read approved entities, actors, workflows, constraints, and existing architecture before
choosing folders or abstractions. Document one concrete domain flow and its invariants.

For small apps, use standard Laravel Controllers, Form Requests, Models, Policies, and
Tests; add workflow Actions/Services where repeated or nontrivial business logic warrants.
For larger apps, group meaningful domains and keep orchestration, domain rules, persistence,
and external adapters understandable. Use DTOs, events, interfaces, repositories, or CQRS
only when a concrete contract, boundary, or tested need justifies them. Do not introduce
microservices, universal repositories, or 25-layer architecture for small CRUD systems.

Define auth/tenant boundaries, transaction ownership, failure modes, idempotency, API
contracts, and external integration behavior. Distinguish synchronous responses from
background jobs. Set queue failure/retry behavior and operational visibility where needed.
Keep billing/booking states explicit and test illegal transitions and concurrent changes.

Record architecture decisions with problem, alternatives, chosen approach, consequences,
and source requirement. Provide a coherent implementation sequence. Do not enforce a new
architecture on an existing project without task need. Verify against real code and tests.
