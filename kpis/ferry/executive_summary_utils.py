from utils.project_metrics import (
    get_current_snapshot,
    get_project_metrics,
)


def get_status(score):

    if score >= 80:
        return "ON TRACK"

    if score >= 60:
        return "WATCHLIST"

    return "AT RISK"


def get_metrics(cl32):

    current_df, _ = get_current_snapshot(
        cl32
    )

    metrics = get_project_metrics(
        current_df
    )

    return {
        "score": metrics["health_score"],
        "readiness": metrics["design_readiness"],
        "programme_drift": metrics["programme_drift"],
        "high_risk": metrics["high_risk"],
        "critical_deliverables": metrics["critical_deliverables"],
    }