import streamlit as st

def get_metrics(cl32):

    DELIVERABLE_NAMES = [
        "Outfall pipework optioneering",
        "Model Existing Tank",
        "Build Terrain Model",
        "BIM Set Up",
        "Civil Modelling - Tank",
        "Civil Modelling - Other Assets",
    ]

    names = (
        cl32["Activity Name"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    deliverables = names.apply(
        lambda x: any(
            d.lower() in x.lower()
            for d in DELIVERABLE_NAMES
        )
    )

    matched = cl32[deliverables]

    st.write("Matched Deliverables")
    st.dataframe(
        matched[
            ["Activity ID", "Activity Name"]
        ]
    )

    return {
        "total_deliverables": len(matched)
    }