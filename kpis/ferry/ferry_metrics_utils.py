import pandas as pd


def get_latest_snapshot(cl32):

    snapshot = cl32["SnapshotDate"].max()

    return cl32[
        cl32["SnapshotDate"] == snapshot
    ]


def get_previous_snapshot(cl32):

    snapshots = sorted(
        cl32["SnapshotDate"].dropna().unique()
    )

    if len(snapshots) < 2:
        return pd.DataFrame()

    return cl32[
        cl32["SnapshotDate"] == snapshots[-2]
    ]