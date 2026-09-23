import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)

HEADER_BG = "#082f49"
CARD_BG = "#0f172a"
BORDER = "#334155"


def build_gauge(score):
    colour = "#ff3b30"

    if score >= 80:
        colour = "#00c853"

    elif score >= 60:
        colour = "#ffd700"

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[
                score,
                100 - score,
                100
            ],
            hole=0.84,
            rotation=180,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    colour,
                    "#667085",
                    "rgba(0,0,0,0)"
                ]
            )
        )
    )

    fig.update_layout(
        height=120,
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
                    size=16,
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

    status_colour = "#7f1d1d"

    if status == "ON TRACK":
        status_colour = "#14532d"

    elif status == "WATCHLIST":
        status_colour = "#92400e"

    st.markdown(
        f"""
        <style>

        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background:{CARD_BG} !important;
            border:1px solid {BORDER} !important;
            border-radius:12px !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    with st.container(border=True):

        title_col, pill_col = st.columns(
            [4, 1]
        )

        with title_col:

            st.markdown(
                """
                <span style="
                    color:#dce8f5;
                    font-size:12px;
                    font-weight:700;
                    letter-spacing:.5px;
                ">
                EXECUTIVE SUMMARY
                </span>
                <span style="
                    color:#94a3b8;
                    font-size:11px;
                ">
                (AI GENERATED)
                </span>
                """,
                unsafe_allow_html=True
            )

        with pill_col:

            st.markdown(
                f"""
                <div style="
                    background:{status_colour};
                    color:white;
                    border-radius:8px;
                    text-align:center;
                    padding:4px;
                    font-size:11px;
                    font-weight:700;
                ">
                {status}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")

        gauge_col, insight_col = st.columns(
            [1, 2.3]
        )

        with gauge_col:

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

            st.markdown(
                f"### {readiness}%"
            )

            st.markdown(
                """
                <span style="
                    color:#22c55e;
                    font-size:12px;
                    font-weight:600;
                ">
                ↑ 5%
                </span>
                <span style="
                    color:#94a3b8;
                    font-size:11px;
                ">
                vs last month
                </span>
                """,
                unsafe_allow_html=True
            )

        with insight_col:

            if programme_drift > 0:
                st.write(
                    f"✅ Programme is behind baseline by {programme_drift} days."
                )

            if high_risk > 0:
                st.write(
                    f"✅ {high_risk} activities with negative float."
                )

            if critical_deliverables > 0:
                st.write(
                    f"✅ Focus on {critical_deliverables} critical deliverables."
                )

