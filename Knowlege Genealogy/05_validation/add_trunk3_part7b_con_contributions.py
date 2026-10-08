"""
Part 7b: Contemporary pioneer contributions CONTR_195-253
Covers T3_CON_001-012 (59 entries)
"""
import csv, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '04_nodes_edges')

FIELDS = ['contribution_id','pioneer_id','node_id','contribution_type',
          'specific_contribution','key_work','date','impact_level','source_ids']

def append_rows(fname, fieldnames, rows):
    path = os.path.join(BASE, fname)
    with open(path, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        for r in rows:
            w.writerow(r)
    print(f"  + {fname}: {len(rows)} rows added")

rows = [
    # ── T3_CON_001: QFT / QED ─────────────────────────────────────────────────
    {'contribution_id':'CONTR_195','pioneer_id':'PION_200','node_id':'T3_CON_001',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Developed Feynman path-integral formulation of quantum mechanics and QED (1948); invented Feynman diagrams as systematic perturbative tool for QED calculations; renormalization programme making QED predictions finite; Nobel Physics 1965',
     'key_work':'Space-Time Approach to Quantum Electrodynamics (1949); QED: The Strange Theory of Light and Matter (1985)','date':'1948-1949','impact_level':'major','source_ids':'SRC_077'},

    {'contribution_id':'CONTR_196','pioneer_id':'PION_201','node_id':'T3_CON_001',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Independently developed QED renormalization using source theory and Green\'s function operator methods (1947-1948); calculated anomalous magnetic moment of electron to high precision; action principle formulation of quantum field theory; Nobel Physics 1965',
     'key_work':'Quantum Electrodynamics I & II (1948)','date':'1947-1948','impact_level':'major','source_ids':'SRC_077'},

    {'contribution_id':'CONTR_197','pioneer_id':'PION_202','node_id':'T3_CON_001',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Developed covariant renormalization of QED (1946-1948) independently using super-many-time formalism; renamed QED renormalization alongside Feynman and Schwinger; Nobel Physics 1965 shared',
     'key_work':'On a Relativistically Invariant Formulation of the Quantum Theory of Wave Fields (1946)','date':'1946-1948','impact_level':'major','source_ids':'SRC_077'},

    {'contribution_id':'CONTR_198','pioneer_id':'PION_203','node_id':'T3_CON_001',
     'contribution_type':'synthesis',
     'specific_contribution':'Proved mathematical equivalence of Feynman, Schwinger, and Tomonaga QED formulations (1949) unifying the three approaches into a single framework; established S-matrix perturbation theory; crucial to establishing the Standard Model foundation',
     'key_work':'The Radiation Theories of Tomonaga, Schwinger, and Feynman (1949)','date':'1949','impact_level':'major','source_ids':'SRC_077'},

    {'contribution_id':'CONTR_199','pioneer_id':'PION_204','node_id':'T3_CON_001',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Introduced strangeness quantum number (1953); developed the eightfold way particle classification (1961); proposed quarks as constituent particles (1964); QCD colour charge concept; effective field theory methods; Nobel Physics 1969',
     'key_work':'The Eightfold Way (1961); A Schematic Model of Baryons and Mesons (1964)','date':'1953-1974','impact_level':'major','source_ids':'SRC_077'},

    {'contribution_id':'CONTR_200','pioneer_id':'PION_205','node_id':'T3_CON_001',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Electroweak unification model (1967) combining electromagnetic and weak forces with spontaneous symmetry breaking and Higgs mechanism; predicted W and Z bosons; Weinberg mixing angle; Nobel Physics 1979 with Glashow and Salam',
     'key_work':'A Model of Leptons (1967)','date':'1967','impact_level':'major','source_ids':'SRC_077'},

    {'contribution_id':'CONTR_201','pioneer_id':'PION_206','node_id':'T3_CON_001',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Discovered asymptotic freedom in QCD (1973) with Politzer and Wilczek showing quark coupling decreases at high energy; made QCD a rigorous quantum field theory tractable for perturbative calculation at high energies; Nobel Physics 2004',
     'key_work':'Ultraviolet Behavior of Non-Abelian Gauge Theories (1973)','date':'1973','impact_level':'major','source_ids':'SRC_077'},

    {'contribution_id':'CONTR_202','pioneer_id':'PION_207','node_id':'T3_CON_001',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Proposed Higgs mechanism (1964) explaining how gauge bosons acquire mass through spontaneous symmetry breaking of local gauge symmetry; Higgs boson prediction confirmed by LHC (2012); Nobel Physics 2013 with Englert',
     'key_work':'Broken Symmetries and the Masses of Gauge Bosons (1964)','date':'1964','impact_level':'major','source_ids':'SRC_077'},

    # ── T3_CON_002: Condensed Matter Physics ──────────────────────────────────
    {'contribution_id':'CONTR_203','pioneer_id':'PION_208','node_id':'T3_CON_002',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Co-invented point-contact transistor with Brattain (1947) founding semiconductor electronics; co-developed BCS theory of superconductivity (1957); only double Nobel laureate in Physics (1956, 1972); surface physics of semiconductor junctions',
     'key_work':'Three-electrode circuit element utilizing semiconductor materials (Patent 1947); BCS theory paper (1957)','date':'1947-1957','impact_level':'major','source_ids':'SRC_078'},

    {'contribution_id':'CONTR_204','pioneer_id':'PION_209','node_id':'T3_CON_002',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Invented bipolar junction transistor (1948) enabling amplification; p-n junction rectification theory; Shockley-Read-Hall recombination; Shockley-Queisser photovoltaic efficiency limit (1961); founded Shockley Semiconductor founding Silicon Valley; Nobel Physics 1956',
     'key_work':'Circuit element utilizing semiconductive material (Patent 1948); Electrons and Holes in Semiconductors (1950)','date':'1948-1956','impact_level':'major','source_ids':'SRC_078'},

    {'contribution_id':'CONTR_205','pioneer_id':'PION_210','node_id':'T3_CON_002',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Anderson localization (1958): disorder causes quantum interference preventing electron diffusion, explaining insulating behaviour; More is Different (1972) establishing emergence as physics principle; magnetic exchange interactions; pseudogap in superconductors; Nobel Physics 1977',
     'key_work':'Absence of Diffusion in Certain Random Lattices (1958); More is Different (1972)','date':'1958-1972','impact_level':'major','source_ids':'SRC_078'},

    {'contribution_id':'CONTR_206','pioneer_id':'PION_211','node_id':'T3_CON_002',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Mott insulator theory: electron correlation can make normally metallic materials insulating when Hubbard U exceeds bandwidth; metal-insulator transitions; electronic structure of transition-metal compounds; disorder effects; Nobel Physics 1977',
     'key_work':'The Basis of the Electron Theory of Metals with Special Reference to the Transition Metals (1949)','date':'1949-1974','impact_level':'major','source_ids':'SRC_078'},

    {'contribution_id':'CONTR_207','pioneer_id':'PION_212','node_id':'T3_CON_002',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Identified Cooper pairs (1956): electrons near Fermi surface with opposite momentum and spin form bound pairs due to phonon-mediated attraction; mechanism foundational to BCS theory; Cooper pair binding energy sets superconducting gap',
     'key_work':'Bound Electron Pairs in a Degenerate Fermi Gas (1956)','date':'1956','impact_level':'major','source_ids':'SRC_078'},

    {'contribution_id':'CONTR_208','pioneer_id':'PION_213','node_id':'T3_CON_002',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Predicted Josephson effect (1962) as PhD student: supercurrent tunnels through insulating barrier between two superconductors; DC and AC Josephson effects; Josephson junctions enable SQUID magnetometers and superconducting qubits; Nobel Physics 1973',
     'key_work':'Possible New Effects in Superconductive Tunnelling (1962)','date':'1962','impact_level':'major','source_ids':'SRC_078'},

    {'contribution_id':'CONTR_209','pioneer_id':'PION_214','node_id':'T3_CON_002',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Discovered integer quantum Hall effect (1980): Hall resistance quantised to h/e² with extraordinary precision regardless of sample; established resistance standard; topological origin from Landau levels; Nobel Physics 1985',
     'key_work':'New Method for High-Accuracy Determination of the Fine-Structure Constant (1980)','date':'1980','impact_level':'major','source_ids':'SRC_078'},

    # ── T3_CON_003: Materials Science ─────────────────────────────────────────
    {'contribution_id':'CONTR_210','pioneer_id':'PION_222','node_id':'T3_CON_003',
     'contribution_type':'institutionalization',
     'specific_contribution':'Spearheaded creation of materials science as a unified academic discipline at MIT integrating metallurgy, ceramics, and polymers under shared physical principles; structural-properties-processing-performance framework; established first materials science departments',
     'key_work':'The Science of Engineering Materials (1964)','date':'1960-1975','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_211','pioneer_id':'PION_223','node_id':'T3_CON_003',
     'contribution_type':'synthesis',
     'specific_contribution':'History and philosophy of materials: structure-properties relationships as central theme; A History of Metallography tracing materials knowledge from antiquity; demonstrated that aesthetic and practical materials knowledge share deep principles; humanistic materials science',
     'key_work':'A History of Metallography (1960)','date':'1950-1980','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_212','pioneer_id':'PION_211','node_id':'T3_CON_003',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Electronic structure theory for transition-metal oxides and correlated materials; Mott insulator concept explaining anomalous electrical properties of many oxide materials used in functional materials; framework for materials beyond simple band theory',
     'key_work':'Metal-Insulator Transitions (1974)','date':'1960-1974','impact_level':'major','source_ids':'SRC_078'},

    {'contribution_id':'CONTR_213','pioneer_id':'PION_208','node_id':'T3_CON_003',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Semiconductor surface states theory enabling engineering of interface properties; junction physics providing theoretical basis for semiconductor device materials engineering; band-bending and work-function concepts for materials interfaces',
     'key_work':'Surface States and Rectification at a Metal Semiconductor Contact (1947)','date':'1947-1956','impact_level':'major','source_ids':'SRC_078'},

    # ── T3_CON_004: Quantum/Computational Chemistry ───────────────────────────
    {'contribution_id':'CONTR_214','pioneer_id':'PION_235','node_id':'T3_CON_004',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Developed density functional theory with Lu Jeu Sham (1965): Kohn-Sham equations replace many-electron wavefunction with electron density functional; made ab initio quantum chemistry tractable for large molecules; Nobel Chemistry 1998',
     'key_work':'Self-Consistent Equations Including Exchange and Correlation Effects (1965)','date':'1964-1965','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_215','pioneer_id':'PION_236','node_id':'T3_CON_004',
     'contribution_type':'methodological_innovation',
     'specific_contribution':'Developed Gaussian basis set methods and systematic post-Hartree-Fock approaches (MP2, CI, CCSD) enabling systematic accuracy hierarchy in computational chemistry; created Gaussian software (1970) used worldwide; Nobel Chemistry 1998',
     'key_work':'Approximate Wave Functions for Atoms and Molecules (1953); Gaussian software documentation','date':'1964-1998','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_216','pioneer_id':'PION_237','node_id':'T3_CON_004',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Developed molecular orbital theory (1928-1932) representing electrons as delocalised over entire molecule rather than localised bonds; LCAO-MO method; Mulliken population analysis; orbital symmetry; Nobel Chemistry 1966',
     'key_work':'The Assignment of Quantum Numbers for Electrons in Molecules (1928)','date':'1928-1966','impact_level':'major','source_ids':'SRC_076'},

    {'contribution_id':'CONTR_217','pioneer_id':'PION_238','node_id':'T3_CON_004',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Becke exchange functional B88 (1988) first systematically accurate GGA exchange functional; B3LYP hybrid density functional combining exact exchange with GGA correlation became most-cited functional in chemistry; modern DFT accuracy for chemistry',
     'key_work':'Density-Functional Exchange-Energy Approximation with Correct Asymptotic Behavior (1988)','date':'1988-1993','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_218','pioneer_id':'PION_249','node_id':'T3_CON_004',
     'contribution_type':'methodological_innovation',
     'specific_contribution':'Developed CHARMM molecular dynamics force field for biomolecular simulation (1983); Karplus equation relating vicinal NMR coupling constants to dihedral angle; molecular dynamics of proteins and nucleic acids; Nobel Chemistry 2013',
     'key_work':'CHARMM: A Program for Macromolecular Energy, Minimization, and Dynamics Calculations (1983)','date':'1969-1983','impact_level':'major','source_ids':'SRC_079'},

    # ── T3_CON_005: Surface Science ────────────────────────────────────────────
    {'contribution_id':'CONTR_219','pioneer_id':'PION_239','node_id':'T3_CON_005',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Elucidated molecular mechanisms of heterogeneous catalysis on solid surfaces using surface science methods; CO oxidation on platinum showing Langmuir-Hinshelwood mechanism; oscillating reaction on Pd(110); Nobel Chemistry 2007 for surface chemistry',
     'key_work':'Surface science approach to catalysis (Nobel Lecture 2007)','date':'1974-2007','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_220','pioneer_id':'PION_228','node_id':'T3_CON_005',
     'contribution_type':'instrumental_advance',
     'specific_contribution':'Co-invented scanning tunnelling microscope (1981) with Rohrer enabling direct imaging of individual atoms on surfaces; quantum tunnelling current distance dependence gives sub-angstrom vertical resolution; Nobel Physics 1986',
     'key_work':'Surface Studies by Scanning Tunneling Microscopy (1982)','date':'1981-1982','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_221','pioneer_id':'PION_229','node_id':'T3_CON_005',
     'contribution_type':'instrumental_advance',
     'specific_contribution':'Co-invented scanning tunnelling microscope (1981) enabling atomic-resolution surface imaging; first STM images of silicon 7x7 reconstruction; surface physics at atomic scale; Nobel Physics 1986 shared with Binnig',
     'key_work':'Surface Studies by Scanning Tunneling Microscopy (1982)','date':'1981-1982','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_222','pioneer_id':'PION_246','node_id':'T3_CON_005',
     'contribution_type':'instrumental_advance',
     'specific_contribution':'Developed electron spectroscopy for chemical analysis (ESCA/XPS, 1950s-60s) measuring binding energies of core electrons to identify elemental composition and chemical state of surfaces; fundamental analytical technique in surface and materials science; Nobel Physics 1981',
     'key_work':'Electron Spectroscopy for Chemical Analysis (1967)','date':'1954-1967','impact_level':'major','source_ids':'SRC_078'},

    # ── T3_CON_006: Nanotechnology ─────────────────────────────────────────────
    {'contribution_id':'CONTR_223','pioneer_id':'PION_228','node_id':'T3_CON_006',
     'contribution_type':'instrumental_advance',
     'specific_contribution':'STM invention (1981) provides capability to image and later manipulate individual atoms; subsequent development of atomic force microscope (AFM, 1986) extending atomic imaging to insulators and biological specimens; launched entire field of scanning probe microscopies',
     'key_work':'Atomic Force Microscope (1986)','date':'1981-1986','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_224','pioneer_id':'PION_229','node_id':'T3_CON_006',
     'contribution_type':'instrumental_advance',
     'specific_contribution':'STM atomic-resolution imaging (1981) enabling nanotechnology foundation; first images of silicon surface reconstruction revealing atom positions; tunnelling spectroscopy for local electronic structure; established atomic-scale characterisation as routine',
     'key_work':'Surface Studies by Scanning Tunneling Microscopy (1982)','date':'1981-1986','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_225','pioneer_id':'PION_230','node_id':'T3_CON_006',
     'contribution_type':'discovery',
     'specific_contribution':'Co-discovered C60 buckminsterfullerene (1985) with Curl and Kroto using laser vaporisation of graphite; first closed-cage carbon molecule; opened carbon nanostructure chemistry; Nobel Chemistry 1996; early nanotechnology advocate',
     'key_work':'C60: Buckminsterfullerene (1985)','date':'1985','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_226','pioneer_id':'PION_231','node_id':'T3_CON_006',
     'contribution_type':'discovery',
     'specific_contribution':'Co-discovered C60 fullerene (1985); carbon cluster research using supersonic molecular beam techniques; Noble Chemistry 1996 for fullerene discovery; contributed to understanding of carbon nanostructure formation mechanisms',
     'key_work':'C60: Buckminsterfullerene (1985)','date':'1985','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_227','pioneer_id':'PION_232','node_id':'T3_CON_006',
     'contribution_type':'discovery',
     'specific_contribution':'Co-discovered and named buckminsterfullerene C60 (1985) after Buckminster Fuller\'s geodesic domes; interstellar carbon chains research motivating experiment; fullerene chemistry as new branch of carbon science; Nobel Chemistry 1996',
     'key_work':'C60: Buckminsterfullerene (1985)','date':'1985','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_228','pioneer_id':'PION_233','node_id':'T3_CON_006',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Discovered multi-wall carbon nanotubes (1991) by electron microscopy of arc-discharge carbon soot; seminal Nature paper launched CNT research worldwide; single-wall CNTs (1993); nanotube electronic properties and applications',
     'key_work':'Helical Microtubules of Graphitic Carbon (1991)','date':'1991','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_229','pioneer_id':'PION_234','node_id':'T3_CON_006',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'First deliberate atomic manipulation: positioned 35 xenon atoms to spell IBM logo (1989) using STM tip; quantum corral from 48 iron atoms on copper surface (1993) confining electron waves; demonstrated nanotechnology as physical reality',
     'key_work':'Positioning Single Atoms with a Scanning Tunnelling Microscope (1990)','date':'1989-1993','impact_level':'major','source_ids':'SRC_080'},

    # ── T3_CON_007: Semiconductor Physics ─────────────────────────────────────
    {'contribution_id':'CONTR_230','pioneer_id':'PION_208','node_id':'T3_CON_007',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Point-contact transistor (1947) with Brattain: first working transistor amplifying electrical signal using semiconductor surface inversion layer; founded semiconductor electronics; BCS superconductor theory (1957) also shaped semiconductor band physics understanding',
     'key_work':'The Transistor, A Semi-Conductor Triode (1948)','date':'1947-1948','impact_level':'major','source_ids':'SRC_078'},

    {'contribution_id':'CONTR_231','pioneer_id':'PION_209','node_id':'T3_CON_007',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Junction transistor design (1948) more practical than point-contact version; minority carrier injection and p-n junction theory; Shockley diode equation; Shockley-Queisser detailed-balance efficiency limit for photovoltaics (1961); founded commercial semiconductor industry',
     'key_work':'Electrons and Holes in Semiconductors (1950)','date':'1948-1961','impact_level':'major','source_ids':'SRC_078'},

    {'contribution_id':'CONTR_232','pioneer_id':'PION_226','node_id':'T3_CON_007',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Proposed double heterostructure semiconductor laser (1963) and concept of quasi-electric fields in semiconductor heterostructures enabling carrier confinement; theoretical foundation for semiconductor lasers, LEDs, and modern optoelectronics; Nobel Physics 2000',
     'key_work':'A Proposed Class of Hetero-Junction Lasers (1963)','date':'1963','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_233','pioneer_id':'PION_227','node_id':'T3_CON_007',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Demonstrated first practical semiconductor heterostructure diode laser (1970) operating at room temperature; heterostructure bipolar transistors; III-V semiconductor devices; modern semiconductor laser technology for fibre optics and optical discs; Nobel Physics 2000',
     'key_work':'Double heterostructure concept and its applications in physics and technology (Nobel Lecture 2000)','date':'1963-1970','impact_level':'major','source_ids':'SRC_079'},

    # ── T3_CON_008: Polymer/Soft Matter ───────────────────────────────────────
    {'contribution_id':'CONTR_234','pioneer_id':'PION_224','node_id':'T3_CON_008',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Flory-Huggins lattice solution theory (1942) for polymer-solvent thermodynamics; excluded volume and polymer chain statistics; Flory exponent for polymer size scaling; Nobel Chemistry 1974 for fundamental achievements in physical chemistry of macromolecules',
     'key_work':'Thermodynamics of High Polymer Solutions (1942); Principles of Polymer Chemistry (1953)','date':'1942-1953','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_235','pioneer_id':'PION_225','node_id':'T3_CON_008',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Scaling concepts in polymer physics and reptation model for polymer chain dynamics in entangled melts (1971); liquid crystal physics; wetting and adhesion; introduced soft condensed matter as a coherent field; Nobel Physics 1991',
     'key_work':'Scaling Concepts in Polymer Physics (1979)','date':'1971-1979','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_236','pioneer_id':'PION_195','node_id':'T3_CON_008',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Nature of the Chemical Bond (1939) explaining polymer covalent structure through hybridisation and resonance; predicted alpha-helix and beta-sheet protein secondary structures (1951); protein hydrogen-bonding patterns; foundational for polymer structural theory',
     'key_work':'The Nature of the Chemical Bond (1939)','date':'1939-1951','impact_level':'major','source_ids':'SRC_076'},

    # ── T3_CON_009: Biochemistry/Structural Biology ───────────────────────────
    {'contribution_id':'CONTR_237','pioneer_id':'PION_249','node_id':'T3_CON_009',
     'contribution_type':'methodological_innovation',
     'specific_contribution':'Pioneered molecular dynamics simulation of biological macromolecules; CHARMM force field (1983) enabling atomic-level protein and nucleic acid dynamics; stochastic boundary conditions; Karplus equation for protein NMR structure determination; Nobel Chemistry 2013',
     'key_work':'CHARMM: A Program for Macromolecular Energy, Minimization, and Dynamics Calculations (1983)','date':'1977-1983','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_238','pioneer_id':'PION_250','node_id':'T3_CON_009',
     'contribution_type':'methodological_innovation',
     'specific_contribution':'Developed coarse-grained and multiscale molecular dynamics for proteins enabling simulation of much larger systems and longer timescales; pioneered computational protein structure modelling and folding prediction; Nobel Chemistry 2013 for multiscale methods',
     'key_work':'Computer simulation of protein folding (1975)','date':'1975-1990','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_239','pioneer_id':'PION_195','node_id':'T3_CON_009',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Proposed alpha-helix and beta-sheet as universal protein secondary structures (1951) based on hydrogen bonding and bond angles; resonance in peptide bond constraining backbone geometry; antigen-antibody complementarity concept; molecular basis of genetic disease',
     'key_work':'The Structure of Proteins: Two Hydrogen-Bonded Helical Configurations (1951)','date':'1951','impact_level':'major','source_ids':'SRC_076'},

    # ── T3_CON_010: 2D/Topological Materials ──────────────────────────────────
    {'contribution_id':'CONTR_240','pioneer_id':'PION_217','node_id':'T3_CON_010',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Co-isolated graphene using Scotch tape mechanical exfoliation (2004) with Novoselov; characterized anomalous quantum Hall effect in graphene at room temperature; ambipolar field effect; Dirac fermion physics; Nobel Physics 2010',
     'key_work':'Electric Field Effect in Atomically Thin Carbon Films (2004)','date':'2004','impact_level':'major','source_ids':'SRC_080'},

    {'contribution_id':'CONTR_241','pioneer_id':'PION_218','node_id':'T3_CON_010',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Co-isolated and characterised graphene (2004) with Geim; measured two-dimensional electron gas properties in monolayer graphene; high electron mobility and linear dispersion; extended isolation to other 2D materials (BN, MoS2); Nobel Physics 2010',
     'key_work':'Electric Field Effect in Atomically Thin Carbon Films (2004)','date':'2004','impact_level':'major','source_ids':'SRC_080'},

    {'contribution_id':'CONTR_242','pioneer_id':'PION_219','node_id':'T3_CON_010',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'TKNN topological invariant for quantum Hall states (1982) with Thouless, Kohmoto, Nightingale; proved Hall conductance is topological (Chern number); Kosterlitz-Thouless transition theory (1973) for 2D systems; Nobel Physics 2016',
     'key_work':'Quantized Hall Conductance in a Two-Dimensional Periodic Potential (1982)','date':'1973-1982','impact_level':'major','source_ids':'SRC_080'},

    {'contribution_id':'CONTR_243','pioneer_id':'PION_220','node_id':'T3_CON_010',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Haldane model (1988) showing topological band structure can arise without Landau levels or net magnetic flux; AKLT model for integer-spin chains with topological edge states; predicted quantum anomalous Hall effect; Nobel Physics 2016',
     'key_work':'Model for a Quantum Hall Effect without Landau Levels (1988)','date':'1983-1988','impact_level':'major','source_ids':'SRC_080'},

    {'contribution_id':'CONTR_244','pioneer_id':'PION_221','node_id':'T3_CON_010',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Kosterlitz-Thouless transition theory (1973) with Thouless: 2D systems undergo topological phase transition through vortex-antivortex unbinding without conventional order parameter; new class of phase transitions; Nobel Physics 2016',
     'key_work':'Ordering, Metastability and Phase Transitions in Two-Dimensional Systems (1973)','date':'1973','impact_level':'major','source_ids':'SRC_080'},

    # ── T3_CON_011: Quantum Computing ─────────────────────────────────────────
    {'contribution_id':'CONTR_245','pioneer_id':'PION_240','node_id':'T3_CON_011',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Shor\'s algorithm (1994): polynomial-time quantum algorithm for integer factoring threatening RSA cryptography; showed quantum computing offers exponential speedup over classical for specific problems; galvanised quantum computing investment worldwide',
     'key_work':'Algorithms for Quantum Computation: Discrete Logarithms and Factoring (1994)','date':'1994','impact_level':'major','source_ids':'SRC_080'},

    {'contribution_id':'CONTR_246','pioneer_id':'PION_241','node_id':'T3_CON_011',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Trapped-ion quantum computing: laser-cooled ions as qubits; quantum logic gate between ions (1995); quantum logic spectroscopy for optical clocks; demonstrated quantum teleportation and error correction in ion traps; Nobel Physics 2012',
     'key_work':'Demonstration of a Fundamental Quantum Logic Gate (1995)','date':'1995-2012','impact_level':'major','source_ids':'SRC_080'},

    {'contribution_id':'CONTR_247','pioneer_id':'PION_242','node_id':'T3_CON_011',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Quantum error correction theory showing quantum information can be protected from decoherence; coined quantum supremacy; fault-tolerant quantum computation threshold theorem; stabiliser codes; quantum information textbook; threshold theorem for scalable QC',
     'key_work':'Quantum Computing: An Introduction (1997)','date':'1994-2002','impact_level':'major','source_ids':'SRC_080'},

    {'contribution_id':'CONTR_248','pioneer_id':'PION_243','node_id':'T3_CON_011',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Bell inequality violation experiment (1982) with photon pairs from atomic cascade testing quantum entanglement; closed detection loophole; quantum erasure experiments; entanglement-based quantum cryptography; Nobel Physics 2022',
     'key_work':'Experimental Tests of Bell\'s Inequalities Using Time-Varying Analyzers (1982)','date':'1982','impact_level':'major','source_ids':'SRC_080'},

    {'contribution_id':'CONTR_249','pioneer_id':'PION_244','node_id':'T3_CON_011',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'First Bell test (1972) with CHSH inequality violating local hidden variable theories; first convincing experimental proof of quantum entanglement; established experimental quantum foundation for quantum computing and cryptography; Nobel Physics 2022',
     'key_work':'Experimental Test of Local Hidden-Variable Theories (1972)','date':'1972','impact_level':'major','source_ids':'SRC_080'},

    {'contribution_id':'CONTR_250','pioneer_id':'PION_245','node_id':'T3_CON_011',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Quantum teleportation of photon states (1997); entanglement swapping; Greenberger-Horne-Zeilinger (GHZ) multi-photon entanglement; loophole-free Bell test (2017); entanglement-based quantum key distribution; Nobel Physics 2022 for entanglement experiments',
     'key_work':'Experimental Quantum Teleportation (1997)','date':'1997-2022','impact_level':'major','source_ids':'SRC_080'},

    # ── T3_CON_012: Astrochemistry ─────────────────────────────────────────────
    {'contribution_id':'CONTR_251','pioneer_id':'PION_239','node_id':'T3_CON_012',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Surface reaction kinetics and mechanisms on solid surfaces providing the theoretical framework for interstellar grain surface chemistry; Langmuir-Hinshelwood and Eley-Rideal mechanisms applied to H2 formation on dust grains in molecular clouds',
     'key_work':'Physical Chemistry of Surfaces and its Application to Astrophysics (contributions)','date':'1986-2007','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_252','pioneer_id':'PION_235','node_id':'T3_CON_012',
     'contribution_type':'methodological_innovation',
     'specific_contribution':'DFT methods enabling computation of molecular properties (bond lengths, vibrational frequencies, rotational constants) used to predict and identify interstellar molecules by radio astronomy; ab initio quantum chemistry underpins astrochemical spectral databases',
     'key_work':'Nobel Lecture: Electronic Structure of Matter — Wave Functions and Density Functionals (1998)','date':'1964-1998','impact_level':'major','source_ids':'SRC_079'},

    {'contribution_id':'CONTR_253','pioneer_id':'PION_238','node_id':'T3_CON_012',
     'contribution_type':'methodological_innovation',
     'specific_contribution':'Hybrid density functional methods computing accurate molecular energies and spectra of astrochemically relevant species; B3LYP functional widely used to calculate rotational spectra and reaction energetics for interstellar molecule detection and network modelling',
     'key_work':'Density-Functional Exchange-Energy Approximation with Correct Asymptotic Behavior (1988)','date':'1988-2000','impact_level':'major','source_ids':'SRC_079'},
]

print("Running Part 7b: Contemporary pioneer contributions (CONTR_195-253)")
append_rows('pioneer_contributions.csv', FIELDS, rows)
print(f"Part 7b complete. {len(rows)} contributions added.")
