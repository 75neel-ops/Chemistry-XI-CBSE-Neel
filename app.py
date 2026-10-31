"""
CBSE Class XI Chemistry (NCERT) - Learning Game  (Streamlit version)
Part 1: Key words of each chapter
Part 2: Tricky quiz with hints, congratulations / correct answer
Part 3: Chapter-wise practice questions (1, 2, 3 marks) with answers

To add content, add entries to the CHAPTERS dictionary (or to the EXTRA_ banks).
All questions are original practice material written to follow the NCERT
(rationalised) Class XI Chemistry syllabus - they are not copied from the book.
"""
import random

import streamlit as st

CHAPTERS = {
    1: {
        "name": "Some Basic Concepts of Chemistry",
        "keywords": [
            ("Mole", "Amount of substance containing 6.022 x 10^23 elementary entities (Avogadro number)."),
            ("Molar mass", "Mass of one mole of a substance in grams (g/mol)."),
            ("Limiting reagent", "The reactant that is used up first and decides how much product forms."),
            ("Significant figures", "Digits in a measurement that are known with certainty plus one uncertain digit."),
            ("Law of multiple proportions", "Masses of one element combining with a fixed mass of another are in a simple whole-number ratio."),
            ("Empirical formula", "Simplest whole-number ratio of atoms of each element in a compound."),
            ("Molality", "Moles of solute per kg of solvent; does not change with temperature."),
        ],
        "quiz": [
            ("Which concentration unit does NOT change with temperature?",
             ["Molarity", "Molality", "Normality", "Volume percent"], 1,
             "Think of what the unit divides by: volume or mass?",
             "Molality uses mass of solvent, and mass does not change with temperature. The others depend on volume."),
            ("How many significant figures are in 0.00250?",
             ["2", "3", "5", "6"], 1,
             "Leading zeros do not count; a trailing zero after the decimal point does.",
             "Significant digits are 2, 5, 0, so 3."),
            ("4 g of H2 is mixed with 16 g of O2 and reacted to form water (2H2 + O2 -> 2H2O). What mass of water forms?",
             ["36 g", "18 g", "20 g", "9 g"], 1,
             "Convert both reactants to moles first and find which one runs out.",
             "H2 = 2 mol, O2 = 0.5 mol. O2 is limiting: 0.5 mol O2 gives 1 mol H2O = 18 g."),
            ("16 g of O2 and 16 g of O3 contain:",
             ["The same number of molecules", "The same number of oxygen atoms",
              "More atoms in O3", "More atoms in O2"], 1,
             "Both samples are made only of oxygen atoms. Compare the masses.",
             "Same mass of the same element means the same number of atoms. Molecules differ (O2 has more)."),
        ],
        "practice": [
            (1, "State the law of multiple proportions.",
             "When two elements form more than one compound, the different masses of one element that combine with a fixed mass of the other are in a simple whole-number ratio."),
            (2, "Calculate the mass of 0.25 mol of CO2.",
             "Molar mass of CO2 = 44 g/mol. Mass = 0.25 x 44 = 11 g."),
            (2, "Calculate the molarity of a solution containing 4 g NaOH in 500 mL of solution.",
             "Moles = 4/40 = 0.1 mol. Molarity = 0.1 / 0.5 L = 0.2 M."),
            (3, "A compound has 40% C, 6.7% H and 53.3% O. Its molar mass is 180 g/mol. Find the empirical and molecular formula.",
             "Mole ratio C : H : O = 3.33 : 6.7 : 3.33 = 1 : 2 : 1, so empirical formula CH2O (mass 30). 180/30 = 6, so molecular formula C6H12O6."),
        ],
    },
    2: {
        "name": "Structure of Atom",
        "keywords": [
            ("Quantum numbers", "n, l, ml, ms: describe size, shape, orientation and spin of an electron's orbital."),
            ("Heisenberg uncertainty principle", "Position and momentum of a small particle cannot both be known exactly at the same time."),
            ("de Broglie wavelength", "Matter has wave nature; wavelength = h / (mv)."),
            ("Aufbau principle", "Electrons fill orbitals in order of increasing energy ((n + l) rule)."),
            ("Hund's rule", "Degenerate orbitals are singly occupied (same spin) before pairing begins."),
            ("Pauli exclusion principle", "No two electrons in an atom can have the same set of all four quantum numbers."),
            ("Photoelectric effect", "Emission of electrons from a metal surface when light above a threshold frequency falls on it."),
            ("Node", "Region where the probability of finding an electron is zero."),
        ],
        "quiz": [
            ("What is the maximum number of electrons that can be accommodated in the shell with n = 3?",
             ["8", "18", "32", "9"], 1, "Use the 2n^2 formula.", "2 x 3^2 = 18."),
            ("How many radial nodes does a 3p orbital have?",
             ["0", "1", "2", "3"], 1, "Radial nodes = n - l - 1.", "n = 3, l = 1, so 3 - 1 - 1 = 1."),
            ("Which is the correct ground-state configuration of chromium (Z = 24)?",
             ["[Ar] 3d4 4s2", "[Ar] 3d5 4s1", "[Ar] 3d6", "[Ar] 4s2 4p4"], 1,
             "Half-filled d subshell gives extra stability.",
             "One electron shifts from 4s to 3d, giving a half-filled, symmetric 3d5."),
            ("Which set of quantum numbers (n, l, ml, ms) is NOT possible?",
             ["(3, 2, -2, +1/2)", "(2, 2, 0, -1/2)", "(4, 3, 3, +1/2)", "(1, 0, 0, -1/2)"], 1,
             "Check the rule linking l and n.",
             "l can go only from 0 to n - 1. For n = 2, l = 2 is not allowed."),
        ],
        "practice": [
            (1, "State the Pauli exclusion principle.",
             "No two electrons in an atom can have identical values of all four quantum numbers; an orbital holds at most two electrons of opposite spin."),
            (2, "Write the four quantum numbers of the outermost electron of sodium (Z = 11).",
             "Configuration [Ne] 3s1, so n = 3, l = 0, ml = 0, ms = +1/2 (or -1/2)."),
            (2, "Write the electronic configuration of Fe (Z = 26) and Fe3+.",
             "Fe: [Ar] 3d6 4s2. Fe3+: [Ar] 3d5 (4s electrons are lost first)."),
            (3, "Calculate the energy of one photon of light of wavelength 500 nm. (h = 6.626 x 10^-34 J s, c = 3 x 10^8 m/s)",
             "E = hc / wavelength = (6.626e-34 x 3e8) / 5e-7 = about 3.98 x 10^-19 J."),
        ],
    },
    3: {
        "name": "Classification of Elements and Periodicity in Properties",
        "keywords": [
            ("Modern periodic law", "Properties of elements are periodic functions of their atomic numbers."),
            ("Ionisation enthalpy", "Energy needed to remove the outermost electron from an isolated gaseous atom."),
            ("Electron gain enthalpy", "Enthalpy change when a gaseous atom gains an electron."),
            ("Electronegativity", "Tendency of an atom in a molecule to attract the shared pair of electrons."),
            ("Isoelectronic species", "Atoms or ions with the same number of electrons."),
            ("Screening effect", "Inner electrons shield outer electrons from the full nuclear charge."),
            ("Effective nuclear charge", "Net positive charge felt by an outer electron (Z minus shielding)."),
            ("Diagonal relationship", "Similarity between an element and the one diagonally below-right (e.g. Li and Mg)."),
        ],
        "quiz": [
            ("Which element has the most negative electron gain enthalpy?",
             ["Fluorine", "Chlorine", "Bromine", "Oxygen"], 1,
             "The smallest atom is not the winner here; think about electron-electron repulsion.",
             "Chlorine. Fluorine's small 2p subshell causes strong repulsion, so its value is less negative."),
            ("Which has the largest radius: O2-, F-, Na+, Mg2+?",
             ["O2-", "F-", "Na+", "Mg2+"], 0,
             "All have 10 electrons. What differs is the number of protons.",
             "In isoelectronic species, fewer protons means weaker pull and larger size. O2- has 8 protons."),
            ("Which has the higher first ionisation enthalpy?",
             ["Boron", "Beryllium", "Both are equal", "Cannot be predicted"], 1,
             "Think about which outer subshell is fully filled.",
             "Be (2s2) removes an electron from a stable filled s orbital; B (2s2 2p1) loses a higher-energy p electron."),
            ("What is the IUPAC temporary name for the element with Z = 120?",
             ["Unbinilium", "Ununbium", "Unnilbium", "Unbiunium"], 0,
             "Digits: 1 = un, 2 = bi, 0 = nil. End with -ium.",
             "1-2-0 gives un + bi + nil + ium = Unbinilium."),
        ],
        "practice": [
            (1, "State the modern periodic law.",
             "The physical and chemical properties of elements are periodic functions of their atomic numbers."),
            (2, "Why is the first ionisation enthalpy of nitrogen higher than that of oxygen?",
             "Nitrogen has a stable half-filled 2p3 configuration. In oxygen (2p4) one orbital has paired electrons whose repulsion makes removal easier."),
            (2, "Why is the electron gain enthalpy of fluorine less negative than that of chlorine?",
             "Fluorine's very small 2p subshell has strong inter-electronic repulsion, which reduces the energy released on adding an electron."),
            (3, "Arrange Na+, Mg2+, F-, O2- in increasing order of ionic radius and justify.",
             "Mg2+ < Na+ < F- < O2-. All have 10 electrons; greater nuclear charge pulls the electron cloud in more strongly."),
        ],
    },
    4: {
        "name": "Chemical Bonding and Molecular Structure",
        "keywords": [
            ("Octet rule", "Atoms tend to have eight electrons in the valence shell."),
            ("VSEPR theory", "Shape of a molecule is decided by repulsion between electron pairs (lp-lp > lp-bp > bp-bp)."),
            ("Hybridisation", "Mixing of atomic orbitals of similar energy to form new equivalent hybrid orbitals."),
            ("Bond order", "Half the difference between bonding and antibonding electrons."),
            ("Dipole moment", "Product of charge and distance between charges; a vector quantity."),
            ("Resonance", "Actual structure is a hybrid of two or more contributing structures."),
            ("Sigma and pi bonds", "Sigma: head-on overlap. Pi: sideways overlap of p orbitals."),
            ("Formal charge", "Valence electrons - non-bonding electrons - half the bonding electrons."),
            ("Hydrogen bond", "Attraction between H bonded to N, O or F and a lone pair on another N, O or F."),
        ],
        "quiz": [
            ("What is the shape of the NH3 molecule?",
             ["Planar triangular", "Trigonal pyramidal", "Tetrahedral", "Bent"], 1,
             "Count bond pairs and lone pairs on nitrogen.",
             "3 bond pairs + 1 lone pair gives a tetrahedral arrangement of pairs but a pyramidal molecular shape."),
            ("What is the bond order of O2+?",
             ["1.5", "2", "2.5", "3"], 2,
             "O2 has 2. Which electron is removed to form the cation, bonding or antibonding?",
             "An antibonding pi* electron is removed, so bond order = (10 - 5) / 2 = 2.5."),
            ("Which of these is paramagnetic?",
             ["N2", "O2", "F2", "C2"], 1,
             "Look for unpaired electrons in the molecular orbital diagram.",
             "O2 has two unpaired electrons in pi* orbitals. N2, F2 and C2 are diamagnetic."),
            ("NH3 and NF3 both are pyramidal. Which has the larger dipole moment?",
             ["NH3", "NF3", "Equal", "Both are zero"], 0,
             "Compare the direction of the N-X bond dipoles with the lone-pair dipole.",
             "In NH3 the bond dipoles add to the lone-pair dipole; in NF3 they oppose it, so the net value is small."),
        ],
        "practice": [
            (1, "Define bond order.",
             "Half the difference between the number of electrons in bonding and antibonding molecular orbitals."),
            (2, "Why is the H-O-H angle in water 104.5 degrees and not 109.5 degrees?",
             "Oxygen is sp3 hybridised with two lone pairs. Lone pair-lone pair repulsion is greater than bond pair repulsion, which compresses the angle."),
            (3, "Write the molecular orbital configuration of N2. State its bond order and magnetic behaviour.",
             "(sigma1s)2 (sigma*1s)2 (sigma2s)2 (sigma*2s)2 (pi2px)2 (pi2py)2 (sigma2pz)2. Bond order = (10 - 4)/2 = 3. Diamagnetic."),
            (3, "Explain the hybridisation of carbon in ethene.",
             "Each carbon is sp2 hybridised. Two sp2 orbitals form C-H sigma bonds and one forms the C-C sigma bond; the unhybridised p orbitals overlap sideways to form the pi bond. The molecule is planar with 120 degree angles."),
        ],
    },
    5: {
        "name": "Thermodynamics",
        "keywords": [
            ("System and surroundings", "System is the part under study; everything else is surroundings."),
            ("State function", "Property depending only on the initial and final state (U, H, S, G), not the path."),
            ("Enthalpy (H)", "H = U + PV; heat change at constant pressure equals delta H."),
            ("Hess's law", "Total enthalpy change is the same whether a reaction occurs in one step or several."),
            ("Entropy (S)", "Measure of disorder or randomness of a system."),
            ("Gibbs energy (G)", "G = H - TS; delta G < 0 means a process is spontaneous."),
            ("Standard enthalpy of formation", "Enthalpy change when 1 mol of a compound forms from its elements in their standard states."),
            ("Bond enthalpy", "Energy required to break one mole of a particular bond in the gas phase."),
        ],
        "quiz": [
            ("Which of these is NOT a state function?",
             ["Enthalpy", "Entropy", "Internal energy", "Work"], 3,
             "Which one depends on how you get from A to B?",
             "Work (and heat) are path functions."),
            ("A reaction has negative delta H and negative delta S. It is spontaneous at:",
             ["All temperatures", "No temperature", "Low temperature", "High temperature"], 2,
             "Use delta G = delta H - T delta S and see when the T term stays small.",
             "At low T the negative delta H dominates, so delta G is negative."),
            ("For N2(g) + 3H2(g) -> 2NH3(g), delta H - delta U equals:",
             ["+2RT", "-2RT", "-4RT", "0"], 1,
             "Use delta n(g) = moles of gaseous products - moles of gaseous reactants.",
             "delta n(g) = 2 - 4 = -2, so delta H - delta U = -2RT."),
            ("The standard enthalpy of formation of ozone, O3(g), is:",
             ["Zero", "Positive", "Negative", "Cannot be said"], 1,
             "Which form of oxygen is the reference state, O2 or O3?",
             "Zero applies only to O2, the stable standard state. Making O3 from O2 absorbs energy, so it is positive."),
        ],
        "practice": [
            (1, "State the first law of thermodynamics.",
             "Energy can neither be created nor destroyed: delta U = q + w."),
            (2, "Differentiate between extensive and intensive properties with examples.",
             "Extensive properties depend on the amount of matter (mass, volume, enthalpy). Intensive properties do not (temperature, density, pressure)."),
            (3, "Given C(graphite) + O2 -> CO2, delta H = -393.5 kJ and CO + 1/2 O2 -> CO2, delta H = -283.0 kJ, find the enthalpy of formation of CO.",
             "Subtract the second from the first: C + 1/2 O2 -> CO, delta H = -393.5 + 283.0 = -110.5 kJ/mol."),
            (3, "For a reaction delta H = +30 kJ and delta S = +100 J/K. Above what temperature is it spontaneous?",
             "delta G < 0 when T > delta H / delta S = 30000 / 100 = 300 K."),
        ],
    },
    6: {
        "name": "Equilibrium",
        "keywords": [
            ("Le Chatelier's principle", "A system at equilibrium shifts to oppose any change in concentration, pressure or temperature."),
            ("Kc and Kp", "Equilibrium constants in terms of concentrations and partial pressures; Kp = Kc (RT)^(delta n)."),
            ("Reaction quotient (Q)", "Same expression as K at any moment. Q < K: reaction goes forward."),
            ("Common ion effect", "Suppression of ionisation of a weak electrolyte by adding a common ion."),
            ("Buffer solution", "Resists change in pH on adding small amounts of acid or base."),
            ("pH", "Negative log of hydrogen ion concentration."),
            ("Solubility product (Ksp)", "Product of ion concentrations in a saturated solution of a sparingly soluble salt."),
            ("Conjugate acid-base pair", "Two species differing by one proton."),
            ("Lewis acid", "Electron pair acceptor."),
        ],
        "quiz": [
            ("What is the pH of 10^-8 M HCl at 25 C?",
             ["8", "Slightly below 7", "Exactly 7", "6"], 1,
             "Don't forget that water itself supplies H+ ions.",
             "Total [H+] is 10^-8 + 10^-7 = 1.1 x 10^-7 M, so pH is about 6.96."),
            ("For which reaction is Kp equal to Kc?",
             ["N2 + 3H2 <-> 2NH3", "H2 + I2 <-> 2HI", "PCl5 <-> PCl3 + Cl2", "2SO2 + O2 <-> 2SO3"], 1,
             "Kp = Kc (RT)^(delta n). When is the exponent zero?",
             "For H2 + I2 <-> 2HI, delta n = 2 - 2 = 0."),
            ("An inert gas is added to the equilibrium N2 + 3H2 <-> 2NH3 at constant volume. The equilibrium:",
             ["Shifts forward", "Shifts backward", "Does not change", "Stops"], 2,
             "Do the partial pressures of reacting gases change?",
             "At constant volume the concentrations of the reacting gases remain the same, so no shift."),
            ("What is the conjugate base of H2PO4-?",
             ["H3PO4", "HPO4(2-)", "PO4(3-)", "OH-"], 1,
             "A conjugate base is formed by LOSING a proton.",
             "H2PO4- loses H+ to give HPO4(2-)."),
        ],
        "practice": [
            (1, "State Le Chatelier's principle.",
             "If a stress (change in concentration, pressure or temperature) is applied to a system at equilibrium, the system shifts in the direction that reduces the stress."),
            (2, "Why does the solubility of AgCl decrease on adding NaCl?",
             "Common ion effect: extra Cl- shifts AgCl(s) <-> Ag+ + Cl- to the left, so less AgCl dissolves."),
            (3, "Write the Kc expression for N2 + 3H2 <-> 2NH3 and connect Kp with Kc.",
             "Kc = [NH3]^2 / ([N2][H2]^3). Kp = Kc (RT)^(delta n) with delta n = -2, so Kp = Kc (RT)^-2."),
            (3, "Calculate the pH of 0.01 M HCl and of 0.001 M NaOH.",
             "HCl: pH = 2. NaOH: pOH = 3, so pH = 14 - 3 = 11."),
        ],
    },
    7: {
        "name": "Redox Reactions",
        "keywords": [
            ("Oxidation and reduction", "Oxidation: loss of electrons (oxidation number increases). Reduction: gain of electrons."),
            ("Oxidation number", "Hypothetical charge on an atom if all bonds were ionic."),
            ("Oxidising agent", "Substance that gains electrons (gets reduced)."),
            ("Reducing agent", "Substance that loses electrons (gets oxidised)."),
            ("Disproportionation", "Same element is simultaneously oxidised and reduced."),
            ("Half-reaction", "Separate oxidation or reduction part of a redox equation."),
            ("Electrochemical series", "Metals/ions arranged by standard electrode potential."),
            ("Stock notation", "Oxidation state written in Roman numerals, e.g. Fe(III) oxide."),
        ],
        "quiz": [
            ("What is the average oxidation number of sulphur in Na2S4O6?",
             ["+2", "+2.5", "+3", "+6"], 1,
             "2(+1) + 4x + 6(-2) = 0.", "4x = 10, so x = +2.5 (an average value)."),
            ("What is the oxidation state of oxygen in OF2?",
             ["-2", "-1", "0", "+2"], 3,
             "Compare the electronegativity of F and O.",
             "Fluorine is more electronegative, so oxygen is +2."),
            ("Which is a disproportionation reaction?",
             ["Zn + CuSO4 -> ZnSO4 + Cu", "2H2O2 -> 2H2O + O2", "H2 + Cl2 -> 2HCl", "CaCO3 -> CaO + CO2"], 1,
             "Look for one species whose same element goes both up and down.",
             "In H2O2, oxygen goes from -1 to -2 (in H2O) and to 0 (in O2)."),
            ("Which of these can act ONLY as a reducing agent?",
             ["SO2", "H2S", "H2SO4", "HNO2"], 1,
             "Check whether the central element can still be oxidised but cannot be reduced.",
             "S in H2S is at its lowest state (-2), so it can only increase."),
        ],
        "practice": [
            (1, "Define oxidation in terms of electron transfer.",
             "Oxidation is loss of electrons by an atom, ion or molecule."),
            (2, "Find the oxidation number of Mn in KMnO4 and Cr in Cr2O7(2-).",
             "Mn = +7. Cr = +6."),
            (2, "Why can copper not displace zinc from zinc sulphate solution?",
             "Zinc is above copper in the electrochemical series (more reactive, more negative E), so Cu cannot reduce Zn2+."),
            (3, "Balance in acidic medium: MnO4- + Fe2+ -> Mn2+ + Fe3+.",
             "MnO4- + 8H+ + 5Fe2+ -> Mn2+ + 4H2O + 5Fe3+."),
        ],
    },
    8: {
        "name": "Organic Chemistry - Some Basic Principles and Techniques",
        "keywords": [
            ("Functional group", "Atom or group that decides the characteristic reactions of a compound."),
            ("Homologous series", "Family of compounds with the same functional group differing by CH2."),
            ("Inductive effect", "Permanent polarisation of a sigma bond due to electronegativity difference, transmitted along the chain."),
            ("Resonance (mesomeric) effect", "Delocalisation of pi electrons or lone pairs through conjugation."),
            ("Hyperconjugation", "Delocalisation of sigma electrons of C-H into an adjacent empty p or pi orbital."),
            ("Electrophile and nucleophile", "Electrophile loves electrons (electron-poor); nucleophile donates an electron pair."),
            ("Carbocation", "Carbon with a positive charge and sextet; order 3 > 2 > 1 > methyl."),
            ("Isomerism", "Same molecular formula, different structures (chain, position, functional, metamerism)."),
            ("Lassaigne's test", "Sodium fusion extract used to detect N, S and halogens."),
            ("Chromatography", "Separation based on differential movement over a stationary phase."),
        ],
        "quiz": [
            ("Which carbocation is the most stable?",
             ["CH3+", "CH3CH2+", "(CH3)2CH+", "(CH3)3C+"], 3,
             "Count the alkyl groups available for hyperconjugation and the +I effect.",
             "The tertiary carbocation has nine C-H bonds for hyperconjugation and three +I groups."),
            ("What is the IUPAC name of CH3-CH(CH3)-CH2-CH3?",
             ["Isopentane", "2-Methylbutane", "3-Methylbutane", "Pentane"], 1,
             "Find the longest chain, then number to give the substituent the lowest locant.",
             "Longest chain has 4 carbons with a methyl at C-2."),
            ("In Lassaigne's test, nitrogen is confirmed by the formation of a:",
             ["Red colour", "Prussian blue colour", "Yellow precipitate", "Black precipitate"], 1,
             "Iron(II) and iron(III) take part here.",
             "Sodium cyanide, then ferrocyanide, then ferric ferrocyanide, which is Prussian blue."),
            ("How many sigma and pi bonds are present in propyne, CH3-C triple-bond CH?",
             ["6 sigma, 2 pi", "7 sigma, 1 pi", "5 sigma, 3 pi", "6 sigma, 1 pi"], 0,
             "Count C-H bonds first, then the C-C bonds, remembering a triple bond is 1 sigma + 2 pi.",
             "4 C-H + 1 C-C + 1 sigma of triple bond = 6 sigma; triple bond has 2 pi."),
        ],
        "practice": [
            (1, "What is a homologous series?",
             "A series of organic compounds with the same functional group and similar chemical properties, successive members differing by a CH2 unit."),
            (2, "Write the IUPAC name of CH3CH2CH(OH)CH3.",
             "Butan-2-ol."),
            (2, "Explain the principle of paper chromatography.",
             "It is partition chromatography: components distribute between water held on the paper (stationary phase) and the mobile solvent; components with different solubilities travel different distances (Rf values)."),
            (3, "Explain the inductive effect with examples of +I and -I groups.",
             "It is the permanent polarisation of a sigma bond transmitted through the chain. +I groups: alkyl groups (CH3-). -I groups: -NO2, -CN, -F, -Cl. The effect weakens rapidly with distance."),
        ],
    },
    9: {
        "name": "Hydrocarbons",
        "keywords": [
            ("Alkane, alkene, alkyne", "Saturated; C=C double bond; C triple bond C. General formulas CnH2n+2, CnH2n, CnH2n-2."),
            ("Markovnikov's rule", "In addition of HX to an unsymmetrical alkene, the negative part goes to the carbon with fewer hydrogens."),
            ("Peroxide (Kharasch) effect", "In presence of peroxide, HBr adds to alkenes in anti-Markovnikov fashion."),
            ("Wurtz reaction", "Alkyl halide + Na in dry ether gives a higher alkane."),
            ("Aromaticity", "Cyclic, planar, fully conjugated, with (4n + 2) pi electrons (Huckel rule)."),
            ("Electrophilic substitution", "Characteristic reaction of benzene: nitration, halogenation, sulphonation, Friedel-Crafts."),
            ("Ozonolysis", "Cleavage of C=C by ozone then Zn/H2O to give carbonyl compounds."),
            ("Conformations", "Different arrangements of atoms by rotation about a C-C single bond (staggered is more stable than eclipsed)."),
        ],
        "quiz": [
            ("Which of these follows Huckel's rule and is aromatic?",
             ["Cyclobutadiene", "Cyclooctatetraene", "Benzene", "Cyclopentane"], 2,
             "Need a cyclic, planar, conjugated ring with 4n + 2 pi electrons.",
             "Benzene has 6 pi electrons (n = 1)."),
            ("HBr is added to propene in the presence of peroxide. The major product is:",
             ["2-Bromopropane", "1-Bromopropane", "Propane", "Allyl bromide"], 1,
             "Peroxide reverses the usual orientation.",
             "Free radical mechanism gives the anti-Markovnikov product, 1-bromopropane."),
            ("Which hydrocarbon is the most acidic?",
             ["Ethane", "Ethene", "Ethyne", "Methane"], 2,
             "Think of the s-character of the carbon bonded to hydrogen.",
             "sp carbon (50% s) is the most electronegative, so the terminal H of ethyne is the most acidic."),
            ("Ozonolysis of but-2-ene followed by reductive work-up gives:",
             ["Methanal only", "Two molecules of ethanal", "Propanal and methanal", "Butanal"], 1,
             "Break the double bond and put an oxygen on each carbon.",
             "CH3-CH=CH-CH3 is symmetrical and gives 2 CH3CHO."),
        ],
        "practice": [
            (1, "State Markovnikov's rule.",
             "When an unsymmetrical reagent HX adds across an unsymmetrical alkene, the negative part (X) attaches to the carbon bearing fewer hydrogen atoms."),
            (2, "Give the Wurtz reaction for preparing ethane.",
             "2 CH3Br + 2 Na (dry ether) -> CH3-CH3 + 2 NaBr."),
            (3, "Why is benzene aromatic?",
             "It is cyclic, planar and fully conjugated with 6 delocalised pi electrons, satisfying Huckel's (4n + 2) rule for n = 1, which gives extra resonance stability."),
            (3, "Write the products of ozonolysis of propene.",
             "Methanal (HCHO) and ethanal (CH3CHO)."),
        ],
    },
}

