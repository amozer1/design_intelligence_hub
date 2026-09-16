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

    st.sidebar.markdown(
        """
        <style>

        [data-testid="stSidebar"] {
            background:
            linear-gradient(
                180deg,
                #081428 0%,
                #091735 50%,
                #07121f 100%
            );
        }

        .hub-title{
            color:white;
            font-size:26px;
            font-weight:700;
            line-height:1.1;
        }

        .hub-sub{
            color:#9aa6cc;
            font-size:12px;
            margin-bottom:20px;
        }

        .section-title{
            color:#A9B5D9;
            font-size:11px;
            letter-spacing:1px;
            text-transform:uppercase;
            font-weight:600;
            margin-top:20px;
            margin-bottom:10px;
        }

        .framework-title{
            color:white;
            font-size:14px;
            font-weight:600;
            margin-top:12px;
            margin-bottom:8px;
        }

        .project{
            padding:10px;
            color:#dfe6ff;
            border-radius:10px;
            margin-bottom:4px;
        }

        .project:hover{
            background:#13264A;
        }

        .active-project{
            background:#7427F5;
            color:white;
            font-weight:600;
        }

        .nav-item{
            padding:10px;
            border-radius:10px;
            color:white;
            margin-bottom:4px;
        }

        .nav-item:hover{
            background:#13264A;
        }

        .active-nav{
            background:#7427F5;
            color:white;
            font-weight:600;
        }

        .snapshot-row{
            display:flex;
            justify-content:space-between;
            color:white;
            font-size:13px;
            margin-bottom:8px;
        }

        .badge{
            background:#162750;
            border-radius:6px;
            padding:2px 8px;
        }

        .metric-card{

            background:#0D1F49;

            border:1px solid #294780;

            border-radius:16px;

            padding:18px;

            margin-top:10px;

            margin-bottom:20px;

            box-shadow:
            0 0 15px rgba(70,100,255,.12);
        }

        .metric-row{

            display:flex;

            justify-content:space-between;

            margin-bottom:16px;

            color:white;

            font-size:14px;
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
            color:#FF4F6F;
            font-weight:600;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------------------------
    # TITLE
    # ------------------------------------------------

    st.sidebar.markdown(
        """
        <div class="hub-title">
        DESIGN<br>
        INTELLIGENCE HUB
        </div>

        <div class="hub-sub">
        Design Smarter. Deliver Better.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------------------------
    # FRAMEWORKS
    # ------------------------------------------------

    st.sidebar.markdown(
        """
        <div class="section-title">
        Frameworks
        </div>
        """,
        unsafe_allow_html=True
    )

    for framework, projects in frameworks.items():

        st.sidebar.markdown(
            f"""
            <div class="framework-title">
            ▼ {framework}
            </div>
            """,
            unsafe_allow_html=True
        )

        for project in projects.keys():

            css_class = (
                "project active-project"
                if project == "Ferry PS"
                else "project"
            )

            st.sidebar.markdown(
                f"""
                <div class="{css_class}">
                {project}
                </div>
                """,
                unsafe_allow_html=True
            )

    # ------------------------------------------------
    # NAVIGATION
    # ------------------------------------------------

    st.sidebar.markdown(
        """
        <div class="section-title">
        Main Navigation
        </div>
        """,
        unsafe_allow_html=True
    )

    navigation = [
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
        "📄 Reports",
        "🔍 Data Explorer",
        "⚙️ Settings"
    ]

    for i, nav in enumerate(navigation):

        nav_class = (
            "nav-item active-nav"
            if i == 0
            else "nav-item"
        )

        st.sidebar.markdown(
            f"""
            <div class="{nav_class}">
            {nav}
            </div>
            """,
            unsafe_allow_html=True
        )

    # ------------------------------------------------
    # SNAPSHOT HISTORY
    # ------------------------------------------------

    st.sidebar.markdown(
        """
        <div class="section-title">
        Snapshot History
        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        f"""
        <div class="snapshot-row">
            <span>{snapshot.strftime('%B %Y')}</span>
            <span class="badge">Current</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------------------------
    # PROJECT HEALTH
    # ------------------------------------------------

    st.sidebar.markdown(
        """
        <div class="section-title">
        Project Health
        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-row">
                <span>Design Readiness</span>
                <span class="green">
                {metrics['design_readiness']}%
                </span>
            </div>

            <div class="metric-row">
                <span>Critical Deliverables</span>
                <span class="amber">
                {metrics['critical_deliverables']}
                </span>
            </div>

            <div class="metric-row">
                <span>High Risk Activities</span>
                <span class="red">
                {metrics['high_risk']}
                </span>
            </div>

            <div class="metric-row">
                <span>Upcoming Submissions</span>
                <span class="amber">
                {metrics['upcoming_submissions']}
                </span>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------------------------
    # PROJECT BASELINE
    # ------------------------------------------------

    st.sidebar.markdown(
        """
        <div class="section-title">
        Project Baseline (BL1)
        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-row">
                <span>Baseline Finish</span>
                <span>
                {metrics['baseline_finish'].strftime('%d %b %Y')}
                </span>
            </div>

            <div class="metric-row">
                <span>Current Forecast</span>
                <span>
                {metrics['forecast_finish'].strftime('%d %b %Y')}
                </span>
            </div>

            <div class="metric-row">
                <span>Programme Drift</span>
                <span class="red">
                +{metrics['programme_drift']} Days
                </span>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )