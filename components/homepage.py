import streamlit as st
from components.header import render_header

PAGE_BG = "#061F3B"
CARD_BG = "#08264F"
CARD_BORDER = "#1B4B77"


def card_placeholder(title, height=250):

    with st.container(border=True):
        st.markdown(f"**{title}**")

        for _ in range(max(1, height // 80)):
            st.write("")


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

        .block-container {{
            padding-top:1rem;
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

    st.write("")

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

    st.write("")

    # ==================================================
    # ROW 1
    # ==================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        card_placeholder("Executive Summary", 320)

    with c2:
        card_placeholder("Deliverables by Status", 320)

    with c3:
        card_placeholder("Deliverables by Discipline", 320)

    with c4:
        card_placeholder("Upcoming Submissions", 320)

    st.write("")

    # ==================================================
    # ROW 2
    # ==================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        card_placeholder("Critical Deliverables", 260)

    with c2:
        card_placeholder("What's Changed", 260)

    with c3:
        card_placeholder("Top 5 Biggest Slippers", 260)

    with c4:
        card_placeholder("Discipline Health", 260)

    st.write("")

    # ==================================================
    # ROW 3
    # ==================================================

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        card_placeholder("AI Risk Forecast", 240)

    with c2:
        card_placeholder("Design Dependencies", 240)

    with c3:
        card_placeholder("Queries & TQs", 240)

    with c4:
        card_placeholder("AI Insights", 240)

    with c5:
        card_placeholder("Quick Actions", 240)

    st.write("")

    # ==================================================
    # FOOTER
    # ==================================================

    f1, f2, f3, f4, f5 = st.columns(5)

    with f1:
        card_placeholder("Data Status", 70)

    with f2:
        card_placeholder("Last Refresh", 70)

    with f3:
        card_placeholder("Snapshots Loaded", 70)

    with f4:
        card_placeholder("Activities Tracked", 70)

    with f5:
        card_placeholder("Powered By", 70)