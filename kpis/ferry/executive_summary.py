import streamlit as st

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
            f"Programme is behind baseline by {metrics['programme_drift']} days."
        )

    if metrics["high_risk"] > 0:
        insights.append(
            f"{metrics['high_risk']} high-risk deliverables require attention."
        )

    if metrics["critical_deliverables"] > 0:
        insights.append(
            f"{metrics['critical_deliverables']} critical deliverables have low float."
        )

    if len(insights) == 0:
        insights.append(
            "No significant delivery risks identified."
        )

    return insights[:3]


def render(cl32):

    current_df, _ = get_current_snapshot(cl32)

    metrics = get_project_metrics(current_df)

    readiness = metrics["design_readiness"]

    health_score = metrics["health_score"]

    status = get_status(metrics)

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

        st.metric(
            "Design Readiness Index",
            f"{readiness}%"
        )

        st.metric(
            "Health Score",
            health_score
        )

    with right:

        for insight in insights:
            st.write(f"✅ {insight}")