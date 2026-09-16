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


def sidebar_heading(text):

    st.markdown(
        f"""
        <div style="
            color:#93A2D2;
            font-size:11px;
            font-weight:700;
            letter-spacing:1px;
            text-transform:uppercase;
            margin-top:8px;
            margin-bottom:8px;
        ">
        {text}
        </div>
        """,
        unsafe_allow_html=True
    )


def build_sidebar(metrics, snapshot):

    frameworks = load_frameworks()

    with st.sidebar:

        st.markdown(
            """
            <div style="
                color:white;
                font-size:20px;
                font-weight:700;
                margin-bottom:2px;
            ">
            🎯 Design Intelligence Hub
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption("Design Smarter. Deliver Better.")

        st.divider()

        # ==================================================
        # FRAMEWORKS
        # ==================================================

        sidebar_heading("Frameworks")

        # ---------- Enterprise Card ----------

        with st.container(border=True):

            st.markdown(
                "**UU Enterprise Framework**"
            )

            st.write("Pennington Flash")
            st.write("Davyhulme ASP4")

        # ---------- DD&B Card ----------

        with st.container(border=True):

            st.markdown(
                "**UU DD&B Framework**"
            )

            st.success("Ferry PS")

            st.write("Rossall Outfall")
            st.write("Flass Lane")
            st.write("Tally Ho")
            st.write("Eccleston Bridge")

        # ==================================================
        # NAVIGATION
        # ==================================================

        sidebar_heading("Navigation")

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

        sidebar_heading("Snapshot History")

        with st.container(border=True):

            st.info(
                snapshot.strftime("%B %Y")
            )

        # ==================================================
        # PROJECT HEALTH
        # ==================================================

        sidebar_heading("Project Health")

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

        sidebar_heading("Project Baseline")

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