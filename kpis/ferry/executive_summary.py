import streamlit as st

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)

GREEN = "#16A34A"
GOLD = "#D4AF37"
RED = "#DC2626"

BODY = "#374151"
ICON_GREEN = "#10B981"


def render(cl32):
    metrics = get_metrics(cl32)

    score = metrics["health_score"]
    readiness = metrics["design_readiness"]
    programme_drift = metrics["programme_drift"]
    high_risk = metrics["high_risk"]
    critical_deliverables = metrics["critical_deliverables"]

    status = get_status(score)

    status_colour = RED

    if score >= 80:
        status_colour = GREEN

    elif score >= 60:
        status_colour = GOLD

    with st.container(border=True):

        # ===================================
        # HEADER
        # ===================================

        title_col, status_col = st.columns([5, 1])

        with title_col:
            st.markdown(
                """
                <div style="
                    color:#111827;
                    font-size:16px;
                    font-weight:700;
                    margin-bottom:20px;
                ">
                    EXECUTIVE SUMMARY
                </div>
                """,
                unsafe_allow_html=True
            )

        with status_col:
            st.markdown(
                f"""
                <div style="
                    background:{status_colour};
                    color:white;
                    text-align:center;
                    border-radius:8px;
                    padding:4px 8px;
                    font-size:10px;
                    font-weight:700;
                ">
                    {status}
                </div>
                """,
                unsafe_allow_html=True
            )

        # ===================================
        # BODY
        # ===================================

        score_col, insight_col = st.columns([1, 2])

        with score_col:
            st.markdown(
                f"""
                <div style="
                    font-size:42px;
                    font-weight:700;
                    color:{status_colour};
                    text-align:center;
                    margin-top:10px;
                ">
                    {score}%
                </div>

                <div style="
                    text-align:center;
                    color:#6B7280;
                    font-size:11px;
                ">
                    Health Score
                </div>
                """,
                unsafe_allow_html=True
            )

        with insight_col:
            st.markdown(
                f"""
                <div style="
                    color:{BODY};
                    font-size:13px;
                    margin-bottom:10px;
                ">
                    <span style="
                        color:{ICON_GREEN};
                        font-size:16px;
                        font-weight:700;
                    ">
                        ⊕
                    </span>
                    Programme behind baseline by
                    <b>{programme_drift} days</b>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div style="
