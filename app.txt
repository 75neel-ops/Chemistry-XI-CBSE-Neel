#!/usr/bin/env python3
"""
CBSE Class XI Chemistry (NCERT) - Learning Game
-----------------------------------------------
Part 1: Key words of each chapter
Part 2: Tricky quiz with hints, congratulations / correct answer
Part 3: Chapter-wise practice questions (1, 2, 3 marks) with answers

Run:  python3 chem_game.py
No packages needed. To add content, edit the CHAPTERS dictionary below.
All questions are original practice material written to follow the NCERT
(rationalised) Class XI Chemistry syllabus - they are not copied from the book.
"""
import random
import sys

# Each chapter:
#   keywords : list of (term, meaning)
#   quiz     : list of (question, [options], index_of_correct, hint, explanation)
#   practice : list of (marks, question, answer)
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

LINE = "=" * 62
LABELS = "abcd"


def ask(prompt):
    """input() that exits cleanly on Ctrl+D / Ctrl+C."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye! Keep practising.")
        sys.exit(0)


def choose_chapter():
    print("\n" + LINE)
    for number, ch in CHAPTERS.items():
        print(f"  {number}. {ch['name']}")
    print("  0. Back")
    print(LINE)
    while True:
        pick = ask("Choose chapter number: ")
        if pick == "0":
            return None
        if pick.isdigit() and int(pick) in CHAPTERS:
            return int(pick)
        print("Please enter a valid chapter number.")


def show_keywords():
    n = choose_chapter()
    if n is None:
        return
    ch = CHAPTERS[n]
    print(f"\n{LINE}\nChapter {n}: {ch['name']}\nKEY WORDS\n{LINE}")
    for term, meaning in ch["keywords"]:
        print(f"\n* {term}\n    {meaning}")
    ask("\nPress Enter to go back to the menu...")


def run_quiz():
    n = choose_chapter()
    if n is None:
        return
    ch = CHAPTERS[n]
    questions = ch["quiz"][:]
    random.shuffle(questions)
    score = 0
    print(f"\n{LINE}\nQUIZ - Chapter {n}: {ch['name']}")
    print("Type a, b, c or d to answer.  h = hint,  q = quit quiz.\n" + LINE)
    for number, (q, options, correct, hint, why) in enumerate(questions, 1):
        order = list(range(len(options)))
        random.shuffle(order)
        correct_pos = order.index(correct)
        print(f"\nQuestion {number}/{len(questions)}:\n{q}\n")
        for pos, idx in enumerate(order):
            print(f"  {LABELS[pos]}) {options[idx]}")
        hint_used = False
        while True:
            ans = ask("\nYour answer (h for hint): ").lower()
            if ans == "q":
                print(f"\nQuiz stopped. Score: {score}/{number - 1}")
                return
            if ans == "h":
                print(f"  Hint: {hint}")
                hint_used = True
                continue
            if ans in LABELS[: len(options)]:
                break
            print("  Please type a, b, c, d, h or q.")
        if LABELS.index(ans) == correct_pos:
            score += 1
            print("\nCorrect! Congratulations, well done!" + (" (with a hint)" if hint_used else ""))
        else:
            print(f"\nNot quite. The right answer is {LABELS[correct_pos]}) {options[correct]}")
        print(f"Explanation: {why}")
        if number < len(questions):
            ask("\nPress Enter for the next question...")
    print(f"\n{LINE}\nQuiz finished! Score: {score}/{len(questions)}")
    if score == len(questions):
        print("Perfect score! Excellent work.")
    elif score >= len(questions) / 2:
        print("Good effort. Revise the keywords and try again.")
    else:
        print("Review the key words of this chapter and try again.")
    ask("\nPress Enter to go back to the menu...")


def practice_questions():
    n = choose_chapter()
    if n is None:
        return
    ch = CHAPTERS[n]
    print(f"\n{LINE}\nPRACTICE QUESTIONS - Chapter {n}: {ch['name']}\n{LINE}")
    marks = ask("Filter by marks (1/2/3) or press Enter for all: ")
    items = [p for p in ch["practice"] if not marks.isdigit() or p[0] == int(marks)]
    if not items:
        print("No questions with those marks in this chapter.")
        return
    for number, (m, q, a) in enumerate(items, 1):
        print(f"\nQ{number}. [{m} mark{'s' if m > 1 else ''}] {q}")
        ask("   (Try it yourself, then press Enter to see the answer)")
        print(f"   Answer: {a}")
        if number < len(items):
            if ask("\nEnter = next question, q = stop: ").lower() == "q":
                break
    ask("\nPress Enter to go back to the menu...")


def main():
    print(LINE + "\n  CBSE CLASS XI CHEMISTRY (NCERT) - LEARNING GAME\n" + LINE)
    while True:
        print("\nMAIN MENU")
        print("  1. Key words of each chapter")
        print("  2. Quiz (tricky questions with hints)")
        print("  3. Chapter-wise practice questions")
        print("  4. Quit")
        choice = ask("Your choice: ")
        if choice == "1":
            show_keywords()
        elif choice == "2":
            run_quiz()
        elif choice == "3":
            practice_questions()
        elif choice == "4":
            print("Goodbye! Keep practising.")
            break
        else:
            print("Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
