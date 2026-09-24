import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


CARD_BG = "#1E3A5F"
BORDER = "#3B82F6"


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
            hole=0.78,
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
                    size=22,
                    color="#FFFFFF"
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

    badge_colour = "#DC2626"

    if "TRACK" in str(status).upper():
        badge_colour = "#16A34A"

    elif "WATCH" in str(status).upper():
        badge_colour = "#CA8A04"

    st.markdown(
        f"""
        <div style="
            background:{CARD_BG};
            border:3px solid {BORDER};
            border-radius:12px;
            padding:12px;
        ">
        </div>
        """,
        unsafe_allow_html=True
    )

    title_col, badge_col = st.columns([4, 1])

    with title_col:

        st.markdown(
            """
            <div style="
                color:#FFFFFF;
                font-size:16px;
                font-weight:700;
            ">
            EXECUTIVE SUMMARY
            </div>
            """,
            unsafe_allow_html=True
        )

    with badge_col:

        st.markdown(
            f"""
            <div style="
                background:{badge_colour};
                color:white;
                text-align:center;
                padding:4px;
                border-radius:6px;
                font-size:10px;
                font-weight:700;
            ">
            {status}
            </div>
            """,
            unsafe_allow_html=True
        )

    gauge_col, insight_col = st.columns([1, 1.6])

    with gauge_col:

        st.plotly_chart(
            build_gauge(score),
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

        st.markdown(
            """
            <div style="
                color:#CBD5E1;
                font-size:11px;
            ">
            READINESS
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                color:#FFFFFF;
                font-size:24px;
                font-weight:700;
            ">
            {readiness}%
            </div>
            """,
            unsafe_allow_html=True
        )

    with insight_col:

        st.markdown(
            f"""
            <div style="
                color:#F8FAFC;
                font-size:13px;
                font-weight:600;
            ">
            🔴 Baseline: {programme_drift}d
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                color:#F8FAFC;
                font-size:13px;
                font-weight:600;
                margin-top:8px;
            ">
            🟠 Float: {high_risk}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                color:#F8FAFC;
                font-size:13px;
                font-weight:600;
                margin-top:8px;
            ">
            🟡 Critical: {critical_deliverables}
            </div>
            """,
            unsafe_allow_html=True
        )