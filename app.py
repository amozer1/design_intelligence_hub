import streamlit as st

from sidebar.layout import render_sidebar
from sidebar.branding import render_branding
from sidebar.frameworks import render_frameworks
from sidebar.navigation import render_navigation
from sidebar.health import render_health


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Design Intelligence Hub",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# SIDEBAR STYLING
# ==================================================

render_sidebar()

# ==================================================
# SESSION STATE DEFAULTS
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "Executive Dashboard"

if "project" not in st.session_state:
    st.session_state.project = "Ferry PS"

# ==================================================
# PROJECT METRICS
# ==================================================
# Replace with real data later

metrics = {
    "health_score": 58,
    "design_readiness": 78,
    "critical_deliverables": 18,
    "high_risk": 5,
    "upcoming_submissions": 5
}

# ==================================================
# SIDEBAR CONTENT
# ==================================================

with st.sidebar:

    render_branding()

    st.divider()

    render_frameworks()

    st.divider()

    render_navigation()

    st.divider()

    render_health(metrics)

# ==================================================
# PAGE ROUTING
# ==================================================

page = st.session_state.page

if page == "Executive Dashboard":

    st.title("Executive Dashboard")

elif page == "Deliverables":

    st.title("Deliverables")

elif page == "Discipline Performance":

    st.title("Discipline Performance")

elif page == "Programme Drift":

    st.title("Programme Drift")

elif page == "Design Readiness":

    st.title("Design Readiness")

elif page == "Upcoming Submissions":

    st.title("Upcoming Submissions")

elif page == "Critical Path & Alerts":

    st.title("Critical Path & Alerts")

elif page == "Design Dependencies"