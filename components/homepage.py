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
        }}

        h1,h2,h3,h4,h5,h6 {{
            color:white !important;
        }}

        p {{
            color:white !important;
        }}

        /* EXECUTIVE SUMMARY SECTION */

        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background:#0f172a !important;
            border:1px solid #334155 !important;
            border-radius:12px !important;
            padding:20px !important;
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
    # EXECUTIVE SUMMARY SECTION
    # ==================================================

    summary_section = st.container(
        border=True
    )

    with summary_section:

        render_executive_summary(
            cl32
        )

    st.write("")

    # ==================================================
    # ROW 1
    # ==================================================

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)

    with r1c1:
        st.empty()

    with r1c2:
        st.empty()

    with r1c3:
        st.empty()

    with r1c4:
        st.empty()

    st.write("")

    # ==================================================
    # ROW 2
    # ==================================================

    r2c1, r2c2, r2c3, r2c4 = st.columns(4)

    with r2c1:
        st.empty()

    with r2c2:
        st.empty()

    with r2c3:
        st.empty()

    with r2c4:
        st.empty()