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

        </style>
        """,
        unsafe_allow_html=True
    )

    render_header(
        project=project,
        snapshot=snapshot
    )

    st.write("")

    summary_col, spacer_col = st.columns([5, 7])

    with summary_col:
        render_executive_summary(cl32)

    with spacer_col:
        st.empty()