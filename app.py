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
# GLOBAL STYLING
# ==================================================

st.markdown("""
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
}

.section-card{
    background:#0D1F49;
    border:1px solid #294780;
    border-radius:18px;
    padding:20px;
    margin-top:10px;
    margin-bottom:20px;
}

.header-title{
    color:white;
    font-size:34px;
    font-weight:700;
}

.header-sub{
    color:#aeb9dd;
    font-size:14px;
}

.metric-number{
    color:white;
    font-size:38px;
    font-weight:700;
}

.metric-label{
    color:#aeb9dd;
    font-size:14px;
}

.section-title{
    color:white;
    font-size:20px;
    font-weight:600;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)


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


st.markdown("<br>", unsafe_allow_html=True)


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

    Latest CL32 snapshot loaded successfully.

    This section will soon contain:

    • Programme Health

    • Deliverables Slipped Since Previous CL32

    • New Critical Activities

    • Upcoming Submissions

    • AI Recommendations

    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# CHART ROW
# ==================================================

c1, c2 = st.columns(2)

with c1:

    st.markdown(
        """
        <div class="section-card">

        <div class="section-title">
            Deliverables Status
        </div>

        Donut chart placeholder

        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        """
        <div class="section-card">

        <div class="section-title">
            Discipline Performance
        </div>

        Donut chart placeholder

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

    Table placeholder

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

    Comparison engine placeholder

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