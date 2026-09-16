import pandas as pd


def get_current_snapshot(cl32):

    latest_snapshot = cl32["SnapshotDate"].max()

    current_df = cl32[
        cl32["SnapshotDate"] == latest_snapshot
    ].copy()

    return current_df, latest_snapshot


def get_project_metrics(current_df):

    current_df.columns = (
        current_df.columns
        .astype(str)
        .str.strip()
    )

    # -------------------------
    # Baseline
    # -------------------------

    milestone = current_df[
        current_df["Activity ID"]
        == "FER-PD-1030"
    ]

    baseline_finish = pd.to_datetime(
        milestone["BL1 Finish"].iloc[0],
        errors="coerce"
    )

    forecast_finish = pd.to_datetime(
        milestone["Finish"].iloc[0],
        errors="coerce"
    )

    programme_drift = (
        forecast_finish - baseline_finish
    ).days

    # -------------------------
    # Critical Deliverables
    # -------------------------

    float_col = pd.to_numeric(
        current_df["Total Float"],
        errors="coerce"
    )

    critical_deliverables = len(
        current_df[float_col <= 10]
    )

    # -------------------------
    # High Risk
    # -------------------------

    variance_col = pd.to_numeric(
        current_df[
            "Variance - BL1 Finish Date"
        ],
        errors="coerce"
    )

    high_risk = len(
        current_df[
            (float_col <= 5)
            &
            (variance_col < 0)
        ]
    )

    # -------------------------
    # Design Readiness
    # -------------------------

    remaining = pd.to_numeric(
        current_df["Remaining Duration"],
        errors="coerce"
    )

    complete = len(
        remaining[remaining == 0]
    )

    total = len(
        remaining.dropna()
    )

    design_readiness = round(
        complete / total * 100
    ) if total else 0

    # -------------------------
    # Upcoming Submissions
    # -------------------------

    finish_dates = pd.to_datetime(
        current_df["Finish"],
        errors="coerce"
    )

    activities = (
        current_df["Activity Name"]
        .astype(str)
        .fillna("")
    )

    today = pd.Timestamp.today()

    next_7 = today + pd.Timedelta(days=7)

    upcoming_submissions = len(
        current_df[
            activities.str.contains(
                "Submission|Review",
                case=False,
                na=False
            )
            &
            finish_dates.between(
                today,
                next_7
            )
        ]
    )

    # -------------------------
    # Health Score
    # -------------------------

    health_score = max(
        0,
        min(
            100,
            round(
                (
                    design_readiness * 0.4
                )
                +
                (
                    max(
                        0,
                        (100 - critical_deliverables)
                    ) * 0.2
                )
                +
                (
                    max(
                        0,
                        (100 - high_risk)
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