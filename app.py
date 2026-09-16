import streamlit as st

from loaders.ferry_loader import load_ferry
from utils.project_metrics import (
    get_current_snapshot,
    get_project_metrics
)
from components.sidebar import build_sidebar


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
# LOAD CSS
# ==================================================

with open("assets/styles.css") as f:

    st.markdown(
        f"""
        <style>
        {f.read()}
        </style>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# LOAD DATA
# ==================================================

cl31, cl32 = load_ferry()

if cl32.empty:

    st.error("No CL32 files found.")

    st.stop()

current_df, snapshot = get_current_snapshot(cl32)

metrics = get_project_metrics(current_df)


# ==================================================
# SIDEBAR
# ==================================================

build_sidebar(
    metrics=metrics,
    snapshot=snapshot
)


# ==================================================
# HEADER
# ==================================================

left, right = st.columns([5, 1])

with left:

    st.markdown(
        """
        <div class="header-title">
            Ferry PS
        </div>

        <div class="header-subtitle">
            UU DD&B Framework
        </div>
        """,
        unsafe_allow_html=True
    )

with right:

    st.info(
        snapshot.strftime("%B %Y")
    )


st.write("")


# ==================================================
# KPI ROW
# ==================================================

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-value">
                {metrics["health_score"]}
            </div>

            <div class="kpi-label">
                Health Score
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k2:

    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-value">
                {metrics["critical_deliverables"]}
            </div>

            <div class="kpi-label">
                Critical Activities
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k3:

    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-value">
                {metrics["high_risk"]}
            </div>

            <div class="kpi-label">
                High Risk Activities
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k4:

    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-value">
                {metrics["programme_drift"]}
            </div>

            <div class="kpi-label">
                Programme Drift (Days)
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.markdown(
    """
    <div class="page-card">

        <h3>Executive Summary</h3>

        Latest Ferry PS CL32 snapshot loaded successfully.

    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# ROW 2
# ==================================================

c1, c2 = st.columns(2)

with c1:

    st.markdown(
        """
        <div class="page-card">

            <h3>Deliverables Status</h3>

            Chart placeholder

        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        """
        <div class="page-card">

            <h3>Discipline Performance</h3>

            Chart placeholder

        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# UPCOMING SUBMISSIONS
# ==================================================

st.markdown(
    """
    <div class="page-card">

        <h3>Upcoming Submissions</h3>

        Table placeholder

    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# CHANGES SINCE LAST SNAPSHOT
# ==================================================

st.markdown(
    """
    <div class="page-card">

        <h3>What's Changed Since Last Snapshot</h3>

        Comparison placeholder

    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# AI INSIGHTS
# ==================================================

st.markdown(
    """
    <div class="page-card">

        <h3>AI Insights & Forecast</h3>

        Forecasting placeholder

    </div>
    """,
    unsafe_allow_html=True
)