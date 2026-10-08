---
name: qa-review
description: Use for implementation verification, bug reproduction, regression testing,
  responsive/interaction review, or acceptance checks in client applications.
---

# QA and Regression Review

Read acceptance criteria, existing tests, affected workflows, and actual environment.
For bugs, capture reproducible steps, expected/actual behavior, and evidence before fixing.
Choose meaningful checks based on changed behavior and impact; do not write tests that
only repeat implementation details or add unnecessary tests for simple reversible copy edits.

Cover relevant happy paths, validation, errors, permissions/tenant access, key lifecycle
rules, persistence after refresh, and concurrency for stateful operations. For UI, inspect
desktop/mobile, keyboard/focus, long/missing data, loading/empty/error states, and navigation.
Use stable selectors and deterministic fixtures for browser automation; never destructive
production tests. Test integrations with safe environments/mocks clearly identified.

Run configured tests/build/type/lint checks appropriate to scope. Record exact commands,
outcomes, failures, skipped checks, and why. Review the final diff for unintended changes.
A passing build is not proof of working booking/payment behavior. Report residual risks
and verification gaps plainly. Stop redundant reruns unless changes/failures justify them.
