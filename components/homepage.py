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

        /* PAGE BACKGROUND */

        .stApp {{
            background:{PAGE_BG} !important;
        }}

        [data-testid="stAppViewContainer"] {{
            background:{PAGE_BG} !important;
        }}

        [data-testid="stMain"] {{
            background:{PAGE_BG} !important;
        }}

        .main {{
            background:{PAGE_BG} !important;
        }}

        /* TEST 1 */

        [data-testid="stVerticalBlock"] {{
            border:3px solid lime !important;
        }}

        /* TEST 2 */

        [data-testid="column"] {{
            border:3px solid red !important;
        }}

        /* TEST 3 */

        [data-testid="stElementContainer"] {{
            border:2px solid yellow !important;
        }}

        /* PAGE SETTINGS */

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

    render_executive_summary(cl32)

    st.write("")

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)

    with r1c1:
        st.empty()

    with r1c2:
        st.empty()

    with r1c3:
        st.empty()

    with r1c4:
        st.empty()