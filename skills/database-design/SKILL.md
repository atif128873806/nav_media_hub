---
name: database-design
description: Use for schema changes, relational modeling, migrations, transaction
  boundaries, tenant isolation, inventory or booking concurrency, and data performance.
---

# Database and Domain Integrity

Start from approved entities, ownership, lifecycle, and actual queries. Inspect the current
database engine/version and schema. Define foreign keys, nullability, uniqueness, relevant
indexes, and deletion/retention rules. Model monetary values and time consistently.

For stock, booking slots, or payments, define what must remain true under simultaneous
requests. Choose database constraints, conditional updates, locking, or idempotency based
on the actual invariant. An application-only precheck may race. Keep transactions scoped.
Tenant filtering belongs in server-side data access and authorization; include tenant scope
in uniqueness rules where the domain requires it.

Plan migrations for existing data and realistic rollback. Avoid destructive defaults.
Review query plans/measurement for material performance concerns before adding cache.
Record schema decisions and test ownership, constraints, lifecycle changes, and relevant
concurrency rather than tests that merely mirror model getters.