EXTRA_A = {
    1: {
        "quiz": [
            ("How many atoms are present in 0.5 mol of water (H2O)?",
             ["3.011 x 10^23", "9.033 x 10^23", "1.8 x 10^24", "6.022 x 10^23"], 1,
             "Count atoms per molecule first.",
             "0.5 mol = 3.011 x 10^23 molecules, each with 3 atoms, so 9.033 x 10^23 atoms."),
            ("Which of these contains the largest number of atoms in 1 g?",
             ["Li", "Na", "K", "Mg"], 0,
             "Same mass: the lightest atom gives the most atoms.",
             "Li has the lowest molar mass (7 g/mol), so 1 g has the most atoms."),
            ("1 g of hydrogen combines with 8 g oxygen to form H2O, and with 16 g oxygen to form H2O2. Which law does this show?",
             ["Conservation of mass", "Definite proportions", "Multiple proportions", "Gay-Lussac's law"], 2,
             "Compare the two oxygen masses for the same 1 g of hydrogen.",
             "The oxygen masses 8 : 16 = 1 : 2, a simple whole-number ratio."),
            ("10 mL of 1 M HCl is diluted to 100 mL. The new molarity is:",
             ["0.01 M", "0.1 M", "1 M", "10 M"], 1,
             "Use M1V1 = M2V2.", "1 x 10 = M2 x 100, so M2 = 0.1 M."),
            ("10 g NaCl is dissolved in 90 g water. The mass percent of NaCl is:",
             ["11.1 %", "10 %", "9 %", "90 %"], 1,
             "Divide by the mass of the SOLUTION, not the solvent.",
             "10 / (10 + 90) x 100 = 10 %."),
            ("How many significant figures are in 6.022 x 10^23?",
             ["3", "4", "23", "26"], 1,
             "Only the digits before the power of ten count.", "6, 0, 2, 2 gives 4."),
            ("The sum 2.5 + 3.76 should be reported (with correct significant-figure rules) as:",
             ["6.26", "6.3", "6", "6.2"], 1,
             "For addition, round to the least number of decimal places.",
             "2.5 has one decimal place, so 6.26 becomes 6.3."),
            ("The molar volume of an ideal gas at 273.15 K and 1 bar (current IUPAC STP) is about:",
             ["22.4 L", "22.7 L", "24.0 L", "11.2 L"], 1,
             "22.4 L belongs to 1 atm.", "At 1 bar the value is 22.7 L/mol (22.4 L at 1 atm)."),
            ("A hydrocarbon has 92.3 % carbon and 7.7 % hydrogen. Its empirical formula is:",
             ["CH", "CH2", "C2H3", "C3H4"], 0,
             "Divide percentages by atomic masses (12 and 1).", "7.69 : 7.7 = 1 : 1, so CH."),
            ("5 mol N2 and 9 mol H2 react: N2 + 3H2 -> 2NH3. Maximum NH3 formed is:",
             ["10 mol", "6 mol", "9 mol", "4.5 mol"], 1,
             "Find which reactant is limiting.",
             "H2 is limiting: 9 mol H2 gives 9 x 2/3 = 6 mol NH3."),
            ("1 mol ethanol is mixed with 3 mol water. The mole fraction of ethanol is:",
             ["0.25", "0.33", "0.75", "0.5"], 0,
             "Mole fraction = moles of component / total moles.", "1 / (1 + 3) = 0.25."),
            ("Which of the following is NOT an SI base unit?",
             ["Mole", "Kelvin", "Newton", "Ampere"], 2,
             "Newton is built from other units.", "Newton = kg m s^-2 is a derived unit."),
            ("Equal volumes of H2 and He at the same T and P contain the same number of:",
             ["Atoms", "Molecules", "Protons", "Neutrons"], 1,
             "H2 is diatomic and He is monatomic.", "Avogadro's law concerns molecules, not atoms."),
            ("The mass of one atom of carbon-12 is approximately:",
             ["1.99 x 10^-23 g", "2 x 10^-24 g", "12 g", "1.66 x 10^-24 g"], 0,
             "Molar mass divided by Avogadro number.", "12 / 6.022 x 10^23 = 1.99 x 10^-23 g."),
            ("18 g glucose (M = 180) is dissolved in 500 g water. The molality is:",
             ["0.1 m", "0.2 m", "0.36 m", "2 m"], 1,
             "Molality uses kg of solvent.", "0.1 mol / 0.5 kg = 0.2 m."),
            ("The number of molecules in 4.4 g of CO2 is:",
             ["6.022 x 10^22", "6.022 x 10^23", "1.2 x 10^23", "4.4"], 0,
             "Moles first.", "4.4 / 44 = 0.1 mol = 6.022 x 10^22 molecules."),
        ],
        "practice": [
            (1, "Define molarity.", "Number of moles of solute dissolved per litre of solution (mol/L)."),
            (1, "State the law of definite proportions.",
             "A pure compound always contains the same elements combined in the same fixed proportion by mass, whatever its source."),
            (2, "Calculate the number of molecules in 18 g of water.",
             "18 g = 1 mol, so 6.022 x 10^23 molecules."),
            (2, "How many significant figures are in 0.0450 and in 1.200 x 10^3?",
             "0.0450 has 3 (leading zeros do not count). 1.200 x 10^3 has 4."),
            (2, "Calculate the mass percent of each element in H2SO4 (H = 1, S = 32, O = 16).",
             "M = 98. H = 2/98 x 100 = 2.04 %, S = 32/98 x 100 = 32.65 %, O = 64/98 x 100 = 65.31 %."),
            (2, "How many grams of NaOH are needed to prepare 250 mL of 0.5 M solution?",
             "Moles = 0.5 x 0.25 = 0.125. Mass = 0.125 x 40 = 5 g."),
            (3, "10 g of CaCO3 is heated: CaCO3 -> CaO + CO2. Find the mass of CaO and the volume of CO2 at STP.",
             "10 g = 0.1 mol. CaO = 0.1 x 56 = 5.6 g. CO2 = 0.1 mol = 2.27 L at 1 bar (2.24 L at 1 atm)."),
            (3, "A hydrocarbon has 85.7 % C and 14.3 % H and molar mass 42. Find its molecular formula.",
             "C : H = 7.14 : 14.3 = 1 : 2, so CH2 (mass 14). 42/14 = 3, so C3H6."),
            (3, "Calculate the molarity of a solution made by dissolving 49 g H2SO4 in water to make 2.5 L of solution.",
             "Moles = 49/98 = 0.5. Molarity = 0.5/2.5 = 0.2 M."),
        ],
    },
    2: {
        "quiz": [
            ("Which orbital has the HIGHEST energy in a multi-electron atom?",
             ["3d", "4s", "4p", "3p"], 2,
             "Use (n + l). If equal, the larger n is higher.",
             "3d = 5, 4p = 5 (tie), but 4p has the larger n, so it is higher. 4s and 3p = 4."),
            ("The total number of orbitals in the shell with n = 4 is:",
             ["4", "9", "16", "32"], 2, "Use n^2.", "n^2 = 16 orbitals (holding 32 electrons)."),
            ("How many unpaired electrons are present in Mn2+ (Z = 25)?",
             ["3", "4", "5", "6"], 2,
             "Write the configuration after removing the 4s electrons.", "Mn2+ is [Ar] 3d5, with 5 unpaired electrons."),
            ("If the velocity of a moving electron is doubled, its de Broglie wavelength becomes:",
             ["Double", "Half", "Four times", "Unchanged"], 1,
             "Wavelength = h / mv.", "Wavelength is inversely proportional to velocity."),
            ("Which of these is NOT hydrogen-like (one-electron species)?",
             ["H", "He+", "Li+", "Be3+"], 2,
             "Count electrons, not protons.", "Li+ has 2 electrons."),
            ("The radius of the 2nd Bohr orbit of hydrogen compared with the 1st is:",
             ["2 times", "4 times", "8 times", "1/4"], 1, "r is proportional to n^2.", "r2 / r1 = 4."),
            ("The energy of the electron in the n = 2 level of hydrogen is:",
             ["-13.6 eV", "-3.4 eV", "-6.8 eV", "-1.51 eV"], 1,
             "E = -13.6 / n^2 eV.", "-13.6 / 4 = -3.4 eV."),
            ("Which spectral series of hydrogen lies in the visible region?",
             ["Lyman", "Balmer", "Paschen", "Brackett"], 1,
             "Transitions ending at n = 2.", "Balmer series (n -> 2)."),
            ("How many radial nodes does a 2s orbital have?",
             ["0", "1", "2", "3"], 1, "n - l - 1.", "2 - 0 - 1 = 1."),
            ("The number of angular nodes in a 4f orbital is:",
             ["1", "2", "3", "4"], 2, "Angular nodes = l.", "For f, l = 3."),
            ("The correct ground state configuration of copper (Z = 29) is:",
             ["[Ar] 3d9 4s2", "[Ar] 3d10 4s1", "[Ar] 3d8 4s2 4p1", "[Ar] 3d10 4s2"], 1,
             "Completely filled d subshell is extra stable.", "One 4s electron shifts to 3d, giving 3d10 4s1."),
            ("Which of these is isoelectronic with argon?",
             ["K+", "Na+", "F-", "Mg2+"], 0, "Argon has 18 electrons.", "K+ has 19 - 1 = 18 electrons."),
            ("In Rutherford's experiment a very small fraction of alpha particles bounced back. This showed:",
             ["Electrons move in orbits", "The atom is a solid sphere",
              "The nucleus is small, dense and positive", "Neutrons exist"], 2,
             "Think about what could repel a heavy positive particle.",
             "A tiny, dense, positively charged nucleus."),
            ("Light below the threshold frequency falls on a metal. If its intensity is increased greatly:",
             ["More electrons are emitted", "Electrons get higher kinetic energy",
              "Still no electrons are emitted", "Emission is delayed"], 2,
             "Energy depends on frequency, not intensity.",
             "Each photon is too weak to free an electron, however many arrive."),
            ("The maximum number of electrons in an atom with l = 2 (any n) in a single subshell is:",
             ["6", "10", "14", "2"], 1, "A d subshell has 5 orbitals.", "5 x 2 = 10."),
            ("Which quantum number determines the orientation of an orbital in space?",
             ["n", "l", "ml", "ms"], 2, "It takes values from -l to +l.", "The magnetic quantum number ml."),
        ],
        "practice": [
            (1, "State the Heisenberg uncertainty principle.",
             "It is impossible to determine simultaneously and exactly both the position and momentum of an electron: delta x . delta p >= h / 4 pi."),
            (1, "What is an orbital?", "The three-dimensional region around the nucleus where the probability of finding an electron is maximum."),
            (2, "Write the electronic configuration of Cr3+ (Z = 24).", "Cr: [Ar] 3d5 4s1. Cr3+: [Ar] 3d3."),
            (2, "Calculate the de Broglie wavelength of an electron moving at 1 x 10^6 m/s (m = 9.11 x 10^-31 kg).",
             "Wavelength = h / mv = 6.626 x 10^-34 / (9.11 x 10^-31 x 10^6) = 7.27 x 10^-10 m."),
            (2, "Differentiate between an orbit and an orbital.",
             "An orbit is a fixed circular path of an electron (Bohr model). An orbital is a region of high probability of finding the electron (quantum model)."),
            (2, "State Hund's rule with an example.",
             "Electrons occupy degenerate orbitals singly with parallel spins before pairing. In nitrogen (2p3) each p orbital gets one electron."),
            (3, "Calculate the energy of the electron in the first Bohr orbit of hydrogen in joules.",
             "E1 = -2.18 x 10^-18 J (= -13.6 eV)."),
            (3, "Calculate the wavelength of the first line of the Balmer series (n = 3 to 2). R = 1.097 x 10^7 per m.",
             "1/wavelength = R (1/4 - 1/9) = 1.097 x 10^7 x 5/36 = 1.524 x 10^6, so wavelength = 656 nm."),
            (3, "Why does the 4s orbital fill before 3d? Explain with the (n + l) rule.",
             "4s has n + l = 4 and 3d has n + l = 5. Lower (n + l) means lower energy, so 4s fills first."),
            (3, "Give the shapes and the number of orbitals of s, p and d subshells.",
             "s: spherical, 1 orbital. p: dumbbell, 3 orbitals. d: mostly double dumbbell (cloverleaf), 5 orbitals."),
        ],
    },
    3: {
        "quiz": [
            ("Which is the MOST electronegative among Cl, O, N, S?",
             ["Cl", "O", "N", "S"], 1, "Pauling values: O = 3.5, Cl = 3.0.", "Oxygen is second only to fluorine."),
            ("Which has the largest atomic radius among Na, Mg, Al, Si?",
             ["Na", "Mg", "Al", "Si"], 0, "Radii decrease across a period.", "Na has the lowest nuclear charge in the period."),
            ("Which of these is an amphoteric oxide?",
             ["Na2O", "MgO", "Al2O3", "SO3"], 2, "It reacts with both acids and bases.", "Al2O3 shows both behaviours."),
            ("The atomic radii of Zr and Hf are almost equal because of:",
             ["Screening effect", "Lanthanoid contraction", "Inert pair effect", "Diagonal relationship"], 1,
             "Think about 4f electrons filling before Hf.", "Poor shielding by 4f electrons shrinks Hf."),
            ("Which has the smallest radius among Na+, Mg2+, Al3+, O2-?",
             ["Na+", "Mg2+", "Al3+", "O2-"], 2, "All have 10 electrons.", "Al3+ has the most protons (13)."),
            ("Which element has the highest SECOND ionisation enthalpy?",
             ["Na", "Mg", "Al", "Si"], 0, "Removing an electron from a noble gas core is hard.", "Na+ has a neon core."),
            ("Which is the correct order of FIRST ionisation enthalpy?",
             ["Li < Be < B < C", "Li < B < Be < C", "B < Li < Be < C", "Be < Li < B < C"], 1,
             "Be (2s2) and B (2p1): which is lower?", "Li (5.4) < B (8.3) < Be (9.3) < C (11.3) eV."),
            ("The temporary IUPAC name of the element with Z = 104 is:",
             ["Unnilquadium", "Unnilpentium", "Unnilbium", "Ununquadium"], 0,
             "1 = un, 0 = nil, 4 = quad.", "Un + nil + quad + ium = Unnilquadium."),
            ("Which pair shows a diagonal relationship?",
             ["Li and Na", "Li and Mg", "Be and Mg", "B and Al"], 1,
             "One group right and one period down.", "Li and Mg are similar in size and polarising power."),
            ("Which has a POSITIVE electron gain enthalpy?",
             ["F", "Cl", "Ne", "S"], 2, "Think of a full octet.", "Noble gases need energy to add an electron."),
            ("Which of these is NOT isoelectronic with Ne?",
             ["Na+", "Mg2+", "Cl-", "F-"], 2, "Ne has 10 electrons.", "Cl- has 18."),
            ("The van der Waals radius of an atom is ______ its covalent radius.",
             ["Smaller than", "Larger than", "Equal to", "Unrelated to"], 1,
             "Non-bonded atoms are farther apart.", "Van der Waals radii are always larger."),
            ("Effective nuclear charge increases across a period because:",
             ["Shielding increases strongly", "Nuclear charge increases but shielding barely changes",
              "Number of shells increases", "Electron repulsion falls"], 1,
             "Electrons are added to the same shell.", "Same-shell electrons shield poorly."),
            ("The element with the highest electron gain enthalpy (most negative) is:",
             ["F", "Cl", "Br", "I"], 1, "Fluorine is the exception.", "Cl is more negative than F."),
            ("The element with Z = 35 belongs to:",
             ["Group 17, period 4", "Group 17, period 3", "Group 16, period 4", "Group 15, period 4"], 0,
             "Configuration [Ar] 3d10 4s2 4p5.", "Bromine."),
        ],
        "practice": [
            (1, "Define electronegativity.", "The tendency of an atom in a molecule to attract the shared pair of electrons towards itself."),
            (1, "What is lanthanoid contraction?", "The gradual decrease in size of atoms and ions across the lanthanoids due to poor shielding by 4f electrons."),
            (2, "Why do lithium and magnesium show similar properties?",
             "Diagonal relationship: similar charge/size ratio (polarising power) and electronegativity."),
            (2, "Why is the second ionisation enthalpy always greater than the first?",
             "Removing an electron from a positive ion needs more energy because of increased effective nuclear charge and smaller size."),
            (2, "How does the nature of oxides change across a period? Give examples.",
             "Basic (Na2O) to amphoteric (Al2O3) to acidic (SO3, Cl2O7) as electronegativity increases."),
            (3, "Explain the trends in atomic radius across a period and down a group.",
             "Across a period it decreases because nuclear charge rises with the same shell. Down a group it increases because new shells are added."),
            (3, "Why are noble gases' electron gain enthalpies large and positive?",
             "They have stable fully filled shells, so an added electron goes to the next shell and needs energy."),
            (3, "Arrange K+, Cl-, S2-, Ca2+ in decreasing order of ionic radii and justify.",
             "S2- > Cl- > K+ > Ca2+. All have 18 electrons; larger nuclear charge gives smaller size."),
            (3, "Why are halogens strong oxidising agents?",
             "They have very high negative electron gain enthalpies and high electronegativity, so they readily gain one electron."),
        ],
    },
}

