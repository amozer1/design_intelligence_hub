import streamlit as st
from components.header import render_header


PAGE_BG = "#061F3B"
CARD_BG = "#08264F"
CARD_BORDER = "#1B4B77"


def card_placeholder(title, height=250):

    st.markdown(
        f"""
        <div style="
            background:{CARD_BG};
            border:1px solid {CARD_BORDER};
            border-radius:12px;
            padding:16px;
            height:{height}px;
            box-shadow:0 2px 6px rgba(0,0,0,0.15);
        ">
            <div style="
                color:white;
                font-size:14px;
                font-weight:600;
            ">
                {title}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
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

        .block-container {{
            padding-top:0.8rem;
            padding-left:1rem;
            padding-right:1rem;
            max-width:100%;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )

    # ==================================================
    # HEADER
    # ==================================================

    render_header(
        project=project,
        snapshot=snapshot,
    )

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # ==================================================
    # KPI STRIP
    # ==================================================

    k1, k2, k3, k4, k5, k6, k7 = st.columns(7)

    with k1:
        card_placeholder("Executive Summary", 80)

    with k2:
        card_placeholder("Programme Finish", 80)

    with k3:
        card_placeholder("Contract Completion", 80)

    with k4:
        card_placeholder("Total Deliverables", 80)

    with k5:
        card_placeholder("Critical Deliverables", 80)

    with k6:
        card_placeholder("Average Float", 80)

    with k7:
        card_placeholder("Average Variance", 80)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # ==================================================
    # ROW 1
    # ==================================================

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)

    with r1c1:
        card_placeholder("Executive Summary", 320)

    with r1c2:
        card_placeholder("Deliverables by Status", 320)

    with r1c3:
        card_placeholder("Deliverables by Discipline", 320)

    with r1c4:
        card_placeholder("Upcoming Submissions", 320)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # ==================================================
    # ROW 2
    # ==================================================

    r2c1, r2c2, r2c3, r2c4 = st.columns(4)

    with r2c1:
        card_placeholder("Critical Deliverables", 260)

    with r2c2:
        card_placeholder("What's Changed", 260)

    with r2c3:
        card_placeholder("Top 5 Biggest Slippers", 260)

    with r2c4:
        card_placeholder("Discipline Health", 260)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # ==================================================
    # ROW 3
    # ==================================================

    r3c1, r3c2, r3c3, r3c4, r3c5 = st.columns(5)

    with r3c1:
        card_placeholder("AI Risk Forecast", 240)

    with r3c2:
        card_placeholder("Design Dependencies", 240)

    with r3c3:
        card_placeholder("Queries & TQs", 240)

    with r3c4:
        card_placeholder("AI Insights", 240)

    with r3c5:
        card_placeholder("Quick Actions", 240)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # ==================================================
    # FOOTER
    # ==================================================

    f1, f2, f3, f4, f5 = st.columns(5)

    with f1:
        card_placeholder("Data Status", 60)

    with f2:
        card_placeholder("Last Refresh", 60)

    with f3:
        card_placeholder("Snapshots Loaded", 60)

    with f4:
        card_placeholder("Activities Tracked", 60)

    with f5:
        card_placeholder("Powered By", 60)