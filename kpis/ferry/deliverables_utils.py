import pandas as pd


def get_metrics(cl32):

    ids = (
        cl32["Activity ID"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    deliverables = cl32[
        (ids != "")
        & (~ids.str.startswith("FER-"))
    ]

    total_deliverables = len(deliverables)

    return {
        "total_deliverables": total_deliverables,
    }