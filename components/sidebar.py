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

    st.markdown("""
    <style>

    [data-testid="stSidebar"]{
        background:linear-gradient(
            180deg,
            #04112B 0%,
            #031837 100%
        );
    }

    [data-testid="stSidebar"] *{
        color:white;
    }

    .sidebar-section-title{
        color:#93A2D2;
        font-size:11px;
        font-weight:700;
        letter-spacing:1px;
        text-transform:uppercase;
        margin-bottom:12px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]{
        border:1px solid #24468A !important;
        border-radius:14px !important;
        background:#0A1C48 !important;
        padding:0.7rem !important;
        margin-bottom:12px !important;
    }

    div[data-testid="metric-container"]{
        background:#10224D;
        border:none;
        padding:8px;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:

        # =======================================
        # HEADER
        # =======================================

        st.markdown("### 🎯 Design Intelligence Hub")
        st.caption("Design Smarter. Deliver Better.")

        st.write("")

        # =======================================
        # FRAMEWORKS
        # =======================================

        st.markdown(
            '<div class="sidebar-section-title">Frameworks</div>',
            unsafe_allow_html=True
        )

        for framework, projects in frameworks.items():

            with st.container(border=True):

                st.markdown(
                    f"**{framework}**"
                )

                st.write("")

                for project in projects.keys():

                    if project == "Ferry PS":

                        st.success(project)

                    else:

                        st.write(project)

        # =======================================
        # NAVIGATION
        # =======================================

        st.markdown(
            '<div class="sidebar-section-title">Navigation</div>',
            unsafe_allow_html=True
        )

        with st.container(border=True):

            pages = [
                "🏠 Executive Dashboard",
                "📋 Deliverables",
                "📊 Discipline Performance",
                "📈 Programme Drift",
                "🎯 Design Readiness",
                "📅 Upcoming Submissions",
                "⚠️ Critical Path & Alerts",
                "🔗 Dependencies",
                "❓ Queries & TQs",
                "🤖 AI Insights",
                "📄 Reports"
            ]

            for page in pages:
                st.write(page)

        # =======================================
        # SNAPSHOTS
        # =======================================

        st.markdown(
            '<div class="sidebar-section-title">Snapshot History</div>',
            unsafe_allow_html=True
        )

        with st.container(border=True):

            st.info(
                snapshot.strftime("%B %Y")
            )

        # =======================================
        # PROJECT HEALTH
        # =======================================

        st.markdown(
            '<div class="sidebar-section-title">Project Health</div>',
            unsafe_allow_html=True
        )

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

        # =======================================
        # PROJECT BASELINE
        # =======================================

        st.markdown(
            '<div class="sidebar-section-title">Project Baseline</div>',
            unsafe_allow_html=True
        )

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