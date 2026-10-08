---
name: deployment
description: Use for hosting setup, deployment planning, migrations, queues, health
  checks, rollback, or authorized operational changes; verify environment and permissions.
---

# Deployment Preparation and Operations

Read deployment docs and verify local/staging/production identity, stack, and previous
authorization. Prepare the concrete release plan before asking for a missing final action
approval. Do not make production changes merely because a generic skill mentions a command.

Inspect dependencies/configuration, build artifacts, migrations/data impact, queues/scheduler,
file permissions, TLS, logs, secrets, and health checks relevant to this project. Use its
actual hosting workflow, not a generic VPS script. Plan backup and rollback for affected
data and release state; distinguish code rollback from irreversible schema/data changes.

Run relevant local/staging checks, then execute only authorized actions. Verify actual
service health and critical workflows after deployment. Report commands/checks and failures
without leaking secrets. Never claim deployment completed when only a plan or build exists.
