# Codex / Probe bundle notes

This is a portable skill copy, not the upstream plugin installation. The task and the host's actual tools determine what can run. Read supporting resources only when relevant.

- Reuse the confirmed Probe problem, acceptance criteria and existing `probe-notes/` records. A selected workflow does not restart completed discovery, erase prior decisions, or require every installed skill to run.
- Honor the user's existing authorization and requested time budget. Ask only for missing material decisions or actions that still need approval; do not repeat approvals already supplied in the conversation.
- Tool names, shell snippets, model names, pricing and package APIs in upstream examples require checking against the actual environment. Never invent a tool result, independent review, participant answer or test outcome.
- This bundle does not register hooks, change global configuration, read unrelated conversation histories or publish project data. A skill request is not permission for those side effects.

## Superpowers in this bundle

Use `$using-superpowers` for the overall workflow, or a specific installed name such as `$writing-plans`, `$test-driven-development`, `$systematic-debugging` or `$verification-before-completion`. The upstream `superpowers:<name>` notation maps to the bare installed skill `<name>`; read its SKILL.md when no Skill tool exists.

The overall entrypoint applies to software development workflow requests, not every unrelated conversation. Relevant skills remain automatically discoverable. Do not interpret the original "1%" language as an instruction to load every skill or start a new design discussion after the user has already delegated a concrete implementation.

The current `systematic-debugging` copy retains this bundle's existing standalone adaptations. Use existing approval and design evidence before asking the user to decide the same thing again. Testing should cover the actual behavior changed; documentation-only or trivial changes do not require an artificial failing test.

Subagent workflows require actual host support and authorization. If unavailable, execute the work sequentially and report that a separate reviewer was not used. Follow the live tool schema for models, context sharing, waiting and lifecycle; do not install agent roles or edit ~/.codex/config.toml as a side effect. All Git actions remain within the user's requested scope.

Browser brainstorming resources are optional; inspect the startup helper and environment before running them. Installation does not start a server or enable a visual companion.

For session diagnosis, inspect only the current session or transcript explicitly selected by the user. Prefer a task-local diagnostic folder over the upstream home-directory example. Producing a local report does not authorize exporting transcripts or posting an issue.
