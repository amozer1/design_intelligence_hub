import streamlit as st

from components.header import render_header

from kpis.ferry.executive_summary import (
    render as render_executive_summary
)

PAGE_BG = "#081322"


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

        </style>
        """,
        unsafe_allow_html=True
    )

    render_header(
        project=project,
        snapshot=snapshot
    )

    st.write("")

    k1, k2, k3, k4, k5, k6, k7 = st.columns(
        [3.5, 1.8, 1.8, 1.4, 1.4, 1.2, 1.4]
    )

    with k1:
        render_executive_summary(cl32)

    with k2:
        st.empty()

    with k3:
        st.empty()

    with k4:
        st.empty()

    with k5:
        st.empty()

    with k6:
        st.empty()

    with k7:
        st.empty()