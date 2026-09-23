import streamlit as st

from sidebar.layout import render_sidebar
from sidebar.branding import render_branding
from sidebar.frameworks import render_frameworks
from sidebar.navigation import render_navigation
from sidebar.health import (
    calculate_health_metrics,
    render_health
)

from components.homepage import render_homepage

from loaders.ferry_loader import load_ferry

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
# LOAD DATA
# ==================================================

cl31, cl32 = load_ferry()

metrics = calculate_health_metrics(cl32)

# ==================================================
# SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "Executive Dashboard"

if "project" not in st.session_state:
    st.session_state.project = "Ferry PS"

# ==================================================
# SIDEBAR STYLING
# ==================================================

render_sidebar()

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    render_branding()

    render_frameworks()

    render_navigation()

    render_health(metrics)

# ==================================================
# SNAPSHOT
# ==================================================

latest_snapshot = "No Snapshot"

if not cl32.empty:

    latest_snapshot = (
        cl32
        .sort_values("SnapshotDate")
        ["Snapshot"]
        .iloc[-1]
    )

# ==================================================
# PAGE ROUTING
# ==================================================

page = st.session_state.page

if page == "Executive Dashboard":

    render_homepage(
        project=st.session_state.project,
        snapshot=latest_snapshot,
        metrics=metrics,
        cl31=cl31,
        cl32=cl32
    )

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