# Sources, licenses, and local adaptations

This is a curated redistribution, not a claim of authorship of the upstream tools. Exact source commits and paths are recorded in `sources.lock.json`. Third-party license texts are retained in `licenses/` and in each redistributed skill directory, so skill-only copies retain attribution.

| Component | Upstream | License |
|---|---|---|
| Handoff | https://github.com/mattpocock/skills | MIT, Matt Pocock |
| Planning with Files | https://github.com/OthmanAdi/planning-with-files | MIT, Ahmad Adi |
| Visual Explainer | https://github.com/nicobailon/visual-explainer | MIT, Nico Bailon |
| Graphify | https://github.com/Graphify-Labs/graphify | Apache-2.0, with upstream LICENSE-MIT and NOTICE retained |
| Understand Anything | https://github.com/Egonex-AI/Understand-Anything | MIT, Yuxiang Lin and Infinite Universe, Inc. |
| Probe Hackathon Coach | https://github.com/gunbbaaang/probe-hackathon-kit | Original preparation material from this user's project; no new blanket license is assigned here |

Local packaging changes:

- Frontmatter is normalized to common Codex-compatible fields. Native host hook declarations and tool allowlists are not installed or enabled. Brief bundle-specific usage notes are added after frontmatter.
- Handoff notes Codex's invocation style and that an explicitly requested output path takes precedence.
- Planning with Files includes its scripts/templates but explicitly distinguishes manual file-based continuity from native hook-based automatic injection. Existing coach notes should be reused or mapped, not duplicated.
- Visual Explainer includes the full adjacent kit, references, templates, and command resources. Pi/MCP integration is not assumed available.
- Graphify includes the Codex skill and its reference sidecar. `BUNDLE.md` directs first-use setup to an isolated pinned CLI instead of an automatic system-Python upgrade. No AGENTS.md hook or multi-agent setting is installed.
- Understand Anything includes eight relevant skills plus shared plugin runtime source under `skills/understand/runtime/`. Duplicate skill entrypoints, generated dependencies, and the Figma-only skill are omitted. A portable runtime locator/setup helper avoids global symlinks. Upstream plugin-path searches receive the resolved root through per-command environment variables.
- The original hackathon coach is copied without behavioral changes. Original evaluation photographs, personal identifiers, credentials, and local conversation transcripts are not included.

Local installer and packaging helpers are provided for this bundle. Third-party components retain their original licenses; no repository-wide license is substituted for them.
