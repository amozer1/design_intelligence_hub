import streamlit as st
import plotly.graph_objects as go

from utils.project_metrics import (
    get_current_snapshot,
    get_project_metrics,
)


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
            f"Programme is behind baseline by "
            f"{metrics['programme_drift']} days."
        )

    if metrics["high_risk"] > 0:
        insights.append(
            f"{metrics['high_risk']} activities have negative float."
        )

    if metrics["critical_deliverables"] > 0:
        insights.append(
            f"{metrics['critical_deliverables']} deliverables have ≤5d float."
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
                100
            ],
            hole=0.78,
            rotation=180,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    "#FF5A1F",
                    "#50627D",
                    "rgba(0,0,0,0)"
                ]
            )
        )
    )

    fig.update_layout(
        height=180,
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
                    size=34,
                    color="white"
                )
            )
        ]
    )

    return fig


def render(cl32):

    current_df, _ = get_current_snapshot(cl32)

    metrics = get_project_metrics(current_df)

    health_score = metrics["health_score"]

    design_readiness = metrics["design_readiness"]

    trend = get_trend(cl32)

    status = get_status(health_score)

    insights = build_insights(metrics)

    header_left, header_right = st.columns(
        [4, 1]
    )

    with header_left:

        st.caption(
            "EXECUTIVE SUMMARY (AI GENERATED)"
        )

    with header_right:

        if status == "AT RISK":
            st.error(status)

        elif status == "WATCHLIST":
            st.warning(status)

        else:
            st.success(status)

    gauge_col, insight_col = st.columns(
        [2, 3]
    )

    with gauge_col:

        st.plotly_chart(
            build_gauge(health_score),
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

        st.caption(
            "Design Readiness Index"
        )

        arrow = "↑" if trend >= 0 else "↓"

        colour = "normal" if trend >= 0 else "inverse"

        st.metric(
            label="",
            value=f"{design_readiness}%",
            delta=f"{arrow} {abs(trend)} vs last snapshot",
            delta_color=colour
        )

    with insight_col:

        st.write("")

        for insight in insights:
            st.write(
                f"✅ {insight}"
            )