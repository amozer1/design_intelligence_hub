import pandas as pd


def calculate_health_metrics(cl32):

    if cl32.empty:
        return {
            "health_score": 0,
            "design_readiness": 0,
            "critical_deliverables": 0,
            "high_risk": 0,
            "upcoming_submissions": 0
        }

    df = cl32.copy()

    # Numeric conversions
    for col in [
        "Activity % Complete",
        "Total Float",
        "Variance - BL1 Finish Date"
    ]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Dates
    if "Finish" in df.columns:
        df["Finish"] = pd.to_datetime(
            df["Finish"],
            dayfirst=True,
            errors="coerce"
        )

    # Activities only
    activities = df[
        df["Activity ID"].astype(str).str.contains("-", na=False)
    ].copy()

    # Design Readiness
    design_readiness = round(
        activities["Activity % Complete"].fillna(0).mean(),
        0
    )

    # Critical Deliverables
    critical_deliverables = len(
        activities[
            (activities["Total Float"] <= 0)
            & (activities["Activity % Complete"] < 100)
        ]
    )

    # High Risk
    high_risk = len(
        activities[
            activities["Variance - BL1 Finish Date"] <= -14
        ]
    )

    # Upcoming Submissions
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

    # Health Score
    score = (
        design_readiness
        - (critical_deliverables * 1.5)
        - (high_risk * 2)
    )

    health_score = max(
        0,
        min(100, round(score))
    )

    return {
        "health_score": health_score,
        "design_readiness": design_readiness,
        "critical_deliverables": critical_deliverables,
        "high_risk": high_risk,
        "upcoming_submissions": upcoming_submissions
    }