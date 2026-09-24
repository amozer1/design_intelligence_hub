import streamlit as st

from components.header import render_header

from kpis.ferry.executive_summary import (
    render as render_executive_summary
)

from kpis.ferry.programme_completion import (
    render as render_programme_completion
)

PAGE_BG = "#EAF2FF"


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
            background: {PAGE_BG};
        }}

        [data-testid="stAppViewContainer"] {{
            background: {PAGE_BG};
        }}

        [data-testid="stMain"] {{
            background: {PAGE_BG};
        }}

        .main {{
            background: {PAGE_BG};
        }}

        [data-testid="stHeader"] {{
            display: none;
        }}

        [data-testid="stToolbar"] {{
            display: none;
        }}

        .block-container {{
            padding-top: 0rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: 100%;
        }}

        body {{
            color: #111827;
        }}

        p {{
            color: #374151;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    # ==========================================
    # HEADER
    # ==========================================

    render_header(
        project=project,
        snapshot=snapshot
    )

    st.write("")

    # ==========================================
    # KPI ROW 1
    # ==========================================

    summary_col, programme_col = st.columns([5, 5])

    with summary_col:

        render_executive_summary(
            cl32
        )

    with programme_col:

        render_programme_completion(
            programme_finish="20 Oct 2026",
            programme_baseline="24 Sep 2026",
            contract_completion="14 Sep 2026",
            contract_baseline="07 Oct 2026",
        )

    st.write("")

    # ==========================================
    # FUTURE KPI CARDS
    # ==========================================

    # k1, k2, k3, k4 = st.columns(4)
    #
    # with k1:
    #     render_programme_finish()
    #
    # with k2:
    #     render_completion()
    #
    # with k3:
    #     render_deliverables()
    #
    # with k4:
    #     render_float()