import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


def build_gauge(score):
    colour = "#FF3B30"

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
                    "#64748B",
                    "rgba(0,0,0,0)"
                ]
            )
        )
    )

    fig.update_layout(
        height=140,
        margin=dict(l=0, r=0, t=0, b=0),
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

    if status == "ON TRACK":
        status_colour = "#16A34A"

    elif status == "WATCHLIST":
        status_colour = "#CA8A04"

    # ==================================================
    # VERY OBVIOUS TEST BOUNDARY
    # ==================================================

    st.markdown(
        """
        <div style="
            background:#FFD700;
            border:10px solid #FF0000;
            border-radius:16px;
            padding:20px;
            margin-bottom:15px;
            color:black;
            font-weight:bold;
        ">
            EXECUTIVE SUMMARY BOUNDARY TEST
        </div>
        """,
        unsafe_allow_html=True
    )

    header_l, header_r = st.columns([5, 1])

    with header_l:

        st.markdown(
            """
            **EXECUTIVE SUMMARY**

            <span style="color:#94A3B8;">
            (AI GENERATED)
            </span>
            """,
            unsafe_allow_html=True
        )

    with header_r:

        st.markdown(
            f"""
            <div style="
                background:{status_colour};
                color:white;
                padding:4px;
                border-radius:6px;
                text-align:center;
                font-size:11px;
                font-weight:700;
            ">
                {status}
            </div>
            """,
            unsafe_allow_html=True
        )

    left, right = st.columns([1, 2])

    with left:

        st.plotly_chart(
            build_gauge(score),
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

        st.caption(
            "Design Readiness Index"
        )

        change = readiness - score

        colour = "#22C55E"

        if change < 0:
            colour = "#EF4444"

        arrow = "↑" if change >= 0 else "↓"

        st.markdown(
            f"""
            <span style="
                color:{colour};
                font-size:14px;
                font-weight:700;
            ">
                {arrow} {abs(change)}%
            </span>
            """,
            unsafe_allow_html=True
        )

    with right:

        st.write(
            f"🟢 Programme is behind baseline by {programme_drift} days."
        )

        st.write(
            f"🟢 {high_risk} activities with negative float."
        )

        st.write(
            f"🟢 Focus on {critical_deliverables} critical deliverables."
        )