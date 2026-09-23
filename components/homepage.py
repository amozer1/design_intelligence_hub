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

        </style>
        """,
        unsafe_allow_html=True
    )

    render_header(
        project=project,
        snapshot=snapshot
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="
            background:#1E293B;
            padding:20px;
            border-radius:12px;
            border-left:6px solid #3B82F6;
            border:1px solid #64748B;
            box-shadow:0 4px 10px rgba(0,0,0,0.25);
            margin-bottom:20px;
        ">
        <div style="
            font-size:20px;
            font-weight:700;
            color:white;
            margin-bottom:10px;
        ">
            Executive Summary
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_executive_summary(cl32)

    st.markdown("<br>", unsafe_allow_html=True)