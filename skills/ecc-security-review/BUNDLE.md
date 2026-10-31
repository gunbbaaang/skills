# Codex / Probe bundle notes

This is a portable skill copy, not the upstream plugin installation. The task and the host's actual tools determine what can run. Read supporting resources only when relevant.

- Reuse the confirmed Probe problem, acceptance criteria and existing `probe-notes/` records. A selected workflow does not restart completed discovery, erase prior decisions, or require every installed skill to run.
- Honor the user's existing authorization and requested time budget. Ask only for missing material decisions or actions that still need approval; do not repeat approvals already supplied in the conversation.
- Tool names, shell snippets, model names, pricing and package APIs in upstream examples require checking against the actual environment. Never invent a tool result, independent review, participant answer or test outcome.
- This bundle does not register hooks, change global configuration, read unrelated conversation histories or publish project data. A skill request is not permission for those side effects.

## ECC in this bundle

These are eight selected MIT skills from `affaan-m/ECC` (formerly `everything-claude-code`), not the complete ECC plugin. Invoke them as `$ecc-<name>`. Existing Probe coaching, records, web/PPT skills and verification evidence remain the working context.

- `ecc-search-first`: search the current project and existing dependencies before external research. Use available search tools yourself; a separately installed researcher agent is not required. Time-box research to the decision it can change.
- `ecc-api-design` and `ecc-error-handling`: apply patterns to the current stack and actual failure cases. Examples do not require creating production infrastructure or a generic abstraction layer for a small MVP. Redact sensitive values in logs and user-facing errors.
- `ecc-security-review`: review the relevant attack surfaces and report evidence-backed findings. Example secret strings are placeholders. Report paths/line numbers and redacted findings rather than printing real secrets. Do not claim a grep or checklist proves security or authorize scanning other systems.
- `ecc-verification-loop`: use the project's actual build/type/lint/test commands and preserve exit statuses. Classify checks as passed, failed, not applicable or not run. Coverage thresholds come from the project or user, not a universal 80% gate. Inspect the actual task diff; HEAD~1 is not automatically the task baseline. Keep local checks separate from deployment acceptance.
- `ecc-cost-aware-llm-pipeline`: use current provider documentation and actual usage before estimating costs. The example models/prices are illustrative. Do not make paid calls, switch providers or claim savings solely because the reference recommends routing.
- `ecc-iterative-retrieval`: progressively narrow relevant files or evidence. It also works within a single session; do not spawn agents just to follow the diagram. An arbitrary cycle count does not prove enough context was found.
- `ecc-architecture-decision-records`: first reuse `probe-notes/decisions.md` or the project's existing decision records. A request to record a decision authorizes that local record; do not ask again just to create an empty template. Distinguish proposed choices, the participant's actual decisions and Codex recommendations.

No ECC hooks, MCP servers, autonomous loops, continuous-learning background jobs, external services or named agent configurations are enabled. Adapt the illustrative commands to the current shell and runtime. Unavailable integrations must be reported, not simulated.
