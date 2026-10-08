# Trunk Definitions

**Version:** 1.1
**Last Updated:** 2026-05-20
**Status:** Active
**Affected chats:** all (especially Source Librarian and Extractor at the start of each new trunk)

## Change Log
- v1.0 (2026-05-20): Initial version. Defines the 10 vertical trunk lineages, era-by-era arcs, key transitions, and known controversies. Trunk 3 (pilot) gets the deepest treatment; others are framed adequately for activation when their turn comes.
- v1.1 (2026-05-20): Added per-trunk note that pioneer + breakthrough extraction (per ontology v2.0) accompanies node extraction. Cross-trunk enabler examples expanded in the "Cross-trunk patterns to watch for" section.

---

## What a trunk is

A trunk is a *continuous tradition of inquiry* traced from antiquity to the present. Each trunk is a moving target: it begins with a recognizable cluster of problems people were asking about, passes through conceptual breakthroughs, eventually acquires a name, gets institutionalized, and reaches a modern formulation that may itself be undergoing transformation.

The 10 trunks are not airtight boxes — they overlap, cross-pollinate, and produce hybrid children (computer science as a merge of mathematics and logic; molecular biology as a merge of chemistry and life sciences). Cross-trunk edges are first-class and will be added explicitly in Weeks 33–36.

## Era conventions

Within each trunk we use five eras:
- **Ancient** (≤500 CE)
- **Medieval** (500–1500)
- **Early Modern** (1500–1800)
- **Modern** (1800–1950)
- **Contemporary** (1950–present)

These are conventional, not historical truth. Assign an era by a node's `date_start`. Some traditions have nothing meaningful in an era — that's expected, leave the gap and note it.

---

## Trunk 1 — Mathematical Sciences

**Identity:** The investigation of quantity, structure, space, and pattern. Mathematics is unique in this list because its results, once proven, do not get falsified — they get extended, recontextualized, and re-foundationalized.

**Why it matters across the graph:** Mathematics is the most prolific method exporter in the project. Cross-trunk edges of type `mathematized_by` and `method_imported_from` originating in Trunk 1 land in Trunk 2 (celestial mechanics), Trunk 3 (Newtonian physics), Trunk 5 (mathematical economics), Trunk 4 (population genetics), and Trunk 9 (computer science).

**Arc:**
- **Ancient:** Babylonian and Egyptian arithmetic and geometry; Greek geometry as deductive system (Euclid); Greek arithmetic, number theory, mechanics (Archimedes); Indian numerical and combinatorial work (Brahmagupta context); Chinese arithmetic.
- **Medieval:** Islamic algebra (Al-Khwarizmi, Omar Khayyam); Indian decimal positional system; trigonometry; transmission into Europe via Toledo school.
- **Early Modern:** Analytic geometry (Descartes, Fermat); calculus (Newton/Leibniz, with priority dispute as a `disputed_claim`); probability (Pascal/Fermat correspondence).
- **Modern:** Pure/applied split crystallizes; rigorous analysis (Cauchy, Weierstrass); set theory and foundations (Cantor, Frege, Russell); statistics emerges as a discipline.
- **Contemporary:** Mathematical logic matures; computer science branches off via merge with Trunk 9; statistics evolves into data science; cryptography; ML theory.

**Key transitions to capture:**
- The deductive turn in Greek geometry.
- The Hindu–Arabic numeral transmission (multi-region, multi-century).
- The calculus priority dispute (with both Newton and Leibniz as parents of the field).
- The foundations crisis (1880s–1930s).
- The branching of computer science (~1936–1956).

**Known controversies:**
- Newton vs Leibniz priority — record as `disputed_claim`, not a winner.
- Whether Babylonian work is "mathematics" or "calculation procedures" — flag the categorical question.
- Whether non-Western mathematical traditions are independent or downstream of Greek work (Indian mathematics is well-documented as substantially independent; Chinese mathematics partially so).

---

## Trunk 2 — Celestial Studies

**Identity:** Observation and explanation of the heavens. Astronomy was the first natural science to mathematize seriously and the first to clearly split from a sibling tradition (astrology).

