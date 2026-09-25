def get_metrics(cl32):

    activity_ids = (
        cl32["Activity ID"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    # Find Deliverables section
    start_idx = activity_ids[
        activity_ids == "Deliverables"
    ].index

    if len(start_idx) == 0:
        return {
            "total_deliverables": 0
        }

    start = start_idx[0]

    # Stop at Retired Activities
    end_idx = activity_ids[
        activity_ids == "Retired Activities"
    ].index

    end = (
        end_idx[0]
        if len(end_idx)
        else len(cl32)
    )

    section = cl32.iloc[start + 1:end]

    ids = (
        section["Activity ID"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    deliverable_count = 0

    for value in ids:

        if (
            value
            and value != "Deliverables"
            and not value.startswith("FER-")
            and value not in {
                "Civils Design",
                "Mechanical Design",
                "Process Design",
                "Client Review",
                "Geotechnical",
                "Detailed Shaft Design",
                "New Manholes",
                "Rising Mains",
                "Instrumentation & Control",
                "Storm Tank Air Vent",
                "Ducting/Cable Troughs",
                "Documents",
                "Drawings",
                "EICA Design",
                "Client Review & Design Assurance",
            }
        ):
            deliverable_count += 1

    return {
        "total_deliverables": deliverable_count
    }