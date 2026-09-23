from utils.project_metrics import (
    get_current_snapshot,
    get_project_metrics,
)


def get_metrics(cl32):

    current_df, _ = get_current_snapshot(cl32)

    return get_project_metrics(current_df)


def get_status(score):

    if score >= 80:
        return "ON TRACK"

    if score >= 60:
        return "WATCHLIST"

    return "AT RISK"