**Why it matters across the graph:** The astronomy/astrology split is the cleanest case study in the project of how `split_from` works. The instrument-enabled emergence pattern (`instrument_enabled` edges) is central here — telescope, spectroscope, radio telescope, space-based observatory.

**Arc:**
- **Ancient:** Babylonian observation records and predictive arithmetic; Greek geometric cosmology (Eudoxus, Ptolemy); Chinese independent observational tradition (continuous records spanning centuries); astrology and astronomy unified.
- **Medieval:** Islamic astronomy (Al-Battani, Al-Tusi, Ibn al-Shatir, with influence on Copernican models); Indian siddhanta tradition; Chinese observational refinement.
- **Early Modern:** Copernican heliocentrism; Tycho's instruments; Kepler's laws; Galileo's telescope (`instrument_enabled`); Newtonian celestial mechanics (cross-trunk `mathematized_by` from Trunk 1); astronomy/astrology split crystallizes through 1600s.
- **Modern:** Spectroscopy (Fraunhofer, Kirchhoff) enables astrophysics as a distinct subfield (`instrument_enabled` + `split_from`); stellar evolution; cosmology emerges with Einstein and Hubble.
- **Contemporary:** Radio astronomy, space-based observation; gravitational wave astronomy (LIGO, 2015); exoplanet science; astrobiology emerges as a chimeric field merging with Trunk 4.

**Key transitions to capture:**
- Babylonian → Greek transmission of observational data.
- The Islamic refinement of Ptolemaic models (often skipped in Western narratives — capture it).
- The Copernican revolution as a slow shift, not a sudden break.
- Astronomy/astrology divergence (gradual, 1500s–1700s).
- Astrophysics emergence as instrument-driven.

**Known controversies:**
- Whether Islamic Tusi-couple models directly influenced Copernicus (recent scholarship says yes; older narratives ignored it).
- Exact dating of when astrology becomes excluded from "respectable" astronomy.

---

## Trunk 3 — Material Investigation **(PILOT)**

**Identity:** The investigation of matter, substances, and the laws governing physical reality. What is matter made of? How do substances transform? What rules govern motion, force, and change?

**Why it matters / why it's the pilot:** Trunk 3 forces every difficult case the project must handle: deep ancient roots, multiple non-European contributing traditions, a gradual split (alchemy → chemistry) that resists clean dating, a clear merge (physics + chemistry → physical chemistry), instrument-driven emergence (spectroscopy), and contested historical boundaries throughout.

