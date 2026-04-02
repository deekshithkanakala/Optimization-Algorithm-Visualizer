"""
Home — Optimization Algorithm Visualizer
"""

import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Optimization Visualizer",
    layout="wide",
    page_icon="🔍"
)

# ------------------ SIDEBAR ------------------
st.sidebar.title("🔍 Navigation")
st.sidebar.page_link("Home.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/1_Unconstrained_Minimization.py", label="Unconstrained", icon="📈")
st.sidebar.page_link("pages/2_Pareto_Front.py", label="Pareto Front", icon="📊")
st.sidebar.page_link("pages/3_Genetic_Algorithm.py", label="Genetic Algorithm", icon="🧬")
st.sidebar.page_link("pages/4_Simulated_Annealing.py", label="Simulated Annealing", icon="🌡️")

# ------------------ MAIN TITLE ------------------
st.title("🔍 Optimization Algorithm Visualizer")

# ------------------ INTRO ------------------
st.markdown("""
Welcome! This app helps you **visualize and understand optimization algorithms**
through interactive simulations.

👨‍🎓 Ideal for students, researchers, and anyone exploring optimization techniques.
""")

st.info("💡 Tip: Start with *Unconstrained Minimization* to understand the basics.")

st.markdown("---")

# ------------------ LAYOUT ------------------
col1, col2 = st.columns(2)

# ---------- COLUMN 1 ----------
with col1:

    # ---- Unconstrained Minimization ----
    with st.container():
        st.subheader("📈 1 — Unconstrained Minimization")
        st.markdown("""
Compare three gradient-based methods on any 2D function:

- **Steepest Descent (SD)**
- **Newton's Method**
- **Conjugate Gradient (CG)**

📊 Watch their trajectories on a contour plot and compare convergence speed.
        """)
        st.page_link(
            "pages/1_Unconstrained_Minimization.py",
            label="Open Module",
            icon="📈"
        )

    st.markdown("---")

    # ---- Genetic Algorithm ----
    with st.container():
        st.subheader("🧬 3 — Genetic Algorithm")
        st.markdown("""
Solve the **0/1 Knapsack problem** using a Genetic Algorithm:

- Tune population size, mutation rate, crossover rate
- Observe evolution across generations
- Track diversity and best solution

🎯 Understand exploration vs exploitation in GA.
        """)
        st.page_link(
            "pages/3_Genetic_Algorithm.py",
            label="Open Module",
            icon="🧬"
        )

# ---------- COLUMN 2 ----------
with col2:

    # ---- Pareto Front ----
    with st.container():
        st.subheader("📊 2 — Pareto Front")
        st.markdown("""
Explore **multi-objective optimization** trade-offs:

- Upload your own dataset (CSV)
- Choose any two objectives
- Identify Pareto optimal solutions

⚖️ Visualize trade-offs between conflicting objectives.
        """)
        st.page_link(
            "pages/2_Pareto_Front.py",
            label="Open Module",
            icon="📊"
        )

    st.markdown("---")

    # ---- Simulated Annealing ----
    with st.container():
        st.subheader("🌡️ 4 — Simulated Annealing")
        st.markdown("""
Schedule **10 exams into time slots** using SA:

- Adjust temperature, cooling rate, iterations
- Watch conflict reduction over time
- Compare cooling strategies

🔥 Learn how randomness helps escape local minima.
        """)
        st.page_link(
            "pages/4_Simulated_Annealing.py",
            label="Open Module",
            icon="🌡️"
        )

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("🚀 Built with Streamlit • Optimization Algorithms Visualizer")