EXTRA_B = {
    4: {
        "quiz": [
            ("The hybridisation of sulphur in SF6 is:",
             ["sp3d", "sp3d2", "sp3", "sp2"], 1, "Six bond pairs.", "sp3d2 with octahedral geometry."),
            ("The shape of XeF4 is:",
             ["Tetrahedral", "Square planar", "See-saw", "Octahedral"], 1,
             "Xe has 4 bond pairs and 2 lone pairs.", "Lone pairs sit opposite each other, giving square planar."),
            ("Which has the LARGEST bond angle?",
             ["H2O", "NH3", "CH4", "BF3"], 3, "Think of sp2 vs sp3.", "BF3 is trigonal planar at 120 degrees."),
            ("Which molecule has zero dipole moment?",
             ["CO2", "H2O", "NH3", "SO2"], 0, "Look for symmetry.", "The two C=O dipoles cancel in linear CO2."),
            ("The bond order of N2+ is:",
             ["3", "2.5", "2", "3.5"], 1, "Which kind of electron is removed from N2?",
             "A bonding electron is lost: (9 - 4) / 2 = 2.5."),
            ("Which species is diamagnetic?",
             ["O2-", "O2", "O2(2-)", "O2+"], 2, "Look for any unpaired electron.", "Peroxide ion has all electrons paired."),
            ("The shape of ClF3 is:",
             ["Trigonal planar", "T-shaped", "Pyramidal", "Bent"], 1,
             "5 electron pairs, 2 of them lone pairs.", "Trigonal bipyramidal pairs, two lone pairs equatorial: T-shape."),
            ("The hybridisation of carbon in CO2 is:",
             ["sp", "sp2", "sp3", "dsp2"], 0, "Two sigma bonds, no lone pairs.", "Linear, so sp."),
            ("Which has the highest lattice enthalpy?",
             ["NaCl", "MgO", "KCl", "CaO"], 1, "High charges and small ions.", "Mg2+ and O2- are small and doubly charged."),
            ("Which has the shortest bond length?",
             ["C-C", "C=C", "C triple bond C", "C-H"], 2, "Higher bond order means shorter.", "A triple bond is the shortest."),
            ("o-Nitrophenol is more volatile than p-nitrophenol because of:",
             ["Intermolecular hydrogen bonding", "Intramolecular hydrogen bonding",
              "Higher molecular mass", "Resonance"], 1, "Which isomer can fold on itself?",
             "In the ortho isomer the H-bond stays within the molecule."),
            ("How many lone pairs are on Xe in XeF2?",
             ["1", "2", "3", "0"], 2, "Xe has 8 valence electrons and uses 2.", "Three lone pairs, so the molecule is linear."),
            ("Which has the larger H-X-H bond angle?",
             ["NH3", "PH3", "Both equal", "Cannot say"], 0, "Compare electronegativity of the central atoms.",
             "N is more electronegative, so bond pairs are closer and repel more."),
            ("The formal charge on nitrogen in NH4+ is:",
             ["0", "+1", "-1", "+2"], 1, "Valence e - nonbonding e - half bonding e.", "5 - 0 - 4 = +1."),
            ("According to MOT, which does NOT exist?",
             ["He2", "H2", "Li2", "B2"], 0, "Compute bond order.", "He2 has bond order 0."),
            ("Which molecule is polar?",
             ["BF3", "CCl4", "CHCl3", "CO2"], 2, "Check symmetry.", "CHCl3 is asymmetric."),
        ],
        "practice": [
            (1, "Define dipole moment.", "Product of the magnitude of charge and the distance between the two charges (mu = q x d); unit debye."),
            (1, "What is a coordinate (dative) bond?", "A covalent bond in which both shared electrons are provided by one atom, e.g. NH4+."),
            (2, "Draw the Lewis structure of CO and give the formal charges.",
             "C triple bond O with a lone pair on each atom. Formal charge: C = -1, O = +1."),
            (2, "Why is the dipole moment of NH3 greater than that of NF3?",
             "In NH3 the N-H bond dipoles point the same way as the lone-pair dipole; in NF3 the N-F dipoles oppose it, giving a small net value."),
            (2, "Predict the shapes of SF4 and XeF2 using VSEPR.",
             "SF4: 4 bond pairs + 1 lone pair, see-saw. XeF2: 2 bond pairs + 3 lone pairs, linear."),
            (2, "What is hydrogen bonding? How does it affect the boiling point of water?",
             "An attraction between H bonded to N, O or F and a lone pair on another N, O or F. It raises the boiling point because extra energy is needed to break these bonds."),
            (3, "Explain the bonding in O2 using molecular orbital theory.",
             "Configuration: ... (sigma2pz)2 (pi2px)2 (pi2py)2 (pi*2px)1 (pi*2py)1. Bond order = (10 - 6)/2 = 2. Two unpaired electrons make it paramagnetic."),
            (3, "Explain the hybridisation and shape of PCl5.",
             "P undergoes sp3d hybridisation (five orbitals). The shape is trigonal bipyramidal with 3 equatorial and 2 axial bonds; axial bonds are longer."),
            (3, "Explain resonance with the carbonate ion.",
             "CO3(2-) has three equivalent contributing structures with one C=O and two C-O-. The actual structure is a hybrid with equal C-O bonds of bond order 1.33."),
            (3, "Why is ice less dense than water?",
             "In ice, hydrogen bonding creates an open hexagonal cage with empty spaces, so the volume is larger and density lower."),
        ],
    },
    5: {
        "quiz": [
            ("Which of these is an INTENSIVE property?",
             ["Enthalpy", "Mass", "Density", "Volume"], 2, "It does not depend on the amount.", "Density is mass / volume, independent of amount."),
            ("For the isothermal reversible expansion of an ideal gas, the change in internal energy is:",
             ["Positive", "Negative", "Zero", "Depends on volume"], 2, "Internal energy of an ideal gas depends only on T.", "T is constant, so delta U = 0."),
            ("The heat change of a reaction at constant volume equals:",
             ["Delta H", "Delta U", "Delta G", "Delta S"], 1, "No pressure-volume work is done.", "q(v) = delta U."),
            ("Which has the highest entropy?",
             ["1 g ice at 0 C", "1 g water at 25 C", "1 g steam at 100 C", "All equal"], 2,
             "Gases are the most disordered.", "Steam."),
            ("For a spontaneous process, which statement is always true?",
             ["Delta S of system > 0", "Delta S of surroundings > 0", "Delta S total > 0", "Delta H < 0"], 2,
             "The second law applies to the universe.", "Total entropy change must be positive."),
            ("If K = 1 for a reaction, delta G standard is:",
             ["Positive", "Negative", "Zero", "Infinite"], 2, "Use delta G = -RT ln K.", "ln 1 = 0."),
            ("Which has a standard enthalpy of formation equal to ZERO?",
             ["Br2(l)", "Br2(g)", "C(diamond)", "O3(g)"], 0,
             "Zero only for the most stable form at 298 K and 1 bar.", "Bromine is liquid in its standard state."),
            ("Work done by 1 mol of ideal gas expanding freely into a vacuum is:",
             ["nRT ln(V2/V1)", "Zero", "Negative", "P x delta V"], 1, "External pressure is zero.", "w = -P(ext) delta V = 0."),
            ("If the enthalpy of atomisation of CH4 is 1664 kJ/mol, the average C-H bond enthalpy is:",
             ["416 kJ", "1664 kJ", "208 kJ", "6656 kJ"], 0, "Four C-H bonds are broken.", "1664 / 4 = 416 kJ."),
            ("In an adiabatic expansion of an ideal gas, the temperature:",
             ["Rises", "Falls", "Stays constant", "Doubles"], 1, "q = 0, so delta U = w.", "The gas does work at the cost of its internal energy."),
            ("For an ideal gas, Cp - Cv per mole equals:",
             ["R/2", "R", "2R", "Zero"], 1, "Mayer's relation.", "Cp - Cv = R."),
            ("A reaction with delta H > 0 and delta S < 0 is:",
             ["Always spontaneous", "Never spontaneous", "Spontaneous at high T", "Spontaneous at low T"], 1,
             "Both terms make delta G positive.", "delta G = delta H - T delta S is always positive."),
            ("The molar entropy of vaporisation of water at 373 K (delta H = 40.7 kJ/mol) is about:",
             ["109 J/K/mol", "40.7 J/K/mol", "0.109 J/K/mol", "373 J/K/mol"], 0,
             "delta S = delta H / T.", "40700 / 373 = 109 J/K/mol."),
            ("A system absorbs 50 kJ of heat and does 20 kJ of work. Delta U is:",
             ["+70 kJ", "+30 kJ", "-30 kJ", "-70 kJ"], 1, "Work done BY the system is negative.", "delta U = 50 - 20 = +30 kJ."),
            ("Heat of neutralisation of acetic acid with NaOH is less than 57.1 kJ because:",
             ["Acetic acid is a gas", "Energy is used to ionise the weak acid", "NaOH is weak", "Water is not formed"], 1,
             "Compare with a strong acid.", "Part of the energy released goes into ionising acetic acid."),
        ],
        "practice": [
            (1, "State Hess's law of constant heat summation.", "The total enthalpy change of a reaction is the same whether it takes place in one step or several steps."),
            (1, "Define standard enthalpy of combustion.", "Enthalpy change when 1 mol of a substance burns completely in oxygen under standard conditions."),
            (2, "Differentiate between open, closed and isolated systems.",
             "Open: exchanges matter and energy. Closed: exchanges only energy. Isolated: exchanges neither."),
            (2, "A system absorbs 2 kJ of heat and 500 J of work is done ON it. Find delta U.", "delta U = q + w = 2000 + 500 = +2500 J = 2.5 kJ."),
            (2, "Predict the sign of delta S for CaCO3(s) -> CaO(s) + CO2(g). Why?", "Positive, because a gas is produced and disorder increases."),
            (2, "How much heat is needed to raise the temperature of 100 g of water from 20 C to 70 C? (c = 4.18 J/g/K)",
             "q = m c delta T = 100 x 4.18 x 50 = 20 900 J = 20.9 kJ."),
            (3, "Calculate delta G at 300 K if delta H = -40 kJ and delta S = -100 J/K. Is the reaction spontaneous?",
             "delta G = -40 000 - 300(-100) = -40 000 + 30 000 = -10 000 J = -10 kJ. Negative, so spontaneous."),
            (3, "Find the enthalpy of formation of CH4 given the combustion enthalpies of CH4 = -890, C = -393.5, H2 = -286 kJ/mol.",
             "delta f H = [-393.5 + 2(-286)] - (-890) = -965.5 + 890 = -75.5 kJ/mol."),
            (3, "Explain the spontaneity criteria with delta H and delta S signs.",
             "delta H -, delta S +: always spontaneous. delta H +, delta S -: never. delta H -, delta S -: spontaneous at low T. delta H +, delta S +: spontaneous at high T."),
            (3, "State the second and third laws of thermodynamics.",
             "Second: the entropy of the universe increases in a spontaneous process. Third: the entropy of a perfectly crystalline substance is zero at absolute zero."),
        ],
    },
    6: {
        "quiz": [
            ("Which of these is a Lewis base?",
             ["BF3", "NH3", "AlCl3", "H+"], 1, "It donates an electron pair.", "NH3 has a lone pair."),
            ("The pH of 0.001 M NaOH is:",
             ["3", "11", "10", "9"], 1, "Find pOH first.", "pOH = 3, so pH = 11."),
            ("On heating pure water, its pH:",
             ["Rises above 7", "Falls but it stays neutral", "Stays 7", "Becomes acidic"], 1,
             "Kw increases with temperature.", "[H+] = [OH-] still, so neutral, but pH < 7."),
            ("Which aqueous salt solution is acidic?",
             ["NH4Cl", "NaCl", "CH3COONa", "KNO3"], 0, "Salt of a strong acid and a weak base.", "NH4+ hydrolyses to give H+."),
            ("Which mixture forms a buffer?",
             ["HCl + NaCl", "CH3COOH + CH3COONa", "NaOH + NaCl", "HNO3 + KNO3"], 1,
             "Weak acid with its salt.", "CH3COOH / CH3COO- is an acidic buffer."),
            ("A catalyst added to a reaction at equilibrium:",
             ["Shifts it forward", "Does not change the position of equilibrium", "Increases K", "Decreases K"], 1,
             "It affects both rates equally.", "It only helps reach equilibrium faster."),
            ("For PCl5 <-> PCl3 + Cl2, increasing the pressure shifts the equilibrium:",
             ["Forward", "Backward", "No change", "Cannot say"], 1, "Count gas moles on each side.", "Fewer moles on the left, so it shifts backward."),
            ("For N2O4 <-> 2NO2, Kp / Kc equals:",
             ["1", "RT", "(RT)^-1", "(RT)^2"], 1, "delta n(g) = 1.", "Kp = Kc (RT)^1."),
            ("The Ksp of Ca3(PO4)2 in terms of solubility s is:",
             ["4 s^3", "27 s^4", "108 s^5", "s^2"], 2, "Ca3(PO4)2 gives 3 Ca2+ and 2 PO4(3-).", "(3s)^3 (2s)^2 = 108 s^5."),
            ("As a weak acid is diluted, its degree of ionisation:",
             ["Decreases", "Increases", "Stays the same", "Becomes zero"], 1, "Ostwald's dilution law.", "alpha = sqrt(Ka / C) increases as C falls."),
            ("If Q > K for a reaction mixture, the reaction proceeds:",
             ["Forward", "Backward", "Is at equilibrium", "Stops"], 1, "Too many products.", "It moves backward to reduce Q."),
            ("The conjugate acid of HCO3- is:",
             ["CO3(2-)", "H2CO3", "H3O+", "CO2"], 1, "Add a proton.", "HCO3- + H+ = H2CO3."),
            ("Which species is amphoteric (Bronsted)?",
             ["HCO3-", "Cl-", "NH4+", "H3O+"], 0, "It can both donate and accept a proton.", "HCO3- can do both."),
            ("The pH of 0.1 M acetic acid (Ka = 1.8 x 10^-5) is about:",
             ["1", "2.87", "4.74", "7"], 1, "[H+] = sqrt(Ka C).", "[H+] = 1.34 x 10^-3, pH = 2.87."),
            ("A precipitate forms when the ionic product ______ the solubility product.",
             ["Is less than", "Equals", "Exceeds", "Is unrelated to"], 2, "Q vs Ksp.", "Q > Ksp means supersaturation."),
        ],
        "practice": [
            (1, "Define pH.", "The negative logarithm (base 10) of the hydrogen ion concentration: pH = -log [H+]."),
            (1, "State Ostwald's dilution law for a weak acid.", "alpha = sqrt(Ka / C): the degree of ionisation increases on dilution."),
            (2, "What is a buffer solution? Give an acidic and a basic example.",
             "A solution resisting a change in pH on adding small amounts of acid or base. Acidic: CH3COOH + CH3COONa. Basic: NH4OH + NH4Cl."),
            (2, "Calculate the pH of 0.05 M H2SO4 (assume complete ionisation).", "[H+] = 0.1 M, so pH = 1."),
            (2, "Write the conjugate acid and base of H2O.", "Conjugate acid: H3O+. Conjugate base: OH-."),
            (2, "Why does K of an exothermic reaction decrease on heating?",
             "By Le Chatelier's principle heat shifts the equilibrium backward, lowering the product-to-reactant ratio."),
            (3, "A 0.1 M weak acid is 1 % ionised. Calculate Ka.", "Ka = C alpha^2 = 0.1 x (0.01)^2 = 1 x 10^-5."),
            (3, "Calculate [OH-] and pH of 0.1 M NH3 (Kb = 1.8 x 10^-5).",
             "[OH-] = sqrt(1.8 x 10^-6) = 1.34 x 10^-3 M. pOH = 2.87, pH = 11.13."),
            (3, "Explain how the Haber process conditions follow from Le Chatelier's principle.",
             "N2 + 3H2 <-> 2NH3 is exothermic with fewer gas moles. High pressure favours NH3. Low temperature favours yield but is slow, so a compromise ~700 K with an iron catalyst is used."),
            (3, "At equilibrium [PCl5] = 0.8, [PCl3] = [Cl2] = 0.2 mol/L. Find Kc for PCl5 <-> PCl3 + Cl2.",
             "Kc = (0.2 x 0.2) / 0.8 = 0.05."),
        ],
    },
}

