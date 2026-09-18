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

    if not insights:
        insights.append(
            "No significant delivery risks identified."
        )

    return insights[:3]


def build_gauge(score):

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[score, 100 - score, 100],
            hole=0.80,
            rotation=180,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    "#FF6A00",
                    "#2D3B52",
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
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        annotations=[
            dict(
                text=f"<b>{score}%</b>",
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

    status = get_status(health_score)

    insights = build_insights(metrics)

    header_left, header_right = st.columns([4, 1])

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

    fig = build_gauge(health_score)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )

    st.markdown(
        "<div style='text-align:center;color:white;font-weight:600;'>"
        "Design Readiness Index"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div style='text-align:center;"
        f"color:#A8D1FF;"
        f"font-size:18px;"
        f"font-weight:700;'>"
        f"{design_readiness}%"
        f"</div>",
        unsafe_allow_html=True
    )

    st.divider()

    for insight in insights:
        st.write(f"✅ {insight}")