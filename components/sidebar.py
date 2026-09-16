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


def section_title(text):

    st.markdown(
        f"""
        <div style="
            color:#91A5E5;
            font-size:11px;
            font-weight:700;
            letter-spacing:1px;
            text-transform:uppercase;
            margin-top:14px;
            margin-bottom:8px;
        ">
        {text}
        </div>
        """,
        unsafe_allow_html=True
    )


def card_begin():
    return """
    <div style="
        background:#0A1C48;
        border:1px solid #284A8A;
        border-radius:14px;
        padding:14px;
        margin-bottom:12px;
    ">
    """


def card_end():
    return "</div>"


def build_sidebar(metrics, snapshot):

    frameworks = load_frameworks()

    with st.sidebar:

        # =================================================
        # HEADER
        # =================================================

        st.markdown(
            """
            <div style="
                color:white;
                font-size:22px;
                font-weight:700;
            ">
            🎯 Design Intelligence Hub
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                color:#9BAAD8;
                font-size:11px;
                margin-bottom:10px;
            ">
            Design Smarter. Deliver Better.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # =================================================
        # FRAMEWORKS
        # =================================================

        section_title("Frameworks")

        for framework, projects in frameworks.items():

            html = card_begin()

            html += f"""
            <div style="
                color:white;
                font-weight:700;
                margin-bottom:12px;
            ">
                {framework}
            </div>
            """

            for project in projects.keys():

                if project == "Ferry PS":

                    html += f"""
                    <div style="
                        background:#D9E8E0;
                        color:#113425;
                        padding:10px;
                        border-radius:8px;
                        margin-bottom:6px;
                        font-weight:600;
                    ">
                    {project}
                    </div>
                    """

                else:

                    html += f"""
                    <div style="
                        color:white;
                        padding:8px 4px;
                    ">
                    {project}
                    </div>
                    """

            html += card_end()

            st.markdown(
                html,
                unsafe_allow_html=True
            )

        # =================================================
        # NAVIGATION
        # =================================================

        section_title("Navigation")

        nav_html = card_begin()

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
            "📄 Reports",
        ]

        for page in pages:

            nav_html += f"""
            <div style="
                color:white;
                padding:8px 4px;
            ">
            {page}
            </div>
            """

        nav_html += card_end()

        st.markdown(
            nav_html,
            unsafe_allow_html=True
        )

        # =================================================
        # SNAPSHOTS
        # =================================================

        section_title("Snapshot History")

        st.markdown(
            f"""
            <div style="
                background:#0A1C48;
                border:1px solid #284A8A;
                border-radius:14px;
                padding:14px;
                margin-bottom:12px;
            ">

                <div style="
                    background:#DCE8F7;
                    color:#082549;
                    padding:10px;
                    border-radius:8px;
                    text-align:center;
                    font-weight:600;
                ">
                {snapshot.strftime("%B %Y")}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        # =================================================
        # PROJECT HEALTH
        # =================================================

        section_title("Project Health")

        st.markdown(
            f"""
            <div style="
                background:#0A1C48;
                border:1px solid #284A8A;
                border-radius:14px;
                padding:14px;
                margin-bottom:12px;
                color:white;
            ">

                <div style="
                    text-align:center;
                    font-size:32px;
                    font-weight:700;
                    margin-bottom:16px;
                ">
                {metrics['health_score']}/100
                </div>

                <div style="display:flex;justify-content:space-between;margin-bottom:10px;">
                    <span>Design Readiness</span>
                    <span style="color:#00D26A;">
                    {metrics['design_readiness']}%
                    </span>
                </div>

                <div style="display:flex;justify-content:space-between;margin-bottom:10px;">
                    <span>Critical Activities</span>
                    <span style="color:#FFB100;">
                    {metrics['critical_deliverables']}
                    </span>
                </div>

                <div style="display:flex;justify-content:space-between;margin-bottom:10px;">
                    <span>High Risk Activities</span>
                    <span style="color:#FF5E6C;">
                    {metrics['high_risk']}
                    </span>
                </div>

                <div style="display:flex;justify-content:space-between;">
                    <span>Upcoming Submissions</span>
                    <span style="color:#FFB100;">
                    {metrics['upcoming_submissions']}
                    </span>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        # =================================================
        # PROJECT BASELINE
        # =================================================

        section_title("Project Baseline")

        st.markdown(
            f"""
            <div style="
                background:#0A1C48;
                border:1px solid #284A8A;
                border-radius:14px;
                padding:14px;
                color:white;
            ">

                <div style="display:flex;justify-content:space-between;margin-bottom:12px;">
                    <span>Baseline Finish</span>
                    <span>
                    {metrics['baseline_finish'].strftime('%d %b %Y')}
                    </span>
                </div>

                <div style="display:flex;justify-content:space-between;margin-bottom:12px;">
                    <span>Current Forecast</span>
                    <span>
                    {metrics['forecast_finish'].strftime('%d %b %Y')}
                    </span>
                </div>

                <div style="display:flex;justify-content:space-between;">
                    <span>Programme Drift</span>
                    <span style="color:#FF5E6C;">
                    +{metrics['programme_drift']} Days
                    </span>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )