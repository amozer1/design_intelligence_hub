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

    st.title("Ferry PS")

    st.caption("UU DD&B Framework")

with right:

    st.info(
        snapshot.strftime("%B %Y")
    )


st.divider()


# ==================================================
# KPI ROW
# ==================================================

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Health Score",
        metrics["health_score"]
    )

with k2:

    st.metric(
        "Critical Activities",
        metrics["critical_deliverables"]
    )

with k3:

    st.metric(
        "High Risk Activities",
        metrics["high_risk"]
    )

with k4:

    st.metric(
        "Programme Drift",
        f"{metrics['programme_drift']} Days"
    )


st.write("")


# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

with st.container(border=True):

    st.subheader("Executive Summary")

    st.write(
        "Latest Ferry PS CL32 snapshot loaded successfully."
    )


st.write("")


# ==================================================
# ROW 2
# ==================================================

c1, c2 = st.columns(2)

with c1:

    with st.container(border=True):

        st.subheader("Deliverables Status")

        st.write("Chart placeholder")

with c2:

    with st.container(border=True):

        st.subheader("Discipline Performance")

        st.write("Chart placeholder")


st.write("")


# ==================================================
# UPCOMING SUBMISSIONS
# ==================================================

with st.container(border=True):

    st.subheader("Upcoming Submissions")

    st.write("Table placeholder")


st.write("")


# ==================================================
# CHANGES SINCE LAST SNAPSHOT
# ==================================================

with st.container(border=True):

    st.subheader("What's Changed Since Last Snapshot")

    st.write("Comparison placeholder")


st.write("")


# ==================================================
# AI INSIGHTS
# ==================================================

with st.container(border=True):

    st.subheader("AI Insights & Forecast")

    st.write("Forecasting placeholder")