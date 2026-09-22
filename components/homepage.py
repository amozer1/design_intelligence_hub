import streamlit as st

from components.header import render_header
from kpis.ferry.executive_summary import (
    render as render_executive_summary
)

PAGE_BG = "#051A33"
CARD_BG = "#103766"
CARD_BORDER = "#4B80C7"


def card_placeholder(title, height=250):

    st.markdown(
        f"""
        <div style="
            background:{CARD_BG};
            border:2px solid {CARD_BORDER};
            border-radius:14px;
            padding:16px;
            height:{height}px;
            box-shadow:0 4px 12px rgba(0,0,0,0.35);
        ">
            <div style="
                color:#FFFFFF;
                font-size:16px;
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

        .block-container {{
            padding-top:0rem !important;
            max-width:100%;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )

    render_header(
        project=project,
        snapshot=snapshot
    )

    st.write("")

    # KPI STRIP

    k1, k2, k3, k4, k5, k6, k7 = st.columns(7)

    with k1:
        st.metric(
            "Executive Summary",
            f"{metrics['health_score']}%"
        )

    with k2:
        card_placeholder("Programme Finish", 90)

    with k3:
        card_placeholder("Contract Completion", 90)

    with k4:
        card_placeholder("Total Deliverables", 90)

    with k5:
        card_placeholder("Critical Deliverables", 90)

    with k6:
        card_placeholder("Average Float", 90)

    with k7:
        card_placeholder("Average Variance", 90)

    st.write("")

    # ROW 1

    left, right = st.columns([2, 5])

    with left:
        render_executive_summary(cl32)

    with right:
        card_placeholder(
            "Deliverables by Status",
            320
        )

    st.write("")

    # ROW 2

    r2c1, r2c2 = st.columns(2)

    with r2c1:
        card_placeholder(
            "Deliverables by Discipline",
            320
        )

    with r2c2:
        card_placeholder(
            "Upcoming Submissions",
            320
        )

    st.write("")

    # ROW 3

    r3c1, r3c2, r3c3, r3c4 = st.columns(4)

    with r3c1:
        card_placeholder(
            "Critical Deliverables",
            260
        )

    with r3c2:
        card_placeholder(
            "What's Changed",
            260
        )

    with r3c3:
        card_placeholder(
            "Top 5 Biggest Slippers",
            260
        )

    with r3c4:
        card_placeholder(
            "Discipline Health",
            260
        )