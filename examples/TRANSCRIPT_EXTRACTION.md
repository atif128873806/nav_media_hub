# Transcript extraction example — fictional training data

SRC-DEMO-001, 03:12: Client: “Customers should book without making an account.”
SRC-DEMO-001, 04:02: Client: “Maybe loyalty points later.”
SRC-DEMO-001, 05:10: Client: “Could we add online payment?”

| Statement | Extracted item | Initial status |
| --- | --- | --- |
| Guest booking | REQ-DEMO-001: allow guest booking | proposed pending applicable approval basis |
| Loyalty points later | Future suggestion, not current scope | deferred proposal |
| Online payment question | Open decision on provider, flow, and scope | question |

If the user instructs “implement the client's guest-booking requirement,” REQ-DEMO-001
can become approved using that message as approval evidence. Criteria could verify a
guest reaches confirmation, required contact fields are validated, and no login gate is
introduced. Criteria must be agreed/within the authorized task, not silently expanded.
An old account-only reference becomes a conflicting observation; the accepted requirement wins.
No fictional example is evidence for a real project.
