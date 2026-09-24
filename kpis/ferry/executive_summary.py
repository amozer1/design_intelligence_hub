import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


GREEN = "#16A34A"
GOLD = "#D4AF37"
RED = "#DC2626"

BODY = "#374151"
TRACK = "#DCE3EB"


def build_gauge(score):

    if score >= 80:
        colour = GREEN

    elif score >= 60:
        colour = GOLD

    else:
        colour = RED

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[
                score,
                100 - score,
                100
            ],
            hole=0.75,
            rotation=180,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    colour,
                    TRACK,
                    "rgba(0,0,0,0)"
                ]
            )
        )
    )

    fig.update_layout(
        height=70,
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        annotations=[
            dict(
                text=f"{score}%",
                x=0.5,
                y=0.42,
                showarrow=False,
                font=dict(
                    size=18,
                    color=colour
                )
            )
        ]
    )

    return fig


def render(cl32):

    metrics = get_metrics(cl32)

    score = metrics["health_score"]
    readiness = metrics["design_readiness"]
    programme_drift = metrics["programme_drift"]
    high_risk = metrics["high_risk"]
    critical_deliverables = metrics[
        "critical_deliverables"
    ]

    status = get_status(score)

    status_colour = RED

    if score >= 80:
        status_colour = GREEN

    elif score >= 60:
        status_colour = GOLD

    # ===================================
    # RAG ICON COLOURS
    # ===================================

    if programme_drift <= 10:
        programme_icon = GREEN
    elif programme_drift <= 25:
        programme_icon = GOLD
    else:
        programme_icon = RED

    if high_risk <= 10:
        risk_icon = GREEN
    elif high_risk <= 25:
        risk_icon = GOLD
    else:
        risk_icon = RED

    if critical_deliverables <= 10:
        deliverable_icon = GREEN
    elif critical_deliverables <= 25:
        deliverable_icon = GOLD
    else:
        deliverable_icon = RED

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
                    margin-bottom:18px;
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

        gauge_col, insight_col = st.columns(
            [0.8, 2.2]
        )

        with gauge_col:

            st.plotly_chart(
                build_gauge(score),
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
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
                        color:{programme_icon};
                        font-size:16px;
                        font-weight:700;
                    ">
                        ●
                    </span>
                    Programme behind baseline by
                    <b>{programme_drift} 