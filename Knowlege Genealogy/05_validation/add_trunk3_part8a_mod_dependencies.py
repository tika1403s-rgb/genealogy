"""
Part 8a: Modern breakthrough→node dependencies DEP_091-125
Covers T3_MOD_001-011 (35 entries)
ID map:
  MOD_001: DEP_091-093  MOD_002: DEP_094-096  MOD_003: DEP_097-098
  MOD_004: DEP_099-101  MOD_005: DEP_102-104  MOD_006: DEP_105-106
  MOD_007: DEP_107-109  MOD_008: DEP_110-114  MOD_009: DEP_115-119
  MOD_010: DEP_120-122  MOD_011: DEP_123-125
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

def D(dep_id, brkth_id, node_id, rel, mech, src='SRC_075'):
    return {'dependency_id':dep_id,'breakthrough_id':brkth_id,'node_id':node_id,
            'relationship_type':rel,'mechanism':mech,'quantitative_impact':'','source_ids':src}

rows = [
    # ── T3_MOD_001: Organic Chemistry (DEP_091-093) ────────────────────────────
    D('DEP_091','BRKTH_092','T3_MOD_001','transformed_by',
      'Systematic organic synthesis methods (esterification, reductions, functional-group transformations 1850-1940) transformed Organic Chemistry from descriptive classification into a creative constructive science; Wöhler\'s urea synthesis was the proof of concept that opened purposeful molecular construction'),

    D('DEP_092','BRKTH_068','T3_MOD_001','contributed_to',
      'Periodic table provided systematic context for organic compounds, highlighting carbon\'s tetravalent position; explained the uniqueness of carbon chain-forming chemistry and framed organic reactivity patterns within a broader elemental framework'),

    D('DEP_093','BRKTH_088','T3_MOD_001','transformed_by',
      'X-ray crystallography enabled direct determination of three-dimensional molecular structures of organic compounds; resolved debates over benzene ring geometry and natural product configurations; transformed structure determination from chemical inference to direct experimental observation',
      'SRC_076'),

    # ── T3_MOD_002: Analytical Chemistry (DEP_094-096) ────────────────────────
    D('DEP_094','BRKTH_080','T3_MOD_002','transformed_by',
      'Emission spectroscopy transformed Analytical Chemistry by providing the first method for unambiguous elemental identification via spectral fingerprints; enabled analysis of materials in any physical state without prior separation; founded spectroanalytical methods as primary analytical approach'),

    D('DEP_095','BRKTH_093','T3_MOD_002','transformed_by',
      'Chromatographic separation techniques (paper, column, gas, liquid chromatography 1900-1940) gave analytical chemists systematic means to isolate components of complex mixtures; enabled analysis of biological fluids, environmental samples, and synthetic mixtures with multiple components',
      'SRC_076'),

    D('DEP_096','BRKTH_087','T3_MOD_002','contributed_to',
      'Mass spectrometry contributed precise atomic mass measurements and isotopic composition data to Analytical Chemistry; became a primary tool for molecular weight and fragmentation pattern identification; transformed trace-level organic analysis',
      'SRC_076'),

    # ── T3_MOD_003: Inorganic Chemistry (DEP_097-098) ─────────────────────────
    D('DEP_097','BRKTH_068','T3_MOD_003','transformed_by',
      'Periodic table transformed Inorganic Chemistry into a predictive framework: elemental groups share chemical behaviour, oxidation states follow periodic trends, and missing elements were predicted with their properties; systematic inorganic synthesis became organised around periodic structure'),

    D('DEP_098','BRKTH_088','T3_MOD_003','transformed_by',
      'X-ray crystallography directly determined three-dimensional structures of inorganic crystals, minerals, and coordination compounds; confirmed Werner\'s octahedral coordination geometry; enabled structure-property relationships in inorganic solid-state materials',
      'SRC_076'),

    # ── T3_MOD_004: Physical Chemistry (DEP_099-101) ──────────────────────────
    D('DEP_099','BRKTH_065','T3_MOD_004','enabled_by',
      'Conservation of energy principle provided Physical Chemistry with its thermodynamic foundation: chemical reactions involve energy changes governed by universal conservation; enthalpy and free energy concepts rest on energy conservation as their axiomatic basis'),

    D('DEP_100','BRKTH_066','T3_MOD_004','enabled_by',
      'Second law and entropy enabled Physical Chemistry to predict direction and equilibrium position of chemical reactions via Gibbs free energy (ΔG = ΔH - TΔS); spontaneity criterion essential for electrochemistry, solution equilibria, and phase behaviour'),

    D('DEP_101','BRKTH_091','T3_MOD_004','transformed_by',
      'Electrochemical methods enabled precise measurements of electrode potentials, ionic conductivities, and electrolyte activities; underpinned Nernst equation, Arrhenius ionisation theory, and van\'t Hoff osmotic work; made Physical Chemistry quantitatively precise'),

    # ── T3_MOD_005: Thermodynamics (DEP_102-104) ──────────────────────────────
    D('DEP_102','BRKTH_065','T3_MOD_005','transformed_by',
      'Conservation of energy transformed Thermodynamics from engineering science of heat engines into a universal physical theory; Joule\'s mechanical equivalent established the first law quantitatively; energy conservation unified heat, work, and mechanical motion under one principle'),

    D('DEP_103','BRKTH_066','T3_MOD_005','transformed_by',
      'Second law formulation and entropy concept constituted the conceptual core of thermodynamics as a mature theory; entropy as state function quantified irreversibility; the two laws together with absolute temperature gave thermodynamics its complete axiomatic structure'),

    D('DEP_104','BRKTH_090','T3_MOD_005','contributed_to',
      'Precision thermochemical calorimetry provided reliable enthalpy data for chemical and physical processes; Hess\'s law verification; formation enthalpies enabling free energy calculations via Gibbs-Helmholtz equation; calorimetric accuracy underpinned quantitative thermodynamics'),

    # ── T3_MOD_006: Electromagnetism (DEP_105-106) ────────────────────────────
    D('DEP_105','BRKTH_067','T3_MOD_006','transformed_by',
      'Maxwell\'s electromagnetic theory transformed Electromagnetism from a collection of empirical laws into a unified mathematical field theory; predicted electromagnetic waves at the speed of light unifying optics with electromagnetism; the definitive synthesis of the discipline'),

    D('DEP_106','BRKTH_064','T3_MOD_006','enabled_by',
      'Voltaic pile battery enabled continuous current experiments underpinning Oersted\'s electromagnetic discovery, Ampère\'s quantitative laws, and Faraday\'s induction experiments; sustained current was necessary for systematic electromagnetic investigation'),

    # ── T3_MOD_007: Modern Optics (DEP_107-109) ───────────────────────────────
    D('DEP_107','BRKTH_067','T3_MOD_007','transformed_by',
      'Maxwell\'s electromagnetic theory transformed Modern Optics by identifying light as electromagnetic waves; established frequency and wavelength of visible light; predicted and unified radio, infrared, visible, ultraviolet, and X-ray radiation as one electromagnetic spectrum'),

    D('DEP_108','BRKTH_084','T3_MOD_007','transformed_by',
      'Michelson interferometer and ether null result transformed Modern Optics by eliminating the mechanical ether and establishing precision interference measurement as primary optical metrology; interferometry enabled wavelength-based length standards and high spectral resolution'),

    D('DEP_109','BRKTH_080','T3_MOD_007','enabled_by',
      'Emission spectroscopy enabled Modern Optics by demonstrating discrete spectral lines as precise probes of atomic structure; spectral analysis of light sources drove the identification of elements in stars and motivated the quantum explanation of atomic line spectra'),

    # ── T3_MOD_008: Atomic/Nuclear Physics (DEP_110-114) ──────────────────────
    D('DEP_110','BRKTH_081','T3_MOD_008','transformed_by',
      'Electron discovery constituted the first identification of a subatomic particle transforming Atomic/Nuclear Physics from chemical atomic theory to sub-atomic particle physics; demonstrated atoms have internal structure motivating Thomson\'s model and Rutherford\'s scattering experiment'),

    D('DEP_111','BRKTH_082','T3_MOD_008','transformed_by',
      'Radioactivity discovery revealed spontaneous nuclear transformations showing atoms are not immutable; alpha, beta, gamma emissions; elemental transmutation; provided the alpha-particle probes used in Rutherford\'s nuclear model experiment founding nuclear physics'),

    D('DEP_112','BRKTH_086','T3_MOD_008','transformed_by',
      'Alpha scattering experiment established the nuclear atomic model replacing Thomson\'s plum pudding; tiny dense positive nucleus concentrating most of the atomic mass; estimated nuclear radius from scattering angles founding quantitative nuclear structure studies'),

    D('DEP_113','BRKTH_083','T3_MOD_008','enabled_by',
      'X-ray discovery provided a new high-energy radiation probing atomic inner shells and crystal structure; Moseley\'s X-ray atomic number measurements placed the periodic table on quantitative basis identifying atomic number as the fundamental atomic property',
      'SRC_075'),

    D('DEP_114','BRKTH_094','T3_MOD_008','transformed_by',
      'Nuclear fission and chain reaction demonstrated that nuclear binding energy vastly exceeds chemical energy and can be released in cascade; transformed Atomic/Nuclear Physics from basic science into applied nuclear technology; raised questions about stellar energy from nuclear reactions',
      'SRC_076'),

    # ── T3_MOD_009: Quantum Mechanics (DEP_115-119) ───────────────────────────
    D('DEP_115','BRKTH_070','T3_MOD_009','enabled_by',
      'Planck\'s energy quantisation provided the foundational seed of quantum theory; the concept that energy exchanges occur in discrete quanta E=hν broke the classical continuum assumption and made discreteness a fundamental feature of the quantum world'),

    D('DEP_116','BRKTH_073','T3_MOD_009','enabled_by',
      'Bohr\'s atomic model introduced quantised orbits and discrete energy levels explaining hydrogen line spectra; correspondence principle bridged classical and quantum domains; its explicit quantum postulates were the direct precursors that Heisenberg and Schrödinger reformulated rigorously'),

    D('DEP_117','BRKTH_076','T3_MOD_009','transformed_by',
      'Matrix mechanics and wave mechanics formulations constituted the mathematical completion of quantum mechanics; Born\'s probabilistic interpretation, Dirac\'s transformation theory, and Heisenberg\'s commutation relations established the axiomatic structure of quantum mechanics',
      'SRC_076'),

    D('DEP_118','BRKTH_077','T3_MOD_009','transformed_by',
      'Uncertainty principle transformed Quantum Mechanics epistemologically: ΔxΔp ≥ ℏ/2 is an intrinsic feature of quantum states, not merely a measurement limitation; complementarity of conjugate observables defines the quantum-classical boundary',
      'SRC_076'),

    D('DEP_119','BRKTH_079','T3_MOD_009','transformed_by',
      'Dirac equation extended quantum mechanics to the relativistic regime predicting spin-½ naturally and antimatter existence; established QM compatibility with special relativity; provided the foundation for quantum field theory as the next level of quantum description',
      'SRC_076'),

    # ── T3_MOD_010: Relativity (DEP_120-122) ──────────────────────────────────
    D('DEP_120','BRKTH_071','T3_MOD_010','transformed_by',
      'Special relativity transformed physics by establishing Lorentz invariance as fundamental symmetry; time dilation, length contraction, relativity of simultaneity, and E=mc² mass-energy equivalence; eliminated the ether; unified space and time into a four-dimensional spacetime'),

    D('DEP_121','BRKTH_074','T3_MOD_010','transformed_by',
      'General relativity transformed Relativity into a theory of gravitation and spacetime geometry; curvature of spacetime by mass-energy; gravitational time dilation and redshift; prediction of black holes, gravitational waves, and expanding cosmology',
      'SRC_076'),

    D('DEP_122','BRKTH_084','T3_MOD_010','enabled_by',
      'Michelson-Morley null ether result (1887) provided crucial experimental motivation for special relativity; demonstrating that light speed is frame-independent eliminated the mechanical ether that classical electrodynamics required and demanded a new kinematic theory'),

    # ── T3_MOD_011: Statistical Mechanics (DEP_123-125) ───────────────────────
    D('DEP_123','BRKTH_065','T3_MOD_011','enabled_by',
      'Conservation of energy provided Statistical Mechanics its macroscopic anchor: microscopic molecular motions must conserve total energy, constraining phase-space trajectories and establishing the microcanonical ensemble as the fundamental equilibrium ensemble'),

    D('DEP_124','BRKTH_069','T3_MOD_011','transformed_by',
      'Statistical interpretation of entropy S=k·ln(W) was the central achievement of Statistical Mechanics: thermodynamic entropy explained as logarithm of microscopic configurations; Boltzmann constant k bridged macroscopic temperature to microscopic kinetic energy'),

    D('DEP_125','BRKTH_066','T3_MOD_011','enabled_by',
      'Second law and entropy gave Statistical Mechanics its explanatory target: deriving macroscopic irreversibility from time-reversible microscopic mechanics; Boltzmann\'s H-theorem and Gibbs ensemble theory both aimed to explain entropy increase from molecular statistics'),
]

print("Running Part 8a: Modern breakthrough dependencies (DEP_091-125)")
append_rows('breakthrough_dependencies.csv', FIELDS, rows)
print(f"Part 8a complete. {len(rows)} dependencies added.")
