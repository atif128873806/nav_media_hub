# Client context intake

The AI performs this workflow with available tools; the CLI does not extract transcripts.

1. Preserve raw input in the project's context folders. Do not overwrite originals with
   AI summaries. Assign a stable `SRC-...` ID in `context/sources.yaml`.
2. Record type, local path/URL, received date if known, reference roles, authority,
   processing status, and a concise summary. External URL content is mutable; retain dated
   relevant observations or an authorized local snapshot when fidelity matters.
3. Extract atomic statements: requirement, decision, suggestion, question, reference,
   rejection, or supersession. Use `SRC-ID + timestamp/page/section` for each material item.
4. Inspect existing requirements/decisions for duplicates, conflicts, and impact. A transcript
   question, joke, aspiration, or AI interpretation is not an approved requirement.
5. Write proposed items with status, acceptance criteria, dependencies, and open questions.
   Promote to approved only under the authority rules. If the user has already authorized
   the exact change, record it without asking again.
6. Update `CLIENT_BRIEF.md` and `CONTEXT_INDEX.md` with compact, source-linked summaries;
   update tasks from accepted scope, and note pending items separately.
7. Set each source's processing status honestly: `pending`, `processed`, `blocked`, or
   `superseded`. Mark inaccessible PDFs/pages blocked, rather than pretending to read them.
8. Report adopted facts, proposed changes, material conflicts, and needed decisions.

## Practical limits

Use a relevant document/OCR tool when an attachment has no extractable text. Do not infer
text from an unread image. A source index is a navigation aid, not a substitute for evidence.
Before affected work, check new pending material so it cannot be silently ignored. Keep
work outside the pending material's impact moving. Minimize retained personal data and
redact secrets from tracked summaries. Apply project retention/access preferences.
