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
# LOAD DATA
# ==================================================

cl31, cl32 = load_ferry()

if cl32.empty:
    st.error("No CL32 files found in data/Ferry")
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
# PAGE CSS
# ==================================================

st.markdown(
    """
    <style>

    .stApp{
        background:#071028;
    }

    .dashboard-card{
        background:#0D1F49;
        border:1px solid #294780;
        border-radius:18px;
        padding:20px;
        min-height:140px;
        color:white;
    }

    .section-card{
        background:#0D1F49;
        border:1px solid #294780;
        border-radius:18px;
        padding:20px;
        margin-top:10px;
        margin-bottom:20px;
        color:white;
    }

    .header-title{
        color:white;
        font-size:34px;
        font-weight:700;
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

    .section-title{
        color:white;
        font-size:20px;
        font-weight:600;
        margin-bottom:15px;
    }

    </style>
    """,
    unsafe_allow_html=True,
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

        <div class="header-sub">
            UU DD&B Framework
        </div>
        """,
        unsafe_allow_html=True
    )

with right:

    st.info(
        f"Current Snapshot\n\n{snapshot.strftime('%B %Y')}"
    )


st.write("")


# ==================================================
# KPI CARDS
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
        unsafe_allow_html=True
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
        unsafe_allow_html=True
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
        unsafe_allow_html=True
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
        unsafe_allow_html=True
    )


# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.markdown(
    """
    <div class="section-card">

        <div class="section-title">
            Executive Summary
        </div>

        Latest CL32 snapshot loaded.

        Dashboard sections below will be populated
        dynamically from Ferry PS programme data.

    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# DELIVERABLES + DISCIPLINES
# ==================================================

left, right = st.columns(2)

with left:

    st.markdown(
        """
        <div class="section-card">

            <div class="section-title">
                Deliverables Status
            </div>

            Chart placeholder

        </div>
        """,
        unsafe_allow_html=True
    )

with right:

    st.markdown(
        """
        <div class="section-card">

            <div class="section-title">
                Discipline Performance
            </div>

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
    <div class="section-card">

        <div class="section-title">
            Upcoming Submissions (Next 7 Days)
        </div>

        Upcoming submissions table placeholder

    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# CHANGES SINCE LAST CL32
# ==================================================

st.markdown(
    """
    <div class="section-card">

        <div class="section-title">
            What's Changed Since Last CL32
        </div>

        Snapshot comparison placeholder

    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# AI INSIGHTS
# ==================================================

st.markdown(
    """
    <div class="section-card">

        <div class="section-title">
            AI Insights & Forecast
        </div>

        Forecasting placeholder

    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# DEBUG
# ==================================================

with st.expander("Debug"):

    st.write("Snapshot:", snapshot)

    st.write("Rows:", len(current_df))

    st.write(current_df.columns.tolist())

    if (
        "Activity ID" in current_df.columns
        and
        "Activity Name" in current_df.columns
    ):
        st.dataframe(
            current_df[
                ["Activity ID", "Activity Name"]
            ].head(20)
        )