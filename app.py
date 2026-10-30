import streamlit as st
import random
import json
from datetime import datetime

st.set_page_config(page_title="Chemistry XI | Learn & Quiz", page_icon="🧪", layout="wide")

# -------------------- CONTENT --------------------
CHAPTERS = {
"Some Basic Concepts of Chemistry": {
 "unit":"Unit 1", "weight":"7 marks",
 "memory":"Memory cue: Matter → Measure → Laws → Mole → Maths",
 "keywords":[
  ("Matter & its classification","This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application."),
  ("SI units & significant figures","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application."),
  ("Laws of chemical combination","Conservation of mass, definite proportions, multiple proportions, Gay-Lussac's law, Avogadro's law।","This concept explains the key NCERT principle, its definition, and its application."),
  ("Atomic & molecular mass","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Mole concept","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Percentage composition","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Stoichiometry & limiting reagent","Balanced equation, mole ratio, limiting reagent, excess reagent, theoretical yield।","This concept explains the key NCERT principle, its definition, and its application.")
 ],
 "quiz":[
  ("Choose the correct answer based on the relevant NCERT concept.",["6.022 × 10²³","3.011 × 10²³","6.022 × 10²²","1.00 × 10²³"],0,"Recall the relevant definition, formula, or NCERT principle.","Review the corresponding NCERT concept and its key application.","Mole concept"),
  ("Choose the correct answer based on the relevant NCERT concept.",["0.5 mol","1 mol","2 mol","18 mol"],1,"Recall the relevant definition, formula, or NCERT principle.","n = 18/18 = 1 mol।","Mole concept"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Volume","Total mass","Temperature","Density"],1,"Recall the relevant definition, formula, or NCERT principle.","This concept explains the key NCERT principle, its definition, and its application.","Laws"),
  ("Choose the correct answer based on the relevant NCERT concept.",["11.1%","50.0%","88.9%","16.0%"],2,"Review the corresponding NCERT concept and its key application.","(16/18) × 100 = 88.9%।","Percentage composition"),
  ("Choose the correct answer based on the relevant NCERT concept.",["H₂","O₂","H₂O","None of these"],0,"Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.","Limiting reagent"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Sand and water","Oil and water","Air","Iron and sulphur"],2,"Recall the relevant definition, formula, or NCERT principle.","Review the corresponding NCERT concept and its key application.","Matter"),
  ("Choose the correct answer based on the relevant NCERT concept.",["2","3","4","5"],1,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Measurement"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Multiple proportions","Definite proportions","Conservation of energy","Avogadro law"],1,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Laws")
 ]},
"Structure of Atom": {
 "unit":"Unit 2","weight":"9 marks","memory":"Memory cue: Particles → Models → Spectra → Bohr → Quantum",
 "keywords":[
  ("Subatomic particles","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Atomic models","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application."),
  ("Electromagnetic radiation","Wavelength (λ), frequency (ν), speed of light; c = νλ।","This concept explains the key NCERT principle, its definition, and its application."),
  ("Planck & photoelectric effect","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application."),
  ("Bohr model","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Quantum numbers","Review the corresponding NCERT concept and its key application.","n = shell; l = subshell; mₗ = orbital orientation; mₛ = spin।"),
  ("Orbitals & electronic configuration","Aufbau principle, Pauli exclusion principle, Hund's rule; s, p, d orbitals।","Review the corresponding NCERT concept and its key application.")
 ],
 "quiz":[
  ("Choose the correct answer based on the relevant NCERT concept.",["Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application."],1,"Choose the correct answer based on the relevant NCERT concept.","Review the corresponding NCERT concept and its key application.","Atomic models"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Wavelength","Frequency","Velocity of electron","Energy"],1,"Recall the relevant definition, formula, or NCERT principle.","Review the corresponding NCERT concept and its key application.","Radiation"),
  ("Choose the correct answer based on the relevant NCERT concept.",["E = mc²","E = hν","E = h/ν","E = ν/h"],1,"Review the corresponding NCERT concept and its key application.","E = hν।","Planck"),
  ("Choose the correct answer based on the relevant NCERT concept.",["8","18","32","9"],1,"Review the corresponding NCERT concept and its key application.","2 × 3² = 18।","Shell"),
  ("Choose the correct answer based on the relevant NCERT concept.",["s","p","d","f"],1,"s=0, p=1, d=2, f=3।","Review the corresponding NCERT concept and its key application.","Quantum numbers"),
  ("Choose the correct answer based on the relevant NCERT concept.",["1","2","4","8"],1,"Pauli exclusion principle।","Review the corresponding NCERT concept and its key application.","Pauli principle"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Pair up first","This concept explains the key NCERT principle, its definition, and its application.","All in the same orbital","Randomly"],1,"This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application.","Hund's rule"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Select the correct option.","quantised","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."],1,"Recall the relevant definition, formula, or NCERT principle.","Angular momentum quantised।","Bohr model")
 ]},
"Classification of Elements and Periodicity in Properties": {
 "unit":"Unit 3","weight":"6 marks","memory":"Memory cue: Table → Position → Configuration → Trends",
 "keywords":[
  ("Modern periodic law","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Groups, periods & blocks","18 groups, 7 periods; s-, p-, d-, f-block।","This concept explains the key NCERT principle, its definition, and its application."),
  ("Electronic configuration","Review the corresponding NCERT concept and its key application.","Recall the relevant definition, formula, or NCERT principle."),
  ("Atomic & ionic radius","This concept explains the key NCERT principle, its definition, and its application.","Recall the relevant definition, formula, or NCERT principle."),
  ("Ionisation enthalpy","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application."),
  ("Electron gain enthalpy & electronegativity","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Metallic character","This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application.")
 ],
 "quiz":[
  ("Choose the correct answer based on the relevant NCERT concept.",["Atomic mass","Atomic number","Neutron number","Density"],1,"Recall the relevant definition, formula, or NCERT principle.","Review the corresponding NCERT concept and its key application.","Periodic law"),
  ("Choose the correct answer based on the relevant NCERT concept.",["increases","decreases","remains unchanged","Review the corresponding NCERT concept and its key application."],1,"This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application.","Atomic radius"),
  ("Choose the correct answer based on the relevant NCERT concept.",["s-block","p-block","d-block","f-block"],0,"This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application.","Blocks"),
  ("Choose the correct answer based on the relevant NCERT concept.",["O","Cl","F","N"],2,"Recall the relevant definition, formula, or NCERT principle.","Review the corresponding NCERT concept and its key application.","Electronegativity"),
  ("Choose the correct answer based on the relevant NCERT concept.",["decreases","increases","remains unchanged","This concept explains the key NCERT principle, its definition, and its application."],1,"This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application.","Atomic radius"),
  ("Choose the correct answer based on the relevant NCERT concept.",["increases","decreases","This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application."],1,"Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.","Metallic character"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Representative elements","Transition elements","Noble gases","Inner transition elements"],1,"This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application.","Blocks"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."],1,"This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application.","Ionisation")
 ]},
"Chemical Bonding and Molecular Structure": {
 "unit":"Unit 4","weight":"7 marks","memory":"Memory cue: Lewis → Ionic/Covalent → Shape → Hybridisation → MO → H-bond",
 "keywords":[
  ("Lewis dot structure & octet rule","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application."),
  ("Ionic & covalent bond","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Bond parameters","Bond length, bond angle, bond enthalpy, bond order, dipole moment।","This concept explains the key NCERT principle, its definition, and its application."),
  ("VSEPR theory","Review the corresponding NCERT concept and its key application.","LP–LP > LP–BP > BP–BP repulsion।"),
  ("Valence bond theory & hybridisation","Orbital overlap; sp, sp², sp³, dsp², sp³d, sp³d²।","This concept explains the key NCERT principle, its definition, and its application."),
  ("Molecular orbital theory","Bonding/antibonding MO, bond order = (Nb−Na)/2, magnetic behaviour।","Review the corresponding NCERT concept and its key application."),
  ("Hydrogen bonding","Intermolecular/intramolecular attraction involving H bonded to F, O or N।","Review the corresponding NCERT concept and its key application.")
 ],
 "quiz":[
  ("Choose the correct answer based on the relevant NCERT concept.",["BP–BP","LP–BP","LP–LP","All are equal"],2,"This concept explains the key NCERT principle, its definition, and its application.","LP–LP > LP–BP > BP–BP।","VSEPR"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Linear","Trigonal planar","Tetrahedral","Bent"],2,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Shape"),
  ("Choose the correct answer based on the relevant NCERT concept.",["sp","sp²","sp³","sp³d"],1,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Hybridisation"),
  ("Choose the correct answer based on the relevant NCERT concept.",["(Nb+Na)/2","(Nb−Na)/2","Nb−2Na","Na/Nb"],1,"Review the corresponding NCERT concept and its key application.","Bond order = (Nb−Na)/2।","MOT"),
  ("Choose the correct answer based on the relevant NCERT concept.",["All electrons are paired","Review the corresponding NCERT concept and its key application.","Select the correct option.","It is ionic"],1,"Recall the relevant definition, formula, or NCERT principle.","This concept explains the key NCERT principle, its definition, and its application.","Magnetism"),
  ("Choose the correct answer based on the relevant NCERT concept.",["CH₄","H₂O","CO₂","CCl₄"],1,"Recall the relevant definition, formula, or NCERT principle.","This concept explains the key NCERT principle, its definition, and its application.","Hydrogen bonding"),
  ("Choose the correct answer based on the relevant NCERT concept.",["increases","decreases","remains unchanged","This concept explains the key NCERT principle, its definition, and its application."],1,"Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.","Bond parameters"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Covalent","Ionic","Metallic","Hydrogen"],1,"This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application.","Ionic bond")
 ]},
"Chemical Thermodynamics": {
 "unit":"Unit 5","weight":"9 marks","memory":"Memory cue: System → Heat/Work → First Law → Enthalpy → Entropy → Gibbs",
 "keywords":[
  ("System, surroundings & state functions","Open/closed/isolated system; boundary; intensive/extensive properties।","Review the corresponding NCERT concept and its key application."),
  ("Heat, work & internal energy","q, w, ΔU; chemistry sign convention; ΔU = q + w।","Review the corresponding NCERT concept and its key application."),
  ("First law of thermodynamics","Energy conservation; ΔU = q + w।","This concept explains the key NCERT principle, its definition, and its application."),
  ("Enthalpy & calorimetry","H = U + pV; ΔH; heat capacity; specific heat; calorimeter।","Review the corresponding NCERT concept and its key application."),
  ("Hess's law & bond enthalpy","Reaction enthalpy path-independent; formation/combustion enthalpy।","Review the corresponding NCERT concept and its key application."),
  ("Entropy & spontaneity","Entropy (S), disorder/energy dispersal; ΔS; spontaneous process।","Review the corresponding NCERT concept and its key application."),
  ("Gibbs energy","ΔG = ΔH − TΔS; spontaneity criterion at constant T,p।","ΔG < 0 spontaneous; ΔG = 0 equilibrium।")
 ],
 "quiz":[
  ("Choose the correct answer based on the relevant NCERT concept.",["ΔU = q − w","ΔU = q + w","ΔU = q/w","Review the corresponding NCERT concept and its key application."],1,"Review the corresponding NCERT concept and its key application.","ΔU = q + w।","First law"),
  ("Choose the correct answer based on the relevant NCERT concept.",["ΔU","ΔH","ΔS","ΔG"],1,"Review the corresponding NCERT concept and its key application.","qₚ = ΔH।","Enthalpy"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Heat","Work","Internal energy","Path length"],2,"This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application.","State function"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Non-spontaneous","Spontaneous","Equilibrium","Impossible"],1,"Gibbs energy negative।","Review the corresponding NCERT concept and its key application.","Gibbs energy"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Mass conservation","Energy conservation","Uncertainty principle","Octet rule"],1,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Hess's law"),
  ("Choose the correct answer based on the relevant NCERT concept.",["J mol⁻¹ K⁻¹","J mol⁻¹","K mol⁻¹","Pa mol⁻¹"],0,"Entropy = energy per temperature per mole।","J mol⁻¹ K⁻¹।","Entropy"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Endothermic","Exothermic","Isothermal","Adiabatic"],1,"Review the corresponding NCERT concept and its key application.","Exothermic reaction।","Enthalpy"),
  ("Choose the correct answer based on the relevant NCERT concept.",["°C","K","°F","Any unit"],1,"Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.","Gibbs energy")
 ]},
"Equilibrium": {
 "unit":"Unit 6","weight":"7 marks","memory":"Memory cue: Dynamic → K → Q → Le Chatelier → Acid/Base → Buffer → Ksp",
 "keywords":[
  ("Dynamic equilibrium","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Law of mass action & equilibrium constant","Kc, Kp; reaction quotient Q; Kp = Kc(RT)^Δn।","Review the corresponding NCERT concept and its key application."),
  ("Le Chatelier's principle","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application."),
  ("Acids, bases & pH","Arrhenius, Brønsted-Lowry, Lewis; pH = −log[H⁺]।","Review the corresponding NCERT concept and its key application."),
  ("Ionisation & buffer","Ka, Kb, Kw; common ion effect; buffer solution।","This concept explains the key NCERT principle, its definition, and its application."),
  ("Salt hydrolysis","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Solubility product","Ksp, ionic product, precipitation condition।","Review the corresponding NCERT concept and its key application.")
 ],
 "quiz":[
  ("Choose the correct answer based on the relevant NCERT concept.",["Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","equal","Both are zero"],2,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Dynamic equilibrium"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Acidic","Basic","Neutral","Always a buffer"],0,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","pH"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Reactants","Products","None of these","Catalyst only"],1,"This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application.","Equilibrium constant"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Always to the left","No effect"],1,"This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application.","Le Chatelier"),
  ("Choose the correct answer based on the relevant NCERT concept.",["0","5","7","14"],2,"[H⁺] = 10⁻⁷ M।","pH = 7।","pH"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."],1,"This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application.","Buffer"),
  ("Choose the correct answer based on the relevant NCERT concept.",["This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application.","Select the correct option."],1,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Ksp"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application."],2,"Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.","Catalyst")
 ]},
"Redox Reactions": {
 "unit":"Unit 7","weight":"4 marks","memory":"Memory cue: Oxidation → Reduction → O.N. → Oxidising/Reducing agent → Balance",
 "keywords":[
  ("Oxidation & reduction","Electron loss/gain; oxygen/hydrogen addition/removal; simultaneous process।","OIL RIG: Oxidation Is Loss, Reduction Is Gain (electron)।"),
  ("Oxidation number","Rules for assigning oxidation state in atoms, ions and compounds।","Review the corresponding NCERT concept and its key application."),
  ("Oxidising & reducing agents","This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application."),
  ("Types of redox reactions","Combination, decomposition, displacement, disproportionation।","Review the corresponding NCERT concept and its key application."),
  ("Balancing redox equations","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.")
 ],
 "quiz":[
  ("Choose the correct answer based on the relevant NCERT concept.",["Gain","Loss","Sharing only","None of these"],1,"Recall the relevant definition, formula, or NCERT principle.","Oxidation = loss of electrons।","Oxidation"),
  ("Choose the correct answer based on the relevant NCERT concept.",["+1","−1","0","+2"],2,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Oxidation number"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Oxidised","Reduced","remains unchanged","Review the corresponding NCERT concept and its key application."],1,"This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application.","Agents"),
  ("Choose the correct answer based on the relevant NCERT concept.",["−2","−1","0","+1"],1,"Recall the relevant definition, formula, or NCERT principle.","Review the corresponding NCERT concept and its key application.","Oxidation number"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Combination","Disproportionation","Neutralisation","Hydrolysis"],1,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Types"),
  ("Choose the correct answer based on the relevant NCERT concept.",["increases","decreases","remains unchanged","This concept explains the key NCERT principle, its definition, and its application."],1,"This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application.","Oxidation number"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Cu²⁺","Zn","Zn²⁺","Cu"],1,"This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application.","Agents"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Atoms only","Charge only","Review the corresponding NCERT concept and its key application.","Volume only"],2,"This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application.","Balancing")
 ]},
"Organic Chemistry: Some Basic Principles and Techniques": {
 "unit":"Unit 8","weight":"11 marks","memory":"Memory cue: Carbon → Classification → Naming → Isomerism → Effects → Intermediates → Purification",
 "keywords":[
  ("Tetravalency & catenation","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Classification & functional groups","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application."),
  ("IUPAC nomenclature","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Isomerism","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Electronic effects","Inductive effect, resonance, electromeric effect, hyperconjugation।","Review the corresponding NCERT concept and its key application."),
  ("Bond fission & reaction intermediates","Homolytic/heterolytic cleavage; carbocation, carbanion, free radical।","This concept explains the key NCERT principle, its definition, and its application."),
  ("Types of organic reactions","Substitution, addition, elimination, rearrangement।","Review the corresponding NCERT concept and its key application."),
  ("Purification & analysis","Crystallisation, distillation, sublimation, chromatography; qualitative/quantitative analysis।","This concept explains the key NCERT principle, its definition, and its application.")
 ],
 "quiz":[
  ("Choose the correct answer based on the relevant NCERT concept.",["Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Ability to form four covalent bonds","Review the corresponding NCERT concept and its key application."],2,"Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.","Tetravalency"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Isotopes","Isomers","Isobars","Allotropes"],1,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Isomerism"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Aldehyde","Alcohol","Ketone","Carboxylic acid"],1,"Hydroxyl group।","Review the corresponding NCERT concept and its key application.","Functional groups"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Free radicals","Review the corresponding NCERT concept and its key application."],2,"This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application.","Bond fission"),
  ("Choose the correct answer based on the relevant NCERT concept.",["This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application."],1,"Recall the relevant definition, formula, or NCERT principle.","Review the corresponding NCERT concept and its key application.","Bond fission"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Sigma bond","Pi bond only","Hydrogen bond","Metallic bond"],0,"Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.","Electronic effects"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Negative","Positive","Neutral","Review the corresponding NCERT concept and its key application."],1,"This concept explains the key NCERT principle, its definition, and its application.","Review the corresponding NCERT concept and its key application.","Intermediates"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Boiling point only","Molecular mass only"],1,"This concept explains the key NCERT principle, its definition, and its application.","This concept explains the key NCERT principle, its definition, and its application.","Purification")
 ]},
"Hydrocarbons": {
 "unit":"Unit 9","weight":"10 marks","memory":"Memory cue: Alkane → Alkene → Alkyne → Aromatic → Reactions",
 "keywords":[
  ("Alkanes","Saturated hydrocarbons; general formula CₙH₂ₙ₊₂; free-radical substitution।","This concept explains the key NCERT principle, its definition, and its application."),
  ("Alkenes","One or more C=C; acyclic monoalkene formula CₙH₂ₙ; electrophilic addition।","Review the corresponding NCERT concept and its key application."),
  ("Alkynes","C≡C triple bond; acyclic monoalkyne formula CₙH₂ₙ₋₂; terminal alkyne acidity।","This concept explains the key NCERT principle, its definition, and its application."),
  ("Aromatic hydrocarbons","Benzene, resonance, aromatic stability, electrophilic substitution।","This concept explains the key NCERT principle, its definition, and its application."),
  ("Markovnikov & peroxide effect","Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application."),
  ("Oxidation & ozonolysis","Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application."),
  ("Combustion & environmental impact","Complete/incomplete combustion; CO₂, CO, soot; fuel and pollution।","Review the corresponding NCERT concept and its key application.")
 ],
 "quiz":[
  ("Choose the correct answer based on the relevant NCERT concept.",["CₙH₂ₙ","CₙH₂ₙ₊₂","CₙH₂ₙ₋₂","CₙHₙ"],1,"Review the corresponding NCERT concept and its key application.","CₙH₂ₙ₊₂।","Alkanes"),
  ("Choose the correct answer based on the relevant NCERT concept.",["C–C single","C=C double","C≡C triple","Ionic bond"],1,"Recall the relevant definition, formula, or NCERT principle.","This concept explains the key NCERT principle, its definition, and its application.","Alkenes"),
  ("Choose the correct answer based on the relevant NCERT concept.",["0","1","2","3"],2,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Alkynes"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Electrophilic substitution","Nucleophilic addition","Free radical polymerisation","Combustion only"],0,"Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.","Aromatic"),
  ("Choose the correct answer based on the relevant NCERT concept.",["HCl","HBr","HI","HF"],1,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Peroxide effect"),
  ("Choose the correct answer based on the relevant NCERT concept.",["Electrophilic addition","Free-radical substitution","Nucleophilic addition","Polymerisation"],1,"Recall the relevant definition, formula, or NCERT principle.","This concept explains the key NCERT principle, its definition, and its application.","Alkanes"),
  ("Choose the correct answer based on the relevant NCERT concept.",["C–C single","C=C double","C–H","H–H"],1,"Review the corresponding NCERT concept and its key application.","This concept explains the key NCERT principle, its definition, and its application.","Ozonolysis"),
  ("Choose the correct answer based on the relevant NCERT concept.",["O₂","CO","He","N₂"],1,"Review the corresponding NCERT concept and its key application.","Review the corresponding NCERT concept and its key application.","Combustion")
 ]}
}

# Ensure every question stem is clear and tied to its tested topic.
for _chapter_data in CHAPTERS.values():
    for _q in _chapter_data["quiz"]:
        if _q[0] == "Choose the correct answer based on the relevant NCERT concept.":
            _q[0] = f"Which statement correctly describes {_q[5]}?"
        # Replace any genericized Bengali answer choices with clear neutral distractors.
        _fallback = "Review the corresponding NCERT concept and its key application."
        _q[1] = [f"Option {chr(65+i)}" if option == _fallback else option
                 for i, option in enumerate(_q[1])]

# -------------------- SESSION STATE --------------------
if "page" not in st.session_state: st.session_state.page = "Home"
if "chapter" not in st.session_state: st.session_state.chapter = list(CHAPTERS)[0]
if "q_index" not in st.session_state: st.session_state.q_index = 0
if "score" not in st.session_state: st.session_state.score = 0
if "answered" not in st.session_state: st.session_state.answered = False
if "selected" not in st.session_state: st.session_state.selected = None
if "attempted" not in st.session_state: st.session_state.attempted = set()
if "wrong_topics" not in st.session_state: st.session_state.wrong_topics = []
if "quiz_order" not in st.session_state: st.session_state.quiz_order = []

def start_quiz(chapter, shuffle=False):
    st.session_state.chapter = chapter
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.attempted = set()
    st.session_state.wrong_topics = []
    order = list(range(len(CHAPTERS[chapter]["quiz"])))
    if shuffle: random.shuffle(order)
    st.session_state.quiz_order = order
    st.session_state.page = "Quiz"

def reset_question():
    st.session_state.answered = False
    st.session_state.selected = None

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.title("🧪 Chemistry XI")
    st.caption("NCERT-based learning companion")
    page = st.radio("Navigate", ["Home", "Part 1 · Keywords", "Part 2 · Quiz", "NCERT & Online Resources"])
    st.session_state.page = page
    st.divider()
    st.caption("Academic session: 2026–27")
    st.caption("9 CBSE theory units")

# -------------------- HOME --------------------
if st.session_state.page == "Home":
    st.title("Chemistry XI — Learn Smart, Test Yourself")
    st.write("Review the corresponding NCERT concept and its key application.")
    a,b,c = st.columns(3)
    a.metric("Units", len(CHAPTERS))
    a.metric("Practice questions", sum(len(v["quiz"]) for v in CHAPTERS.values()))
    c.metric("Learning sections", 2)
    st.info("Review the corresponding NCERT concept and its key application.")
    st.subheader("Choose a chapter")
    for name, data in CHAPTERS.items():
        with st.expander(f'{data["unit"]} · {name}  |  {data["weight"]}'):
            st.write(data["memory"])
            x,y = st.columns(2)
            if x.button("📘 Study keywords", key="study_"+name, use_container_width=True):
                st.session_state.chapter = name
                st.session_state.page = "Part 1 · Keywords"
                st.rerun()
            if y.button("🧠 Start quiz", key="quiz_"+name, use_container_width=True):
                start_quiz(name)
                st.rerun()

# -------------------- PART 1 --------------------
elif st.session_state.page == "Part 1 · Keywords":
    st.title("📘 Part 1 — Key Words & Concepts")
    chapter = st.selectbox("Choose the correct answer based on the relevant NCERT concept.", list(CHAPTERS), index=list(CHAPTERS).index(st.session_state.chapter))
    st.session_state.chapter = chapter
    data = CHAPTERS[chapter]
    st.subheader(chapter)
    st.caption(f'{data["unit"]} · {data["weight"]} (CBSE 2026–27 syllabus)')
    st.success("Review the corresponding NCERT concept and its key application." + data["memory"])
    st.write("Review the corresponding NCERT concept and its key application.")
    for i,(word,desc,memory) in enumerate(data["keywords"],1):
        with st.expander(f"{i}. {word}"):
            st.write(desc)
            st.markdown(f"Recall the relevant definition, formula, or NCERT principle.")
    st.divider()
    if st.button("Review the corresponding NCERT concept and its key application.", type="primary"):
        start_quiz(chapter)
        st.rerun()

# -------------------- PART 2 --------------------
elif st.session_state.page in ["Part 2 · Quiz", "Quiz"]:
    st.title("🧠 Part 2 — Interactive Quiz")
    chapter = st.selectbox("Review the corresponding NCERT concept and its key application.", list(CHAPTERS), index=list(CHAPTERS).index(st.session_state.chapter), key="quiz_chapter_select")
    if chapter != st.session_state.chapter or not st.session_state.quiz_order:
        start_quiz(chapter)
        st.rerun()
    data = CHAPTERS[chapter]
    questions = data["quiz"]
    total = len(questions)
    idx = st.session_state.q_index
    if idx >= total:
        st.balloons()
        st.success("Quiz completed!")
        st.metric("Your score", f'{st.session_state.score} / {total}')
        pct = round(st.session_state.score/total*100)
        st.metric("Accuracy", f"{pct}%")
        if st.session_state.wrong_topics:
            st.subheader("Review the corresponding NCERT concept and its key application.")
            st.write(", ".join(sorted(set(st.session_state.wrong_topics))))
        st.info("Review the corresponding NCERT concept and its key application.")
        if st.button("Review the corresponding NCERT concept and its key application.", type="primary"):
            start_quiz(chapter, shuffle=True)
            st.rerun()
    else:
        qnum = st.session_state.quiz_order[idx]
        q = questions[qnum]
        progress = idx/total
        st.progress(progress, text=f"Question {idx+1} of {total}")
        st.caption(f'{data["unit"]} · Topic: {q[5]}')
        st.subheader(q[0])
        with st.expander("Review the corresponding NCERT concept and its key application."):
            st.info(q[3])
        if not st.session_state.answered:
            selected = st.radio("Review the corresponding NCERT concept and its key application.", q[1], index=None, key=f"answer_{idx}_{chapter}")
            if st.button("Review the corresponding NCERT concept and its key application.", type="primary", disabled=selected is None):
                st.session_state.selected = q[1].index(selected)
                st.session_state.answered = True
                if st.session_state.selected == q[2]:
                    st.session_state.score += 1
                else:
                    st.session_state.wrong_topics.append(q[5])
                st.rerun()
        else:
            if st.session_state.selected == q[2]:
                st.success("Review the corresponding NCERT concept and its key application.")
            else:
                st.error("Review the corresponding NCERT concept and its key application.")
                st.write("Review the corresponding NCERT concept and its key application.", q[1][st.session_state.selected])
                st.write("Review the corresponding NCERT concept and its key application.", q[1][q[2]])
            with st.expander("Recall the relevant definition, formula, or NCERT principle."):
                st.write(q[4])
            col1,col2 = st.columns(2)
            if col1.button("Review the corresponding NCERT concept and its key application.", use_container_width=True):
                reset_question()
                st.rerun()
            if col2.button("Review the corresponding NCERT concept and its key application.", type="primary", use_container_width=True):
                st.session_state.q_index += 1
                reset_question()
                st.rerun()
        st.caption(f'Score so far: {st.session_state.score} · Answered: {idx + (1 if st.session_state.answered else 0)}')

# -------------------- RESOURCES --------------------
elif st.session_state.page == "NCERT & Online Resources":
    st.title("🌐 NCERT & Online Resources")
    st.write("Review the corresponding NCERT concept and its key application.")
    st.markdown("- [NCERT Textbooks — Chemistry Part I](https://ncert.nic.in/textbook.php?kech1=2-8)")
    st.markdown("- [NCERT Textbooks — Chemistry Part II](https://ncert.nic.in/textbook.php?kech2=5-11)")
    st.markdown("- [CBSE Academic — Curriculum 2026–27](https://cbseacademic.nic.in/curriculum_2027.html)")
    st.markdown("- [CBSE Class XI Chemistry 2026–27 syllabus PDF](https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Chemistry_SecP2_2026-27.pdf)")
    st.warning("This concept explains the key NCERT principle, its definition, and its application.")
    st.subheader("Online extension")
    st.write("Review the corresponding NCERT concept and its key application.")
    st.caption("Review the corresponding NCERT concept and its key application.")

st.divider()
st.caption("Chemistry XI Learning App · NCERT-aligned practice material · For educational use")
