import streamlit as st
import json
from pathlib import Path


def load_frameworks():

    config_file = Path("config/frameworks.json")

    if config_file.exists():
        with open(config_file, "r") as f:
            return json.load(f)

    return {
        "UU Enterprise Framework": {
            "Pennington Flash": {},
            "Davyhulme ASP4": {}
        },
        "UU DD&B Framework": {
            "Ferry PS": {},
            "Rossall Outfall": {},
            "Flass Lane": {},
            "Tally Ho": {},
            "Eccleston Bridge": {}
        }
    }


def build_sidebar(metrics, snapshot):

    frameworks = load_frameworks()

    with st.sidebar:

        # ==================================================
        # HEADER
        # ==================================================

        st.title("🎯 Design Intelligence Hub")
        st.caption("Design Smarter. Deliver Better.")

        st.divider()

        # ==================================================
        # FRAMEWORKS
        # ==================================================

        st.caption("FRAMEWORKS")

        # Enterprise Card
        with st.container(border=True):

            st.markdown("**UU Enterprise Framework**")

            st.write("Pennington Flash")
            st.write("Davyhulme ASP4")

        # DD&B Card
        with st.container(border=True):

            st.markdown("**UU DD&B Framework**")

            st.success("Ferry PS")

            st.write("Rossall Outfall")
            st.write("Flass Lane")
            st.write("Tally Ho")
            st.write("Eccleston Bridge")

        # ==================================================
        # NAVIGATION
        # ==================================================

        st.caption("NAVIGATION")

        with st.container(border=True):

            st.write("🏠 Executive Dashboard")
            st.write("📋 Deliverables")
            st.write("📊 Discipline Performance")
            st.write("📈 Programme Drift")
            st.write("🎯 Design Readiness")
            st.write("📅 Upcoming Submissions")
            st.write("⚠️ Critical Path & Alerts")
            st.write("🔗 Dependencies")
            st.write("❓ Queries & TQs")
            st.write("🤖 AI Insights")
            st.write("📄 Reports")

        # ==================================================
        # SNAPSHOT HISTORY
        # ==================================================

        st.caption("SNAPSHOT HISTORY")

        with st.container(border=True):

            st.info(
                snapshot.strftime("%B %Y")
            )

        # ==================================================
        # PROJECT HEALTH
        # ==================================================

        st.caption("PROJECT HEALTH")

        with st.container(border=True):

            st.metric(
                "Health Score",
                f"{metrics['health_score']}/100"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Readiness",
                    f"{metrics['design_readiness']}%"
                )

            with col2:

                st.metric(
                    "Critical",
                    metrics["critical_deliverables"]
                )

            st.metric(
                "High Risk Activities",
                metrics["high_risk"]
            )

            st.metric(
                "Upcoming Submissions",
                metrics["upcoming_submissions"]
            )

        # ==================================================
        # PROJECT BASELINE
        # ==================================================

        st.caption("PROJECT BASELINE")

        with st.container(border=True):

            st.metric(
                "Baseline Finish",
                metrics["baseline_finish"].strftime(
                    "%d %b %Y"
                )
            )

            st.metric(
                "Current Forecast",
                metrics["forecast_finish"].strftime(
                    "%d %b %Y"
                )
            )

            st.metric(
                "Programme Drift",
                f"{metrics['programme_drift']} Days"
            )