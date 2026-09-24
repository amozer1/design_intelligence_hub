import pandas as pd


DATE_FMT = "%d %b %Y"


def fmt_date(value):

    if pd.isna(value):
        return "N/A"

    return pd.to_datetime(value).strftime(
        DATE_FMT
    )


def get_metrics(cl32):

    latest_snapshot = (
        cl32["SnapshotDate"].max()
    )

    latest = cl32[
        cl32["SnapshotDate"] == latest_snapshot
    ]

    programme_row = latest[
        latest["Activity Name"]
        .astype(str)
        .str.contains(
            "Planned Project Completion",
            case=False,
            na=False
        )
    ]

    contract_row = latest[
        latest["Activity Name"]
        .astype(str)
        .str.contains(
            "Contract Completion",
            case=False,
            na=False
        )
    ]

    programme_finish = (
        fmt_date(
            programme_row.iloc[0]["Finish"]
        )
        if not programme_row.empty
        else "N/A"
    )

    programme_baseline = (
        fmt_date(
            programme_row.iloc[0]["BL1 Finish"]
        )
        if not programme_row.empty
        else "N/A"
    )

    programme_variance = (
        int(
            programme_row.iloc[0][
                "Variance - BL1 Finish Date"
            ]
        )
        if not programme_row.empty
        else 0
    )

    contract_finish = (
        fmt_date(
            contract_row.iloc[0]["Finish"]
        )
        if not contract_row.empty
        else "N/A"
    )

    contract_baseline = (
        fmt_date(
            contract_row.iloc[0]["BL1 Finish"]
        )
        if not contract_row.empty
        else "N/A"
    )

    contract_variance = (
        int(
            contract_row.iloc[0][
                "Variance - BL1 Finish Date"
            ]
        )
        if not contract_row.empty
        else 0
    )

    return {
        "programme_finish": programme_finish,
        "programme_baseline": programme_baseline,
        "programme_variance": programme_variance,
        "contract_finish": contract_finish,
        "contract_baseline": contract_baseline,
        "contract_variance": contract_variance,
    }