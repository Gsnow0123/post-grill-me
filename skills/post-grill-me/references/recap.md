# Feature recap

Keep one useful record for the same project and change, even when its context spans multiple chats. This is a reading aid and a record of corrected understanding; it is not an acceptance certificate.

Use a short opening that a future teammate can understand in a screen or two. Put necessary detail and source links afterward. Include only the sections that help:

- **Purpose and scope:** the original problem, intended audience, and boundaries.
- **Confirmed or candidate behavior:** a plain-language example and important changes, labeled by branch/stage/use case if needed.
- **Choices and evolution:** why a path was chosen, which earlier decisions were superseded, and which alternatives remain exploratory.
- **Understanding corrections:** the interpretation actually used, the human clarification, and its consequence for subsequent work. Separate clarification from a later change of requirement or a code fix.
- **Sources and limits:** relevant conversation links or identifiers, their scope/time, code references when useful, coverage gaps, and unresolved version questions.

Never label unanswered judgments as confirmed. Do not let a new inference silently replace a human decision. If an explicit same-scope correction supersedes an earlier confirmation, preserve the history and source. A recap of an earlier implementation does not prove current code, tests, deployment, or real-world delivery.

When refreshing the user's memory, summarize purpose, behavior, and choices first. Preserve meaningful limits while shortening: “this happens here” does not imply “this happens only here.” Offer the full record as optional depth.

The destination rules in `SKILL.md` apply. Update the existing file in place, open it in a supported side panel when available, and avoid repeating its full text in the main conversation.
