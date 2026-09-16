import pandas as pd


def get_current_snapshot(cl32):

    if cl32.empty:
        return pd.DataFrame(), pd.Timestamp.today()

    latest_snapshot = cl32["SnapshotDate"].max()

    current_df = cl32[
        cl32["SnapshotDate"] == latest_snapshot
    ].copy()

    return current_df, latest_snapshot


def get_project_metrics(current_df):

    if current_df.empty:

        return {
            "baseline_finish": pd.Timestamp.today(),
            "forecast_finish": pd.Timestamp.today(),
            "programme_drift": 0,
            "critical_deliverables": 0,
            "high_risk": 0,
            "design_readiness": 0,
            "upcoming_submissions": 0,
            "health_score": 0,
        }

    # --------------------------------------------
    # CLEAN DATA
    # --------------------------------------------

    df = current_df.copy()

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
    )

    # --------------------------------------------
    # KEEP REAL ACTIVITIES ONLY
    # --------------------------------------------

    activities = df[
        df["Activity ID"]
        .astype(str)
        .str.startswith("FER-", na=False)
    ].copy()

    if activities.empty:
        activities = df.copy()

    # --------------------------------------------
    # DATES
    # --------------------------------------------

    activities["Finish"] = pd.to_datetime(
        activities["Finish"],
        errors="coerce"
    )

    activities["BL1 Finish"] = pd.to_datetime(
        activities["BL1 Finish"],
        errors="coerce"
    )

    # --------------------------------------------
    # FORECAST FINISH
    # --------------------------------------------

    forecast_finish = activities[
        "Finish"
    ].max()

    # --------------------------------------------
    # BASELINE FINISH
    # --------------------------------------------

    baseline_finish = activities[
        "BL1 Finish"
    ].max()

    if pd.isna(forecast_finish):
        forecast_finish = pd.Timestamp.today()

    if pd.isna(baseline_finish):
        baseline_finish = pd.Timestamp.today()

    programme_drift = (
        forecast_finish - baseline_finish
    ).days

    # --------------------------------------------
    # FLOAT
    # --------------------------------------------

    activities["Total Float"] = pd.to_numeric(
        activities["Total Float"],
        errors="coerce"
    )

    critical_deliverables = int(
        (
            activities["Total Float"] <= 5
        ).sum()
    )

    # --------------------------------------------
    # VARIANCE
    # --------------------------------------------

    activities[
        "Variance - BL1 Finish Date"
    ] = pd.to_numeric(
        activities[
            "Variance - BL1 Finish Date"
        ],
        errors="coerce"
    )

    high_risk = int(
        (
            (
                activities["Total Float"] <= 0
            )
            &
            (
                activities[
                    "Variance - BL1 Finish Date"
                ] < 0
            )
        ).sum()
    )

    # --------------------------------------------
    # DESIGN READINESS
    # --------------------------------------------

    activities[
        "Remaining Duration"
    ] = pd.to_numeric(
        activities["Remaining Duration"],
        errors="coerce"
    )

    total_activities = len(
        activities[
            "Remaining Duration"
        ].dropna()
    )

    completed_activities = int(
        (
            activities[
                "Remaining Duration"
            ] == 0
        ).sum()
    )

    if total_activities > 0:

        design_readiness = round(
            (
                completed_activities
                /
                total_activities
            ) * 100
        )

    else:

        design_readiness = 0

    # --------------------------------------------
    # UPCOMING SUBMISSIONS
    # --------------------------------------------

    today = pd.Timestamp.today()

    next_7_days = (
        today + pd.Timedelta(days=7)
    )

    submission_mask = (
        activities["Activity Name"]
        .astype(str)
        .str.contains(
            "Submission|Review",
            case=False,
            na=False
        )
    )

    upcoming_submissions = int(
        (
            submission_mask
            &
            activities["Finish"].between(
                today,
                next_7_days
            )
        ).sum()
    )

    # --------------------------------------------
    # HEALTH SCORE
    # --------------------------------------------

    health_score = round(

        (
            design_readiness * 0.40
        )

        +

        (
            max(
                0,
                100 - critical_deliverables
            ) * 0.20
        )

        +

        (
            max(
                0,
                100 - high_risk
            ) * 0.20
        )

        +

        (
            max(
                0,
                100 - abs(programme_drift)
            ) * 0.20
        )

    )

    health_score = max(
        0,
        min(
            health_score,
            100
        )
    )

    return {

        "baseline_finish":
            baseline_finish,

        "forecast_finish":
            forecast_finish,

        "programme_drift":
            programme_drift,

        "critical_deliverables":
            critical_deliverables,

        "high_risk":
            high_risk,

        "design_readiness":
            design_readiness,

        "upcoming_submissions":
            upcoming_submissions,

        "health_score":
            health_score,

        "activity_count":
            len(activities)

    }
