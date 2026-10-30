# First-use setup in Codex

This bundle includes the Codex skill and every packaged reference. The CLI is a separate dependency: Python 3.10+ and `graphifyy==0.9.97` (the package name has two `y` characters).

If `graphify --version` already works, inspect its version before deciding whether an upgrade is needed. Do not replace a working user-managed installation silently. For a new installation with uv:

```sh
uv tool install graphifyy==0.9.97
```

Use the executable path printed by uv if it is not on PATH. Do not modify permanent shell configuration just to invoke it. Resolve the matching Python interpreter from the uv tool directory. Alternatively create a project-local virtual environment and use its Python with `-m pip install graphifyy==0.9.97`; keep that interpreter and its Scripts/bin directory for subsequent commands.

The upstream Step 1's automatic upgrade/system-pip fallback is replaced by this isolated, pinned setup. In subsequent upstream examples use the resolved interpreter for `PYTHON`, and the resolved executable when the command is `graphify`. Never use `--break-system-packages` for this bundle.

The skill is already registered by the bundle. Running `graphify install` again is unnecessary; this bundle does not install hooks, change AGENTS.md, or enable multi-agent settings. If the host cannot use parallel agents, perform the extraction sequentially or use the supported local structural path. Report the actual route and limitations.

Build a graph only for the user's requested files. Optional PDF, video, database, MCP, or API-provider extras are not installed by default. Use `$graphify` in Codex even where upstream examples show `/graphify`.
