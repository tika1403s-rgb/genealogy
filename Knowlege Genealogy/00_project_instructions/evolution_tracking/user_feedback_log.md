# User Feedback Log

**Owner:** Instruction Curator
**Status:** Active log
**Last updated:** 2026-05-20

---

Every direct user statement that reads as "always do X," "never do Y," "from now on Z," or otherwise specifies a preference is logged here. Even rejected proposals are kept (with a "rejected" note) so the history of decisions is preserved.

## Entry format

```markdown
### YYYY-MM-DD — [short title]
**User said:** "[exact quote]"
**Curator interpretation:** [the rule we drafted]
**Outcome:** approved / approved-with-revision / rejected / pending
**Files updated:** [list with version bumps]
**Retroactive scope:** [future-only / applied to existing X items / declined]
**Notes:** [anything else]
```

---

### 2026-05-20 — Add Pioneers, Ideas, and Enabling Factors as first-class data
**User said:** "Include the following in the plan for the Gap Identified: Pioneers, Ideas, and Enabling Factors" — accompanied by a comprehensive specification covering pioneer schema, breakthrough schema, join tables, four new edge types, the AI canonical example (enabled by transistor + statistics + Boolean logic + Turing machine + information theory + neural net model + backpropagation + datasets + GPU), and new visualization deliverables.
**Curator interpretation:** the v1.0 ontology represented fields and their relationships but did not give first-class structure to people and enabling discoveries. Promoting pioneers and breakthroughs to first-class entities (with two new tables + two join tables + four new edge relation types), plus matching audit metrics, addresses the gap.
**Outcome:** approved (executed as part of bootstrap).
**Files updated:** ontology v1.0 → **v2.0**; audit framework v1.0 → v1.1; trunk definitions v1.0 → v1.1; six chat instruction files v1.0 → v1.1; three audit templates extended; two evolving-rules files v1.0 → v1.1; nodes.csv schema expanded 19→24 cols; four new master CSVs created; snapshot at `version_history/v1.1_pioneers_breakthroughs/`. Full detail in `instruction_update_history.md`.
**Retroactive scope:** N/A — no existing data; this is bootstrap.
**Notes:** treated as ontology major bump (v1.0 → v2.0) per Curator policy "changing a fundamental approach." Other affected files received minor bumps (v1.x → v1.y). Snapshot folder name uses v1.1 (project-wide minor bump label) rather than v2.0 (ontology-only major bump) to keep the snapshot history consistent.

---

### 2026-05-26 — Unified two-step interaction for pioneer and breakthrough cards
**User said:** "when a node is clicked, uniformise the pioneer and breakthrough UI i.e. Make it so that both have one click allowing person to read a part of the extract and allowing them to read on with a button/link which pops out the window and gives them the whole information."
**Curator interpretation:** pioneer and breakthrough cards in the detail panel must use identical interaction: (1) click card → inline expand with a short excerpt; (2) "Full profile / Full details" button → modal overlay with complete record. Neither should open the full overlay on first click, nor expand inline with no popup option.
**Outcome:** approved (implemented in `viz_interactive_T3.html` v1.1 and locked into `visualization_builder_instructions.md` v1.2).
**Files updated:** `07_exports/viz_interactive_T3.html`, `07_exports/changelog.md`, `visualization_builder_instructions.md` v1.1 → v1.2, `instruction_update_history.md`.
**Retroactive scope:** future-only (applies to all subsequent `viz_interactive_*.html` files).
**Notes:** the breakthrough card fix also resolved a bug where apostrophes in long text fields broke inline `onclick` JSON, silently disabling all breakthrough cards.

---

### 2026-05-26 — Correct edge direction labeling (From = origin, To = emerging)
**User said:** "when a connection is clicked, the from and to section seem to have inverted names. for eg. connection between song dynasty material investigation and daoist natural observation, where song dynasty investigation emerged from daoist observation, the from should indicate daoist observation and to should say song investigation. Correct this for all the connections."
**Curator interpretation:** the edge panel "From" label must show the knowledge *origin* (edge `target` field — the older tradition knowledge flowed FROM), and "To" must show the *emerging* tradition (edge `source` field — the node that emerged). This is a semantic direction rule, not a raw-field-name rule.
**Outcome:** approved (implemented and locked into `visualization_builder_instructions.md` v1.2).
**Files updated:** `07_exports/viz_interactive_T3.html`, `07_exports/changelog.md`, `visualization_builder_instructions.md`, `instruction_update_history.md`.
**Retroactive scope:** future-only (future visualizations must follow this labeling convention).
**Notes:** all 21 tradition edges use `emerged_from` or `method_imported_from`, both of which have source = emerging node and target = origin node — the fix is consistently correct for all edge types present.

---

### 2026-05-26 — More spacing between nodes, edges, pioneers, and breakthroughs
**User said:** "More spacing between the different nodes, edges, pioneers and breakthroughs so that map is more legible."
**Curator interpretation:** node positions in preset layouts should be scaled to avoid visual crowding. A ×1.7 uniform scale (applied to all x/y positions) is the baseline fix; future visualizations must build in sufficient spacing from the start (minimum 200 px between nodes in the same regional cluster at default zoom).
**Outcome:** approved (implemented in `viz_interactive_T3.html` v1.1 and encoded as a guideline in `visualization_builder_instructions.md` v1.2).
**Files updated:** `07_exports/viz_interactive_T3.html`, `07_exports/changelog.md`, `visualization_builder_instructions.md`, `instruction_update_history.md`.
**Retroactive scope:** future-only.
**Notes:** the ×1.7 scale was applied uniformly to all node types (tradition, pioneer, breakthrough), preserving relative positions while spreading the overall layout.

---

*(future entries below as user feedback arrives)*
