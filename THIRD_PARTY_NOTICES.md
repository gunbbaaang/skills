# Sources, licenses, and local adaptations

This is a curated redistribution, not a claim of authorship of the upstream tools. Exact source commits and paths are recorded in `sources.lock.json`. Third-party license texts are retained in `licenses/` and in each redistributed skill directory, so skill-only copies retain attribution.

| Component | Upstream | License |
|---|---|---|
| Handoff | https://github.com/mattpocock/skills | MIT, Matt Pocock |
| Planning with Files | https://github.com/OthmanAdi/planning-with-files | MIT, Ahmad Adi |
| Visual Explainer | https://github.com/nicobailon/visual-explainer | MIT, Nico Bailon |
| Graphify | https://github.com/Graphify-Labs/graphify | Apache-2.0, with upstream LICENSE-MIT and NOTICE retained |
| Understand Anything | https://github.com/Egonex-AI/Understand-Anything | MIT, Yuxiang Lin and Infinite Universe, Inc. |
| Frontend Design / Webapp Testing | https://github.com/anthropics/skills | Apache-2.0 in each selected skill's LICENSE.txt |
| React Best Practices / Web Design Guidelines | https://github.com/vercel-labs/agent-skills | MIT as declared by the upstream README; React skill also declares MIT in frontmatter |
| Web Interface Guidelines snapshot | https://github.com/vercel-labs/web-interface-guidelines | MIT, Vercel Labs |
| Slides | https://github.com/JetBrains/skills/tree/main/slides | Apache-2.0; upstream OpenAI author/source attribution retained |
| Probe Hackathon Coach | https://github.com/gunbbaaang/probe-hackathon-kit | Original preparation material from this user's project; no new blanket license is assigned here |

Local packaging changes:

- Frontmatter is normalized to common Codex-compatible fields. Native host hook declarations and tool allowlists are not installed or enabled. Brief bundle-specific usage notes are added after frontmatter.
- Handoff notes Codex's invocation style and that an explicitly requested output path takes precedence.
- Planning with Files includes its scripts/templates but explicitly distinguishes manual file-based continuity from native hook-based automatic injection. Existing coach notes should be reused or mapped, not duplicated.
- Visual Explainer includes the full adjacent kit, references, templates, and command resources. Pi/MCP integration is not assumed available.
- Graphify includes the Codex skill and its reference sidecar. `BUNDLE.md` directs first-use setup to an isolated pinned CLI instead of an automatic system-Python upgrade. No AGENTS.md hook or multi-agent setting is installed.
- Understand Anything includes eight relevant skills plus shared plugin runtime source under `skills/understand/runtime/`. Duplicate skill entrypoints, generated dependencies, and the Figma-only skill are omitted. A portable runtime locator/setup helper avoids global symlinks. Upstream plugin-path searches receive the resolved root through per-command environment variables.
- The hackathon coach includes a practical field guide connecting the existing workflow with web/PPT skills. Original evaluation photographs, personal identifiers, credentials, and local conversation transcripts are not included.
- Frontend Design is scoped to the confirmed MVP; its fictional design brief is not treated as a real user statement. Webapp Testing adds portable setup guidance and bounded user-visible waits for streaming/polling apps. Upstream examples remain as reference material.
- React Best Practices is used only for relevant React/Next.js work. Web Design Guidelines adds a dated fallback snapshot when its upstream web fetch is unavailable. A plain MIT license text plus the upstream license declaration is retained for agent-skills, which has no standalone root LICENSE at the pinned commit.
- Slides retains the PptxGenJS workflow, utilities, assets, license and OpenAI attribution from JetBrains/skills. BUNDLE.md adds terminal setup, Korean font checks, evidence-based content guidance and explicit reporting when visual validation cannot run.

Local installer and packaging helpers are provided for this bundle. Third-party components retain their original licenses; no repository-wide license is substituted for them.
