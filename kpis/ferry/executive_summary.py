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


def build_insights(metrics):

    insights = []

    if metrics["programme_drift"] > 0:
        insights.append(
            f"Programme is behind baseline by "
            f"{metrics['programme_drift']} days."
        )

    if metrics["high_risk"] > 0:
        insights.append(
            f"{metrics['high_risk']} high-risk deliverables require attention."
        )

    if metrics["critical_deliverables"] > 0:
        insights.append(
            f"{metrics['critical_deliverables']} critical deliverables have low float."
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
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    "#FF6A00",
                    "#324760",
                    "rgba(0,0,0,0)"
                ]
            )
        )
    )

    fig.update_layout(
        height=130,
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0,
        ),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        annotations=[
            dict(
                text=f"<b>{score}%</b>",
                x=0.5,
                y=0.40,
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

    current_df, _ = get_current_snapshot(cl32)

    metrics = get_project_metrics(current_df)

    health_score = metrics["health_score"]

    design_readiness = metrics["design_readiness"]

    status = get_status(health_score)

    insights = build_insights(metrics)

    with st.container(border=True):

        title_col, status_col = st.columns([4, 1])

        with title_col:
            st.subheader("Executive Summary")

        with status_col:

            if status == "AT RISK":
                st.error(status)

            elif status == "WATCHLIST":
                st.warning(status)

            else:
                st.success(status)

        st.plotly_chart(
            build_gauge(health_score),
            use_container_width=True,
            config={
                "displayModeBar": False
            },
        )

        st.metric(
            "Design Readiness Index",
            f"{design_readiness}%"
        )

        st.divider()

        for insight in insights:
            st.write(f"✅ {insight}")