import streamlit as st

def get_metrics(cl32):

    ids = (
        cl32["Activity ID"]
        .fillna("")
        .astype(str)
    )

    st.write(
        ids[
            ~ids.str.startswith("FER-", na=False)
            & (ids != "")
        ].tolist()
    )

    return {
        "total_deliverables": 0
    }
``