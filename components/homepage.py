import streamlit as st

from components.header import render_header

from kpis.ferry.executive_summary import (
    render as render_executive_summary
)

PAGE_BG = "#051A33"


def card_placeholder(title, height=250):

    st.markdown(
        f"""
        <div style="
            background:#103766;
            border:1px solid #4B80C7;
            border-radius:12px;
            padding:12px;
            height:{height}px;
        ">
            <div style="
                color:white;
                font-size:14px;
                font-weight:700;
            ">
                {title}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_homepage(
    project,
    snapshot,
    metrics,
    cl31,
    cl32,
):

    st.markdown(
        f"""
        <style>

        .stApp {{
            background:{PAGE_BG};
        }}

        [data-testid="stAppViewContainer"] {{
            background:{PAGE_BG};
        }}

        .main {{
            background:{PAGE_BG};
        }}

        [data-testid="stHeader"] {{
            display:none;
        }}

        [data-testid="stToolbar"] {{
            display:none;
        }}

        .block-container {{
            padding-top:0rem !important;
            max-width:100%;
        }}

        h1,h2,h3,h4,h5,h6 {{
            color:white !important;
        }}

        p {{
            color:white !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # HEADER
    # ==================================================

    render_header(
        project=project,
        snapshot=snapshot
    )

    st.write("")

    # ==================================================
    # KPI RIBBON
    # ==================================================

    k1, k2, k3, k4, k5, k6, k7 = st.columns(
        [3.5, 1.8, 1.8, 1.4, 1.4, 1.2, 1.4]
    )

    with k1:
        render_executive_summary(cl32)

    with k2:
        card_placeholder(
            "Programme Finish",
            120
        )

    with k3:
        card_placeholder(
            "Contract Completion",
            120
        )

    with k4:
        card_placeholder(
            "Total Deliverables",
            120
        )

    with k5:
        card_placeholder(
            "Critical Deliverables",
            120
        )

    with k6:
        card_placeholder(
            "Average Float",
            120
        )

    with k7:
        card_placeholder(
            "Average Variance (BL1)",
            120
        )

    st.write("")

    # ==================================================
    # ROW 1
    # ==================================================

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)

    with r1c1:
        card_placeholder(
            "Deliverables by Status",
            320
        )

    with r1c2:
        card_placeholder(
            "Deliverables by Discipline",
            320
        )

    with r1c3:
        card_placeholder(
            "Deliverables by Design Stage",
            320
        )

    with r1c4:
        card_placeholder(
            "Upcoming Submissions",
            320
        )

    st.write("")

    # ==================================================
    # ROW 2
    # ==================================================

    r2c1, r2c2, r2c3, r2c4 = st.columns(4)

    with r2c1:
        card_placeholder(
            "Critical Deliverables",
            260
        )

    with r2c2:
        card_placeholder(
            "What's Changed",
            260
        )

    with r2c3:
        card_placeholder(
            "Top 5 Biggest Slippers",
            260
        )

    with r2c4:
        card_placeholder(
            "Discipline Health",
            260
        )

    st.write("")

    # ==================================================
    # ROW 3
    # ==================================================

    r3c1, r3c2, r3c3, r3c4, r3c5 = st.columns(5)

    with r3c1:
        card_placeholder(
            "AI Risk Forecast",
            240
        )

    with r3c2:
        card_placeholder(
            "Design Dependencies",
            240
        )

    with r3c3:
        card_placeholder(
            "Queries & TQs Overview",
            240
        )

    with r3c4:
        card_placeholder(
            "AI Insights",
            240
        )

    with r3c5:
        card_placeholder(
            "Quick Actions",
            240
        )

    st.write("")

    # ==================================================
    # FOOTER
    # ===========================================