import streamlit as st
import json
from pathlib import Path


def load_frameworks():

    config_file = Path("config/frameworks.json")

    if config_file.exists():

        with open(config_file, "r") as f:
            return json.load(f)

    return {}


def build_sidebar(metrics, snapshot):

    frameworks = load_frameworks()

    # ===================================================
    # TITLE
    # ===================================================

    st.sidebar.title("🎯 Design Intelligence Hub")

    st.sidebar.caption(
        "Design Smarter. Deliver Better."
    )

    st.sidebar.divider()

    # ===================================================
    # FRAMEWORKS
    # ===================================================

    st.sidebar.subheader("Frameworks")

    for framework, projects in frameworks.items():

        with st.sidebar.expander(
            framework,
            expanded=True
        ):

            for project in projects.keys():

                if project == "Ferry PS":
                    st.success(project)
                else:
                    st.write(project)

    st.sidebar.divider()

    # ===================================================
    # NAVIGATION
    # ===================================================

    st.sidebar.subheader("Navigation")

    pages = [
        "🏠 Executive Dashboard",
        "📋 Deliverables",
        "📊 Discipline Performance",
        "📈 Programme Drift",
        "🎯 Design Readiness",
        "📅 Upcoming Submissions",
        "⚠️ Critical Path & Alerts",
        "🔗 Design Dependencies",
        "❓ Queries & TQs",
        "🤖 AI Insights & Forecast",
        "📄 Reports"
    ]

    st.sidebar.radio(
        "Select Page",
        pages,
        label_visibility="collapsed"
    )

    st.sidebar.divider()

    # ===================================================
    # SNAPSHOTS
    # ===================================================

    st.sidebar.subheader(
        "Snapshot History"
    )

    st.sidebar.info(
        snapshot.strftime("%B %Y")
    )

    st.sidebar.divider()

    # ===================================================
    # HEALTH
    # ===================================================

    st.sidebar.subheader(
        "Project Health"
    )

    st.sidebar.metric(
        "Health Score",
        f"{metrics['health_score']}/100"
    )

    st.sidebar.metric(
        "Design Readiness",
        f"{metrics['design_readiness']}%"
    )

    st.sidebar.metric(
        "Critical Activities",
        metrics["critical_deliverables"]
    )

    st.sidebar.metric(
        "High Risk Activities",
        metrics["high_risk"]
    )

    if metrics["upcoming_submissions"] == 0:

        st.sidebar.info(
            "No submissions due in next 7 days"
        )

    else:

        st.sidebar.metric(
            "Upcoming Submissions",
            metrics["upcoming_submissions"]
        )

    st.sidebar.divider()

    # ===================================================
    # BASELINE
    # ===================================================

    st.sidebar.subheader(
        "Project Baseline"
    )

    st.sidebar.metric(
        "Baseline Finish",
        metrics["baseline_finish"].strftime(
            "%d %b %Y"
        )
    )

    st.sidebar.metric(
        "Current Forecast",
        metrics["forecast_finish"].strftime(
            "%d %b %Y"
        )
    )

    st.sidebar.metric(
        "Programme Drift",
        f"{metrics['programme_drift']} Days"
    )