EXTRA_C = {
    7: {
        "quiz": [
            ("The oxidation number of iron in Fe3O4 is (average):",
             ["+2", "+3", "+8/3", "+4"], 2, "3x + 4(-2) = 0.", "x = +8/3."),
            ("The oxidation number of carbon in CH2Cl2 is:",
             ["-2", "0", "+2", "+4"], 1, "2(+1) + 2(-1) + x = 0.", "x = 0."),
            ("The oxidation state of oxygen in KO2 (superoxide) is:",
             ["-2", "-1", "-1/2", "0"], 2, "K is +1 and the compound is neutral.", "2 atoms of O share -1, so -1/2 each."),
            ("The oxidation number of sulphur in H2S2O8 (peroxodisulphuric acid) is:",
             ["+7", "+6", "+8", "+4"], 1, "It has one peroxide O-O bond.", "6 O at -2 and 2 O at -1 give S = +6."),
            ("In NH4NO3 the two nitrogen atoms have oxidation numbers:",
             ["-3 and +3", "-3 and +5", "+3 and +5", "-3 and -3"], 1, "Treat NH4+ and NO3- separately.", "-3 in NH4+ and +5 in NO3-."),
            ("In Cl2 + 2OH- -> Cl- + ClO- + H2O, chlorine acts as:",
             ["Only an oxidising agent", "Only a reducing agent", "Both oxidising and reducing", "Neither"], 2,
             "Cl goes from 0 to -1 and to +1.", "Disproportionation."),
            ("The number of electrons gained when MnO4- changes to Mn2+ in acid is:",
             ["1", "3", "5", "7"], 2, "+7 to +2.", "5 electrons."),
            ("Which is the strongest reducing agent in aqueous solution (E standard)?",
             ["Li", "Na", "K", "Cs"], 0, "Look at the most negative E.", "Li has the most negative E (-3.05 V) due to high hydration."),
            ("Which of these is NOT a redox reaction?",
             ["2Na + Cl2 -> 2NaCl", "AgNO3 + NaCl -> AgCl + NaNO3", "Zn + 2HCl -> ZnCl2 + H2", "2H2 + O2 -> 2H2O"], 1,
             "Check for any change in oxidation number.", "It is a precipitation reaction; no oxidation numbers change."),
            ("The oxidation number of manganese in K2MnO4 is:",
             ["+4", "+6", "+7", "+2"], 1, "2(+1) + x + 4(-2) = 0.", "x = +6."),
            ("Which can act ONLY as an oxidising agent?",
             ["KMnO4", "H2S", "SO2", "H2O2"], 0, "Mn is already at its highest oxidation state (+7).", "It cannot be oxidised further."),
            ("The mole ratio MnO4- : C2O4(2-) in acidic medium is:",
             ["1 : 1", "2 : 5", "5 : 2", "1 : 5"], 1, "Balance the electrons (5 and 2).", "2 MnO4- take 10 e-; 5 C2O4(2-) give 10 e-."),
            ("In the Daniell cell, oxidation takes place at:",
             ["The copper electrode", "The zinc electrode", "The salt bridge", "Both electrodes"], 1,
             "Zn is the more reactive metal.", "Zn -> Zn2+ + 2e-."),
            ("Which metal does NOT liberate H2 from dilute HCl?",
             ["Cu", "Zn", "Fe", "Mg"], 0, "It lies below hydrogen in the electrochemical series.", "Copper."),
            ("The oxidation number of phosphorus in H3PO3 is:",
             ["+1", "+3", "+5", "+2"], 1, "3(+1) + x + 3(-2) = 0.", "x = +3."),
        ],
        "practice": [
            (1, "Define a reducing agent.", "A substance that loses electrons (or increases its oxidation number) and so reduces another species."),
            (1, "What is the oxidation number of oxygen in H2O2 and in OF2?", "H2O2: -1. OF2: +2."),
            (2, "Find the oxidation number of S in H2SO4 and the average in Na2S2O3.", "H2SO4: +6. Na2S2O3: +2 (average)."),
            (2, "Identify the oxidising and reducing agent in 2Mg + O2 -> 2MgO.", "Mg is oxidised, so it is the reducing agent. O2 is reduced, so it is the oxidising agent."),
            (2, "Why can hydrogen peroxide act as both an oxidising and a reducing agent?",
             "Oxygen is at the intermediate state -1, so it can go down to -2 (reduction) or up to 0 (oxidation)."),
            (2, "Differentiate between a disproportionation reaction and an ordinary redox reaction with an example.",
             "In disproportionation the same element is both oxidised and reduced, e.g. Cl2 + 2NaOH -> NaCl + NaClO + H2O."),
            (3, "Balance in acidic medium: Cr2O7(2-) + Fe2+ -> Cr3+ + Fe3+.",
             "Cr2O7(2-) + 14H+ + 6Fe2+ -> 2Cr3+ + 7H2O + 6Fe3+."),
            (3, "Balance in basic medium: MnO4- + I- -> MnO2 + I2.",
             "2MnO4- + 6I- + 4H2O -> 2MnO2 + 3I2 + 8OH-."),
            (3, "Using the electrochemical series explain whether Zn can displace Cu from CuSO4 solution.",
             "Zn lies above Cu (more negative E), so Zn is a stronger reducing agent and displaces Cu: Zn + Cu2+ -> Zn2+ + Cu."),
            (3, "Write the half-reactions for Zn + Cu2+ -> Zn2+ + Cu.",
             "Oxidation: Zn -> Zn2+ + 2e-. Reduction: Cu2+ + 2e- -> Cu."),
        ],
    },
    8: {
        "quiz": [
            ("The IUPAC name of CH3CH2CH(CH3)CH2OH is:",
             ["Pentan-1-ol", "2-Methylbutan-1-ol", "3-Methylbutan-1-ol", "2-Ethylpropan-1-ol"], 1,
             "Number the chain from the end nearest -OH.", "A butane chain with -OH at C-1 and CH3 at C-2."),
            ("The number of structural isomers of C4H10 is:",
             ["2", "3", "4", "5"], 0, "n-butane and isobutane.", "Two."),
            ("Which carbanion is the MOST stable?",
             ["(CH3)3C-", "(CH3)2CH-", "CH3CH2-", "CH3-"], 3, "+I groups destabilise a negative charge.", "Methyl carbanion."),
            ("Which of these is an electrophile?",
             ["NH3", "H2O", "BF3", "OH-"], 2, "It accepts an electron pair.", "BF3 has an empty p orbital."),
            ("Homolytic bond fission produces:",
             ["A carbocation and a carbanion", "Free radicals", "Two anions", "Two cations"], 1,
             "Each atom keeps one electron.", "Free radicals."),
            ("Which compound shows geometrical isomerism?",
             ["But-1-ene", "But-2-ene", "Propene", "2-Methylpropene"], 1,
             "Each double-bond carbon needs two different groups.", "But-2-ene has cis and trans forms."),
            ("Which has a chiral carbon?",
             ["CH3CH2Cl", "CH3CHClBr", "CH2Cl2", "CH3CH2CH3"], 1,
             "Four different groups on one carbon.", "In CH3CHClBr the middle carbon has H, CH3, Cl, Br."),
            ("CH3OCH3 and C2H5OH are:",
             ["Chain isomers", "Position isomers", "Functional isomers", "Metamers"], 2,
             "Same formula, different functional group.", "Ether vs alcohol."),
            ("Which group shows a +R (+M) effect?",
             ["-OH", "-NO2", "-CHO", "-COOH"], 0, "Lone pair donation into the ring.", "-OH."),
            ("Which acid is the strongest?",
             ["ClCH2COOH", "CH3COOH", "FCH2COOH", "CH3CH2COOH"], 2, "Stronger -I effect stabilises the anion.", "F is more electronegative than Cl."),
            ("The number of sp2 hybridised carbons in toluene is:",
             ["6", "7", "5", "1"], 0, "The methyl carbon is sp3.", "Six ring carbons."),
            ("Which carbocation is the MOST stable?",
             ["(CH3)3C+", "C6H5CH2+", "CH3CH2+", "CH3+"], 1, "Resonance usually beats hyperconjugation.", "The benzyl cation is stabilised by delocalisation."),
            ("In Lassaigne's test, a pale yellow precipitate (sparingly soluble in NH4OH) with AgNO3 indicates:",
             ["Chlorine", "Bromine", "Iodine", "Sulphur"], 1, "White = Cl, yellow = I.", "Bromine."),
            ("Kjeldahl's method is NOT suitable for compounds containing:",
             ["Amino groups", "Amides", "Nitro groups", "Amines"], 2, "Nitrogen is not converted to ammonium sulphate.", "Nitro and azo compounds."),
            ("Steam distillation is used for liquids which are:",
             ["Miscible with water and non-volatile", "Steam volatile and immiscible with water",
              "Thermally stable", "Highly polar"], 1, "Mixture boils below 100 C.", "e.g. aniline."),
            ("Distillation under reduced pressure is used for liquids which:",
             ["Have low boiling points", "Decompose below their boiling point", "Are miscible with water", "Are volatile"], 1,
             "Lowering pressure lowers the boiling point.", "e.g. glycerol."),
        ],
        "practice": [
            (1, "What are isomers?", "Compounds with the same molecular formula but different structures or spatial arrangements."),
            (1, "Define an electrophile and give two examples.", "An electron-seeking species that accepts an electron pair, e.g. H+, NO2+, BF3."),
            (2, "Write the IUPAC names of (CH3)2CHCH2CH3 and CH3CH=CHCH3.", "2-Methylbutane and but-2-ene."),
            (2, "Explain hyperconjugation with an example.",
             "It is delocalisation of sigma electrons of a C-H bond adjacent to a positive carbon or double bond. The ethyl cation has 3 such H, and more alpha hydrogens means higher stability."),
            (2, "Differentiate between homolytic and heterolytic fission.",
             "Homolytic: each atom takes one electron, giving free radicals. Heterolytic: one atom takes both electrons, giving ions."),
            (2, "Explain the principle of steam distillation.",
             "A substance immiscible with water distils at a temperature lower than its boiling point when its vapour pressure plus that of water equals atmospheric pressure."),
            (3, "Write all structural isomers of C5H12 with IUPAC names.",
             "Pentane; 2-methylbutane (isopentane); 2,2-dimethylpropane (neopentane)."),
            (3, "Describe Lassaigne's test for nitrogen, sulphur and halogens.",
             "Fuse the compound with sodium and extract with water. N: FeSO4 + NaOH then acidify gives Prussian blue. S: sodium nitroprusside gives violet, or lead acetate gives black PbS. Halogens: acidify with HNO3 and add AgNO3: white (Cl), pale yellow (Br), yellow (I) precipitate."),
            (3, "0.3 g of an organic compound gave 0.44 g CO2 and 0.18 g H2O. Find the percentage of C and H.",
             "C = (12/44) x (0.44/0.3) x 100 = 40 %. H = (2/18) x (0.18/0.3) x 100 = 6.67 %."),
            (3, "Why is chloroacetic acid stronger than acetic acid?",
             "The -I effect of Cl withdraws electrons, stabilising the chloroacetate ion, so the acid ionises more."),
        ],
    },
    9: {
        "quiz": [
            ("Acid-catalysed hydration of propene gives mainly:",
             ["Propan-1-ol", "Propan-2-ol", "Propanal", "Propanone"], 1, "Markovnikov addition of water.", "OH goes to the carbon with fewer hydrogens."),
            ("Which reagent distinguishes 1-butyne from 2-butyne?",
             ["Bromine water", "Alkaline KMnO4", "Ammoniacal AgNO3", "HBr"], 2, "Look for an acidic terminal hydrogen.", "Only terminal alkynes give a precipitate."),
            ("The attacking electrophile in the nitration of benzene is:",
             ["NO3-", "NO2+", "NO2-", "HNO3"], 1, "Formed by H2SO4 acting on HNO3.", "Nitronium ion."),
            ("Which group is meta-directing?",
             ["-NO2", "-OH", "-CH3", "-Cl"], 0, "It deactivates the ring by -M/-I.", "-NO2."),
            ("The number of sigma bonds in benzene is:",
             ["6", "9", "12", "15"], 2, "6 C-C plus 6 C-H.", "12 sigma bonds and 3 pi bonds."),
            ("Which alkene does NOT show geometrical isomerism?",
             ["But-2-ene", "Propene", "Pent-2-ene", "Hex-3-ene"], 1, "One double-bond carbon has two identical groups.", "Propene has CH2=."),
            ("Friedel-Crafts alkylation of benzene requires:",
             ["Anhydrous AlCl3", "Dilute H2SO4", "NaOH", "Zn dust"], 0, "A Lewis acid catalyst.", "Anhydrous AlCl3."),
            ("The dihedral angle in the staggered conformation of ethane is:",
             ["0 degrees", "60 degrees", "120 degrees", "180 degrees"], 1, "Eclipsed is 0.", "60 degrees; this is the more stable conformation."),
            ("Which has the highest boiling point?",
             ["n-Pentane", "Isopentane", "Neopentane", "All equal"], 0, "Branching reduces surface area.", "n-Pentane (309 K)."),
            ("Cold dilute alkaline KMnO4 oxidises ethene to:",
             ["Ethanol", "Ethane-1,2-diol", "Ethanoic acid", "Ethanal"], 1, "Baeyer's reagent.", "syn-dihydroxylation gives ethylene glycol."),
            ("Hydration of ethyne with HgSO4/H2SO4 gives:",
             ["Ethanol", "Ethanal", "Ethanoic acid", "Ethene"], 1, "The enol tautomerises.", "Vinyl alcohol -> ethanal."),
            ("The cyclopentadienyl anion (C5H5-) is:",
             ["Antiaromatic", "Aromatic", "Non-aromatic", "Saturated"], 1, "Count the pi electrons.", "6 pi electrons, cyclic and planar."),
            ("Reduction of but-2-yne with Na in liquid NH3 gives:",
             ["cis-But-2-ene", "trans-But-2-ene", "Butane", "But-1-ene"], 1, "Lindlar gives cis.", "Dissolving-metal reduction gives trans."),
            ("Which is the most reactive towards electrophilic substitution?",
             ["Benzene", "Toluene", "Nitrobenzene", "Chlorobenzene"], 1, "-CH3 activates the ring.", "Toluene."),
            ("Which of these follows Huckel's rule with 10 pi electrons?",
             ["Benzene", "Naphthalene", "Cyclobutadiene", "Cyclohexane"], 1, "4n + 2 with n = 2.", "Naphthalene has 10 pi electrons."),
        ],
        "practice": [
            (1, "State Huckel's rule.", "A planar, cyclic, fully conjugated molecule is aromatic if it has (4n + 2) pi electrons, n = 0, 1, 2..."),
            (1, "What is a conformation?", "Different spatial arrangements of atoms arising from free rotation about a C-C single bond."),
            (2, "Write the steps of the mechanism of nitration of benzene.",
             "1) HNO3 + 2H2SO4 -> NO2+ + H3O+ + 2HSO4-. 2) NO2+ attacks benzene to form the arenium ion. 3) Loss of H+ restores aromaticity, giving nitrobenzene."),
            (2, "How will you convert ethyne into benzene?", "Pass ethyne through a red-hot iron tube at 873 K: cyclic polymerisation of three molecules gives benzene."),
            (2, "Why does benzene undergo substitution rather than addition?",
             "Addition would destroy the stable delocalised pi system (resonance energy), but substitution retains it."),
            (2, "Which conformation of ethane is more stable and why?",
             "Staggered, because the hydrogen atoms are farthest apart, so torsional strain and repulsion are minimum."),
            (3, "How will you distinguish ethane, ethene and ethyne?",
             "Bromine water or Baeyer's reagent is decolourised by ethene and ethyne but not ethane. Ethyne alone gives a white precipitate with ammoniacal AgNO3."),
            (3, "Give the products of propene with (i) HBr (ii) HBr/peroxide (iii) cold alkaline KMnO4.",
             "(i) 2-Bromopropane. (ii) 1-Bromopropane. (iii) Propane-1,2-diol."),
            (3, "Explain the directive influence of -OH and -NO2 groups in benzene.",
             "-OH is activating, ortho/para directing (+M effect). -NO2 is deactivating, meta directing (-M, -I)."),
            (3, "Write the Friedel-Crafts alkylation and acylation of benzene.",
             "Alkylation: C6H6 + CH3Cl (anhy. AlCl3) -> C6H5CH3 + HCl. Acylation: C6H6 + CH3COCl (anhy. AlCl3) -> C6H5COCH3 + HCl."),
        ],
    },
}


