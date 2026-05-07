import streamlit as st
from database import run_query
from query_engine import generate_sql

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Analytics Q&A Agent",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* =========================================
HIDE STREAMLIT DEFAULTS
========================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* =========================================
APP BACKGROUND
========================================= */

.stApp {
    background: linear-gradient(135deg, #F8FAFC, #E2E8F0);
    color: #111827;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #F8FAFC, #E2E8F0);
}

[data-testid="stHeader"] {
    background: transparent;
}

/* =========================================
MAIN CONTAINER
========================================= */

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* =========================================
TEXT COLORS
========================================= */

h1, h2, h3, h4, h5, h6, p, label, div {
    color: #111827 !important;
}

/* =========================================
HEADER
========================================= */

.main-title {
    font-size: 3rem;
    font-weight: 700;
    text-align: center;
    color: #111827 !important;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #475569 !important;
    margin-bottom: 2rem;
}

/* =========================================
CARDS
========================================= */

.card {
    background: rgba(255,255,255,0.85);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

/* =========================================
METRIC CARDS
========================================= */

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid #E2E8F0;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    transition: 0.3s;
}

.metric-card:hover {
    transform: translateY(-4px);
}

/* =========================================
BUTTONS
========================================= */

.stButton > button {
    width: 100%;
    height: 3.2em;
    border-radius: 12px;
    border: none;
    background: linear-gradient(90deg, #3B82F6, #2563EB);
    color: white !important;
    font-size: 16px;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #2563EB, #1D4ED8);
    color: white !important;
}

/* =========================================
INPUT BOX
========================================= */

.stTextInput input {
    background-color: white !important;
    color: black !important;
    border-radius: 12px !important;
    border: 1px solid #CBD5E1 !important;
}

/* =========================================
SIDEBAR
========================================= */

section[data-testid="stSidebar"] {
    background-color: #F1F5F9;
}

section[data-testid="stSidebar"] * {
    color: #111827 !important;
}

/* =========================================
DATAFRAME
========================================= */

[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 10px;
}

/* =========================================
CODE BLOCKS
========================================= */

pre {
    background-color: #F8FAFC !important;
    color: black !important;
    border-radius: 10px;
}

/* =========================================
SUCCESS/WARNING/ERROR
========================================= */

.stAlert {
    border-radius: 12px;
}

/* =========================================
REMOVE EXTRA DARK AREAS
========================================= */

[data-testid="stToolbar"] {
    visibility: hidden;
}

/* =========================================
SMOOTH ANIMATIONS
========================================= */

.card, .metric-card {
    animation: fadeInUp 0.5s ease-in-out;
}

@keyframes fadeInUp {
    from {
        transform: translateY(10px);
        opacity: 0;
    }
    to {
        transform: translateY(0px);
        opacity: 1;
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="main-title">
📊 Analytics Q&A Agent
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Ask analytics questions in natural language and get real-time insights from your database.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# METRICS SECTION
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h2>50K+</h2>
        <p>Sessions Analyzed</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h2>5K+</h2>
        <p>Users</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h2>100%</h2>
        <p>Local & API-Free</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("⚙️ About")

    st.info("""
This AI-assisted analytics tool converts natural-language questions into SQL queries and executes them on a SQLite database.

### Supported Queries
- DAU / MAU
- Revenue
- Retention
- US Users
- Weekly Comparisons

### Stack
- Python
- Streamlit
- SQLite
- Pandas
""")

    st.markdown("---")

    st.subheader("🧪 Example Questions")

    st.code("""
What was our DAU?
Show MAU
Revenue
US users only
This week vs last week
""")

# ==========================================
# QUERY CARD
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("💬 Ask Your Analytics Question")

question = st.text_input(
    "",
    placeholder="e.g. What was our DAU last week?"
)

run = st.button("🚀 Run Query")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# QUERY EXECUTION
# ==========================================

if run:

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        sql = generate_sql(question)

        # Ambiguous
        if sql is None:

            st.error("""
Ambiguous question detected.

Try asking about:
- DAU
- MAU
- Revenue
- Retention
- Weekly comparison
""")

        else:

            # SQL Card
            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.subheader("🧠 Generated SQL")

            st.code(sql, language="sql")

            st.markdown('</div>', unsafe_allow_html=True)

            # Run Query
            df = run_query(sql)

            # Results Card
            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.subheader("📈 Query Result")

            st.dataframe(df, use_container_width=True)

            st.markdown('</div>', unsafe_allow_html=True)

            # Chart
            if len(df.columns) >= 2:

                st.markdown('<div class="card">', unsafe_allow_html=True)

                st.subheader("📊 Visualization")

                st.line_chart(df.set_index(df.columns[0]))

                st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; color:#64748B;'>
Built using Streamlit • SQLite • Python • Natural Language SQL Mapping
</div>
""", unsafe_allow_html=True)