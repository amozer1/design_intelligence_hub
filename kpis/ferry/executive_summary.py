import streamlit as st
import plotly.graph_objects as go

from utils.project_metrics import (
    get_current_snapshot,
    get_project_metrics,
)


def get_status(score):

    if score >= 80:
        return "🟢 ON TRACK"

    if score >= 60:
        return "🟡 WATCHLIST"

    return "🔴 AT RISK"


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
            f"Forecast finish exceeds baseline by "
            f"{metrics['programme_drift']} days."
        )

    if metrics["high_risk"] > 0:
        insights.append(
            f"{metrics['high_risk']} activities have negative float exposure."
        )

    if metrics["critical_deliverables"] > 0:
        insights.append(
            f"{metrics['critical_deliverables']} deliverables have ≤5 days float."
        )

    if metrics["upcoming_submissions"] > 0:
        insights.append(
            f"{metrics['upcoming_submissions']} submissions due within 7 days."
        )

    if not insights:
        insights.append(
            "No significant delivery risks identified."
        )

    return insights[:3]


def build_gauge(score):

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[
                score,
                100 - score,
                100,
            ],
            hole=0.82,
            rotation=180,
            direction="clockwise",
            sort=False,
            textinfo="none",
            marker=dict(
                colors=[
                    "#FF6A00",
                    "#34495E",
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
                    size=24,
                    color="white"
                )
            )
        ]
    )

    return fig


def render(cl32):

    current_df, _ = get_current_snapshot(
        cl32
    )

    metrics = get_project_metrics(
        current_df
    )

    health_score = metrics["health_score"]

    design_readiness = metrics[
        "design_readiness"
    ]

    trend = get_trend(cl32)

    status = get_status(
        health_score
    )

    insights = build_insights(
        metrics
    )

    with st.container(border=True):

        left_header, right_header = st.columns(
            [4, 1]
        )

        with left_header:
            st.caption(
                "EXECUTIVE SUMMARY (AI GENERATED)"
            )

        with right_header:
            st.write(status)

        gauge_col, insight_col = st.columns(
            [2, 3]
        )

        with gauge_col:

            st.plotly_chart(
                build_gauge(
                    health_score
                ),
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )

            st.caption(
                "Design Readiness Index"
            )

            st.metric(
                label="",
                value=f"{design_readiness}%",
                delta=f"{trend:+.0f}% vs last snapshot"
            )

        with insight_col:

            for insight in insights:
                st.write(
                    f"✅ {insight}"
                )
