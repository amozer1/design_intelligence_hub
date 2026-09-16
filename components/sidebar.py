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

    st.markdown(
        """
        <style>

        section[data-testid="stSidebar"]{
            background: linear-gradient(
                180deg,
                #081428 0%,
                #0A1530 100%
            );
        }

        section[data-testid="stSidebar"] *{
            color:white;
        }

        .sidebar-title{
            font-size:22px;
            font-weight:700;
            margin-bottom:4px;
        }

        .sidebar-subtitle{
            color:#9ca9d7;
            font-size:12px;
            margin-bottom:20px;
        }

        .section-header{
            margin-top:18px;
            margin-bottom:10px;
            font-size:12px;
            letter-spacing:1px;
            color:#9ca9d7;
            text-transform:uppercase;
            font-weight:600;
        }

        .framework-card{
            background:#101b3d;
            border:1px solid #263c7a;
            border-radius:12px;
            padding:10px;
            margin-bottom:10px;
        }

        .project-active{
            background:#d8efe4;
            color:#0c3321 !important;
            padding:8px;
            border-radius:8px;
            font-weight:600;
            margin:4px 0;
        }

        .project-normal{
            color:#dbe5ff;
            padding:6px 8px;
        }

        .health-card{
            background:#101b3d;
            border:1px solid #263c7a;
            border-radius:16px;
            padding:16px;
            margin-top:10px;
        }

        .health-score{
            text-align:center;
            margin-bottom:15px;
        }

        .health-number{
            font-size:34px;
            font-weight:700;
            color:white;
        }

        .metric-line{
            display:flex;
            justify-content:space-between;
            margin-top:10px;
            margin-bottom:10px;
        }

        .green{
            color:#00D26A;
            font-weight:600;
        }

        .amber{
            color:#FFB100;
            font-weight:600;
        }

        .red{
            color:#FF5F73;
            font-weight:600;
        }

        .snapshot-pill{
            background:#d9e9ff;
            color:#0d2348 !important;
            padding:10px;
            border-radius:10px;
            font-weight:600;
            text-align:center;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:

        st.markdown(
            """
            <div class="sidebar-title">
            🎯 Design Intelligence Hub
            </div>

            <div class="sidebar-subtitle">
            Design Smarter. Deliver Better.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        # ==================================================
        # FRAMEWORKS
        # ==================================================

        st.markdown(
            '<div class="section-header">Frameworks</div>',
            unsafe_allow_html=True
        )

        for framework, projects in frameworks.items():

            st.markdown(
                f"""
                <div class="framework-card">
                    <strong>{framework}</strong>
                """,
                unsafe_allow_html=True
            )

            for project in projects.keys():

                if project == "Ferry PS":

                    st.markdown(
                        f"""
                        <div class="project-active">
                        {project}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                else:

                    st.markdown(
                        f"""
                        <div class="project-normal">
                        {project}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

        st.divider()

        # ==================================================
        # NAVIGATION
        # ==================================================

        st.markdown(
            '<div class="section-header">Navigation</div>',
            unsafe_allow_html=True
        )

        st.radio(
            "",
            [
                "Executive Dashboard",
                "Deliverables",
                "Discipline Performance",
                "Programme Drift",
                "Design Readiness",
                "Upcoming Submissions",
                "Critical Path & Alerts",
                "Dependencies",
                "Queries & TQs",
                "AI Insights",
                "Reports",
            ],
            label_visibility="collapsed",
        )

        st.divider()

        # ==================================================
        # SNAPSHOT HISTORY
        # ==================================================

        st.markdown(
            '<div class="section-header">Snapshot History</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="snapshot-pill">
            {snapshot.strftime("%B %Y")}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # ==================================================
        # PROJECT HEALTH
        # ==================================================

        st.markdown(
            '<div class="section-header">Project Health</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="health-card">

                <div class="health-score">
                    <div class="health-number">
                        {metrics['health_score']}/100
                    </div>
                </div>

                <div class="metric-line">
                    <span>Design Readiness</span>
                    <span class="green">
                        {metrics['design_readiness']}%
                    </span>
                </div>

                <div class="metric-line">
                    <span>Critical Activities</span>
                    <span class="amber">
                        {metrics['critical_deliverables']}
                    </span>
                </div>

                <div class="metric-line">
                    <span>High Risk Activities</span>
                    <span class="red">
                        {metrics['high_risk']}
                    </span>
                </div>

                <div class="metric-line">
                    <span>Upcoming Submissions</span>
                    <span class="amber">
                        {metrics['upcoming_submissions']}
                    </span>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        