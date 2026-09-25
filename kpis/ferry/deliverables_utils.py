import streamlit as st


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

    start_idx = ids[
        ids == "Deliverables"
    ].index

    if len(start_idx) == 0:

        st.error(
            "Deliverables section not found"
        )

        return {
            "total_deliverables": 0
        }

    start = start_idx[0]

    end_idx = ids[
        ids == "Retired Activities"
    ].index

    end = (
        end_idx[0]
        if len(end_idx)
        else len(cl32)
    )

    section = cl32.iloc[start:end].copy()

    st.write("Deliverables Section")

    st.dataframe(
        section[
            ["Activity ID", "Activity Name"]
        ]
    )

    section_ids = (
        section["Activity ID"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    deliverables = section[
        (section_ids != "")
        & (~section_ids.str.startswith("FER-", na=False))
        & (section_ids != "Deliverables")
        & (section_ids != "Retired Activities")
    ]

    st.write(
        "Rows Being Counted"
    )

    st.dataframe(
        deliverables[
            ["Activity ID", "Activity Name"]
        ]
    )

    st.write(
        "Count:",
        len(deliverables)
    )

    return {
        "total_deliverables": len(
            deliverables
        )
    }