# Merge the extra question banks into CHAPTERS
for _bank in (EXTRA_A, EXTRA_B, EXTRA_C):
    for _n, _extra in _bank.items():
        CHAPTERS[_n]["quiz"].extend(_extra["quiz"])
        CHAPTERS[_n]["practice"].extend(_extra["practice"])

st.set_page_config(page_title="CBSE XI Chemistry Game", page_icon="🧪")

ALL = 0  # chapter id meaning "all chapters mixed"


def pool_for(scope):
    """Return list of (chapter_id, quiz_tuple) for a chapter or for all chapters."""
    ids = list(CHAPTERS) if scope == ALL else [scope]
    return [(c, q) for c in ids for q in CHAPTERS[c]["quiz"]]


def new_quiz(scope, count):
    pool = pool_for(scope)
    chosen = random.sample(pool, min(count, len(pool)))
    items = []
    for cid, (q, options, correct, hint, why) in chosen:
        opts = options[:]
        random.shuffle(opts)
        items.append({"ch": cid, "q": q, "opts": opts, "ans": options[correct],
                      "hint": hint, "why": why})
    run = st.session_state.get("quiz", {}).get("run", 0) + 1
    st.session_state.quiz = {
        "scope": scope, "count": count, "items": items, "pos": 0, "score": 0,
        "submitted": False, "hint": False, "was_correct": False, "run": run,
    }


