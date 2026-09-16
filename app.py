import streamlit as st

from sidebar.layout import render_sidebar
from sidebar.branding import render_branding
from sidebar.frameworks import render_frameworks
from sidebar.navigation import render_navigation


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
# SIDEBAR CONTENT
# ==================================================

with st.sidebar:

    render_branding()

    render_frameworks()

    render_navigation()

# ==================================================
# DEFAULT PAGE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "Executive Dashboard"


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

elif page == "Design Dependencies":

    st.title("Design Dependencies")

elif page == "Queries & TQs":

    st.title("Queries & TQs")

elif page == "AI Insights & Forecast":

    st.title("AI Insights & Forecast")

elif page == "Reports":

    st.title("Reports")

elif page == "Data Explorer":

    st.title("Data Explorer")

elif page == "Settings":

    st.title("Settings")