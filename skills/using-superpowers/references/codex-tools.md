# Codex tool adaptation for the portable bundle

Read the current tool schemas and environment instructions. They take precedence over historical command, model and feature examples.

- Invoke installed skills using `$name`, or read their SKILL.md when no Skill tool exists. Do not assume plugin namespace names are installed.
- Use host-supported file and shell tools. Unix shell examples need adaptation on Windows.
- Subagents are optional and require actual tool support and authorization. If unavailable, execute sequentially and describe the limitation. Do not fabricate independent review.
- Use the current schema for context sharing, model selection, waiting and lifecycle. Do not copy old role/model IDs or alter ~/.codex/config.toml to enable a workflow.
- Keep progress communication responsive while waiting; follow the host's permitted wait duration.
- Inspect Git status and existing worktrees before changes. Reuse a suitable worktree and preserve unrelated user changes. Detached HEAD alone does not prove that branch creation or pushing is impossible; check actual permissions and tools.
- Commit, push, create PRs, merge and publish only within the user's authorization. Use the host's managed worktree tools when appropriate. Do not delete or reset a checkout just because a generic cleanup recipe says to.