def keywords_view(ch_id):
    ch = CHAPTERS[ch_id]
    st.header("Key words")
    for term, meaning in ch["keywords"]:
        st.markdown(f"**{term}**  \n{meaning}")


def quiz_view(scope):
    st.header("Quiz")
    pool_size = len(pool_for(scope))
    default = min(10, pool_size)
    count = st.sidebar.slider("Questions in this round", 5, min(pool_size, 50), default)
    qz = st.session_state.get("quiz")
    if qz is None or qz["scope"] != scope or qz["count"] != count:
        new_quiz(scope, count)
        qz = st.session_state.quiz
    st.caption(f"{pool_size} questions available here. Each round picks {len(qz['items'])} at random.")

    total = len(qz["items"])
    if qz["pos"] >= total:
        st.subheader(f"Quiz finished! Score: {qz['score']}/{total}")
        if qz["score"] == total:
            st.success("Perfect score! Excellent work.")
            st.balloons()
        elif qz["score"] >= total / 2:
            st.info("Good effort. Revise the key words and try again.")
        else:
            st.warning("Review the key words of these chapters and try again.")
        if st.button("Play a new round", type="primary"):
            new_quiz(scope, count)
            st.rerun()
        return

    item = qz["items"][qz["pos"]]
    st.progress(qz["pos"] / total)
    st.subheader(f"Question {qz['pos'] + 1} of {total}")
    if scope == ALL:
        st.caption(f"From Chapter {item['ch']}: {CHAPTERS[item['ch']]['name']}")
    st.write(item["q"])
    choice = st.radio(
        "Choose one:", item["opts"], index=None,
        key=f"choice_{qz['run']}_{qz['pos']}", disabled=qz["submitted"],
    )

    if not qz["submitted"]:
        col1, col2 = st.columns(2)
        if col1.button("💡 Show hint"):
            qz["hint"] = True
        submit = col2.button("Submit answer", type="primary")
        if qz["hint"]:
            st.info(f"Hint: {item['hint']}")
        if submit:
            if choice is None:
                st.warning("Please pick an option first.")
            else:
                qz["submitted"] = True
                qz["was_correct"] = (choice == item["ans"])
                if qz["was_correct"]:
                    qz["score"] += 1
                st.rerun()
    else:
        if qz["hint"]:
            st.info(f"Hint: {item['hint']}")
        if qz["was_correct"]:
            st.success("Correct! Congratulations, well done!")
        else:
            st.error(f"Not quite. The right answer is: {item['ans']}")
        st.write(f"**Explanation:** {item['why']}")
        last = qz["pos"] + 1 >= total
        if st.button("See my score" if last else "Next question ➡️", type="primary"):
            qz["pos"] += 1
            qz["submitted"] = False
            qz["hint"] = False
            st.rerun()


