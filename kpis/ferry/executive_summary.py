import streamlit as st

from utils.project_metrics import (
    get_current_snapshot,
    get_project_metrics
)


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

    if not insights:
        insights.append(
            "Programme performance remains stable."
        )

    return insights[:3]


def get_status(metrics):

    if metrics["health_score"] >= 80:
        return "ON TRACK"

    if metrics["health_score"] >= 60:
        return "WATCHLIST"

    return "AT RISK"


def render(cl32):

    current_df, _ = get_current_snapshot(
        cl32
    )

    metrics = get_project_metrics(
        current_df
    )

    readiness_index = metrics[
        "design_readiness"
    ]

    risk_status = get_status(
        metrics
    )

    insights = build_insights(
        metrics
    )

    title_col, status_col = st.columns(
        [4, 1]
    )

    with title_col:

        st.caption(
            "EXECUTIVE SUMMARY (AI GENERATED)"
        )

    with status_col:

        if risk_status == "ON TRACK":
            st.success(risk_status)

        elif risk_status == "AT RISK":
            st.error(risk_status)

        else:
            st.warning(risk_status)

    left, right = st.columns(
        [2, 3]
    )

    with left:

        st.metric(
            label="Design Readiness Index",
            value=f"{readiness_index}%"
        )

        st.caption(
            f"Health Score: {metrics['health_score']}"
        )

    with right:

        for insight in insights:
            st.write(f"✅ {insight}")
