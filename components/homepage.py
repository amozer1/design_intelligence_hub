import streamlit as st

from components.header import render_header

from kpis.ferry.executive_summary import (
    render as render_executive_summary
)

from kpis.ferry.programme_completion import (
    render as render_programme_completion
)

from kpis.ferry.total_deliverables import (
    render as render_total_deliverables
)

from kpis.ferry.critical_deliverables import (
    render as render_critical_deliverables
)

from kpis.ferry.average_float import (
    render as render_average_float
)

from kpis.ferry.average_variance import (
    render as render_average_variance
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
    # ROW 1
    # ==========================================

    c1, c2, c3, c4, c5, c6 = st.columns(
        [4, 4, 1.5, 1.5, 1.5, 1.5]
    )

    with c1:

        render_executive_summary(
            cl32
        )

    with c2:

        render_programme_completion(
            cl32
        )

    with c3:

        render_total_deliverables(
            cl32
        )

    with c4:

        render_critical_deliverables(
            cl32
        )

    with c5:

        render_average_float(
            cl32
        )

    with c6:

        render_average_variance(
            cl32
        )