def practice_view(ch_id):
    ch = CHAPTERS[ch_id]
    st.header("Practice questions")
    pick = st.radio("Marks", ["All", 1, 2, 3], horizontal=True)
    items = [p for p in ch["practice"] if pick == "All" or p[0] == pick]
    st.caption(f"{len(items)} questions")
    if not items:
        st.write("No questions with those marks in this chapter.")
    for n, (marks, q, ans) in enumerate(items, 1):
        st.markdown(f"**Q{n}. [{marks} mark{'s' if marks > 1 else ''}]** {q}")
        with st.expander("Try it yourself, then click to see the answer"):
            st.write(ans)


st.title("🧪 CBSE Class XI Chemistry (NCERT)")
part = st.sidebar.radio("Choose a part", ["1. Key words", "2. Quiz", "3. Practice questions"])

if part.startswith("2"):
    options = [ALL] + list(CHAPTERS)
else:
    options = list(CHAPTERS)
scope = st.sidebar.selectbox(
    "Chapter", options,
    format_func=lambda n: "All chapters (mixed)" if n == ALL else f"{n}. {CHAPTERS[n]['name']}",
)

if part.startswith("1"):
    st.caption(f"Chapter {scope}: {CHAPTERS[scope]['name']}")
    keywords_view(scope)
elif part.startswith("2"):
    quiz_view(scope)
else:
    st.caption(f"Chapter {scope}: {CHAPTERS[scope]['name']}")
    practice_view(scope)
