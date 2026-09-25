def get_metrics(cl32):

    activity_ids = (
        cl32["Activity ID"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    # Find Deliverables section
    deliverables_idx = activity_ids[
        activity_ids == "Deliverables"
    ].index

    if len(deliverables_idx) == 0:
        return {
            "total_deliverables": 0
        }

    start_idx = deliverables_idx[0]

    # Stop at Retired Activities
    retired_idx = activity_ids[
        activity_ids == "Retired Activities"
    ].index

    end_idx = (
        retired_idx[0]
        if len(retired_idx)
        else len(cl32)
    )

    deliverables_section = cl32.iloc[
        start_idx + 1:end_idx
    ]

    section_ids = (
        deliverables_section["Activity ID"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    # Deliverable packages:
    # - Not FER activities
    # - Not blank
    deliverables = deliverables_section[
        (section_ids != "")
        & (~section_ids.str.startswith("FER-", na=False))
    ]

    return {
        "total_deliverables": len(
            deliverables
        )
    }