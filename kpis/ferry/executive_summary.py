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

    if metrics["upcoming_submissions"] > 0:
        insights.append(
            f"{metrics['upcoming_submissions']} submissions are due in the next 7 days."
        )

    if not insights:
        insights.append(
            "No significant delivery risks identified."
        )

    return insights[:3]


def render(cl32):

    current_df, _ = get_current_snapshot(cl32)

    metrics = get_project_metrics(current_df)

    status = get_status(metrics)

    insights = build_insights(metrics)

    st.markdown("#### Executive Summary")

    if status == "AT RISK":
        st.error(status)

    elif status == "WATCHLIST":
        st.warning(status)

    else:
        st.success(status)

    st.metric(
        "Design Readiness Index",
        f"{metrics['design_readiness']}%"
    )

    st.metric(
        "Health Score",
        metrics["health_score"]
    )

    st.divider()

    for insight in insights:
        st.write(f"✅ {insight}")