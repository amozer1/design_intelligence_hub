import streamlit as st

from kpis.ferry.executive_summary_styles import (
    load_executive_summary_styles
)

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status
)


def render(cl32):

    load_executive_summary_styles()

    metrics = get_metrics(cl32)

    status = get_status(
        metrics["score"]
    )

    with st.container(border=True):

        st.caption(
            "EXECUTIVE SUMMARY (AI GENERATED)"
        )

        st.write(status)

        ...