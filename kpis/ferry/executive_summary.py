import streamlit as st
import plotly.graph_objects as go

from utils.project_metrics import (
    get_current_snapshot,
    get_project_metrics,
)


def get_status(metrics):

    score = metrics["health_score"]

    if score >= 80:
        return "ON TRACK"

    if score >= 60:
        return "WATCHLIST"

    return "AT RISK"


def build_insights(metrics):

    insights = []

    if metrics["programme_drift"] > 0:
        insights.append(
            f"Programme is behind baseline by "
            f"{metrics['programme_drift']} days."
        )

    if metrics["high_risk"] > 0:
        insights.append(
            f"{metrics['high_risk']} high-risk deliverables "
            f"require attention."
        )

    if metrics["critical_deliverables"] > 0:
        insights.append(
            f"{metrics['critical_deliverables']} critical deliverables "
            f"have low float."
        )

    if metrics["upcoming_submissions"] > 0:
        insights.append(
            f"{metrics['upcoming_submissions']} submissions are due "
            f"within the next 7 days."
        )

    if not insights:
        insights.append(
            "No significant delivery risks identified."
        )

    return insights[:3]


def get_trend(cl32):

    if cl32.empty:
        return 0

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

    current_metrics = get_project_metrics(current_df)
    previous_metrics = get_project_metrics(previous_df)

    return (
        current_metrics["health_score"]
        - previous_metrics["health_score"]
    )


def build_gauge(score):

    remaining = max(0, 100 - score)

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[score, remaining, 100],
            rotation=180,
            hole=0.72,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    "#FF6B00",
                    "#2D3C55",
                    "rgba(0,0,0,0)"
                ]
            ),
        )
    )

    fig.update_layout(
        height=180,
        margin=dict(
            l=0,
            r=0,
            t=10,
            b=0
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        annotations=[
            dict(
                text=f"<b>{score}%</b>",
                x=0.5,
                y=0.46,
                showarrow=False,
                font=dict(
                    size=28,
                    color="white"
                )
            )
        ]
    )

    return fig


def render(cl32):

    current_df, _ = get_current_snapshot(cl32)

    metrics = get_project_metrics(current_df)

    score = metrics["health_score"]

    readiness = metrics["design_readiness"]

    status = get_status(metrics)

    trend = get_trend(cl32)

    insights = build_insights(metrics)

    title_col, status_col = st.columns([4, 1])

    with title_col:

        st.caption(
            "EXECUTIVE SUMMARY (AI GENERATED)"
        )

    with status_col:

        if status == "AT RISK":
            st.error(status)

        elif status == "WATCHLIST":
            st.warning(status)

        else:
            st.success(status)

    left, right = st.columns([2, 3])

    with left:

        fig = build_gauge(score)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

        st.caption(
            "Design Readiness Index"
        )

        arrow = "↑" if trend >= 0 else "↓"

        colour = (
            "normal"
            if trend >= 0
            else "inverse"
        )

        st.metric(
            "",
            f"{readiness}%",
            delta=f"{