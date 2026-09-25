def get_metrics(cl32):

    ids = (
        cl32["Activity ID"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    start_idx = ids[ids == "Deliverables"].index

    if len(start_idx) == 0:
        return {
            "total_deliverables": 0
        }

    start = start_idx[0]

    end_idx = ids[ids == "Retired Activities"].index

    end = (
        end_idx[0]
        if len(end_idx)
        else len(cl32)
    )

    section = cl32.iloc[start + 1:end]

    section_ids = (
        section["Activity ID"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    deliverable_count = 0

    rows = section_ids.tolist()

    for i, current in enumerate(rows):

        if (
            current
            and not current.startswith("FER-")
        ):

            next_row = (
                rows[i + 1]
                if i < len(rows) - 1
                else ""
            )

            if next_row.startswith("FER-"):
                deliverable_count += 1

    return {
        "total_deliverables": deliverable_count
    }