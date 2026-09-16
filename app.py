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
# GLOBAL STYLING
# ==================================================

st.markdown(
    """
    <style>

    .stApp{
        background:
        linear-gradient(
            180deg,
            #050b1f 0%,
            #071028 100%
        );
    }

    .block-container{
        padding-top:1rem;
        padding-left:2rem;
        padding-right:2rem;
        max-width:1800px;
    }

    .dashboard-card{
        background:#0D1F49;
        border:1px solid #294780;
        border-radius:16px;
        padding:20px;
        color:white;
        min-height:180px;
    }

    .section-card{
        background:#0D1F49;
        border:1px solid #294780;
        border-radius:16px;
        padding:18px;
        margin-bottom:20px;
        color:white;
    }

    .header-title{
        color:white;
        font-size:36px;
        font-weight:700;
        margin-bottom:0;
    }

    .header-sub{
        color:#A9B5D9;
        font-size:14px;
    }

    .metric-number{
        color:white;
        font-size:36px;
        font-weight:700;
    }

    .metric-label{
        color:#A9B5D9;
        font-size:14px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# LOAD DATA
# ==================================================

cl31, cl32 = load_ferry()

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
        f"""
        <div class="header-title">
        Ferry PS
        </div>

        <div class="header-sub">
        UU DD&B Framework
        </div>
        """,
        unsafe_allow_html=True
    )

with right:

    st.info(
        f"""
Current Snapshot

{snapshot.strftime("%B %Y")}
"""
    )


# ==================================================
# KPI ROW
# ==================================================

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.markdown(
        f"""
        <div class="dashboard-card">
            <div class="metric-number">
                {metrics["health_score"]}
            </div>

            <div class="metric-label">
                Health Score
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k2:

    st.markdown(
        f"""
        <div class="dashboard-card">
            <div class="metric-number">
                {metrics["critical_deliverables"]}
            </div>

            <div class="metric-label">
                Critical Deliverables
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k3:

    st.markdown(
        f"""
        <div class="dashboard-card">
            <div class="metric-number">
                {metrics["high_risk"]}
            </div>

            <div class="metric-label">
                High Risk Activities
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k4:

    st.markdown(
        f"""
        <div class="dashboard-card">
            <div class="metric-number">
                {metrics["programme_drift"]}
            </div>

            <div class="metric-label">
                Programme Drift (Days)
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.write("")


# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.markdown(
    """
    <div class="section-card">

    <h3>Executive Summary</h3>

    Latest CL32 snapshot currently loaded.

    This section will contain:

    • Programme Health

    • New Critical Activities

    • Deliverables Slipped Since Previous