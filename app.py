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

    /* ==========================================
       APP
    ========================================== */

    .stApp{
        background:#071028;
    }

    .block-container{
        padding-top:1rem;
        padding-left:2rem;
        padding-right:2rem;
        max-width:1800px;
    }

    /* ==========================================
       SIDEBAR
    ========================================== */

    section[data-testid="stSidebar"]{

        background:
        linear-gradient(
            180deg,
            #050D22 0%,
            #06122D 40%,
            #081938 100%
        ) !important;
    }

    section[data-testid="stSidebar"] *{
        color:white !important;
    }

    /* ==========================================
       SIDEBAR CARDS
    ========================================== */

    div[data-testid="stVerticalBlockBorderWrapper"]{

        background:#081A42 !important;

        border:1px solid #12346E !important;

        border-radius:14px !important;

        padding:22px !important;

        margin-bottom:20px !important;

        box-shadow:
        0 0 12px rgba(42,88,255,.15);
    }

    /* ==========================================
       FERRY PS HIGHLIGHT
    ========================================== */

    div[data-testid="stAlert"]{

        background:
        linear-gradient(
            90deg,
            #5D16FF,
            #7C29F6
        ) !important;

        border:none !important;

        border-radius:10px !important;
    }

    div[data-testid="stAlert"] *{

        color:white !important;

        font-weight:600 !important;
    }

    /* ==========================================
       SNAPSHOT BOX
    ========================================== */

    div[data-testid="stInfo"]{

        background:#17254B !important;

        border:1px solid #294780 !important;

        border-radius:10px !important;
    }

    div[data-testid="stInfo"] *{

        color:white !important;
    }

    /* ==========================================
       METRICS
    ========================================== */

    div[data-testid="metric-container"]{

        background:transparent !important;

        border:none !important;

        box-shadow:none !important;
    }

    div[data-testid="metric-container"] label{

        color:#B6C0E0 !important;
    }

    div[data-testid="stMetricValue"]{

        color:white !important;

        font-weight:700 !important;
    }

    /* ==========================================
       PAGE CARDS
    ========================================== */

    .page-card{

        background:#081A42;

        border:1px solid #12346E;

        border-radius:14px;

        padding:20px;

        color:white;

        min-height:180px;
    }

    /* ==========================================
       HEADER
    ========================================== */

    .header-title{

        color:white;

        font-size:36px;

        font-weight:700;
    }

    .header-subtitle{

        color:#B6C0E0;

        font-size:14px;
    }

    /* ==========================================
       KPI
    ========================================== */

    .kpi{

        background:#081A42;

        border:1px solid #12346E;

        border-radius:14px;

        padding:20px;
    }

    .kpi-value{

        color:white;

        font-size:34px;

        font-weight:700;
    }

    .kpi-label{

        color:#B6C0E0;

        font-size:13px;
    }

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

# ==================================================
# KPI ROW
# ==================================================

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-value">
                {metrics['health_score']}
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
                {metrics['critical_deliverables']}
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
                {metrics['high_risk']}
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
                {metrics['programme_drift']}
            </div>
            <div class="kpi-label">
                Programme Drift (Days)
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.markdown(
    """
    <div class="page-card">

    <h3>Executive Summary</h3>

    Latest Ferry PS 