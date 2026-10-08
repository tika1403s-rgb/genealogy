#!/usr/bin/env python3
"""
Part 4: Add contemporary breakthroughs (BRKTH_095-BRKTH_116).
Run from project root: python3 05_validation/add_trunk3_part4_con_breakthroughs.py
"""
import csv, json, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '04_nodes_edges')

def append_rows(fname, fieldnames, rows):
    path = os.path.join(BASE, fname)
    with open(path, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        for r in rows:
            w.writerow(r)
    print(f"  + {fname}: {len(rows)} rows added")

def J(lst): return json.dumps(lst, ensure_ascii=False)

BRKTH_FIELDS = ['breakthrough_id','name','type','date_or_range','date_precision',
                'pioneers_involved','description','enabling_factors','fields_enabled',
                'fields_transformed','representative_publication_json','cascading_impact',
                'source_ids','confidence','evidence_type']

con_breakthroughs = [
  # ── CONCEPTUAL BREAKTHROUGHS (12) ─────────────────────────────────────────
  {'breakthrough_id':'BRKTH_095','name':'Quantum Electrodynamics Renormalization','type':'formalization',
   'date_or_range':'1946-1949','date_precision':'decade',
   'pioneers_involved':'Richard Feynman, Julian Schwinger, Sin-Itiro Tomonaga, Freeman Dyson',
   'description':'Complete quantum treatment of electromagnetic interaction between electrons and photons. Renormalization procedure removes ultraviolet divergences. Anomalous magnetic moment of electron calculated to 12 significant figures — most precisely confirmed prediction in physics. Three independent formulations (Feynman path integral, Schwinger operator, Tomonaga covariant) proved equivalent by Dyson. Nobel 1965.',
   'enabling_factors':'Quantum mechanics (BRKTH_076); special relativity (BRKTH_071); Dirac equation (BRKTH_079); precision electron magnetic moment measurements',
   'fields_enabled':'T3_CON_001','fields_transformed':'T3_MOD_009',
   'representative_publication_json':J([{"title":"Space-Time Approach to Quantum Electrodynamics","author":"Feynman, R.P.","date":"1949","note":"Path-integral QED formulation"},{"title":"The Radiation Theories of Tomonaga, Schwinger, and Feynman","author":"Dyson, F.J.","date":"1949","note":"Proof of equivalence of three formulations"}]),
   'cascading_impact':'Template for Standard Model gauge theories; Feynman diagrams ubiquitous in physics; precision tests of quantum mechanics; renormalization group methods; electroweak and QCD theories follow QED template',
   'source_ids':'SRC_099','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_096','name':'Transistor Invention','type':'invention',
   'date_or_range':'1947','date_precision':'year',
   'pioneers_involved':'John Bardeen, Walter Brattain, William Shockley',
   'description':'Point-contact transistor (Bardeen and Brattain, Bell Labs, December 16, 1947): semiconductor device that amplifies and switches electrical signals. Junction transistor (Shockley, 1949): improved design. Based on quantum mechanics of semiconductor p-n junctions. Nobel Physics 1956. Most consequential technological invention of 20th century.',
   'enabling_factors':'Quantum mechanics of semiconductors (band theory); purified germanium; quantum mechanics (BRKTH_076); World War II materials research',
   'fields_enabled':'T3_CON_007','fields_transformed':'T3_CON_002',
   'representative_publication_json':J([{"title":"The Transistor, A Semi-Conductor Triode","author":"Bardeen, J. and Brattain, W.H.","date":"1948","note":"Transistor announcement paper, Physical Review"}]),
   'cascading_impact':'Computing civilization enabled; semiconductor industry ($500B+/year); integrated circuit (1958); Moore\'s Law; entire digital world; CON_007 (semiconductor physics) as field founded on this',
   'source_ids':'SRC_093','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_097','name':'BCS Theory of Superconductivity','type':'concept',
   'date_or_range':'1957','date_precision':'year',
   'pioneers_involved':'John Bardeen, Leon Cooper, John Robert Schrieffer',
   'description':'Phonon-mediated Cooper pairing: electrons near Fermi surface attract each other via lattice phonons and form Cooper pairs (bound state with zero total momentum and spin). All Cooper pairs condense into a single macroscopic quantum state with phase coherence. Explains Meissner effect, zero resistance, isotope effect, specific heat anomaly. Nobel 1972.',
   'enabling_factors':'Cooper pairs (Cooper, 1956); quantum statistical mechanics (BRKTH_069); second quantization; many-body quantum theory',
   'fields_enabled':'T3_CON_002','fields_transformed':'T3_CON_002',
   'representative_publication_json':J([{"title":"Theory of Superconductivity","author":"Bardeen, J., Cooper, L.N. and Schrieffer, J.R.","date":"1957","note":"BCS theory, Physical Review 108"}]),
   'cascading_impact':'Most successful many-body quantum theory; Cooper pairing mechanism in nuclear physics; high-Tc superconductivity debate reference; quantum computing via Josephson junctions; MRI superconducting magnets',
   'source_ids':'SRC_091','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_098','name':'More is Different — Emergence Principle','type':'concept',
   'date_or_range':'1972','date_precision':'year',
   'pioneers_involved':'Philip Anderson',
   'description':'Anderson\'s seminal essay "More is Different" (Science, 1972): at each level of complexity entirely new laws can emerge that cannot be derived from lower-level physics. Reductionism is insufficient — emergent properties require their own principles. Justified condensed matter physics as intellectually independent from particle physics.',
   'enabling_factors':'Condensed matter physics maturation; quantum field theory methods applied to many-body problems; superconductivity as example of emergence',
   'fields_enabled':'T3_CON_002','fields_transformed':'T3_CON_002',
   'representative_publication_json':J([{"title":"More is Different","author":"Anderson, P.W.","date":"1972","note":"Science 177: 393-396, philosophical manifesto of condensed matter"}]),
   'cascading_impact':'Philosophical framework for all of condensed matter physics; complexity science emergence concept; justification for materials science as independent field; counterargument to string theory reductionism; biology and social science emergence debates',
   'source_ids':'SRC_091','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_099','name':'Density Functional Theory (DFT)','type':'formalization',
   'date_or_range':'1964-1965','date_precision':'year',
   'pioneers_involved':'Walter Kohn, Pierre Hohenberg, Lu Jeu Sham',
   'description':'Hohenberg-Kohn theorem (1964): ground state of any many-electron system uniquely determined by electron density n(r) alone — reduces 3N-dimensional many-electron wave function to 3-dimensional density. Kohn-Sham scheme (1965): practical computational method using fictitious non-interacting electrons with same density as real system. Nobel Chemistry 1998.',
   'enabling_factors':'Quantum mechanics (BRKTH_076); Thomas-Fermi model (1927); Hartree-Fock method; computers enabling numerical solution',
   'fields_enabled':'T3_CON_004','fields_transformed':'T3_MOD_009',
   'representative_publication_json':J([{"title":"Inhomogeneous Electron Gas","author":"Hohenberg, P. and Kohn, W.","date":"1964","note":"Hohenberg-Kohn theorem, Physical Review 136"},{"title":"Self-Consistent Equations Including Exchange and Correlation Effects","author":"Kohn, W. and Sham, L.J.","date":"1965","note":"Kohn-Sham DFT, Physical Review 140"}]),
   'cascading_impact':'Most used quantum mechanical method in chemistry and materials science; materials discovery by computation; drug design; surface catalysis; B3LYP functional (most cited paper ever); Nobel 1998 recognized maturity',
   'source_ids':'SRC_097, SRC_098','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_100','name':'Standard Model of Particle Physics Completion','type':'formalization',
   'date_or_range':'1967-1974','date_precision':'decade',
   'pioneers_involved':'Sheldon Glashow, Abdus Salam, Steven Weinberg, Murray Gell-Mann, David Gross, Frank Wilczek, David Politzer',
   'description':'Electroweak unification (Glashow-Salam-Weinberg 1961-1968): electromagnetic and weak forces unified via SU(2)×U(1) gauge theory. QCD (1973): SU(3) gauge theory for strong force with quarks and gluons; asymptotic freedom (Gross-Politzer-Wilczek). Standard Model describes all known particles and three of four fundamental forces. Higgs mechanism provides mass generation.',
   'enabling_factors':'QED renormalization (BRKTH_095); quark model (Gell-Mann 1964); Yang-Mills gauge theory (1954); t Hooft proof of electroweak renormalizability (1971)',
   'fields_enabled':'T3_CON_001','fields_transformed':'T3_CON_001',
   'representative_publication_json':J([{"title":"A Model of Leptons","author":"Weinberg, S.","date":"1967","note":"Electroweak unification, Physical Review Letters"},{"title":"Ultraviolet Behavior of Non-Abelian Gauge Theories","author":"Gross, D.J. and Wilczek, F.","date":"1973","note":"QCD asymptotic freedom"}]),
   'cascading_impact':'Most comprehensive physical theory; all predicted particles confirmed (W, Z bosons 1983; top quark 1995; Higgs boson 2012); LHC built to test it; effective field theory methods spread to condensed matter',
   'source_ids':'SRC_100','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_101','name':'Renormalization Group for Critical Phenomena','type':'formalization',
   'date_or_range':'1971-1974','date_precision':'decade',
   'pioneers_involved':'Kenneth Wilson, Leo Kadanoff, Michael Fisher',
   'description':'Wilson\'s renormalization group: systematic procedure for integrating out short-wavelength fluctuations to get effective theory at longer wavelengths. Explains universality — why different materials show same critical exponents near phase transitions (same symmetry and dimensionality = same universality class). Nobel Physics 1982.',
   'enabling_factors':'Kadanoff block spin picture (1966); QED renormalization methods; critical phenomena data (specific heat exponents, correlation lengths)',
   'fields_enabled':'T3_CON_002','fields_transformed':'T3_MOD_011',
   'representative_publication_json':J([{"title":"Renormalization Group and Critical Phenomena I, II","author":"Wilson, K.G.","date":"1971","note":"Physical Review B 4, foundational RG papers"}]),
   'cascading_impact':'Universality classes concept; RG methods spread from particle physics to condensed matter; lattice QCD (Wilson); effective field theories; modern condensed matter phase transition theory; turbulence',
   'source_ids':'SRC_091','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_102','name':'High-Temperature Superconductivity (Cuprates)','type':'discovery',
   'date_or_range':'1986','date_precision':'year',
   'pioneers_involved':'Johannes Georg Bednorz, K. Alex Müller',
   'description':'La-Ba-Cu-O ceramic superconducts at 30 K (1986, IBM Zurich) — well above previous record of 23 K. Quickly extended to 90 K (YBCO, 1987) by other groups — above liquid nitrogen boiling point (77 K). Nobel Physics 1987 (19 months after discovery — fastest Nobel ever). Mechanism still unresolved after 40 years.',
   'enabling_factors':'BCS theory (BRKTH_097) as reference; perovskite oxide expertise; Jahn-Teller effect insight; low-temperature measurement equipment',
   'fields_enabled':'T3_CON_002','fields_transformed':'T3_CON_002',
   'representative_publication_json':J([{"title":"Possible High Tc Superconductivity in the Ba-La-Cu-O System","author":"Bednorz, J.G. and Müller, K.A.","date":"1986","note":"Zeitschrift für Physik B 64, high-Tc discovery"}]),
   'cascading_impact':'Reopened superconductivity research; thousands of groups worldwide; cuprate mechanism unsolved (active frontier); potential for room-temperature superconductors; MRI magnets use superconductors',
   'source_ids':'SRC_091','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_103','name':'Quantum Hall Effects','type':'discovery',
   'date_or_range':'1980-1983','date_precision':'year',
   'pioneers_involved':'Klaus von Klitzing, Horst Störmer, Daniel Tsui, Robert Laughlin',
   'description':'Integer QHE (von Klitzing, 1980): Hall resistance precisely quantized as h/e²n regardless of sample geometry or purity. Nobel 1985. Fractional QHE (Tsui and Störmer, 1982): fractional plateaus; Laughlin (1983) explained by fractionally charged quasiparticle excitations. Nobel 1998. QHE now defines SI resistance standard.',
   'enabling_factors':'2D electron gas in GaAs heterostructures; high magnetic fields; millikelvin temperatures; high-purity semiconductors',
   'fields_enabled':'T3_CON_002','fields_transformed':'T3_CON_002',
   'representative_publication_json':J([{"title":"New Method for High-Accuracy Determination of the Fine-Structure Constant","author":"von Klitzing, K., Dorda, G. and Pepper, M.","date":"1980","note":"Integer QHE discovery, Physical Review Letters 45"},{"title":"Anomalous Quantum Hall Effect","author":"Laughlin, R.B.","date":"1983","note":"FQHE explanation, Physical Review Letters"}]),
   'cascading_impact':'Topological insulators conceptual precursor; SI resistance standard; fractional charges real; topological phases of matter as field; non-Abelian anyons for quantum computing',
   'source_ids':'SRC_093','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_104','name':'Topological Phases of Matter Theory','type':'concept',
   'date_or_range':'1972-2010','date_precision':'decade',
   'pioneers_involved':'David Thouless, J. Michael Kosterlitz, Duncan Haldane, Charles Kane, Eugene Mele',
   'description':'Kosterlitz-Thouless topological phase transition (1972-1973): 2D systems undergo transitions via vortex unbinding — no symmetry breaking. TKNN topological invariant (Thouless et al., 1982): QHE explained by Chern number of occupied bands. Haldane model (1988): topological insulator concept. Z2 topological insulators (Kane-Mele, 2005): bulk insulating but topologically protected conducting surface states. Nobel Physics 2016.',
   'enabling_factors':'QHE experiments (BRKTH_103); Berry phase theory; topology in mathematics; many-body quantum theory',
   'fields_enabled':'T3_CON_002, T3_CON_010','fields_transformed':'T3_CON_002',
   'representative_publication_json':J([{"title":"Ordering, Metastability and Phase Transitions in Two-Dimensional Systems","author":"Kosterlitz, J.M. and Thouless, D.J.","date":"1973","note":"KT transition, Journal of Physics C"},{"title":"Quantum Spin Hall Effect and Topological Phase Transition in HgTe Quantum Wells","author":"Kane, C.L. and Mele, E.J.","date":"2005","note":"Topological insulator prediction"}]),
   'cascading_impact':'Topological insulators and semimetals new material class; Majorana fermions for topological quantum computing; bulk-boundary correspondence as organizing principle; thousands of predicted topological materials',
   'source_ids':'SRC_093','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_105','name':'Shor\'s Quantum Factoring Algorithm','type':'concept',
   'date_or_range':'1994','date_precision':'year',
   'pioneers_involved':'Peter Shor',
   'description':'Quantum algorithm for integer factoring with O(n³) quantum operations — exponentially faster than best known classical algorithm O(exp(n^1/3)). Uses quantum Fourier transform to find period of modular arithmetic function. Threatens RSA public-key cryptography. Also: Shor\'s quantum error correction code (1995).',
   'enabling_factors':'Quantum mechanics (BRKTH_076); Feynman quantum computing concept (1982); Deutsch\'s first quantum algorithm (1985); quantum Fourier transform',
   'fields_enabled':'T3_CON_011','fields_transformed':'T3_CON_011',
   'representative_publication_json':J([{"title":"Algorithms for Quantum Computation: Discrete Logarithms and Factoring","author":"Shor, P.W.","date":"1994","note":"Proceedings 35th Annual IEEE FOCS"}]),
   'cascading_impact':'NIST post-quantum cryptography competition (2022); National Quantum Initiative Act (2018); massive investment in quantum computing; quantum error correction as research area; quantum supremacy race',
   'source_ids':'SRC_103, SRC_104','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_106','name':'Bell Inequality Violation Tests (Quantum Entanglement Confirmed)','type':'experimental_demonstration',
   'date_or_range':'1972-2022','date_precision':'decade',
   'pioneers_involved':'John Clauser, Alain Aspect, Anton Zeilinger, Nicolas Gisin',
   'description':'Clauser and Freedman (1972): first experimental Bell test — photon correlations violate CHSH inequality by 6σ. Aspect (1982): closed detector and locality loopholes simultaneously using fast switching. Hensen et al. (2015): first loophole-free Bell test. Nobel Physics 2022 (Aspect, Clauser, Zeilinger). Quantum mechanics is genuinely non-local.',
   'enabling_factors':'Bell inequality (theoretical, 1964); quantum optics photon source technology; coincidence counting electronics; entangled photon pair production',
   'fields_enabled':'T3_CON_011','fields_transformed':'T3_CON_001',
   'representative_publication_json':J([{"title":"Experimental Test of Local Hidden-Variable Theories","author":"Clauser, J.F. and Freedman, S.J.","date":"1972","note":"First Bell test, Physical Review Letters"},{"title":"Experimental Tests of Bell Inequalities Using Time-Varying Analyzers","author":"Aspect, A. et al.","date":"1982","note":"Definitive Bell test"}]),
   'cascading_impact':'Quantum cryptography protocols (BB84, E91); quantum teleportation; quantum networks; quantum key distribution systems deployed commercially; confirms quantum non-locality as real',
   'source_ids':'SRC_103','confidence':'A','evidence_type':'E2'},

  # ── TECHNOLOGICAL/INSTRUMENTAL BREAKTHROUGHS (10) ─────────────────────────
  {'breakthrough_id':'BRKTH_107','name':'Laser','type':'invention',
   'date_or_range':'1960','date_precision':'year',
   'pioneers_involved':'Theodore Maiman, Charles Townes, Nikolay Basov, Alexander Prokhorov',
   'description':'Maiman (May 1960): first working laser using ruby rod — coherent, monochromatic, intense red light via stimulated emission. Townes et al. developed MASER (microwave laser) principle (1953-1954). Nobel Physics 1964 (Townes, Basov, Prokhorov) for quantum electronics and laser principles.',
   'enabling_factors':'Quantum mechanics stimulated emission theory (Einstein 1917); microwave engineering (MASER 1953); optical pumping; synthetic ruby rods',
   'fields_enabled':'T3_CON_002, T3_CON_005','fields_transformed':'T3_MOD_006',
   'representative_publication_json':J([{"title":"Stimulated Optical Radiation in Ruby","author":"Maiman, T.H.","date":"1960","note":"First laser demonstration, Nature 187"}]),
   'cascading_impact':'Fiber optic communications; laser surgery; semiconductor industry lithography; CD/DVD/Blu-ray; spectroscopy precision; gravitational wave detection (LIGO); laser cooling (Nobel 1997); quantum computing',
   'source_ids':'SRC_092','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_108','name':'Nuclear Magnetic Resonance (NMR) Spectroscopy','type':'instrument',
   'date_or_range':'1946-1950s','date_precision':'decade',
   'pioneers_involved':'Felix Bloch, Edward Purcell, Richard Ernst, Kurt Wüthrich',
   'description':'Bloch and Purcell (1946): nuclei in magnetic field absorb/emit radiofrequency at characteristic Larmor frequency; Nobel Physics 1952. Chemical shift and coupling constants (1950s): NMR resolves molecular structure. 2D NMR (Ernst, Nobel Chemistry 1991). Protein structure by NMR (Wüthrich, Nobel Chemistry 2002). MRI clinical application.',
   'enabling_factors':'Quantum mechanics nuclear spin; radiofrequency electronics (from radar); superconducting magnets; computer data processing',
   'fields_enabled':'T3_CON_004, T3_CON_009','fields_transformed':'T3_MOD_002',
   'representative_publication_json':J([{"title":"Nuclear Induction","author":"Bloch, F.","date":"1946","note":"NMR discovery, Physical Review"},{"title":"Two-dimensional Fourier transform spectroscopy","author":"Aue, W.P., Bartholdi, E. and Ernst, R.R.","date":"1976","note":"2D NMR foundation"}]),
   'cascading_impact':'Most powerful structure determination tool in chemistry; protein solution structures (Trunk 5); MRI diagnostic imaging saves millions of lives; reaction monitoring; quality control; metabolomics',
   'source_ids':'SRC_098','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_109','name':'Scanning Tunneling Microscope (STM) and Atomic Force Microscope (AFM)','type':'instrument',
   'date_or_range':'1981-1986','date_precision':'decade',
   'pioneers_involved':'Gerd Binnig, Heinrich Rohrer, Christoph Gerber, Calvin Quate',
   'description':'STM (Binnig and Rohrer, IBM Zurich, 1981): quantum tunneling current between metallic tip and conducting surface depends exponentially on distance; atomic-resolution surface imaging. Nobel Physics 1986. AFM (Binnig, Quate, Gerber, 1986): measures tip-surface forces; images insulators; ubiquitous in materials and biology.',
   'enabling_factors':'Quantum tunneling theory (from quantum mechanics); piezoelectric actuators; vibration isolation; vacuum electronics',
   'fields_enabled':'T3_CON_005, T3_CON_006','fields_transformed':'T3_CON_005',
   'representative_publication_json':J([{"title":"Surface Studies by Scanning Tunneling Microscopy","author":"Binnig, G. and Rohrer, H.","date":"1982","note":"STM invention, Physical Review Letters 49"},{"title":"Atomic Force Microscope","author":"Binnig, G., Quate, C.F. and Gerber, C.","date":"1986","note":"AFM invention, Physical Review Letters"}]),
   'cascading_impact':'Nanotechnology enabled; single-atom manipulation (Eigler 1989); surface science revolution; biological imaging by AFM; DNA manipulation; semiconductor process control; scanning probe lithography',
   'source_ids':'SRC_095','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_110','name':'Carbon Nanostructures (Fullerenes, Nanotubes, Graphene)','type':'discovery',
   'date_or_range':'1985-2004','date_precision':'decade',
   'pioneers_involved':'Richard Smalley, Robert Curl, Harold Kroto, Sumio Iijima, Andre Geim, Konstantin Novoselov',
   'description':'C60 buckminsterfullerene (Curl, Kroto, Smalley, 1985; Nobel Chemistry 1996): soccer-ball carbon cage. Carbon nanotubes (Iijima, NEC, 1991): rolled graphene cylinders with extraordinary mechanical and electronic properties. Graphene (Geim and Novoselov, Manchester, 2004; Nobel Physics 2010): single atom thick carbon sheet, strongest material known.',
   'enabling_factors':'STM (BRKTH_109); laser ablation spectroscopy; high-resolution electron microscopy; scotch tape exfoliation method',
   'fields_enabled':'T3_CON_006, T3_CON_010','fields_transformed':'T3_CON_006',
   'representative_publication_json':J([{"title":"C60: Buckminsterfullerene","author":"Kroto, H.W. et al.","date":"1985","note":"Nature 318"},{"title":"Helical Microtubules of Graphitic Carbon","author":"Iijima, S.","date":"1991","note":"Carbon nanotubes, Nature 354"},{"title":"Electric Field Effect in Atomically Thin Carbon Films","author":"Novoselov, K.S. et al.","date":"2004","note":"Graphene isolation, Science"}]),
   'cascading_impact':'Carbon nanomaterials as technology platform; 2D materials field opened; van der Waals heterostructures; magic-angle graphene superconductivity (2018); composites; semiconductor device at 2D limit',
   'source_ids':'SRC_095','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_111','name':'Silicon Integrated Circuit and Microprocessor','type':'invention',
   'date_or_range':'1958-1971','date_precision':'decade',
   'pioneers_involved':'Jack Kilby, Robert Noyce, Gordon Moore',
   'description':'Kilby (Texas Instruments, 1958) and Noyce (Fairchild Semiconductor, 1959) independently invented the integrated circuit on silicon. Intel 4004 (1971): first single-chip microprocessor. Moore\'s Law (1965): transistor count doubles every ~2 years. Nobel Physics 2000 (Kilby; Noyce died 1990).',
   'enabling_factors':'Transistor (BRKTH_096); silicon semiconductor manufacturing; photolithography; wire bonding',
   'fields_enabled':'T3_CON_007','fields_transformed':'T3_CON_007',
   'representative_publication_json':J([{"title":"Miniaturized Electronic Circuits (patent application)","author":"Kilby, J.S.","date":"1959","note":"Integrated circuit patent, Texas Instruments"}]),
   'cascading_impact':'Computing civilization; $500B semiconductor industry; Moore\'s Law scaling; internet infrastructure; AI hardware; everything digital',
   'source_ids':'SRC_093, SRC_094','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_112','name':'Cryo-Electron Microscopy (Cryo-EM)','type':'instrument',
   'date_or_range':'1975-2013','date_precision':'decade',
   'pioneers_involved':'Richard Henderson, Jacques Dubochet, Joachim Frank',
   'description':'Dubochet (vitrification, 1980s): flash-freeze biological samples in vitreous ice preserving native structure. Frank (image processing, 1970s-1990s): single-particle reconstruction algorithms. Henderson (1990): first near-atomic resolution membrane protein structure by EM. Revolution 2013+: direct electron detectors + improved algorithms. Nobel Chemistry 2017.',
   'enabling_factors':'Electron microscopy; cryogenic cooling; image processing computers; crystallography experience',
   'fields_enabled':'T3_CON_009','fields_transformed':'T3_MOD_002',
   'representative_publication_json':J([{"title":"Model for the Structure of Bacteriorhodopsin Based on High-Resolution Electron Cryo-Microscopy","author":"Henderson, R. et al.","date":"1990","note":"First near-atomic cryo-EM structure"},{"title":"Cryo-EM and the Electron Microscope Revolution","author":"Frank, J.","date":"2017","note":"Nobel lecture"}]),
   'cascading_impact':'Structural biology revolution (any protein structure without crystals); COVID vaccine development (spike protein structure 2020); drug design; viruses imaged in native state; transforming all of biology',
   'source_ids':'SRC_098','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_113','name':'X-ray Protein Crystallography Maturation','type':'method',
   'date_or_range':'1953-1970s','date_precision':'decade',
   'pioneers_involved':'Max Perutz, John Kendrew, Dorothy Hodgkin, Francis Crick, Rosalind Franklin',
   'description':'X-ray crystallography applied to biological macromolecules. DNA double helix (Franklin\'s X-ray data, Watson-Crick model, 1953). Myoglobin first protein structure (Kendrew, 1957). Hemoglobin (Perutz, 1959). Nobel Chemistry 1962 (Perutz, Kendrew). Led to structural biology and all protein crystallography.',
   'enabling_factors':'X-ray crystallography methods (BRKTH_088); computer programs for structure factor calculation; crystalline proteins and DNA; isomorphous replacement method',
   'fields_enabled':'T3_CON_009','fields_transformed':'T3_MOD_002',
   'representative_publication_json':J([{"title":"A Three-Dimensional Model of the Myoglobin Molecule","author":"Kendrew, J.C. et al.","date":"1958","note":"First protein structure, Nature"},{"title":"Structure of Haemoglobin","author":"Perutz, M.F. et al.","date":"1960","note":"Hemoglobin structure, Nature"}]),
   'cascading_impact':'Structural biology as field; drug design (structure-based); DNA structure (Trunk 5 biology); enzyme mechanisms; thousands of protein structures in PDB; Trunk 3 methods enabling Trunk 5',
   'source_ids':'SRC_098','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_114','name':'Fiber Optic Communications and Blue LED','type':'invention',
   'date_or_range':'1966-2014','date_precision':'decade',
   'pioneers_involved':'Charles Kao, Corning Glass researchers, Shuji Nakamura, Hiroshi Amano, Isamu Akasaki',
   'description':'Kao and Hockham (1966): theoretical basis for low-loss glass fiber optical communication; Nobel Physics 2009. Corning (1970): first practical low-loss glass fiber (20 dB/km). Blue LED (Akasaki, Amano, Nakamura, 1990s): GaN-based blue and UV LEDs enabling white light; Nobel Physics 2014. Fiber optic internet + LED lighting revolutions.',
   'enabling_factors':'Laser (BRKTH_107); quantum mechanics of semiconductor band gaps; GaN crystal growth; optical waveguide theory',
   'fields_enabled':'T3_CON_007','fields_transformed':'T3_CON_007',
   'representative_publication_json':J([{"title":"Dielectric-fibre surface waveguides for optical frequencies","author":"Kao, C.K. and Hockham, G.A.","date":"1966","note":"Fiber optic communications basis, Proceedings IEE"},{"title":"High-brightness InGaN/AlGaN double-heterostructure blue-green-light-emitting diodes","author":"Nakamura, S. et al.","date":"1994","note":"Blue LED, Applied Physics Letters"}]),
   'cascading_impact':'Internet infrastructure (fiber optic cables); LED lighting revolution (~20% of global electricity goes to lighting); optical computing prospects; photonic circuits; solar cell efficiency',
   'source_ids':'SRC_092, SRC_094','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_115','name':'Laser Cooling and Bose-Einstein Condensate','type':'experimental_demonstration',
   'date_or_range':'1985-1995','date_precision':'decade',
   'pioneers_involved':'Steven Chu, Claude Cohen-Tannoudji, William Phillips, Eric Cornell, Carl Wieman, Wolfgang Ketterle',
   'description':'Laser cooling (Chu, Cohen-Tannoudji, Phillips): photon pressure slows atoms to near absolute zero; Nobel 1997. Bose-Einstein condensate (Cornell, Wieman, Ketterle, 1995): rubidium and sodium atoms cooled to 170 nK condense into single quantum state — new state of matter predicted by Einstein (1924-1925); Nobel 2001.',
   'enabling_factors':'Laser (BRKTH_107); quantum mechanics of atomic energy levels; magneto-optical trap; ultrahigh vacuum',
   'fields_enabled':'T3_CON_002, T3_CON_011','fields_transformed':'T3_CON_002',
   'representative_publication_json':J([{"title":"Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor","author":"Anderson, M.H. et al.","date":"1995","note":"First BEC, Science 269"},{"title":"Nobel lecture: Laser cooling and trapping of neutral atoms","author":"Chu, S.","date":"1997","note":"Laser cooling Nobel lecture"}]),
   'cascading_impact':'Optical atomic clocks (most precise timekeeping); quantum simulation with cold atoms; quantum computing (neutral atom platform); gravitational wave detection precision; quantum metrology; GPS correction',
   'source_ids':'SRC_092','confidence':'A','evidence_type':'E2'},

  {'breakthrough_id':'BRKTH_116','name':'Quantum Error Correction Below Threshold (Willow)','type':'experimental_demonstration',
   'date_or_range':'2024','date_precision':'year',
   'pioneers_involved':'Google Quantum AI team, Hartmut Neven, Julian Kelly',
   'description':'Google\'s 105-qubit Willow superconducting quantum chip demonstrated exponential decrease in logical error rate with increasing code size — solving a key error correction challenge posed by Shor (1995). Published Nature (December 2024). First demonstration that fault-tolerant quantum computing is physically achievable via surface code error correction.',
   'enabling_factors':'Josephson junction qubits (BRKTH_097 lineage); quantum error correction theory (Shor 1995); cryogenic engineering; 2D surface code theoretical framework',
   'fields_enabled':'T3_CON_011','fields_transformed':'T3_CON_011',
   'representative_publication_json':J([{"title":"Quantum error correction below the surface code threshold","author":"Google Quantum AI","date":"2024","note":"Nature, December 2024; Willow chip result"}]),
   'cascading_impact':'Demonstrates fault-tolerant quantum computing is physically realizable; logical qubit quality improvement with scale; path to cryptographically relevant quantum computers; superconducting platform as leading hardware approach',
   'source_ids':'SRC_104','confidence':'A','evidence_type':'E2'},
]

print("Running Part 4: Contemporary Breakthroughs")
append_rows('breakthroughs.csv', BRKTH_FIELDS, con_breakthroughs)
print(f"Part 4 complete. {len(con_breakthroughs)} contemporary breakthroughs added (BRKTH_095-BRKTH_116).")
