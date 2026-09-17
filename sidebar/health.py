import pandas as pd
import streamlit as st


def calculate_health_metrics(cl32):

    if cl32.empty:
        return {
            "health_score": 0,
            "design_readiness": 0,
            "critical_deliverables": 0,
            "high_risk": 0,
            "upcoming_submissions": 0,
        }

    latest_date = cl32["SnapshotDate"].max()

    df = cl32[
        cl32["SnapshotDate"] == latest_date
    ].copy()

    numeric_cols = [
        "Activity % Complete",
        "Variance - BL1 Finish Date",
        "Total Float",
        "Remaining Duration"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    if "Finish" in df.columns:
        df["Finish"] = pd.to_datetime(
            df["Finish"],
            dayfirst=True,
            errors="coerce"
        )

    activities = df[
        df["Activity ID"]
        .astype(str)
        .str.contains("-", na=False)
    ].copy()

    design_readiness = round(
        activities["Activity % Complete"]
        .fillna(0)
        .mean(),
        0
    )

    critical_deliverables = len(
        activities[
            (activities["Total Float"] <= 0)
            &
            (activities["Activity % Complete"] < 100)
        ]
    )

    high_risk = len(
        activities[
            activities[
                "Variance - BL1 Finish Date"
            ] <= -14
        ]
    )

    today = pd.Timestamp.today()

    upcoming_submissions = len(
        activities[
            activities["Activity Name"]
            .astype(str)
            .str.contains(
                "submission|review|freeze",
                case=False,
                na=False
            )
            &
            (activities["Finish"] >= today)
            &
            (activities["Finish"] <= today + pd.Timedelta(days=30))
        ]
    )

    health_score = (
        0.60 * design_readiness
        + 0.20 * max(0, 100 - high_risk * 5)
        + 0.20 * max(0, 100 - critical_deliverables * 2)
    )

    health_score = round(
        max(0, min(100, health_score))
    )

    return {
        "health_score": int(health_score),
        "design_readiness": int(design_readiness),
        "critical_deliverables": int(critical_deliverables),
        "high_risk": int(high_risk),
        "upcoming_submissions": int(upcoming_submissions),
    }


def render_health(metrics):

    st.markdown("### PROJECT HEALTH")

    st.metric(
        "Health Score",
        metrics["health_score"]
    )

    st.metric(
        "Design Readiness",
        f"{metrics['design_readiness']}%"
    )

    st.metric(
        "Critical Deliverables",
        metrics["critical_deliverables"]
    )

    st.metric(
        "High Risk Activities",
        metrics["high_risk"]
    )

    st.metric(
        "Upcoming Submissions",
        metrics["upcoming_submissions"]
    )