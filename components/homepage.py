import streamlit as st

from components.header import render_header

from kpis.ferry.executive_summary import (
    render as render_executive_summary
)

PAGE_BG = "#1E293B"


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

    # ==================================================
    # HEADER
    # ==================================================

    render_header(
        project=project,
        snapshot=snapshot
    )

    st.write("")

    # ==================================================
    # KPI RIBBON
    # ==================================================

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

    st.write("")

    # ==================================================
    # ROW 3
    # ==================================================

    r3c1, r3c2, r3c3, r3c4, r3c5 = st.columns(5)

    with r3c1:
        st.empty()

    with r3c2:
        st.empty()

    with r3c3:
        st.empty()

    with r3c4:
        st.empty()

    with r3c5:
        st.empty()

    st.write("")

    # ==================================================
    # FOOTER
    # ==================================================

    f1, f2, f3, f4, f5 = st.columns(5)

    with f1:
        st.empty()

    with f2:
        st.empty()

    with f3:
        st.empty()

    with f4:
        st.empty()

    with f5:
        st.empty()