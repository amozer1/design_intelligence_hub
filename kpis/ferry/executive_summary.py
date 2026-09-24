import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


def build_gauge(score):

    colour = "#ff4d4f"

    if score >= 80:
        colour = "#22c55e"

    elif score >= 60:
        colour = "#f59e0b"

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

    critical_deliverables = metrics[
        "critical_deliverables"
    ]

    status = get_status(score)

    status_colour = "#dc2626"

    if status == "ON TRACK":
        status_colour = "#16a34a"

    elif status == "WATCHLIST":
        status_colour = "#ca8a04"

    # ==================================================
    # PANEL
    # ==================================================

    st.markdown(
        f"""
        <div style="
            background:#1E293B;
            border:1px solid #475569;
            border-radius:10px;
            padding:12px 16px;
            margin-bottom:10px;
        ">
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # HEADER
    # ==================================================

    h1, h2 = st.columns([5, 1])

    with h1:

        st.markdown(
            """
            <span style="
                color:white;
                font-size:14px;
                font-weight:700;
            ">
            EXECUTIVE SUMMARY
            </span>

            <span style="
                color:#94a3b8;
                font-size:11px;
                margin-left:6px;
            ">
            (AI GENERATED)
            </span>
            """,
            unsafe_allow_html=True
        )

    with h2:

        st.markdown(
            f"""
            <div style="
                background:{status_colour};
                color:white;
                text-align:center;
                padding:4px 8px;
                border-radius:6px;
                font-size:11px;
                font-weight:700;
            ">
            {status}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # ==================================================
    # BODY
    # ==================================================

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

        colour = "#22c55e"

        if change < 0:
            colour = "#ef4444"

        st.markdown(
            f"""
            <span style="
                color:{colour};
                font-size:14px;
                font-weight:700;
            ">
            {'↑' if change >= 0 else '↓'} {abs(change)}%
            </span>

            <span style="
                color:#94a3b8;
                font-size:11px;
            ">
            vs health score
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

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )