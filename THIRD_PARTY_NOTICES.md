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
| Explore Data / Validate Data / Data Visualization | https://github.com/anthropics/knowledge-work-plugins/tree/main/data | Apache-2.0 from the data plugin's own LICENSE |
| Superpowers (15 skills, including Systematic Debugging) | https://github.com/obra/superpowers | MIT, Jesse Vincent |
| Ponytail (6 skills) | https://github.com/DietrichGebert/ponytail | MIT, DietrichGebert |
| ECC (8 selected skills) | https://github.com/affaan-m/ECC | MIT, Affaan Mustafa |
| LLM Evaluation | https://github.com/wshobson/agents | MIT, Seth Hobson |
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
- React's upstream `metadata.json` is renamed `upstream-metadata.json` because the skills CLI excludes the original filename. Its contents are preserved and the README distinguishes upstream maintenance instructions from using the bundled reference.
- Slides retains the PptxGenJS workflow, utilities, assets, license and OpenAI attribution from JetBrains/skills. BUNDLE.md adds terminal setup, Korean font checks, evidence-based content guidance and explicit reporting when visual validation cannot run.

Local installer and packaging helpers are provided for this bundle. Third-party components retain their original licenses; no repository-wide license is substituted for them.

2026-10-31 evidence-skills additions (version 1.2.0):

- Three Anthropic data skills preserve their workflow/reference bodies and the data plugin's own Apache license. Host-specific argument hints and invocation flags are removed, connector links are relocated with the original connector document retained, and Korean/local-file guidance distinguishes examples, heuristics and actual evidence. The time-series example sorts each group before plotting.
- Systematic Debugging preserves the four-phase method and supporting operational resources. References to unbundled mandatory Superpowers skills are replaced with self-contained reproduction and verification steps. Repeated failures prompt evidence review rather than an automatic architecture conclusion or mandatory approval for already-authorized work. Authoring logs and pressure-test prompts are omitted. No Superpowers plugin, hooks or subagent workflow is installed.
- LLM Evaluation retains the upstream reference patterns with explicit notice that snippets require adaptation and are not validated turnkey code. A small local-first hackathon evaluation guide is added; perplexity wording and judge calibration guidance are corrected. No API keys, paid models, hosted datasets or external evaluation service are included or automatically invoked.
- Popularity snapshots were checked on 2026-10-31 as discovery signals, not quality or score guarantees: skills.sh installs were approximately 5.9K (explore-data), 3.8K (validate-data), 14.0K (data-visualization), 314.2K (systematic-debugging), and 13.0K (llm-evaluation). The three upstream GitHub repositories had 33,985, 309,250, and 42,009 stars respectively. These values change over time.

2026-10-31 workflow additions (version 1.3.0):

- Superpowers adds the other 14 skills at the same pinned commit; the already packaged Systematic Debugging remains unchanged. Supporting prompts, references and optional helpers are retained. The using-superpowers and brainstorming descriptions are scoped to relevant development/design work, and bundle notes preserve existing user decisions, authorization and Probe records. Automatic discovery remains enabled.
- `using-superpowers/references/codex-tools.md` uses current host schemas rather than stale model routing or configuration instructions. The two inline-execution helpers call sibling scripts through Bash so a copied installation does not rely on Unix executable bits. Helpers, visual companion and subagent workflows are not automatically started.
- All six Ponytail skills preserve their MIT notices. Plugin namespace examples are mapped to standalone Codex names. The help page describes this bundle instead of unavailable global hooks, status bands or session import. Gain numbers remain the upstream author's benchmark claims and were not reproduced for this bundle.
- ECC contributes search-first, api-design, error-handling, security-review, verification-loop, cost-aware-llm-pipeline, iterative-retrieval and architecture-decision-records under `ecc-` names. Existing resource files are retained. BUNDLE.md maps unavailable agent/tool names to current tools, reuses decision records, treats code/model/price examples as illustrative, and distinguishes real verification from placeholders. No ECC hook, background learning, global configuration or MCP service is installed.
- ECC's README identifies its author as a September 2025 Anthropic x Forum Ventures hackathon winner. This is the author's report, not an independently verified event result or a claim that every skill in today's repository was used in that event. Source: the pinned repository README, About section.
