# Codex bundle adaptation

This standalone skill is named `humanize` so the user can invoke `$humanize` or ask for natural Korean prose. It is adapted from `blader/humanizer`, MIT, at the commit in SOURCE.md. The upstream SKILL.md is retained verbatim as `references/upstream-humanizer.md`; it is supporting material, not a second installed entrypoint.

The local entrypoint adds Korean editing guidance, keeps facts and verification status unchanged, and defaults to returning the final rewrite. User-requested file editing is scoped to prose; review requests do not imply overwriting files. No Claude plugin, native slash command, subagent pipeline, external humanization API, or AI-detector service is installed.

The bundle does not copy the separately installed local `humanize-korean` package or claim to provide its strict pipeline. Korean guidance here is original bundle material. No generated grade, edit percentage, or detection score is reported without an actual defined measurement. Added opinions or experiences and silent deletion of distinct claims are disallowed for factual writing, including where upstream examples might suggest otherwise.

No runtime dependency is needed to read and apply this skill. Editing a binary document still needs a suitable document tool.
