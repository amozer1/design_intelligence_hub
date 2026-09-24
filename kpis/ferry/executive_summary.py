import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


PANEL_BG = "#24344D"
BORDER = "#94A3B8"
ACCENT = "#16A34A"


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

    status_colour = "#DC2626"

    if status == "ON TRACK":
        status_colour = "#16A34A"

    elif status == "WATCHLIST":
        status_colour = "#CA8A04"

    # ==================================================
    # PANEL START
    # ==================================================

    panel = st.container(border=True)

    with panel:

        st.markdown(
            f"""
            <style>

            div[data-testid="stVerticalBlockBorderWrapper"] {{
                background:{PANEL_BG} !important;
                border:3px solid {BORDER} !important;
                border-radius:12px !important;
                padding:12px !important;
            }}

            </style>
            """,
            unsafe_allow_html=True
        )

        # ==========================================
        # HEADER
        # ==========================================

        c1, c2 = st.columns([5, 1])

        with c1:

            st.markdown(
                """
                **EXECUTIVE SUMMARY**
                <span style="
                    color:#94A3B8;
                    font-size:11px;
                    margin-left:6px;
                ">
                (AI GENERATED)
                </span>
                """,
                unsafe_allow_html=True
            )

        with c2:

            st.markdown(
                f"""
                <div style="
                    background:{status_colour};
                    color:white;
                    padding:4px;
                    text-align:center;
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

        # ==========================================
        # BODY
        # ==========================================

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

            arrow = "↑" if change >= 0 else "↓"

            colour = "#22C55E"

            if change < 0:
                colour = "#EF4444"

            st.markdown(
                f"""
                <span style="
                    color:{colour};
                    font-size:14px;
                    font-weight:700;
                ">
                {arrow} {abs(change)}%
                </span>

                <span style="
                    color:#CBD5E1;
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