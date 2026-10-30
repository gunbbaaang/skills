# Installing this bundle

This repository is a public, portable Codex skill collection. A request such as
“gunbbaaang GitHub의 skills 레포에 있는 스킬 전부 설치해줘” means install this bundle
in the user's intended working project. Read README.md and INSTALL.md.

- Prefer the included `scripts/install.py --project <absolute-working-project>` after inspecting it. It copies all 13 skills, preserves modified existing copies as backups, and requires no administrator access.
- Preserve the project location from before downloading this repository. Do not accidentally install into a temporary clone instead of the user's project.
- For a clean destination, the README's pinned skills CLI command is also supported.
- Install all skill resources, including `understand/runtime/`; do not copy SKILL.md alone.
- Do not report dependency setup, graph generation, browser rendering, automatic hooks, or score improvement as completed merely because files were installed.
- Check the installed names, then give the short Korean start prompt from README.md. If current-session discovery has not refreshed, read the installed SKILL.md directly or retry in a new session.
- This request does not authorize changing global agent configuration, installing unrelated marketplace plugins, reading other projects' conversation logs, or publishing hackathon data.