**Arc:**
- **Ancient:** Greek natural philosophy (Thales, Anaximander, Aristotle, atomists); Hellenistic alchemy; ancient metallurgy and pharmacy (~3000 BCE onward, practical knowledge); Chinese wu xing system and alchemy; Indian Vaisheshika material atomism; Roman practical chemistry.
- **Medieval:** Islamic alchemy systematizes experimental procedure (Jabirian corpus, Al-Razi); European alchemy receives Islamic work through Iberian and Sicilian translations; scholastic natural philosophy synthesizes Aristotle with experiment; Chinese gunpowder chemistry; medieval optical science (Ibn al-Haytham).
- **Early Modern:** Experimental philosophy (Bacon, Royal Society); mechanical philosophy (Descartes, Boyle); Newtonian mechanics mathematizes natural philosophy (cross-trunk edge from Trunk 1); pneumatic chemistry (Boyle, Hales, Black); phlogiston theory (Stahl); chemical revolution (Lavoisier, Priestley, Cavendish — collective, contested); chemistry as named field crystallizes 1780–1800; physics as named field crystallizes 1750–1850.
- **Modern:** Physics and chemistry institutionalize as separate departments and journals (~1850–1900); thermodynamics; electromagnetism (Faraday, Maxwell); spectroscopy as `instrument_enabled` field; organic chemistry as `split_from` chemistry; physical chemistry as `merged_with` physics + chemistry (Gibbs, van't Hoff, Arrhenius, Ostwald, c. 1880–1900); atomic theory (Dalton through Bohr); statistical mechanics as merge of thermodynamics + atomism; radioactivity.
- **Contemporary:** Quantum mechanics revolutionizes physics (1900–1930); nuclear physics; solid state → condensed matter physics; materials science as merge of physics + chemistry + engineering (cross-trunk to Trunk 8, c. 1960–1990); nanotechnology (1980s+); quantum chemistry; computational materials science.

**Key transitions to capture (planned ~50 nodes):**
1. Greek natural philosophy as first_problem_tradition (~600 BCE–400 CE).
2. Aristotelian four-elements framework as conceptual_breakthrough (~350 BCE–1600 CE).
3. Greek atomism as conceptual_breakthrough (~450 BCE–300 BCE).
4. Hellenistic alchemy as first_problem_tradition (~300 BCE–300 CE).
5. Islamic alchemy as conceptual_breakthrough (~800–1300).
6. Chinese wu xing and alchemy as parallel first_problem_tradition.
7. Indian material philosophy (Vaisheshika atomism).
8. European alchemy as transmission descendant of Islamic alchemy.
9. Scholastic natural philosophy as Aristotle + experiment synthesis.
10. Mechanical philosophy as conceptual_breakthrough (~1630–1700).
11. Newtonian mechanics as conceptual_breakthrough (1687+).
12. Phlogiston theory as conceptual_breakthrough that was later overturned.
13. Chemical revolution as conceptual_breakthrough (1770–1800).
14. Chemistry as named_field (~1780–1800).
15. Physics as named_field / renamed_from natural philosophy (~1750–1850).
16. Thermodynamics, electromagnetism, spectroscopy, organic chemistry as modern subfields.
17. Physical chemistry as merged_with two parents (~1880–1900).
18. Quantum mechanics as conceptual_breakthrough.
19. Materials science as merged_with three parents (cross-trunk).
20. Contemporary specializations.

**Expected edges (planned ~90):**
- Multiple `emerged_from` edges showing tradition continuity.
- At least two `split_from` edges (alchemy → chemistry; natural philosophy → physics).
- At least three `merged_with` edges (physical chemistry; statistical mechanics; materials science).
- One `renamed_as` edge (natural philosophy → physics, partially).
- Multiple `mathematized_by` cross-trunk edges from Trunk 1.
- `instrument_enabled` edges for spectroscopy and quantum experiments.
- `method_imported_from` edges where chemistry imports physics methods.
- `problem_domain_shared_with` edges between Greek, Chinese, and Indian material atomism.

**Known controversies (expected `disputed_claim` entries):**
- Exact dating of alchemy → chemistry split. Lavoisier's 1789 *Traité* is a convenient marker but the transition spans 1660–1830.
- Whether the chemical revolution was a Kuhnian paradigm shift or gradual accumulation.
- The extent to which Islamic alchemy was experimental vs theoretical.
- Whether Jabirian corpus is by Jabir ibn Hayyan or a multi-author corpus spanning ~200 years (recent scholarship: the latter).
- Whether physics existed as a named field before institutionalization (terminology vs practice).

**Geographic target for medieval era:** at least 40% non-European nodes (per audit framework Section 6f).

---

## Trunk 4 — Life Studies

**Identity:** The investigation of living things — their forms, functions, origins, diseases, and ecological relationships. Heaviest branching trunk; constant medicine ↔ biology interaction.

**Arc:**
- **Ancient:** Greek natural history (Aristotle's biological works, Theophrastus on plants); ancient medicine (Hippocratic corpus, Galen); Ayurvedic medicine; Chinese medicine; Mesopotamian and Egyptian materia medica.
- **Medieval:** Islamic medicine systematizes Greco-Roman tradition (Avicenna, Al-Razi, Ibn al-Nafis discovering pulmonary circulation); medieval European herbals; Chinese pharmacological compendia (e.g., Tang and Song materia medica).
- **Early Modern:** Vesalius reforms anatomy; Harvey on circulation; Linnaean taxonomy; microscopy enables microbiology preview (Leeuwenhoek, Hooke); evolution concept germinating (Maupertuis, Lamarck).
- **Modern:** Biology as named_field (~1800, Lamarck/Treviranus coin term); Darwinian evolution; cell theory; Mendelian genetics (independent discovery dispute); germ theory; biochemistry as merge with Trunk 3.
- **Contemporary:** Molecular biology (Watson/Crick/Franklin/Wilkins — multi-pioneer, with the well-documented Franklin attribution controversy); genomics; synthetic biology; systems biology.

**Key transitions:** Aristotle as first_problem_tradition (NOT named_field); medical/biological re-merger in modern era; molecular biology as cross-trunk merge.

**Known controversies:** Mendel's "rediscovery" by three independent workers; the Franklin/Watson-Crick credit allocation; whether Galenic medicine is a "tradition" or a "system."

---

## Trunk 5 — Mind & Society

**Identity:** Investigation of human thought, behavior, and collective organization. Distinctive for late institutionalization — most of these fields acquire their named/institutionalized form in the 1800s, despite ancient first_problem_tradition origins.

**Arc:**
- **Ancient:** Greek ethics (Plato, Aristotle); rhetoric; political theory; early historiography overlapping with Trunk 7.
- **Medieval:** Scholastic philosophy; Islamic political philosophy (Al-Farabi, Ibn Khaldun on social organization); medieval political thought.
- **Early Modern:** Enlightenment moral philosophy; political economy (Smith, 1776); associationist psychology precursors.
- **Modern:** Psychology institutionalizes (Wundt's Leipzig lab, 1879 — a paradigm `institutionalized_field` event); sociology (Comte, Durkheim, Weber); economics professionalizes; anthropology emerges.
- **Contemporary:** Cognitive science (merge with Trunk 9 + neuroscience from Trunk 4); behavioral economics; computational social science; network science applied to social systems.

**Key transitions:** Late institutionalization is the signature pattern; Wundt 1879 is the cleanest `institutionalized_field` date in the entire project; Ibn Khaldun's *Muqaddimah* as a major non-European contribution often omitted.

**Known controversies:** Whether ancient ethics → modern moral philosophy is genuine continuity or retrospective construction; how to attribute economics' founding (Smith is a placeholder; economics has many parents).

---

## Trunk 6 — Language & Meaning

**Identity:** The study of language, signs, and meaning. Merges with computation in the 20th century (formal grammars, NLP) and with logic throughout.

**Arc:**
- **Ancient:** Greek grammar (Dionysius Thrax); Aristotle's logic and rhetoric; Indian grammatical tradition (Pāṇini's *Aṣṭādhyāyī*, a remarkable formal grammar from ~500 BCE).
- **Medieval:** Arabic grammatical tradition; scholastic logic; modistae.
- **Early Modern:** Universal language projects; Port-Royal grammar; comparative philology emerging.
- **Modern:** Historical linguistics (Grimm, Bopp); structural linguistics (Saussure, Bloomfield); formal logic with Frege; semiotics (Peirce).
- **Contemporary:** Generative grammar (Chomsky); computational linguistics; natural language processing; LLMs as 2010s+ phenomenon.

**Key transitions:** Pāṇini deserves serious treatment — formal grammar predates Western awareness by 2000+ years; the merger of linguistics + computation through Chomsky.

**Known controversies:** Whether Chomskyan universals hold; the relationship between formal grammar and statistical NLP.

---

## Trunk 7 — Historical Inquiry

**Identity:** The investigation of the past — how to know what happened, what counts as evidence, how to interpret it.

**Arc:**
- **Ancient:** Greek historiography (Herodotus, Thucydides); Chinese historiographical tradition (Sima Qian's *Shiji*, a major comparable origin); Roman annals; biblical historiography.
- **Medieval:** Chronicle tradition; Islamic historiography (Al-Tabari, Ibn Khaldun's philosophy of history as a major innovation); Chinese dynastic histories.
- **Early Modern:** Humanist philology; antiquarianism; source criticism (Mabillon, Valla); early archaeology (Winckelmann).
- **Modern:** Professional history (Ranke); archaeology institutionalizes; anthropology splits from natural history; oral history later.
- **Contemporary:** Digital humanities; historical sociology; memory studies; environmental history; big history.

**Key transitions:** The Rankean turn to source criticism; Ibn Khaldun's `conceptual_breakthrough` for the philosophy of history.

**Known controversies:** Whether ancient historiography is "history" by modern standards; how to credit non-Western traditions of historical writing.

---

## Trunk 8 — Practical Arts

**Identity:** Engineering, applied sciences, and craft knowledge organized around making things work. Distinctive for technology-science feedback loops — engineering both depends on and drives scientific knowledge.

**Arc:**
- **Ancient:** Roman engineering; ancient agriculture; pre-modern medicine as practical art; ancient architecture; metallurgy.
- **Medieval:** Guild knowledge; practical mathematics; agricultural manuals; Islamic engineering (clockwork, hydraulics).
- **Early Modern:** Renaissance engineering (Brunelleschi, Leonardo); ballistic and fortification; experimental method bridges craft and science.
- **Modern:** Civil engineering, mechanical engineering, electrical engineering institutionalize as distinct disciplines; chemical engineering; aeronautical engineering.
- **Contemporary:** Software engineering; bioengineering; systems engineering; mechatronics; the engineering-science distinction continues to blur.

**Key transitions:** Engineering professionalization through technical schools and societies (École Polytechnique 1794 as a `institutionalized_field` anchor); software engineering emergence (~1968 NATO conference).

**Known controversies:** Whether craft knowledge is properly part of this trunk or a separate tradition; the engineering-vs-science status question.

---

## Trunk 9 — Formal Reasoning

**Identity:** The study of valid inference, formal systems, and proof. Closely intertwined with Trunks 1 (mathematics) and 6 (linguistics); creates computer science via merge with mathematics.

**Arc:**
- **Ancient:** Aristotelian syllogistic; Stoic propositional logic; Indian logic (Nyaya); Buddhist logic (Dignaga, Dharmakirti).
- **Medieval:** Scholastic logic (Peter of Spain, Ockham); Arabic logic commentaries on Aristotle; Indian Navya-Nyaya.
- **Early Modern:** Leibniz's calculus ratiocinator; Boolean algebra (Boole 1854).
- **Modern:** Mathematical logic (Frege 1879 *Begriffsschrift*); set theory; *Principia Mathematica* (Russell/Whitehead); Gödel's incompleteness; Turing's computability (1936) as the crucial `conceptual_breakthrough` enabling computer science.
- **Contemporary:** Computer science as a merged_with field (Trunks 1 + 9); AI; computability theory; type theory; proof assistants.

**Key transitions:** The 1879 Frege publication; Gödel 1931; Turing 1936; computer science as merge event ~1940–1950s.

**Known controversies:** Whether Indian/Buddhist logic is genuinely a precursor or developed independently; how to attribute computer science (Turing/Church/von Neumann/Shannon — all parents).

---

## Trunk 10 — Earth & Environment

**Identity:** Investigation of the planet — its geography, geology, atmosphere, oceans, and now its climate as a system. Highest density of interdisciplinary merges in contemporary era (climate science = chemistry + physics + atmospheric + oceanographic + biological).

**Arc:**
- **Ancient:** Greek geography (Eratosthenes); natural history including mineralogy; meteorological speculation.
- **Medieval:** Islamic geography (Al-Idrisi); Chinese earth sciences (geomancy, seismograph by Zhang Heng); medieval mineralogy.
- **Early Modern:** Scientific expeditions (Humboldt); mineralogy professionalizes; geological theories (Hutton's uniformitarianism, 1788; Werner's Neptunism); paleontology emerging.
- **Modern:** Geology institutionalizes (Lyell); meteorology; oceanography (Challenger expedition, 1872–1876); plate tectonics (mid-20th century synthesis after Wegener).
- **Contemporary:** Climate science as a merged field; earth system science; environmental science; Anthropocene framing; remote sensing.

**Key transitions:** Plate tectonics (1960s synthesis) is a classic example of a long-contested theory finally accepted; climate science as inherently cross-trunk.

**Known controversies:** Wegener's continental drift (rejected for decades, then vindicated — a `disputed_claim` case study in priority/acceptance); the contested boundary between earth science and environmental policy.

---

## Cross-trunk patterns to watch for

Once individual trunks are established, the integration phase (Weeks 33–36) adds explicit cross-trunk edges. Expected patterns:

- **Trunk 1 as universal method exporter.** `mathematized_by` and `method_imported_from` edges from Trunk 1 to Trunks 2, 3, 4, 5, 7, 9, 10.
- **Trunk 9 → Computer Science.** A `merged_with` event combining Trunks 1 and 9 around 1936–1956.
- **Trunk 3 → Trunk 4.** Molecular biology emerges from chemistry meeting life sciences (1953–1970s).
- **Trunk 5 ← Trunk 4.** Neuroscience and behavior research from biological methods into psychology.
- **Trunk 10 as interdisciplinary sink.** Climate science as merge of Trunks 3, 4, 10.
- **Trunk 8 ↔ all sciences.** Engineering both consumes and produces science.

These are first-class edges with their own `confidence` and `source_ids`. They are not bonuses — they are core to representing knowledge as a graph rather than a forest of independent trees.

### Cross-trunk *breakthrough* enablers (v1.1 — for the new `enabling_breakthrough_ids` field)

The Macro-Audit explicitly measures whether contemporary nodes acknowledge cross-trunk enabling breakthroughs (metric §6i, target >60%). Known cross-trunk enabler patterns to look for:

- **Statistical methods (Trunk 1)** → enables modern experimental psychology (T5), randomized clinical trials (T4), econometrics (T5), machine learning (T9), modern data-driven biology (T4).
- **Boolean logic + Turing machine (Trunk 9)** → enables computer science (T9 itself, with Trunk 1 also a parent), AI (T9), modern cryptography (T1).
- **Transistor / integrated circuit (Trunk 3 / Trunk 8)** → enables practical computer science (T9), modern instrument-driven science across all trunks.
- **Microscopy / electron microscopy (Trunk 3 / Trunk 8)** → enables modern biology (T4), materials science (T3+T8), early-modern cell theory (T4).
- **Spectroscopy (Trunk 3)** → enables astrophysics (T2), modern chemistry analysis, even cosmology.
- **GPU + parallel computing (Trunk 3 / Trunk 8)** → enables modern AI/ML (T9), computational genomics (T4), climate modeling (T10).
- **DNA sequencing technology (Trunk 4 / Trunk 8)** → enables modern genetics, genomics, personalized medicine (all T4), forensic anthropology (T7).

## Note on v1.1 extraction scope

As of ontology v2.0, every node extraction also produces:
- 3–10 pioneers (rows in `pioneers.csv`) — capturing the people who shaped the field.
- 2+ breakthroughs for modern/contemporary nodes (rows in `breakthroughs.csv`) — capturing the discoveries, inventions, concepts, methods, and instruments that enabled or transformed the field.
- Join rows in `pioneer_contributions.csv` and `breakthrough_dependencies.csv` linking those entities to the node.

See `chat_specific/extractor_instructions.md` v1.1 for the full extraction workflow and JSON output format.

## Trunk activation order

Per the project charter timeline:

| Weeks | Trunk(s) | Notes |
|-------|----------|-------|
| 2–12 | Trunk 3 (pilot) | Full execution of all five eras + Macro-Audit |
| 13–24 | Trunks 1, 5, 9 | Three trunks in parallel; cross-trunk edges begin |
| 25–32 | Trunks 2, 4, 6, 7, 8, 10 | Remaining six |
| 33–36 | Integration | Cross-trunk edges, global visualization, final docs |

Each trunk begins with the previous trunk's `v{N}.0` instructions (per the Instruction Evolution System). Trunk 1 begins with the v2.0 instructions produced at the end of Trunk 3.
