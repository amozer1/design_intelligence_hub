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
            values=[
                score,
                100 - score,
                100
            ],
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
        height=100,
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
    critical_deliverables = metrics["critical_deliverables"]

    status = get_status(score)

    badge_colour = "#DC2626"

    if "TRACK" in str(status).upper():
        badge_colour = "#16A34A"

    elif "WATCH" in str(status).upper():
        badge_colour = "#CA8A04"

    st.markdown(
        """
        <div style="
            background:#14213D;
            border:3px solid #3B82F6;
            border-radius:12px;
            padding:12px;
            min-height:220px;
        ">
        """,
        unsafe_allow_html=True
    )

    header_left, header_right = st.columns([4, 1])

    with header_left:

        st.markdown(
            """
            <div style="
                color:white;
                font-size:12px;
                font-weight:700;
            ">
            EXECUTIVE SUMMARY
            </div>
            """,
            unsafe_allow_html=True
        )

    with header_right:

        st.markdown(
            f"""
            <div style="
                background:{badge_colour};
                color:white;
                text-align:center;
                border-radius:6px;
                padding:3px;
                font-size:9px;
                font-weight:700;
            ">
            {status}
            </div>
            """,
            unsafe_allow_html=True
        )

    left, right = st.columns([1, 1.5])

    with left:

        st.plotly_chart(
            build_gauge(score),
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

        st.markdown(
            f"""
            <div style="
                color:#94A3B8;
                font-size:10px;
            ">
            Readiness
            </div>

            <div style="
                color:white;
                font-size:18px;
                font-weight:700;
            ">
            {readiness}%
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        st.markdown(
            f"""
            <div style="color:white;font-size:12px;">
            🔴 Baseline: <b>{programme_drift}d</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="color:white;font-size:12px;">
            🟠 Float: <b>{high_risk}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="color:white;font-size:12px;">
            🟡 Critical: <b>{critical_deliverables}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )