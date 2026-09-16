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

    # Clean columns

    current_df.columns = (
        current_df.columns
        .astype(str)
        .str.strip()
    )

    # ----------------------------
    # Find project completion line
    # ----------------------------

    milestone = current_df[
        current_df["Activity ID"]
        .astype(str)
        .str.strip()
        == "FER-PD-1030"
    ]

    if not milestone.empty:

        baseline_finish = pd.to_datetime(
            milestone["BL1 Finish"].iloc[0],
            errors="coerce"
        )

        forecast_finish = pd.to_datetime(
            milestone["Finish"].iloc[0],
            errors="coerce"
        )

    else:

        baseline_finish = pd.Timestamp.today()

        forecast_finish = pd.Timestamp.today()

    # ----------------------------
    # Drift
    # ----------------------------

    if (
        pd.notna(baseline_finish)
        and
        pd.notna(forecast_finish)
    ):

        programme_drift = (
            forecast_finish -
            baseline_finish
        ).days

    else:

        programme_drift = 0

    # ----------------------------
    # Critical Deliverables
    # ----------------------------

    total_float = pd.to_numeric(
        current_df["Total Float"],
        errors="coerce"
    )

    critical_deliverables = int(
        (total_float <= 10).sum()
    )

    # ----------------------------
    # High Risk
    # ----------------------------

    variance = pd.to_numeric(
        current_df[
            "Variance - BL1 Finish Date"
        ],
        errors="coerce"
    )

    high_risk = int(
        (
            (total_float <= 5)
            &
            (variance < 0)
        ).sum()
    )

    # ----------------------------
    # Design Readiness
    # ----------------------------

    remaining = pd.to_numeric(
        current_df["Remaining Duration"],
        errors="coerce"
    )

    total_activities = len(
        remaining.dropna()
    )

    completed = int(
        (remaining == 0).sum()
    )

    if total_activities > 0:

        design_readiness = round(
            completed /
            total_activities *
            100
        )

    else:

        design_readiness = 0

    # ----------------------------
    # Upcoming Submissions
    # ----------------------------

    today = pd.Timestamp.today()

    next_week = today + pd.Timedelta(days=7)

    finish = pd.to_datetime(
        current_df["Finish"],
        errors="coerce"
    )

    activities = (
        current_df["Activity Name"]
        .astype(str)
        .fillna("")
    )

    upcoming_submissions = int(
        (
            activities.str.contains(
                "Submission|Review",
                case=False,
                na=False
            )
            &
            finish.between(
                today,
                next_week
            )
        ).sum()
    )

    # ----------------------------
    # Health Score
    # ----------------------------

    health_score = round(
        (
            design_readiness * 0.4
        )
        +
        (
            max(
                0,
                100 - critical_deliverables
            ) * 0.2
        )
        +
        (
            max(
                0,
                100 - high_risk
            ) * 0.2
        )
        +
        (
            max(
                0,
                100 - abs(programme_drift)
            ) * 0.2
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
    }