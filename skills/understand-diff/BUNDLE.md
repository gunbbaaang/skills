# Portable runtime for this bundle

Resolve the installed directory containing this SKILL.md. Its sibling `../understand/` contains the shared runtime.

1. Run `node "<this-skill-directory>/../understand/scripts/runtime.mjs" --check`.
2. If dependencies/core are missing, run the same script with `--setup`. It requires Node.js 22+ and network access, installs the pinned pnpm dependencies, and builds the core. Report failures; do not claim setup succeeded on a nonzero exit.
3. The command prints the absolute plugin root. Set `PLUGIN_ROOT` and `CLAUDE_PLUGIN_ROOT` to that exact path in subsequent tool commands and delegate messages. These are per-command variables, not permanent changes to shell configuration. On PowerShell use `$env:PLUGIN_ROOT` and `$env:CLAUDE_PLUGIN_ROOT`.
4. Use that root for `packages/`, `agents/`, and the dashboard. Where upstream code searches known install paths, the explicit `CLAUDE_PLUGIN_ROOT` candidate selects this runtime.
5. The full skill set must be installed together. Graph generation still requires the current AI session; installation alone does not analyze the project or produce a dashboard. Use Korean output when requested (`--language ko`).

No global home-directory plugin link, automatic update hook, or Figma integration is installed by this bundle.
