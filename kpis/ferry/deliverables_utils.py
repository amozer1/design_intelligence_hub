def get_metrics(cl32):

    ids = (
        cl32["Activity ID"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    deliverables = ids.str.startswith(
        "FER-",
        na=False
    )

    total_deliverables = int(
        deliverables.sum()
    )

    return {
        "total_deliverables": total_deliverables,
    }