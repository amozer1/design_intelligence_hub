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
            max-width: 100%;
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: white !important;
        }}

        p {{
            color: white !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    # =================================================
    # HEADER
    # =================================================

    render_header(
        project=project,
        snapshot=snapshot
    )

    st.write("")

    # =================================================
    # EXECUTIVE SUMMARY
    # =================================================

    render_executive_summary(
        cl32
    )

    st.write("")

    # =================================================
    # KPI ROW PLACEHOLDERS
    # =================================================

    row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)

    with row1_col1:
        st.empty()

    with row1_col2:
        st.empty()

    with row1_col3:
        st.empty()

    with row1_col4:
        st.empty()
