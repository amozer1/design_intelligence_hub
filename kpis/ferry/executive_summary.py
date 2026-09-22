import streamlit as st
import plotly.graph_objects as go

from utils.project_metrics import (
    get_current_snapshot,
    get_project_metrics,
)


CARD_BG = "#062B5B"
CARD_BORDER = "#0EA5E9"


def get_status(score):

    if score >= 80:
        return "ON TRACK"

    if score >= 60:
        return "WATCHLIST"

    return "AT RISK"


def get_trend(cl32):

    snapshots = sorted(
        cl32["SnapshotDate"].dropna().unique()
    )

    if len(snapshots) < 2:
        return 0

    current_df = cl32[
        cl32["SnapshotDate"] == snapshots[-1]
    ]

    previous_df = cl32[
        cl32["SnapshotDate"] == snapshots[-2]
    ]

    current_metrics = get_project_metrics(
        current_df
    )

    previous_metrics = get_project_metrics(
        previous_df
    )

    return (
        current_metrics["health_score"]
        - previous_metrics["health_score"]
    )


def build_insights(metrics):

    insights = []

    if metrics["programme_drift"] > 0:
        insights.append(
            f"{metrics['programme_drift']} days behind baseline"
        )

    if metrics["high_risk"] > 0:
        insights.append(
            f"{metrics['high_risk']} activities with negative float"
        )

    if metrics["critical_deliverables"] > 0:
        insights.append(
            f"{metrics['critical_deliverables']} deliverables ≤5d float"
        )

    if not insights:
        insights.append(
            "No material delivery risks identified"
        )

    return insights[:3]


def build_gauge(score):

    if score >= 80:
        colour = "#22C55E"

    elif score >= 60:
        colour = "#F59E0B"

    else:
        colour = "#FF3131"

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
                    "#94A3B8",
                    "rgba(0,0,0,0)"
                ]
            )
        )
    )

    fig.update_layout(
        height=190,
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
                    size=40,
                    color="white"
                )
            )
        ]
    )

    return fig


def render(cl32):

    current_df, _ = get_current_snapshot(cl32)

    metrics = get_project_metrics(
        current_df
    )

    score = metrics["health_score"]

    readiness = metrics["design_readiness"]

    trend = get_trend(cl32)

    status = get_status(score)

    insights = build_insights(metrics)

    # CARD HEADER
    st.markdown(
        f"""
        <div style="
            background:{CARD_BG};
            border:2px solid {CARD_BORDER};
            border-bottom:none;
            border-radius:18px 18px 0 0;
            padding:18px 18px 8px 18px;
        ">
            <div style="
                color:#DDEAFF;
                font-size:12px;
                font-weight:600;
                letter-spacing:0.5px;
            ">
                EXECUTIVE SUMMARY (AI GENERATED)
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # BODY
    with st.container(border=True):

        if status == "AT RISK":
            badge_colour = "#E0005A"

        elif status == "WATCHLIST":
            badge_colour = "#D89A00"

        else:
            badge_colour = "#00B15D"

        st.markdown(
            f"""
            <div style="
                display:inline-block;
                background:{badge_colour};
                color:white;
                padding:6px 12px;
                border-radius:8px;
                font-size:12px;
                font-weight:700;
                margin-bottom:12px;
            ">
                {status}
            </div>
            """,
            unsafe_allow_html=True
        )

        gauge_col, insight_col = st.columns(
            [1.4, 2.6]
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
                "<br>",
                unsafe_allow_html=True
            )

            for insight in insights:

                st.markdown(
                    f"""
                    <div style="
                        color:white;
                        font-size:16px;
                        font-weight:700;
                        margin-bottom:16px;
                    ">