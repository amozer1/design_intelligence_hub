import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


def build_gauge(score):

    colour = "#FF3366"

    if score >= 80:
        colour = "#22C55E"

    elif score >= 60:
        colour = "#F59E0B"

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[score, 100 - score, 100],
            hole=0.80,
            rotation=180,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    colour,
                    "#475569",
                    "rgba(0,0,0,0)"
                ]
            )
        )
    )

    fig.update_layout(
        height=110,
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        annotations=[
            dict(
                text=f"{score}%",
                x=0.5,
                y=0.42,
                showarrow=False,
                font=dict(
                    size=18,
                    color="white"
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

    status_colour = "#DC2626"

    if "TRACK" in str(status).upper():
        status_colour = "#16A34A"

    elif "WATCH" in str(status).upper():
        status_colour = "#CA8A04"

    with st.container(border=True):

        title_col, badge_col = st.columns([4, 1])

        with title_col:
            st.markdown(
                "##### EXECUTIVE SUMMARY"
            )

        with badge_col:

            st.markdown(
                f"""
                <div style="
                    background:{status_colour};
                    color:white;
                    text-align:center;
                    border-radius:6px;
                    padding:4px;
                    font-size:10px;
                    font-weight:700;
                ">
                {status}
                </div>
                """,
                unsafe_allow_html=True
            )

        gauge_col, insight_col = st.columns([1, 1.5])

        with gauge_col:

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

        with insight_col:

            st.markdown(
                f"🔴 Baseline: **{programme_drift}d**"
            )

            st.markdown(
                f"🟠 Float: **{high_risk}**"
            )

            st.markdown(
                f"🟡 Critical: **{critical_deliverables}**"
            )