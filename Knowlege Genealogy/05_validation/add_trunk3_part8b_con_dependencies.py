"""
Part 8b: Contemporary breakthrough→node dependencies DEP_126-159
Covers T3_CON_001-012 (34 entries)
ID map:
  CON_001: DEP_126-128  CON_002: DEP_129-132  CON_003: DEP_133-135
  CON_004: DEP_136-138  CON_005: DEP_139-140  CON_006: DEP_141-142
  CON_007: DEP_143-145  CON_008: DEP_146-147  CON_009: DEP_148-151
  CON_010: DEP_152-154  CON_011: DEP_155-157  CON_012: DEP_158-159
"""
import csv, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '04_nodes_edges')

FIELDS = ['dependency_id','breakthrough_id','node_id','relationship_type',
          'mechanism','quantitative_impact','source_ids']

def append_rows(fname, fieldnames, rows):
    path = os.path.join(BASE, fname)
    with open(path, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        for r in rows:
            w.writerow(r)
    print(f"  + {fname}: {len(rows)} rows added")

def D(dep_id, brkth_id, node_id, rel, mech, src='SRC_077'):
    return {'dependency_id':dep_id,'breakthrough_id':brkth_id,'node_id':node_id,
            'relationship_type':rel,'mechanism':mech,'quantitative_impact':'','source_ids':src}

rows = [
    # ── T3_CON_001: QFT/QED (DEP_126-128) ─────────────────────────────────────
    D('DEP_126','BRKTH_079','T3_CON_001','enabled_by',
      'Dirac equation provided the relativistic quantum foundation that QFT extended; second quantisation of the Dirac field yielded QED; the Dirac sea and positron prediction established that relativistic QM requires multi-particle field theory',
      'SRC_076'),

    D('DEP_127','BRKTH_095','T3_CON_001','transformed_by',
      'QED renormalization (Feynman, Schwinger, Tomonaga 1948-1949) resolved the ultraviolet divergence problem, making QFT a predictively successful theory; QED became the template for all subsequent quantum field theories in the Standard Model'),

    D('DEP_128','BRKTH_100','T3_CON_001','transformed_by',
      'Standard Model completion (1967-1974) extended QFT from QED to include weak and strong interactions; electroweak unification, QCD with colour charge and asymptotic freedom; established QFT as the universal framework for fundamental particle physics'),

    # ── T3_CON_002: Condensed Matter Physics (DEP_129-132) ─────────────────────
    D('DEP_129','BRKTH_076','T3_CON_002','enabled_by',
      'Quantum mechanics is the foundational framework of Condensed Matter Physics; band theory, Fermi-Dirac statistics, Bose-Einstein statistics, and quantum many-body theory all derive from QM applied to large numbers of interacting electrons and atoms in solids',
      'SRC_076'),

    D('DEP_130','BRKTH_097','T3_CON_002','transformed_by',
      'BCS theory of superconductivity (1957) provided the first complete microscopic quantum theory of a macroscopic ordered state; Cooper-pair condensation, energy gap, and Josephson effects established CMP as capable of deriving emergent phenomena from microscopic interactions'),

    D('DEP_131','BRKTH_098','T3_CON_002','transformed_by',
      'Anderson\'s More is Different (1972) established emergence and broken symmetry as the organising principles of CMP; legitimised condensed matter as equal to particle physics; symmetry breaking, order parameters, and universality classes became central theoretical tools'),

    D('DEP_132','BRKTH_103','T3_CON_002','transformed_by',
      'Quantum Hall effects (integer 1980, fractional 1982) opened topological physics within CMP; quantised Hall resistance as topological invariant; topological order as new class of quantum phases beyond Landau symmetry-breaking paradigm; transformed CMP theoretical landscape'),

    # ── T3_CON_003: Materials Science (DEP_133-135) ───────────────────────────
    D('DEP_133','BRKTH_088','T3_CON_003','enabled_by',
      'X-ray crystallography enabled Materials Science by revealing atomic-scale structure of metals, ceramics, and polymers; structure-property relationships became quantitative once crystal structures were known; diffraction is the primary structural characterisation tool in materials science',
      'SRC_076'),

    D('DEP_134','BRKTH_096','T3_CON_003','transformed_by',
      'Transistor invention (1947) demonstrated that engineered semiconductor materials with controlled doping could perform electronic functions; created demand for precision materials processing, defect control, and epitaxial growth; drove semiconductor materials science as a discipline'),

    D('DEP_135','BRKTH_102','T3_CON_003','contributed_to',
      'High-temperature superconductivity in cuprates (1986) opened an entirely new class of functional oxide materials; demonstrated that strongly correlated electron systems can be exploited for applications; stimulated discovery of many other oxide functional materials',
      'SRC_079'),

    # ── T3_CON_004: Quantum/Computational Chemistry (DEP_136-138) ─────────────
    D('DEP_136','BRKTH_099','T3_CON_004','transformed_by',
      'Density functional theory (Hohenberg-Kohn 1964, Kohn-Sham 1965) transformed Computational Chemistry by replacing the intractable N-electron wavefunction with electron density functionals; made routine ab initio calculations feasible for molecules with hundreds of atoms',
      'SRC_079'),

    D('DEP_137','BRKTH_108','T3_CON_004','enabled_by',
      'NMR spectroscopy provided experimental molecular geometry and dynamics data that computational chemistry methods needed to validate; coupling constants, chemical shifts, and relaxation times benchmark quantum chemical calculations of molecular electronic structure',
      'SRC_078'),

    D('DEP_138','BRKTH_076','T3_CON_004','enabled_by',
      'Quantum mechanics is the axiomatic foundation of Computational Chemistry; Schrödinger equation provides the exact mathematical target; Hartree-Fock, configuration interaction, and DFT are all approximation schemes for solving the quantum mechanical many-electron problem',
      'SRC_076'),

    # ── T3_CON_005: Surface Science (DEP_139-140) ─────────────────────────────
    D('DEP_139','BRKTH_109','T3_CON_005','transformed_by',
      'STM and AFM (1981-1986) transformed Surface Science by enabling direct real-space imaging of individual atoms on surfaces; surface reconstructions, adsorbate positions, and local electronic structure became directly observable at atomic resolution; made atomic-scale surface chemistry visual',
      'SRC_079'),

    D('DEP_140','BRKTH_083','T3_CON_005','enabled_by',
      'X-ray discovery enabled surface science through development of LEED, XPS, and X-ray scattering techniques probing surface atomic structure and chemistry; X-ray based surface methods provided structural and chemical information before STM era',
      'SRC_075'),

    # ── T3_CON_006: Nanotechnology (DEP_141-142) ──────────────────────────────
    D('DEP_141','BRKTH_109','T3_CON_006','enabled_by',
      'STM and AFM provided the instruments that made nanotechnology experimentally accessible; STM tip manipulation of individual atoms demonstrated practical atomic-scale engineering; AFM enabled biological nanotechnology; scanning probe family is the primary tool of experimental nanotechnology'),

    D('DEP_142','BRKTH_110','T3_CON_006','transformed_by',
      'Carbon nanostructures (C60 1985, CNTs 1991, graphene 2004) transformed Nanotechnology by providing the first practically usable nanomaterials with extraordinary electronic, mechanical, and thermal properties; demonstrated that low-dimensional carbon nanotechnology is chemically stable and scalable',
      'SRC_079'),

    # ── T3_CON_007: Semiconductor Physics (DEP_143-145) ───────────────────────
    D('DEP_143','BRKTH_096','T3_CON_007','transformed_by',
      'Transistor invention (1947) founded Semiconductor Physics as an applied physics discipline; junction transistor design drove systematic band theory and carrier dynamics understanding; silicon semiconductor technology became the dominant platform shaping all subsequent semiconductor physics',
      'SRC_078'),

    D('DEP_144','BRKTH_111','T3_CON_007','transformed_by',
      'Silicon integrated circuit (1958) and microprocessor (1971) transformed Semiconductor Physics by requiring nm-scale precision in doping, lithography, and epitaxy; Moore\'s Law driven miniaturisation pushed semiconductor physics to quantum mechanical limits',
      'SRC_079'),

    D('DEP_145','BRKTH_107','T3_CON_007','contributed_to',
      'Laser (1960) contributed to Semiconductor Physics through semiconductor laser development and optical characterisation; photoluminescence, Raman spectroscopy, and laser epitaxy became primary semiconductor characterisation and fabrication tools',
      'SRC_079'),

    # ── T3_CON_008: Polymer/Soft Matter (DEP_146-147) ─────────────────────────
    D('DEP_146','BRKTH_092','T3_CON_008','enabled_by',
      'Organic synthesis methods enabled Polymer/Soft Matter Chemistry by providing systematic routes to monomers and controlled polymerisation reactions; addition, condensation, and ring-opening polymerisation methods enabled synthesis of designed polymer architectures',
      'SRC_075'),

    D('DEP_147','BRKTH_108','T3_CON_008','transformed_by',
      'NMR spectroscopy transformed Polymer/Soft Matter by enabling chain microstructure determination (tacticity, sequence distribution, branching), polymer dynamics measurements, and gel-phase characterisation; modern polymer characterisation is unthinkable without NMR',
      'SRC_078'),

    # ── T3_CON_009: Biochemistry/Structural Biology (DEP_148-151) ─────────────
    D('DEP_148','BRKTH_088','T3_CON_009','enabled_by',
      'X-ray crystallography enabled Structural Biology by revealing the three-dimensional structures of proteins (myoglobin 1958, haemoglobin 1959), DNA (Watson-Crick 1953), and other biomolecules; atomic-resolution structures provide the mechanistic basis for enzyme catalysis and drug design',
      'SRC_076'),

    D('DEP_149','BRKTH_108','T3_CON_009','transformed_by',
      'NMR spectroscopy transformed Structural Biology by enabling structure determination of proteins in solution rather than crystals; protein dynamics, folding intermediates, and ligand binding kinetics became accessible; complementary to X-ray crystallography for flexible regions',
      'SRC_078'),

    D('DEP_150','BRKTH_112','T3_CON_009','transformed_by',
      'Cryo-electron microscopy (1975-2013) transformed Structural Biology by enabling near-atomic resolution structures of large membrane proteins, virus particles, and assemblies refractory to crystallisation; 2017 Nobel Prize reflected the revolution; made structural biology universal',
      'SRC_079'),

    D('DEP_151','BRKTH_113','T3_CON_009','transformed_by',
      'X-ray protein crystallography (first protein structures 1958-1970s) transformed Structural Biology into a separate discipline from biochemistry; high-resolution structures of enzymes, antibodies, and ribosomes at atomic detail provided molecular mechanisms for life processes',
      'SRC_079'),

    # ── T3_CON_010: 2D/Topological Materials (DEP_152-154) ────────────────────
    D('DEP_152','BRKTH_103','T3_CON_010','enabled_by',
      'Quantum Hall effects demonstrated that topological quantum numbers (TKNN Chern number) govern electronic states in 2D systems; integer QHE is the prototype of a topological insulator phase; fractional QHE exemplified topological order beyond Landau paradigm',
      'SRC_078'),

    D('DEP_153','BRKTH_104','T3_CON_010','transformed_by',
      'Topological phases of matter theory (Haldane model 1988, topological insulator theory 2005-2007, Thouless TKNN) established topological invariants as classifying principle; predicted topological insulators with conducting surface states and bulk gap; entire new materials class',
      'SRC_080'),

    D('DEP_154','BRKTH_110','T3_CON_010','contributed_to',
      'Graphene (2004) and other 2D carbon nanostructures provided the physical realisation of 2D Dirac fermion physics predicted theoretically; anomalous quantum Hall effect in graphene, Klein tunnelling, and massless carriers validated topological band theory predictions',
      'SRC_080'),

    # ── T3_CON_011: Quantum Computing (DEP_155-157) ───────────────────────────
    D('DEP_155','BRKTH_105','T3_CON_011','transformed_by',
      'Shor\'s algorithm (1994) transformed Quantum Computing from academic curiosity to strategic priority; demonstrating exponential speedup for factoring threatened RSA cryptography; motivated massive government and corporate investment in physical qubit implementation',
      'SRC_080'),

    D('DEP_156','BRKTH_106','T3_CON_011','enabled_by',
      'Bell inequality violation experiments (1972-2022) established quantum entanglement as a real physical resource; demonstrated that quantum correlations cannot be explained classically; entanglement is the computational resource underlying quantum gate teleportation and quantum error correction',
      'SRC_080'),

    D('DEP_157','BRKTH_115','T3_CON_011','contributed_to',
      'Laser cooling and BEC (1985-1995) contributed to Quantum Computing by enabling trapped-ion and neutral-atom qubit platforms; laser cooling to sub-millikelvin temperatures initialises quantum state with high fidelity; BEC demonstrated macroscopic quantum coherence motivating quantum computer design',
      'SRC_079'),

    # ── T3_CON_012: Astrochemistry (DEP_158-159) ──────────────────────────────
    D('DEP_158','BRKTH_080','T3_CON_012','enabled_by',
      'Emission spectroscopy enabled Astrochemistry by establishing that celestial bodies share the same chemical elements as Earth; radio spectroscopy extended this to molecular transitions enabling detection of over 200 interstellar molecules via rotational emission lines',
      'SRC_075'),

    D('DEP_159','BRKTH_099','T3_CON_012','enabled_by',
      'Density functional theory methods enabled Astrochemistry by computing accurate rotational constants, vibrational frequencies, and binding energies for astrochemically relevant molecules; ab initio quantum chemical data underpins spectral assignments and astrochemical network modelling',
      'SRC_079'),
]

print("Running Part 8b: Contemporary breakthrough dependencies (DEP_126-159)")
append_rows('breakthrough_dependencies.csv', FIELDS, rows)
print(f"Part 8b complete. {len(rows)} dependencies added.")
