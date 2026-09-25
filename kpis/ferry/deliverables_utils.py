def get_metrics(cl32):

    ids = (
        cl32["Activity ID"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    names = (
        cl32["Activity Name"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    deliverables = cl32[
        (ids != "")
        & (~ids.str.startswith("FER-"))
        & (names != "")
    ]

    return {
        "total_deliverables": len(deliverables)
    }