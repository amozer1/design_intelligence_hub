import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


GREEN = "#10B981"
AMBER = "#F59E0B"
RED = "#EF4444"

TEXT = "#111827"
MUTED = "#6B7280"
TRACK = "#E5E7EB"


def build_gauge(score):

    if score >= 80:
        colour = GREEN

    elif score >= 60:
        colour = "#34D399"

    else:
        colour = GREEN

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[
                score,
                100 - score,
                100
            ],
            hole=0.85,
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
        height=125,
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
                y=0.43,
                showarrow=False,
                font=dict(
                    size=28,
                    color=TEXT
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

    status_colour = RED

    status_upper = str(status).upper()

    if "TRACK" in status_upper:
        status_colour = GREEN

    elif "WATCH" in status_upper:
        status_colour = AMBER

    with st.container(border=True):

        # =====================================
        # HEADER
        # =====================================

        title_col, status_col = st.columns([5, 1])

        with title_col:

            st.markdown(
                """
                <div style="
                    color:#111827;
                    font-size:18px;
                    font-weight:700;
                    letter-spacing:0.3px;
                ">
                    EXECUTIVE SUMMARY
                </div>

                <div style="
                    color:#6B7280;
                    font-size:11px;
                    font-weight:500;
                ">
                    AI Generated
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
                    margin-top:4px;
                ">
                    {status}
                </div>
                """,
                unsafe_allow_html=True
            )

        # =====================================
        # BODY
        # =====================================

        gauge_col, insight_col = st.columns([1, 2])

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
                    color:{TEXT};
                    font-size:13px;
                    margin-bottom:14px;
                ">
                    <span style="
                        color:{GREEN};
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
                    color:{TEXT};
                    font-size:13px;
                    margin-bottom:14px;
                ">
                    <span style="
                        color:{GREEN};
                        font-size:16px;
                        font-weight:700;
                    ">
                    ⊕
                    </span>
                    <b>{high_risk}</b>
                    activities currently carry negative float
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div style="
                    color:{TEXT};
                    font-size:13px;
                ">
                    <span style="
                        color:{GREEN};
                        font-size:16px;
                        font-weight:700;
                    ">
                    ⊕
                    </span>
                    <b>{critical_deliverables}</b>
                    critical deliverables require attention
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        # =====================================
        # FOOTER
        # =====================================

        footer_left, footer_right = st.columns([5, 1])

        with footer_left:

            st.markdown(
                """
                <div style="
                    color:#6B7280;
                    font-size:12px;
                    font-weight:600;
                ">
                    Design Readiness Index
                </div>
                """,
                unsafe_allow_html=True
            )

        with footer_right:

            st.markdown(
                f"""
                <div style="
                    color:{GREEN};
                    font-size:28px;
                    font-weight:700;
                    text-align:right;
                ">
                    {readiness}%
                </div>
                """,
                unsafe_allow_html=True
            )