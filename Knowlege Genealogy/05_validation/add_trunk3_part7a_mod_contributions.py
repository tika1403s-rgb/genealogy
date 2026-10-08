"""
Part 7a: Modern pioneer contributions CONTR_144-194
Covers T3_MOD_001-011 (51 entries)
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
    # ── T3_MOD_001: Organic Chemistry ─────────────────────────────────────────
    {'contribution_id':'CONTR_144','pioneer_id':'PION_144','node_id':'T3_MOD_001',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Synthesised urea from inorganic ammonium cyanate (1828) definitively refuting vitalism and establishing that organic compounds can be made without vital force; opened organic synthesis as a laboratory science',
     'key_work':'Urea synthesis paper (1828)','date':'1828','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_145','pioneer_id':'PION_145','node_id':'T3_MOD_001',
     'contribution_type':'methodological_innovation',
     'specific_contribution':'Developed combustion analysis giving organic chemists a reliable method for determining elemental composition of compounds; established the Giessen laboratory model of research-led chemical education adopted worldwide',
     'key_work':'Organic Chemistry in Its Application to Agriculture and Physiology (1840)','date':'1840','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_146','pioneer_id':'PION_146','node_id':'T3_MOD_001',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Proposed carbon tetravalence (1857) and the cyclic ring structure of benzene (1865) founding structural organic chemistry; carbon-chain theory explained the vast diversity of organic compounds systematically',
     'key_work':'On the Constitution and Metamorphoses of Chemical Compounds (1858); Benzene structure paper (1865)','date':'1857-1865','impact_level':'major','source_ids':'SRC_075'},

    # ── T3_MOD_002: Analytical Chemistry ──────────────────────────────────────
    {'contribution_id':'CONTR_147','pioneer_id':'PION_185','node_id':'T3_MOD_002',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Co-developed emission spectroscopy with Bunsen (1859) establishing spectral lines as unique elemental fingerprints; discovered caesium (1860) and rubidium (1861) spectroscopically; extended spectral analysis to solar and stellar composition',
     'key_work':'Chemical Analysis by Spectral Observations (1860)','date':'1859-1861','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_148','pioneer_id':'PION_186','node_id':'T3_MOD_002',
     'contribution_type':'instrumental_advance',
     'specific_contribution':'Invented the Bunsen burner (1855) providing a clean low-luminosity flame essential for emission spectroscopy; co-developed spectroscopy as systematic analytical tool enabling non-destructive elemental identification in complex mixtures',
     'key_work':'Chemical Analysis by Spectral Observations (1860)','date':'1855-1860','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_149','pioneer_id':'PION_194','node_id':'T3_MOD_002',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Developed Debye-Hückel theory of strong electrolyte solutions (1923); invented X-ray powder diffraction (Debye-Scherrer method, 1916) enabling phase identification of polycrystalline materials; Debye-Waller factor quantifying thermal disorder in crystals',
     'key_work':'Zur Theorie der Elektrolyte (1923); Interferenzen an regellos orientierten Teilchen (1916)','date':'1916-1923','impact_level':'major','source_ids':'SRC_076'},

    # ── T3_MOD_003: Inorganic Chemistry ───────────────────────────────────────
    {'contribution_id':'CONTR_150','pioneer_id':'PION_155','node_id':'T3_MOD_003',
     'contribution_type':'synthesis',
     'specific_contribution':'Constructed periodic table (1869) organising all known elements by atomic weight and chemical periodicity; predicted three undiscovered elements (gallium, scandium, germanium) whose subsequent discovery validated the system; provided a unified framework for inorganic chemistry',
     'key_work':'The Relation between the Properties and Atomic Weights of the Elements (1869)','date':'1869','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_151','pioneer_id':'PION_154','node_id':'T3_MOD_003',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Proposed coordination theory (1893) explaining metal complexes through primary and secondary valence; octahedral geometry of transition-metal complexes; founded modern coordination chemistry as a subfield of inorganic chemistry',
     'key_work':'Beitrag zur Konstitution anorganischer Verbindungen (1893)','date':'1893','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_152','pioneer_id':'PION_195','node_id':'T3_MOD_003',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Developed electronegativity scale and resonance theory unifying organic and inorganic bonding; applied quantum mechanics to chemical bonding via valence bond theory; Nature of the Chemical Bond synthesised inorganic structural chemistry',
     'key_work':'The Nature of the Chemical Bond (1939)','date':'1939','impact_level':'major','source_ids':'SRC_076'},

    # ── T3_MOD_004: Physical Chemistry ────────────────────────────────────────
    {'contribution_id':'CONTR_153','pioneer_id':'PION_147','node_id':'T3_MOD_004',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Formulated osmotic pressure law (van\'t Hoff factor, 1885) quantitatively linking solution concentration and pressure; established tetrahedral carbon stereochemistry (1874); first Nobel Prize in Chemistry (1901) recognising physical chemistry as new discipline',
     'key_work':'Études de dynamique chimique (1884)','date':'1874-1885','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_154','pioneer_id':'PION_148','node_id':'T3_MOD_004',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Proposed ionic dissociation theory (1884) explaining why electrolytes conduct electricity and depress freezing points; formulated Arrhenius equation for temperature dependence of reaction rates; defined acids and bases by hydrogen/hydroxide ions',
     'key_work':'Recherches sur la conductibilité galvanique des électrolytes (1884)','date':'1884-1889','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_155','pioneer_id':'PION_149','node_id':'T3_MOD_004',
     'contribution_type':'institutionalization',
     'specific_contribution':'Founded Zeitschrift für Physikalische Chemie (1887) establishing physical chemistry\'s institutional identity; formulated Ostwald\'s dilution law; coined the term catalyst and defined catalysis; organised physical chemistry internationally',
     'key_work':'Lehrbuch der Allgemeinen Chemie (1885-87); Zeitschrift für Physikalische Chemie (1887)','date':'1887-1906','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_156','pioneer_id':'PION_150','node_id':'T3_MOD_004',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Derived Gibbs free energy and chemical potential (1876-1878) providing thermodynamic criterion for spontaneous chemical change; formulated phase rule; ensemble statistical mechanics (1902) uniting thermodynamics with statistical physics',
     'key_work':'On the Equilibrium of Heterogeneous Substances (1876-1878)','date':'1876-1878','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_157','pioneer_id':'PION_151','node_id':'T3_MOD_004',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Derived Nernst equation (1889) relating electrode potential to ion concentrations; formulated third law of thermodynamics (heat theorem, 1906) establishing absolute zero entropy; calorimetric data enabling free energy calculations',
     'key_work':'Die elektromotorische Wirksamkeit der Ionen (1889); Wärmetheorem (1906)','date':'1889-1906','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_158','pioneer_id':'PION_152','node_id':'T3_MOD_004',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Developed Lewis acid-base electron pair theory (1923) unifying acid-base chemistry; proposed covalent bond electron-pair model (1916); introduced fugacity and activity concepts in thermodynamics; Lewis dot structures for visualising valence electrons',
     'key_work':'Valence and the Structure of Atoms and Molecules (1923)','date':'1916-1923','impact_level':'major','source_ids':'SRC_076'},

    # ── T3_MOD_005: Thermodynamics ─────────────────────────────────────────────
    {'contribution_id':'CONTR_159','pioneer_id':'PION_156','node_id':'T3_MOD_005',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Conceived Carnot cycle and efficiency limit (1824) showing maximum work from heat engine depends only on temperature difference; introduced reversibility as theoretical ideal; founded thermodynamics as a science before energy conservation was known',
     'key_work':'Réflexions sur la puissance motrice du feu (1824)','date':'1824','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_160','pioneer_id':'PION_157','node_id':'T3_MOD_005',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Determined mechanical equivalent of heat (1843-1850) through paddle-wheel water heating experiments establishing quantitative energy conservation; showed work and heat as interconvertible forms of energy laying cornerstone of first law',
     'key_work':'On the Mechanical Equivalent of Heat (1845-1850)','date':'1843-1850','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_161','pioneer_id':'PION_158','node_id':'T3_MOD_005',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Formulated second law of thermodynamics (1850) and coined entropy (1865) as state function quantifying irreversibility; Clausius inequality; provided rigorous mathematical framework for heat engine analysis building on Carnot',
     'key_work':'On the Moving Force of Heat (1850); The Mechanical Theory of Heat (1865)','date':'1850-1865','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_162','pioneer_id':'PION_159','node_id':'T3_MOD_005',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Established absolute thermodynamic temperature scale (1848) independent of thermometric substance; second law formulation via heat flow direction; energy dissipation and heat death concept; unified electromagnetism and thermodynamics',
     'key_work':'On an Absolute Thermometric Scale (1848)','date':'1848-1852','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_163','pioneer_id':'PION_160','node_id':'T3_MOD_005',
     'contribution_type':'synthesis',
     'specific_contribution':'Unified mechanics, heat, electricity and magnetism under conservation of energy as universal law (1847); Helmholtz free energy for constant-temperature processes; vortex theory of hydrodynamics; perception and physiology of sensory energy',
     'key_work':'Über die Erhaltung der Kraft (1847)','date':'1847','impact_level':'major','source_ids':'SRC_075'},

    # ── T3_MOD_006: Electromagnetism ──────────────────────────────────────────
    {'contribution_id':'CONTR_164','pioneer_id':'PION_162','node_id':'T3_MOD_006',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Discovered that electric current deflects a compass needle (1820) establishing the link between electricity and magnetism; founding demonstration that launched experimental electromagnetism research across Europe',
     'key_work':'Experimenta circa effectum conflictus electrici in acum magneticam (1820)','date':'1820','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_165','pioneer_id':'PION_163','node_id':'T3_MOD_006',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Derived Ampère\'s law (1820-1826) quantifying the magnetic force between current-carrying conductors; coined electrodynamics; invented the solenoid; mathematical framework for the force between currents preceding Maxwell\'s field theory',
     'key_work':'Mémoire sur la théorie mathématique des phénomènes électrodynamiques (1827)','date':'1820-1827','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_166','pioneer_id':'PION_164','node_id':'T3_MOD_006',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Discovered electromagnetic induction (1831) enabling generators and transformers; Faraday\'s laws of electrolysis; introduced the concept of electric and magnetic field lines as physical reality; rotating coil generator',
     'key_work':'Experimental Researches in Electricity (1831-1855)','date':'1831-1855','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_167','pioneer_id':'PION_165','node_id':'T3_MOD_006',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Formulated Maxwell\'s equations (1864-1873) mathematically unifying electricity, magnetism, and optics; predicted electromagnetic waves propagating at the speed of light; displacement current concept; A Treatise on Electricity and Magnetism the definitive synthesis',
     'key_work':'A Dynamical Theory of the Electromagnetic Field (1865); A Treatise on Electricity and Magnetism (1873)','date':'1864-1873','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_168','pioneer_id':'PION_166','node_id':'T3_MOD_006',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Experimentally detected electromagnetic radio waves (1887-1888) confirming Maxwell\'s theoretical prediction; measured their speed as equal to light; demonstrated reflection, refraction, and polarisation of radio waves',
     'key_work':'Über Strahlen elektrischer Kraft (1888)','date':'1887-1888','impact_level':'major','source_ids':'SRC_075'},

    # ── T3_MOD_007: Modern Optics ──────────────────────────────────────────────
    {'contribution_id':'CONTR_169','pioneer_id':'PION_185','node_id':'T3_MOD_007',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Formulated Kirchhoff\'s radiation law (1859) showing blackbody emission and absorption are equal at thermal equilibrium; defined blackbody concept whose radiation curve became the key puzzle leading to Planck\'s quantum hypothesis',
     'key_work':'Über den Zusammenhang zwischen Emission und Absorption von Licht und Wärme (1859)','date':'1859','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_170','pioneer_id':'PION_186','node_id':'T3_MOD_007',
     'contribution_type':'methodological_innovation',
     'specific_contribution':'Applied spectroscopy with Kirchhoff to solar and stellar analysis (1859-1862) enabling astrophysics; demonstrated solar absorption lines correspond to emission lines of known elements; introduced spectroscopy as primary method of astronomical chemistry',
     'key_work':'Chemical Analysis by Spectral Observations (1860)','date':'1859-1862','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_171','pioneer_id':'PION_196','node_id':'T3_MOD_007',
     'contribution_type':'instrumental_advance',
     'specific_contribution':'Designed Michelson interferometer (1881) enabling interference measurements of unprecedented precision; Michelson-Morley null ether result (1887) eliminated luminiferous ether; precision speed-of-light measurements; Nobel Physics 1907',
     'key_work':'On the Relative Motion of the Earth and Luminiferous Ether (1887)','date':'1881-1907','impact_level':'major','source_ids':'SRC_075'},

    # ── T3_MOD_008: Atomic/Nuclear Physics ────────────────────────────────────
    {'contribution_id':'CONTR_172','pioneer_id':'PION_168','node_id':'T3_MOD_008',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Discovered the electron (1897) by deflecting cathode rays in electric and magnetic fields and measuring charge-to-mass ratio; first subatomic particle identified; Thomson\'s plum-pudding atomic model proposed positive charge distributed throughout atom',
     'key_work':'Cathode Rays (1897)','date':'1897','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_173','pioneer_id':'PION_179','node_id':'T3_MOD_008',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Discovered radioactivity of thorium independently (1898); isolated radium and polonium from pitchblende (with Pierre Curie); coined the term radioactivity; first woman Nobel laureate (Physics 1903, Chemistry 1911); pioneered radioactive isotope research',
     'key_work':'Recherches sur les substances radioactives (1903)','date':'1896-1911','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_174','pioneer_id':'PION_180','node_id':'T3_MOD_008',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Geiger-Marsden gold-foil experiment (1909-1911) showed most alpha particles pass through but rare large-angle scattering proved a dense positive nucleus; nuclear model of atom replaced Thomson\'s plum-pudding model; coined proton and nucleus',
     'key_work':'The Scattering of α and β Particles by Matter (1911)','date':'1911','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_175','pioneer_id':'PION_189','node_id':'T3_MOD_008',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Discovered the neutron (1932) by bombarding beryllium with alpha particles and detecting neutral radiation; completed the nuclear particle picture with protons and neutrons; enabled precise nuclear mass calculations and opened nuclear physics',
     'key_work':'Possible Existence of a Neutron (1932)','date':'1932','impact_level':'major','source_ids':'SRC_076'},

    {'contribution_id':'CONTR_176','pioneer_id':'PION_190','node_id':'T3_MOD_008',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Built first controlled nuclear chain reaction (Chicago Pile-1, December 1942); Fermi theory of beta decay (1933) introducing weak interaction; neutron-induced transmutation enabling synthetic isotopes; Fermi-Dirac statistics for spin-half particles',
     'key_work':'Versuch einer Theorie der β-Strahlen (1934)','date':'1933-1942','impact_level':'major','source_ids':'SRC_076'},

    # ── T3_MOD_009: Quantum Mechanics ─────────────────────────────────────────
    {'contribution_id':'CONTR_177','pioneer_id':'PION_169','node_id':'T3_MOD_009',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Derived blackbody radiation formula (1900) requiring discrete energy quanta E=hν; introduced Planck constant h founding quantum theory; initial intention was a mathematical fix but it broke the classical continuum assumption irreversibly',
     'key_work':'Über eine Verbesserung der Wien\'schen Spektralgleichung (1900)','date':'1900','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_178','pioneer_id':'PION_170','node_id':'T3_MOD_009',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Proposed photon hypothesis (1905) explaining photoelectric effect as light quanta; extended Planck quanta to free light; Bose-Einstein statistics and condensate prediction (1924); wave-particle duality for light; stimulated emission principle (1917) enabling lasers',
     'key_work':'Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt (1905)','date':'1905','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_179','pioneer_id':'PION_171','node_id':'T3_MOD_009',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Proposed quantised orbital model of hydrogen (1913) with discrete energy levels explaining Balmer spectral series; introduced correspondence principle bridging quantum and classical; complementarity principle; Copenhagen interpretation of QM',
     'key_work':'On the Constitution of Atoms and Molecules (1913)','date':'1913','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_180','pioneer_id':'PION_172','node_id':'T3_MOD_009',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Proposed matter-wave hypothesis (1924): every particle has wavelength λ=h/p; extended wave-particle duality from photons to electrons and all matter; PhD thesis directly inspired Schrödinger equation; confirmed by Davisson-Germer electron diffraction (1927)',
     'key_work':'Recherches sur la théorie des quanta (1924)','date':'1924','impact_level':'major','source_ids':'SRC_076'},

    {'contribution_id':'CONTR_181','pioneer_id':'PION_173','node_id':'T3_MOD_009',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Developed matrix mechanics (1925) first complete formulation of quantum mechanics; uncertainty principle ΔxΔp ≥ ℏ/2 (1927) showing position and momentum cannot be simultaneously precisely known; quantum chromodynamics contributions',
     'key_work':'Über quantentheoretische Umdeutung kinematischer und mechanischer Beziehungen (1925)','date':'1925-1927','impact_level':'major','source_ids':'SRC_076'},

    {'contribution_id':'CONTR_182','pioneer_id':'PION_174','node_id':'T3_MOD_009',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Derived Schrödinger wave equation (1926) providing a differential equation formulation of quantum mechanics equivalent to Heisenberg matrices; time-dependent and time-independent forms; established wavefunction Ψ as central mathematical object',
     'key_work':'Quantisierung als Eigenwertproblem (1926)','date':'1926','impact_level':'major','source_ids':'SRC_076'},

    {'contribution_id':'CONTR_183','pioneer_id':'PION_175','node_id':'T3_MOD_009',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Probabilistic interpretation of wavefunction (Born rule, 1926): |Ψ|² gives probability density; justified QM as fundamentally probabilistic rather than deterministic; Born approximation for scattering cross-sections widely used in nuclear and atomic physics',
     'key_work':'Zur Quantenmechanik der Stossvorgänge (1926)','date':'1926','impact_level':'major','source_ids':'SRC_076'},

    {'contribution_id':'CONTR_184','pioneer_id':'PION_176','node_id':'T3_MOD_009',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Pauli exclusion principle (1925): no two fermions can occupy the same quantum state; explains periodic table structure and electron shell filling; predicted neutrino (1930) to conserve energy in beta decay; spin quantum number introduction',
     'key_work':'Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren (1925)','date':'1925','impact_level':'major','source_ids':'SRC_076'},

    {'contribution_id':'CONTR_185','pioneer_id':'PION_177','node_id':'T3_MOD_009',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Derived Dirac equation (1928) combining quantum mechanics and special relativity predicting antimatter (positron confirmed 1932); Dirac delta function; second quantisation founding quantum field theory; Dirac bracket notation and transformation theory',
     'key_work':'The Quantum Theory of the Electron (1928)','date':'1928-1932','impact_level':'major','source_ids':'SRC_076'},

    # ── T3_MOD_010: Relativity ─────────────────────────────────────────────────
    {'contribution_id':'CONTR_186','pioneer_id':'PION_170','node_id':'T3_MOD_010',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Special relativity (1905): Lorentz invariance, relativity of simultaneity, E=mc², time dilation; general relativity (1915): gravity as spacetime curvature, Einstein field equations; photoelectric effect; cosmological constant; Brownian motion atomic proof',
     'key_work':'Zur Elektrodynamik bewegter Körper (1905); Die Grundlage der allgemeinen Relativitätstheorie (1916)','date':'1905-1915','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_187','pioneer_id':'PION_181','node_id':'T3_MOD_010',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Derived Lorentz transformations (1904) for length contraction and time dilation in electrodynamics; electron mass-velocity relation precursing special relativity; Lorentz factor γ = 1/√(1-v²/c²); provided mathematical machinery Einstein used in special relativity',
     'key_work':'Electromagnetic phenomena in a system moving with any velocity smaller than that of light (1904)','date':'1904','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_188','pioneer_id':'PION_182','node_id':'T3_MOD_010',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Reformulated special relativity in 4D Minkowski spacetime (1908) showing space and time as aspects of a single 4D continuum; interval invariance; light cone structure; spacetime geometrical formalism adopted by Einstein for general relativity',
     'key_work':'Raum und Zeit (1908)','date':'1908','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_189','pioneer_id':'PION_183','node_id':'T3_MOD_010',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Led 1919 Principe solar eclipse expedition confirming general relativity\'s prediction of light bending; stellar structure theory (1920s) explaining stellar energy via nuclear reactions; stellar mass-luminosity relation; Eddington-Dirac large numbers coincidence',
     'key_work':'A Determination of the Deflection of Light by the Sun\'s Gravitational Field (1920)','date':'1919','impact_level':'major','source_ids':'SRC_076'},

    # ── T3_MOD_011: Statistical Mechanics ─────────────────────────────────────
    {'contribution_id':'CONTR_190','pioneer_id':'PION_161','node_id':'T3_MOD_011',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Derived entropy S = k·ln(W) (1877) as logarithm of microstates providing statistical basis for thermodynamic second law; Boltzmann H-theorem deriving irreversibility from molecular dynamics; Boltzmann distribution; defended atoms despite positivist opposition',
     'key_work':'Über die Beziehung zwischen dem zweiten Hauptsatze der mechanischen Wärmetheorie (1877)','date':'1872-1877','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_191','pioneer_id':'PION_165','node_id':'T3_MOD_011',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Derived Maxwell-Boltzmann speed distribution (1860) for gas molecules; kinetic theory of gases relating pressure, temperature and molecular speed; Maxwell\'s demon thought experiment; transport coefficients viscosity and diffusion from molecular theory',
     'key_work':'Illustrations of the Dynamical Theory of Gases (1860)','date':'1860','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_192','pioneer_id':'PION_150','node_id':'T3_MOD_011',
     'contribution_type':'mathematical_formulation',
     'specific_contribution':'Formulated ensemble statistical mechanics (1902) introducing microcanonical, canonical, and grand canonical ensembles; partition function; statistical derivation of thermodynamics from first principles; Gibbs phase rule; statistical chemical equilibrium',
     'key_work':'Elementary Principles in Statistical Mechanics (1902)','date':'1902','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_193','pioneer_id':'PION_170','node_id':'T3_MOD_011',
     'contribution_type':'foundational_idea',
     'specific_contribution':'Brownian motion theory (1905) calculating mean-square displacement proving atoms exist and enabling Avogadro number measurement; Bose-Einstein statistics (1924) for indistinguishable bosons; predicted Bose-Einstein condensate (confirmed 1995)',
     'key_work':'Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung (1905)','date':'1905','impact_level':'major','source_ids':'SRC_075'},

    {'contribution_id':'CONTR_194','pioneer_id':'PION_184','node_id':'T3_MOD_011',
     'contribution_type':'experimental_demonstration',
     'specific_contribution':'Measured sedimentation equilibrium of Brownian particles (1908-1913) yielding Avogadro\'s number to 0.5% accuracy; experimentally confirmed kinetic theory and proved atomic/molecular reality beyond doubt; Nobel Physics 1926',
     'key_work':'Mouvement brownien et réalité moléculaire (1909)','date':'1908-1913','impact_level':'major','source_ids':'SRC_076'},
]

print("Running Part 7a: Modern pioneer contributions (CONTR_144-194)")
append_rows('pioneer_contributions.csv', FIELDS, rows)
print(f"Part 7a complete. {len(rows)} contributions added.")
