import streamlit as st

from components.header import render_header

from kpis.ferry.executive_summary import (
    render as render_executive_summary
)

PAGE_BG = "#10203A"


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

        [data-testid="stMain"] {{
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
            padding-left:1rem;
            padding-right:1rem;
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
    # EXECUTIVE SUMMARY ROW
    # ==========================================

    summary_col, remainder_col = st.columns(
        [5, 7]
    )

    with summary_col:

        render_executive_summary(
            cl32
        )

    with remainder_col:

        st.empty()

    st.write("")

    # ==========================================
    # FUTURE KPI ROWS
    # ==========================================

    # Add future KPI tiles here when ready
    #
    # k1, k2, k3, k4 = st.columns(4)
    #
    # with k1:
    #     render_programme_finish(...)
    #
    # with k2:
    #     render_contract_completion(...)
    #
    # with k3:
    #     render_deliverables(...)
    #
    # with k4:
    #     render_float(...)