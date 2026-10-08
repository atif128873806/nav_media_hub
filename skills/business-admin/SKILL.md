---
name: business-admin
description: Use for approved booking, salon, limo, lead, service, staff, schedule,
  customer, or invoice management; adapt workflows to the actual business.
---

# Booking and Business Admin

Identify this business and its approved managed entities. A lead form admin may need only
submission list/details/status; do not give it inventory, payroll, or booking calendars.

For bookings, define services/resources, duration, timezones, availability, buffer periods,
capacity, guest/customer identity, cancellation/rescheduling rules, and status transitions
only as scope requires. Avoid double booking under concurrent requests. Distinguish salon
staff slots from limo vehicle/driver dispatch and travel constraints.

For leads, define source, fields, status/assignment, follow-up notes, and permitted exports
only when approved. For invoices, define numbering, currency/tax/payment status and whether
the system issues actual financial documents or shows records. Use restricted access and
avoid claiming tax/legal correctness without requirements and authoritative validation.

Design daily operational workflows and useful filters. Support clear transitions and
history where material. Gate notifications/exports by permissions and explicit scope.
Test accepted actions, conflicting resources, forbidden records, boundary times, and
errors. Retain personal data only as required by project policy.
