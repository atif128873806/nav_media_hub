---
name: ecommerce-admin
description: Use for approved ecommerce operations such as products, variants, inventory,
  orders, refunds, shipping, customers, promotions, or commerce reports.
---

# Ecommerce Admin Workflows

Read approved commerce scope and payment/shipping contracts. Select needed modules only.
Use this checklist to find missing decisions, not to generate every feature automatically.

Products: identifiers, categories, media, variants, attributes, status, validation, and
pricing only as required. Inventory: availability, adjustments, movement history, and
overselling prevention when in scope. Orders: line item snapshots, totals, discounts,
tax/shipping rules, lifecycle, fulfillment, cancellation/refund boundaries. Customers:
relevant details with restricted personal data. Promotions/reviews/reports: only accepted.

Distinguish order status from payment and fulfillment state. Prevent contradictory or
duplicate actions. Verify totals and currency precision. Handle payment webhooks with
signature verification/idempotency in the backend. Never treat a browser redirect as
proof of payment. Avoid storing card data in application forms/logs.

Make staff workflows concrete: find order, inspect timeline, apply permitted action,
confirm outcome. Explain irreversible/refund effects. Test real permissions, concurrency,
state changes, invalid totals/quantities, and provider failures as applicable. Use labeled
demo data until real integrations exist. Link each implemented module to approved criteria.
