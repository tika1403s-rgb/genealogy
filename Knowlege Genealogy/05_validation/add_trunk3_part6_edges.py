#!/usr/bin/env python3
"""
Part 6: Add edges (T3_E_065-T3_E_103, 39 edges).
Run from project root: python3 05_validation/add_trunk3_part6_edges.py
"""
import csv, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '04_nodes_edges')

def append_rows(fname, fieldnames, rows):
    path = os.path.join(BASE, fname)
    with open(path, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        for r in rows:
            w.writerow(r)
    print(f"  + {fname}: {len(rows)} rows added")

EDGE_FIELDS = ['edge_id','from_node','to_node','relation_type','date_start','date_end',
               'date_precision','explanation','pioneers_involved','source_ids',
               'confidence','evidence_type']

edges = [
  # ── MODERN SPLITS FROM EMD ─────────────────────────────────────────────────
  {'edge_id':'T3_E_065','from_node':'T3_MOD_001','to_node':'T3_EMD_005',
   'relation_type':'split_from','date_start':'1828','date_end':'1865','date_precision':'year',
   'explanation':'Organic chemistry split from unified chemistry (Lavoisier tradition) following Wöhler urea synthesis (1828) defeating vitalism and Kekulé structure theory (1858-1865). German dye industry accelerated institutionalization.',
   'pioneers_involved':'Friedrich Wöhler, Justus von Liebig, August Kekulé',
   'source_ids':'SRC_085, SRC_076','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_066','from_node':'T3_MOD_002','to_node':'T3_EMD_005',
   'relation_type':'split_from','date_start':'1840','date_end':'1900','date_precision':'decade',
   'explanation':'Analytical chemistry consolidated as service specialty within chemistry from 1840s, driven by Fresenius systematic analysis methods, spectroscopy (1860), and increasing need for quantitative characterization.',
   'pioneers_involved':'Carl Remigius Fresenius, Gustav Kirchhoff, Robert Bunsen',
   'source_ids':'SRC_076','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_067','from_node':'T3_MOD_003','to_node':'T3_EMD_005',
   'relation_type':'split_from','date_start':'1860','date_end':'1900','date_precision':'decade',
   'explanation':'Inorganic chemistry emerged as residual category after organic chemistry split (c.1860s); unified by periodic table (1869) and coordination chemistry (Werner, 1890s-1913) providing theoretical coherence.',
   'pioneers_involved':'Dmitri Mendeleev, Alfred Werner',
   'source_ids':'SRC_076','confidence':'A','evidence_type':'E4'},

  # ── PHYSICAL CHEMISTRY MERGE ───────────────────────────────────────────────
  {'edge_id':'T3_E_068','from_node':'T3_MOD_004','to_node':'T3_EMD_005',
   'relation_type':'merged_with','date_start':'1887','date_end':'1910','date_precision':'year',
   'explanation':'Physical chemistry emerged from the merge of chemistry (EMD_005 tradition) with thermodynamics. Ostwald, Van\'t Hoff, Arrhenius applied physics methods to chemical problems; journal ZfPC (1887) institutionalized the merge.',
   'pioneers_involved':'Wilhelm Ostwald, Jacobus van\'t Hoff, Svante Arrhenius',
   'source_ids':'SRC_075','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_069','from_node':'T3_MOD_004','to_node':'T3_MOD_005',
   'relation_type':'merged_with','date_start':'1876','date_end':'1910','date_precision':'year',
   'explanation':'Physical chemistry incorporated thermodynamics (MOD_005) as its theoretical physics component. Gibbs free energy, entropy, and phase equilibrium from thermodynamics became central to physical chemistry.',
   'pioneers_involved':'J. Willard Gibbs, Walther Nernst, Gilbert N. Lewis',
   'source_ids':'SRC_075','confidence':'A','evidence_type':'E4'},

  # ── PHYSICS SPLITS FROM EMD ────────────────────────────────────────────────
  {'edge_id':'T3_E_070','from_node':'T3_MOD_005','to_node':'T3_EMD_003',
   'relation_type':'emerged_from','date_start':'1824','date_end':'1865','date_precision':'year',
   'explanation':'Thermodynamics emerged from mathematical physics (Newtonian mechanics tradition, EMD_003) applied to heat engines and heat phenomena. Carnot (1824), Clausius (1850-1865), Kelvin established thermodynamics as physics specialty.',
   'pioneers_involved':'Sadi Carnot, Rudolf Clausius, William Thomson (Lord Kelvin)',
   'source_ids':'SRC_081','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_071','from_node':'T3_MOD_006','to_node':'T3_EMD_008',
   'relation_type':'emerged_from','date_start':'1820','date_end':'1887','date_precision':'decade',
   'explanation':'Electromagnetism emerged from and unified the prior electricity and magnetism studies (EMD_008) through Maxwell\'s equations (1864-1873) and Hertz\'s experimental confirmation (1887).',
   'pioneers_involved':'Michael Faraday, James Clerk Maxwell, Heinrich Hertz',
   'source_ids':'SRC_083','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_072','from_node':'T3_MOD_007','to_node':'T3_EMD_007',
   'relation_type':'emerged_from','date_start':'1859','date_end':'1890','date_precision':'decade',
   'explanation':'Modern optics and spectroscopy emerged from classical optics (EMD_007) with addition of spectroscopic methods (Kirchhoff-Bunsen 1860) and precision interferometry (Michelson 1880s). EM theory provided wave basis.',
   'pioneers_involved':'Gustav Kirchhoff, Robert Bunsen, Albert A. Michelson',
   'source_ids':'SRC_083','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_073','from_node':'T3_MOD_008','to_node':'T3_EMD_003',
   'relation_type':'emerged_from','date_start':'1895','date_end':'1920','date_precision':'year',
   'explanation':'Atomic and nuclear physics emerged from mathematical physics tradition (EMD_003) applied to atomic structure. X-ray discovery (1895), radioactivity (1896-1898), electron (1897), nuclear model (1911) founded the field.',
   'pioneers_involved':'J.J. Thomson, Ernest Rutherford, Marie Curie',
   'source_ids':'SRC_079','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_074','from_node':'T3_MOD_008','to_node':'T3_MOD_006',
   'relation_type':'method_imported_from','date_start':'1895','date_end':'1920','date_precision':'decade',
   'explanation':'Atomic physics imported spectroscopic methods from electromagnetism (MOD_006): cathode ray tube, X-ray generation, Zeeman effect, spectral lines. EM provided both experimental tools and theoretical framework for atomic radiation.',
   'pioneers_involved':'J.J. Thomson, Pieter Zeeman, Hendrik Lorentz',
   'source_ids':'SRC_079','confidence':'A','evidence_type':'E3'},

  # ── QUANTUM MECHANICS AND RELATIVITY ──────────────────────────────────────
  {'edge_id':'T3_E_075','from_node':'T3_MOD_009','to_node':'T3_MOD_008',
   'relation_type':'emerged_from','date_start':'1900','date_end':'1927','date_precision':'decade',
   'explanation':'Quantum mechanics emerged from and transformed atomic physics (MOD_008). Spectral line data demanded quantum explanation; Bohr model (1913) applied quantization to atoms; Heisenberg-Schrödinger quantum mechanics (1925-1926) completed the revolution.',
   'pioneers_involved':'Max Planck, Albert Einstein, Niels Bohr, Werner Heisenberg, Erwin Schrödinger',
   'source_ids':'SRC_078','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_076','from_node':'T3_MOD_009','to_node':'T3_MOD_005',
   'relation_type':'method_imported_from','date_start':'1900','date_end':'1930','date_precision':'decade',
   'explanation':'Quantum mechanics imported statistical mechanics methods (MOD_005) for probabilistic interpretation. Boltzmann statistical approach informed Born\'s probabilistic wave function interpretation (1926); quantum statistics (Bose-Einstein 1924, Fermi-Dirac 1926) extended statistical mechanics.',
   'pioneers_involved':'Max Born, Albert Einstein, Enrico Fermi',
   'source_ids':'SRC_078','confidence':'A','evidence_type':'E3'},

  {'edge_id':'T3_E_077','from_node':'T3_MOD_010','to_node':'T3_MOD_006',
   'relation_type':'emerged_from','date_start':'1905','date_end':'1915','date_precision':'year',
   'explanation':'Special relativity (1905) emerged directly from inconsistency between electromagnetic theory (MOD_006 requiring constant c) and Newtonian mechanics. Michelson-Morley null ether result plus Maxwell\'s equations forced relativistic framework. General relativity (1915) extended this.',
   'pioneers_involved':'Albert Einstein, Hendrik Lorentz, Henri Poincaré',
   'source_ids':'SRC_079','confidence':'A','evidence_type':'E4'},

  # ── STATISTICAL MECHANICS MERGE ───────────────────────────────────────────
  {'edge_id':'T3_E_078','from_node':'T3_MOD_011','to_node':'T3_MOD_005',
   'relation_type':'merged_with','date_start':'1860','date_end':'1902','date_precision':'decade',
   'explanation':'Statistical mechanics merged thermodynamics (MOD_005) with atomic theory. Boltzmann showed entropy is statistical; Gibbs systematized (1902). Thermodynamics remains macroscopic component; statistical mechanics provides microscopic derivation.',
   'pioneers_involved':'Ludwig Boltzmann, J. Willard Gibbs',
   'source_ids':'SRC_081','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_079','from_node':'T3_MOD_011','to_node':'T3_EMD_006',
   'relation_type':'merged_with','date_start':'1860','date_end':'1912','date_precision':'decade',
   'explanation':'Statistical mechanics merged atomic theory (EMD_006, Dalton tradition) with thermodynamics. Boltzmann\'s S=klogW required atoms to count microstates. Perrin\'s Brownian motion experiments (1908-1912) confirmed atomism and validated statistical mechanics.',
   'pioneers_involved':'Ludwig Boltzmann, Jean Perrin',
   'source_ids':'SRC_082','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_080','from_node':'T3_MOD_004','to_node':'T3_MOD_011',
   'relation_type':'method_imported_from','date_start':'1900','date_end':'1940','date_precision':'decade',
   'explanation':'Physical chemistry imported statistical mechanics methods after Gibbs\'s systematization (1902): partition functions, chemical equilibrium from Boltzmann factors, Debye-Hückel theory of electrolytes. Physical chemistry increasingly used statistical mechanical framework.',
   'pioneers_involved':'Peter Debye, Walther Nernst, Gilbert N. Lewis',
   'source_ids':'SRC_075','confidence':'B','evidence_type':'E3'},

  # ── CONTEMPORARY: QFT AND CMP ─────────────────────────────────────────────
  {'edge_id':'T3_E_081','from_node':'T3_CON_001','to_node':'T3_MOD_009',
   'relation_type':'emerged_from','date_start':'1928','date_end':'1949','date_precision':'decade',
   'explanation':'Quantum field theory emerged from quantum mechanics (MOD_009) extended to relativistic regime. Dirac equation (1928) initiated QFT; renormalization crisis resolved by Feynman-Schwinger-Tomonaga QED (1946-1949). Field quantization generalizes quantum mechanics.',
   'pioneers_involved':'Paul Dirac, Richard Feynman, Julian Schwinger, Sin-Itiro Tomonaga, Freeman Dyson',
   'source_ids':'SRC_099','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_082','from_node':'T3_CON_001','to_node':'T3_MOD_010',
   'relation_type':'merged_with','date_start':'1928','date_end':'1974','date_precision':'decade',
   'explanation':'QFT is the merge of quantum mechanics with special relativity. Dirac equation (1928) combined them; QED (1946-1949) was their fully consistent quantum field theoretic treatment. Standard Model completion (1974) required relativistic gauge theories.',
   'pioneers_involved':'Paul Dirac, Richard Feynman, Steven Weinberg',
   'source_ids':'SRC_099','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_083','from_node':'T3_CON_002','to_node':'T3_MOD_009',
   'relation_type':'emerged_from','date_start':'1947','date_end':'1970','date_precision':'decade',
   'explanation':'Condensed matter physics emerged from quantum mechanics applied to many-body systems. Transistor (1947) demonstrated quantum mechanics of semiconductors; BCS theory (1957) applied quantum many-body theory to superconductivity; condensed matter renamed from solid state physics ~1978.',
   'pioneers_involved':'John Bardeen, Philip Anderson, Leon Cooper, John Robert Schrieffer',
   'source_ids':'SRC_091','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_084','from_node':'T3_CON_002','to_node':'T3_MOD_011',
   'relation_type':'method_imported_from','date_start':'1947','date_end':'1980','date_precision':'decade',
   'explanation':'Condensed matter physics imported statistical mechanics methods (MOD_011) for phase transitions, many-body systems, and collective phenomena. Renormalization group (Wilson 1971-1974) united QFT methods with statistical mechanics in condensed matter context.',
   'pioneers_involved':'Kenneth Wilson, Leo Kadanoff, Philip Anderson',
   'source_ids':'SRC_091','confidence':'A','evidence_type':'E3'},

  # ── MATERIALS SCIENCE MERGE ────────────────────────────────────────────────
  {'edge_id':'T3_E_085','from_node':'T3_CON_003','to_node':'T3_CON_002',
   'relation_type':'merged_with','date_start':'1960','date_end':'1980','date_precision':'decade',
   'explanation':'Materials science merged condensed matter physics (CON_002) as primary physics component. ARPA IDL program (1960) brought physicists, chemists, metallurgists together; quantum mechanics of defects, band theory of semiconductors from CMP.',
   'pioneers_involved':'Morris Cohen, Philip Anderson, Nevill Mott',
   'source_ids':'SRC_101','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_086','from_node':'T3_CON_003','to_node':'T3_MOD_004',
   'relation_type':'merged_with','date_start':'1960','date_end':'1980','date_precision':'decade',
   'explanation':'Materials science merged physical chemistry (MOD_004) as chemistry component. Thermodynamics of phase equilibria, reaction kinetics, electrochemistry of corrosion all from physical chemistry tradition.',
   'pioneers_involved':'Cyril Stanley Smith, Morris Cohen',
   'source_ids':'SRC_101','confidence':'A','evidence_type':'E4'},

  # ── COMPUTATIONAL CHEMISTRY ────────────────────────────────────────────────
  {'edge_id':'T3_E_087','from_node':'T3_CON_004','to_node':'T3_MOD_009',
   'relation_type':'emerged_from','date_start':'1930','date_end':'1966','date_precision':'decade',
   'explanation':'Quantum chemistry emerged from applying quantum mechanics (MOD_009) to chemical systems. Heitler-London H2 bond (1927) initiated; Mulliken MO theory (1928-); Kohn-Sham DFT (1965) made it computationally practical; Nobel 1966 (Mulliken) confirmed maturation.',
   'pioneers_involved':'Robert S. Mulliken, Walter Kohn, John Pople',
   'source_ids':'SRC_098','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_088','from_node':'T3_CON_004','to_node':'T3_MOD_001',
   'relation_type':'problem_domain_shared_with','date_start':'1950','date_end':'2025','date_precision':'decade',
   'explanation':'Computational chemistry shares problem domain with organic chemistry (MOD_001) — molecular structure, reaction mechanisms, drug design. Kohn-Sham DFT and Pople\'s GAUSSIAN software made QM calculations routine for organic molecules.',
   'pioneers_involved':'John Pople, Axel Becke, Walter Kohn',
   'source_ids':'SRC_098','confidence':'A','evidence_type':'E3'},

  {'edge_id':'T3_E_089','from_node':'T3_CON_004','to_node':'T3_MOD_004',
   'relation_type':'method_imported_from','date_start':'1950','date_end':'1998','date_precision':'decade',
   'explanation':'Quantum chemistry imported physical chemistry methods (MOD_004): thermochemistry for bond energies, kinetics for reaction rates, electrochemistry for redox. DFT extended thermodynamic functionals; Nobel 1998 recognized computational chemistry as physical chemistry subspecialty.',
   'pioneers_involved':'Walter Kohn, Gerhard Ertl, Martin Karplus',
   'source_ids':'SRC_097','confidence':'A','evidence_type':'E3'},

  # ── SURFACE SCIENCE ────────────────────────────────────────────────────────
  {'edge_id':'T3_E_090','from_node':'T3_CON_005','to_node':'T3_MOD_004',
   'relation_type':'emerged_from','date_start':'1960','date_end':'1981','date_precision':'decade',
   'explanation':'Surface science emerged from physical chemistry (MOD_004) applied to surfaces. Langmuir isotherm (1916-1932 Nobel) was early surface chemistry; UHV technology (1960s) enabled clean surface experiments; Surface Science journal (1964) institutionalized.',
   'pioneers_involved':'Irving Langmuir, Gerhard Ertl',
   'source_ids':'SRC_098','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_091','from_node':'T3_CON_005','to_node':'T3_CON_002',
   'relation_type':'method_imported_from','date_start':'1960','date_end':'1990','date_precision':'decade',
   'explanation':'Surface science imported condensed matter physics (CON_002) methods for electronic structure of surfaces: band theory, phonon spectra at surfaces, LEED theory. Binnig-Rohrer STM (1981) applied quantum tunneling from CMP to surface imaging.',
   'pioneers_involved':'Gerd Binnig, Heinrich Rohrer, Kai Siegbahn',
   'source_ids':'SRC_095','confidence':'A','evidence_type':'E3'},

  # ── NANOTECHNOLOGY ─────────────────────────────────────────────────────────
  {'edge_id':'T3_E_092','from_node':'T3_CON_006','to_node':'T3_CON_002',
   'relation_type':'emerged_from','date_start':'1981','date_end':'2000','date_precision':'decade',
   'explanation':'Nanotechnology emerged from condensed matter physics (CON_002) quantum size effects — at nanoscale, discrete energy levels and quantum confinement dominate. CMP provided quantum dot theory, size-dependent band gaps, quantum confinement effects.',
   'pioneers_involved':'Gerd Binnig, Andre Geim, Sumio Iijima',
   'source_ids':'SRC_095','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_093','from_node':'T3_CON_006','to_node':'T3_CON_005',
   'relation_type':'method_imported_from','date_start':'1981','date_end':'2000','date_precision':'decade',
   'explanation':'Nanotechnology imported surface science (CON_005) methods: STM and AFM for imaging and manipulation, UHV for clean nanofabrication, surface functionalization chemistry. Surface science\'s atomic-scale toolkit became nanotechnology\'s primary instrumentation.',
   'pioneers_involved':'Don Eigler, Gerd Binnig, Heinrich Rohrer',
   'source_ids':'SRC_095','confidence':'A','evidence_type':'E3'},

  {'edge_id':'T3_E_094','from_node':'T3_CON_006','to_node':'T3_CON_003',
   'relation_type':'method_imported_from','date_start':'1985','date_end':'2010','date_precision':'decade',
   'explanation':'Nanotechnology imported materials science (CON_003) processing and characterization methods: electron microscopy, X-ray diffraction for nanomaterial structure, thin film deposition, lithography for nanostructure fabrication.',
   'pioneers_involved':'Richard Smalley, Morris Cohen',
   'source_ids':'SRC_095','confidence':'B','evidence_type':'E3'},

  # ── SEMICONDUCTOR, POLYMER, STRUCTURAL BIO ────────────────────────────────
  {'edge_id':'T3_E_095','from_node':'T3_CON_007','to_node':'T3_CON_002',
   'relation_type':'split_from','date_start':'1947','date_end':'1970','date_precision':'decade',
   'explanation':'Semiconductor physics split as specialized applied subfield from condensed matter physics (CON_002). Transistor (1947) drove specialization; Silicon Valley semiconductor industry created distinct commercial focus; IEEE and SIA institutionalized separation from academic CMP.',
   'pioneers_involved':'John Bardeen, William Shockley, Jack Kilby',
   'source_ids':'SRC_093','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_096','from_node':'T3_CON_008','to_node':'T3_MOD_001',
   'relation_type':'emerged_from','date_start':'1920','date_end':'1953','date_precision':'decade',
   'explanation':'Polymer science emerged from organic chemistry (MOD_001). Staudinger (1920) proposed macromolecule concept; polymer synthesis is organic chemistry. Flory\'s theoretical polymer physics came later (1940s-1970s) connecting to physical chemistry.',
   'pioneers_involved':'Hermann Staudinger, Paul Flory, Wallace Carothers',
   'source_ids':'SRC_094','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_097','from_node':'T3_CON_008','to_node':'T3_MOD_004',
   'relation_type':'method_imported_from','date_start':'1940','date_end':'1980','date_precision':'decade',
   'explanation':'Polymer science imported physical chemistry (MOD_004) methods for thermodynamics of solutions (Flory-Huggins theory imports Gibbs free energy formalism), kinetics of polymerization, and rheology/viscometry.',
   'pioneers_involved':'Paul Flory, Pierre-Gilles de Gennes',
   'source_ids':'SRC_094','confidence':'A','evidence_type':'E3'},

  {'edge_id':'T3_E_098','from_node':'T3_CON_009','to_node':'T3_CON_004',
   'relation_type':'method_imported_from','date_start':'1977','date_end':'2013','date_precision':'decade',
   'explanation':'Structural biology (CON_009) imported computational chemistry methods (CON_004): molecular dynamics simulations (Karplus 1977) of proteins; force fields (CHARMM, AMBER); QM/MM for enzyme active site calculations; DFT for metalloenzyme electronic structure.',
   'pioneers_involved':'Martin Karplus, Michael Levitt, Arieh Warshel',
   'source_ids':'SRC_098','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_099','from_node':'T3_CON_009','to_node':'T3_MOD_004',
   'relation_type':'emerged_from','date_start':'1950','date_end':'1970','date_precision':'decade',
   'explanation':'Biochemistry (Trunk 3 component) emerged from physical chemistry (MOD_004) methods applied to biological molecules. Protein X-ray crystallography (Perutz-Kendrew 1957-1960) extended physical chemistry structural methods; biophysical chemistry became distinct identity.',
   'pioneers_involved':'Max Perutz, John Kendrew, Linus Pauling',
   'source_ids':'SRC_098','confidence':'B','evidence_type':'E3'},

  # ── 2D MATERIALS, QUANTUM COMPUTING, ASTROCHEMISTRY ──────────────────────
  {'edge_id':'T3_E_100','from_node':'T3_CON_010','to_node':'T3_CON_002',
   'relation_type':'split_from','date_start':'2004','date_end':'2020','date_precision':'decade',
   'explanation':'2D/topological materials split from condensed matter physics (CON_002) as distinct subfield. Graphene isolation (2004), topological insulator experiments (2007+), magic-angle graphene (2018) created dedicated research community, journal (2D Materials, 2014), and EU flagship program.',
   'pioneers_involved':'Andre Geim, Konstantin Novoselov, David Thouless, Duncan Haldane',
   'source_ids':'SRC_093','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_101','from_node':'T3_CON_011','to_node':'T3_MOD_009',
   'relation_type':'emerged_from','date_start':'1980','date_end':'2000','date_precision':'decade',
   'explanation':'Quantum computing emerged from quantum mechanics (MOD_009) extended to information processing. Feynman\'s concept (1982) that quantum systems should simulate quantum systems; Shor\'s algorithm (1994) demonstrated exponential speedup; Nielsen-Chuang textbook (2000) matured field.',
   'pioneers_involved':'Peter Shor, John Preskill, David Wineland',
   'source_ids':'SRC_103','confidence':'A','evidence_type':'E4'},

  {'edge_id':'T3_E_102','from_node':'T3_CON_011','to_node':'T3_CON_002',
   'relation_type':'method_imported_from','date_start':'1999','date_end':'2025','date_precision':'decade',
   'explanation':'Quantum computing hardware imported condensed matter physics (CON_002) phenomena: superconducting Josephson junction qubits (BCS superconductivity, Josephson effect); topological qubits from topological insulators; quantum Hall states for anyonic computation.',
   'pioneers_involved':'John Bardeen, Brian Josephson, David Wineland',
   'source_ids':'SRC_104','confidence':'A','evidence_type':'E3'},

  {'edge_id':'T3_E_103','from_node':'T3_CON_012','to_node':'T3_MOD_004',
   'relation_type':'emerged_from','date_start':'1960','date_end':'1980','date_precision':'decade',
   'explanation':'Astrochemistry emerged from physical chemistry (MOD_004) applied to extreme conditions. Low-temperature and low-density reaction kinetics, spectroscopic identification of interstellar molecules, and thermochemistry of high-pressure phases all derive from physical chemistry tradition.',
   'pioneers_involved':'William Klemperer, Neil Bartlett',
   'source_ids':'SRC_097','confidence':'B','evidence_type':'E3'},
]

print("Running Part 6: Edges")
append_rows('edges.csv', EDGE_FIELDS, edges)
print(f"Part 6 complete. {len(edges)} edges added (T3_E_065-T3_E_103).")
