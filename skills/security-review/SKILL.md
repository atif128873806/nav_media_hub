---
name: security-review
description: Use for authentication, authorization, tenant access, sensitive data,
  payments, uploads, secrets, APIs, or risk review of backend and admin changes.
---

# Application Security Review

Map actors, resources, trust boundaries, sensitive data, and attack-relevant changed flows.
Read project authorization/tenant rules and actual implementation. Scope review to evidence.

Check authentication/session handling, server-side authorization, record/tenant ownership,
allowlisted input, output escaping, CSRF as applicable, parameterized queries, rate limits
where needed, and error/log data exposure. Hidden admin buttons are not access control.
Validate uploads by content/type/size and safe storage/access, not extension alone.
Review SSRF risks for user-supplied URLs and safe handling of untrusted tool/source text.
Payments need provider authenticity checks and duplicate event handling. Never store raw
payment secrets or card data in docs/logs. Keep environment keys external and redacted.

Add focused negative-path tests when changes justify them. Report concrete vulnerabilities
with impacted flows and remediation; distinguish verified findings from potential concerns.
Do not make unsupported guarantees that an application is fully secure or compliant.
