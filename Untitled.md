Obsidian Vault system:
# Karpathy Style Wiki
General Inbox for Notes is raw/clippings

Vault structure:
- **`raw/`** — one flat folder.  File gets moved to raw/clippings after ingesting. Attachments go to raw/clippings/assets raw/clipping subfolders. 
	- Origin and format in frontmatter, not in the directory structure, if information is not already provided.

- **`wiki/`** — subfolders per page type: `concepts/`, `entities/`, `sources/`, `sops/`, `decisions/`, `outputs/`, `syntheses/`. Type is path; topic is filename.

- **Schema** — root-level config files. Currently `CONTEXT.md`, `AGENTS.md`,

- Hidden tooling dirs (`.obsidian/`, `.agent/, `.claude/`, `.cursor/`) are tool config, not schema.

## General

**A `CONTEXT.md` at the  root** — the durable vocabulary. Defines the seven page types in _your_ language (not the agent's), defines the `raw/` → `wiki/` flow, defines the read test, defines what "explored" means as the validation gate. This is the file every future agent session loads first. It's the equivalent of Pocock's `CONTEXT.md` for your vault. **CONTEXT.md gets written. Will be grilled afterwards.** Good — that's the right sequence. Draft, then stress-test.

**AGENTS.md edits** — small, surgical: tighten the relevance filter section, add a line about authorship living in frontmatter (`author: tom | external | vendor`) so the "who wrote it" question stops being a folder problem.

**B. triage SOP** — `wiki/sops/wiki-triage-flow.md`. The concrete recipe for what happens when you drop a file in `raw/clippings/`: which folder it gets sorted into, which page types get compiled, how the agent decides between "this is one entity page" vs. "this is an entity + three sops."

**`raw/` is read-only after sort.** No content edits. Updates happen via re-ingest of a new source, or via direct edits to the compiled `wiki/` pages — never by mutating raw files. This is the strict version of Karpathy's immutability


Proposal for Skills (actionable Skills for):
- wiki-ingest
- wiki-triage
- wiki-query
- wiki-evolving
- wiki-lint

Strong foundation of vocabularies and strictly typed rules.

All interactively updating the wikis/pages while respecting the rules.

**Structure**

	.docs/
			templates/
		.obsidian/
		.git/
		.agents/
		.claude/
	raw/
		clippings/
	wiki/
		concepts/
		entities/
		sources/
		sops/
		decisions/
		outputs/
		syntheses/
		hot.md
		index.md
		log.md
	
## Tooling

What I want: 
Different options to add new pages/contents into database:
- Quick entry via Raycast etc.
- Via Claude Code
- Via Raycast AI 

using all the tooling: 
- Obsidian CLI
- QMD MCP Server (for queries)
- Tooling Skillset for outstanding page design
-  Top of the class temlates for different pages or sections 
- Wikilinking, High level graphic overviews of contents, sorting options, dashboards
- Obsidian Web Clipper
- Obsidian Templater

**Getting data is the claude/mcp domain**
**Creating beautiful pages is the obsidian tools/skills/plugin domain**

---
https://github.com/kepano/obsidian-skills
https://docs.obsidian.md/Home
https://www.macstories.net/club/macstories-weekly-issue-514/obsidian-into-claude-and-app-quality/
https://github.com/SilentVoid13/Templater/discussions/888