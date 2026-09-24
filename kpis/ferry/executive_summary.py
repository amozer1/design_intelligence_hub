import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


def build_gauge(score):

    colour = "#EF4444"

    if score >= 80:
        colour = "#22C55E"

    elif score >= 60:
        colour = "#F59E0B"

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[
                score,
                100 - score,
                100
            ],
            hole=0.82,
            rotation=180,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    colour,
                    "#94A3B8",
                    "rgba(0,0,0,0)"
                ]
            )
        )
    )

    fig.update_layout(
        height=100,
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
                    size=16,
                    color="#111827"
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
    critical_deliverables = metrics["critical_deliverables"]

    status = get_status(score)

    status_upper = str(status).upper()

    if "TRACK" in status_upper:
        badge_colour = "#16A34A"
    elif "WATCH" in status_upper:
        badge_colour = "#CA8A04"
    else:
        badge_colour = "#DC2626"

    with st.container(border=True):

        h1, h2 = st.columns([4, 1])

        with h1:

            st.markdown(
                """
                <div style="
                    font-size:11px;
                    font-weight:700;
                    color:#0F172A;
                ">
                    EXECUTIVE SUMMARY
                </div>
                <div style="
                    font-size:9px;
                    color:#64748B;
                    margin-top:-4px;
                ">
                    (AI GENERATED)
                </div>
                """,
                unsafe_allow_html=True
            )

        with h2:

            st.markdown(
                f"""
                <div style="
                    background:{badge_colour};
                    color:white;
                    text-align:center;
                    padding:2px 6px;
                    border-radius:6px;
                    font-size:9px;
                    font-weight:700;
                ">
                    {status}
                </div>
                """,
                unsafe_allow_html=True
            )

        left, right = st.columns([1, 1.4])

        with left:

            st.plotly_chart(
                build_gauge(score),
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )

            st.caption("Readiness")

            st.markdown(
                f"**{readiness}%**"
            )

        with right:

            st.markdown(
                f"🔴 Behind baseline: **{programme_drift}d**"
            )

            st.markdown(
                f"🟠 Negative float: **{high_risk}**"
            )

            st.markdown(
                f"🟡 Critical items: **{critical_deliverables}**"
            )