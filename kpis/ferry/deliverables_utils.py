def get_metrics(cl32):

    ids = (
        cl32["Activity ID"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    deliverables = cl32[
        ids.str.startswith(
            "JMS",
            na=False
        )
    ]

    total_deliverables = len(
        deliverables
    )

    return {
        "total_deliverables": total_deliverables,
    }