---
name: admin-panel
description: Use for admin dashboards, management tables, filters, forms, detail views,
  settings, and operational workflows; select modules from approved business scope.
---

# Professional Admin Panel

Read actors, managed entities, approved operations, and data contracts. Create a module
map: module, user role, operational question, required action, data source, permission.
Treat domain companion skills as planning checklists, not permission to add features.

Design navigation around daily work. Use overview metrics only when users need them and
real data exists; show units, period, and actionable meaning. Do not invent revenue charts
or add analytics, coupons, warehouses, or subscriptions to a simple lead admin.

For each approved entity, consider searchable/filterable lists, sorting, pagination,
useful columns, selected details, create/edit forms, and allowed lifecycle actions.
Bulk actions require scope, permissions, and clear feedback. Show active filters and reset.
Support URL state when useful. Avoid unsafe destructive controls disguised as small icons.

Keep validation/errors close to fields, preserve input on failure, and show success clearly.
Design record-level not-found, permission-denied, empty, loading, and server-error states.
Use details pages/drawers/modals based on task complexity, not a universal template.
Keep mobile operationally usable; choose scroll/column prioritization/card transforms
deliberately. Enforce authorization on the backend, including record/tenant scope.

Read business-admin/ecommerce-admin only for matching scope. Apply frontend-ui-ux and
verify real task flows plus forbidden operations. Never call static fixtures a functioning
admin backend. Document mocks and unfinished integrations.
