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
    # KPI ROW
    # ==================================================

    summary_col, finish_col, completion_col, deliverables_col, critical_col = st.columns(
        [3, 2, 2, 2, 2]
    )

    with summary_col:

        render_executive_summary(
            cl32
        )

    with finish_col:

        st.container(
            border=True
        )

    with completion_col:

        st.container(
            border=True
        )

    with deliverables_col:

        st.container(
            border=True
        )

    with critical_col:

        st.container(
            border=True
        )

    st.write("")

    # ==================================================
    # NEXT ROW PLACEHOLDERS
    # ==================================================

    row2_col1, row2_col2, row2_col3, row2_col4 = st.columns(4)

    with row2_col1:
        st.empty()

    with row2_col2:
        st.empty()

    with row2_col3:
        st.empty()

    with row2_col4:
        st.empty()