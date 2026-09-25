import streamlit as st


def get_metrics(cl32):

    st.write("Columns:")
    st.write(cl32.columns.tolist())

    st.write("Deliverables Area")

    deliverables_rows = cl32[
        cl32.astype(str)
        .apply(
            lambda x: x.str.contains(
                "Deliver",
                case=False,
                na=False
            )
        )
        .any(axis=1)
    ]

    st.dataframe(deliverables_rows)

    st.write("Sample Rows")

    st.dataframe(
        cl32.iloc[0:120]
    )

    return {
        "total_deliverables": 0
    }