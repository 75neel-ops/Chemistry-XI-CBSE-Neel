import streamlit as st
import random

# ==========================================
# 1. APPLICATION CONFIGURATION & DATA SETUP
# ==========================================
st.set_page_config(
    page_title="CBSE Class XI Chemistry Learning Game",
    page_icon="🧪",
    layout="centered"
)

# Sample Data Structure - Expand this with your actual NCERT content!
CHAPTERS_DATA = {
    "Chapter 1: Some Basic Concepts of Chemistry": {
        "keywords": {
            "Molarity (M)": "Number of moles of solute dissolved in one litre of the solution. Formula: M = Moles of solute / Volume of solution in L.",
            "Molality (m)": "Number of moles of solute present per kilogram (kg) of the solvent. Formula: m = Moles of solute / Mass of solvent in kg.",
            "Empirical Formula": "Represents the simplest whole-number ratio of various atoms present in a compound.",
            "Limiting Reagent": "The reactant which gets completely consumed first in a chemical reaction, limiting the amount of product formed."
        },
        "quiz": [
            {
                "question": "What is the SI unit of amount of substance?",
                "options": ["Kilogram", "Mole", "Ampere", "Kelvin"],
                "correct": "Mole",
                "hint": "Think about Avogadro's number ($6.022 \\times 10^{23}$ items per unit)."
            },
            {
                "question": "If 4.0 g of NaOH is dissolved in enough water to make 250 mL of solution, what is the molarity? (Molar mass of NaOH = 40 g/mol)",
                "options": ["0.1 M", "0.2 M", "0.4 M", "1.0 M"],
                "correct": "0.4 M",
                "hint": "First find the moles of NaOH ($4 / 40 = 0.1$ moles). Then divide by the volume in liters ($250\\text{ mL} = 0.25\\text{ L}$)."
            }
        ],
        "practice": [
            "Q1. Differentiate between precision and accuracy with an example.",
            "Q2. State and explain the Law of Definite Proportions.",
            "Q3. Calculate the mass percent of different elements present in sodium sulfate ($\\text{Na}_2\\text{SO}_4$)."
        ]
    }
    # You can easily add "Chapter 2: Structure of Atom", etc. here following the same structure!
}

# Initialize session states to track quiz progress without re-running issues
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False
if "answered" not in st.session_state:
    st.session_state.answered = False

# ==========================================
# 2. MAIN APP HEADER
# ==========================================
st.title("🧪 CBSE Class XI Chemistry (NCERT)")
st.subheader("Interactive Learning Game")
st.markdown("---")

# ==========================================
# 3. NAVIGATION / MAIN MENU
# ==========================================
# Using Streamlit components to replace terminal inputs
menu_choice = st.sidebar.radio(
    "MAIN MENU",
    [
        "🏠 Main Menu / Welcome",
        "📖 1. Key Words of Chapters",
        "🎯 2. Tricky Quiz (With Hints)",
        "📝 3. Chapter-Wise Practice Questions",
        "❌ 4. Quit Game"
    ]
)

# Select Chapter Dropdown (Global filter for options 1, 2, and 3)
if menu_choice != "🏠 Main Menu / Welcome" and menu_choice != "❌ 4. Quit Game":
    selected_chapter = st.sidebar.selectbox("Choose a Chapter:", list(CHAPTERS_DATA.keys()))
    chapter_content = CHAPTERS_DATA[selected_chapter]

# ==========================================
# 4. MENU ACTIONS
# ==========================================

# --- WELCOME SCREEN ---
if menu_choice == "🏠 Main Menu / Welcome":
    st.markdown("""
    ### Welcome to the Chemistry Learning App! 👋
    This application is designed to help you master **CBSE Class XI Chemistry** concepts seamlessly.
    
    **How to Navigate:**
    * Use the **Sidebar Menu** on the left to pick your activity.
    * Select specific NCERT chapters from the dropdown menu when working on tasks.
    """)

# --- OPTION 1: KEY WORDS ---
elif menu_choice == "📖 1. Key Words of Chapters":
    st.header(f"🔑 Key Definitions")
    st.write(f"Reviewing terms for: *{selected_chapter}*")
    
    for word, definition in chapter_content["keywords"].items():
        with st.expander(f"🔍 {word}"):
            st.markdown(definition)

# --- OPTION 2: TRICKY QUIZ ---
elif menu_choice == "🎯 2. Tricky Quiz (With Hints)":
    st.header("🎯 Tricky Quiz Mode")
    quiz_list = chapter_content["quiz"]
    
    if len(quiz_list) == 0:
        st.warning("No quiz questions added for this chapter yet!")
    else:
        # Reset if chapter changes unexpectedly
        if st.session_state.quiz_index >= len(quiz_list):
            st.session_state.quiz_index = 0
            st.session_state.score = 0
            
        current_q = quiz_list[st.session_state.quiz_index]
        
        st.markdown(f"#### Question {st.session_state.quiz_index + 1} of {len(quiz_list)}")
        st.info(current_q["question"])
        
        # User submits answer via radio selection
        user_ans = st.radio("Choose the correct option:", current_q["options"], key=f"q_{st.session_state.quiz_index}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💡 Show Hint"):
                st.session_state.show_hint = True
                
        with col2:
            submit_btn = st.button("✅ Submit Answer", disabled=st.session_state.answered)

        if st.session_state.show_hint:
            st.warning(f"**Hint:** {current_q['hint']}")
            
        if submit_btn or st.session_state.answered:
            st.session_state.answered = True
            if user_ans == current_q["correct"]:
                st.success("🎉 Correct Answer!")
                if submit_btn: # avoid doubling score on refresh
                    st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect! The correct answer was: **{current_q['correct']}**")
                
            # Next Question handling
            if st.session_state.quiz_index < len(quiz_list) - 1:
                if st.button("Next Question ➡️"):
                    st.session_state.quiz_index += 1
                    st.session_state.show_hint = False
                    st.session_state.answered = False
                    st.rerun()
            else:
                st.markdown("---")
                st.balloons()
                st.markdown(f"### 🏆 Quiz Completed! Your Final Score: **{st.session_state.score} / {len(quiz_list)}**")
                if st.button("🔄 Restart Quiz"):
                    st.session_state.quiz_index = 0
                    st.session_state.score = 0
                    st.session_state.show_hint = False
                    st.session_state.answered = False
                    st.rerun()

# --- OPTION 3: PRACTICE QUESTIONS ---
elif menu_choice == "📝 3. Chapter-Wise Practice Questions":
    st.header("📝 NCERT Practice Questions")
    st.write(f"Solve these questions to evaluate your understanding of *{selected_chapter}*:")
    
    for question in chapter_content["practice"]:
        st.markdown(f"- {question}")

# --- OPTION 4: QUIT ---
elif menu_choice == "❌ 4. Quit Game":
    st.header("Game Closed")
    st.write("Thank you for using the CBSE Class XI Chemistry App! Close this browser tab whenever you are ready.")
