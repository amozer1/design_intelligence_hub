import streamlit as st

from kpis.ferry.deliverables_utils import (
    get_metrics,
)

from kpis.ferry.deliverables_styles import (
    ICON_PURPLE,
)


def render(cl32):

    metrics = get_metrics(cl32)

    total_deliverables = (
        metrics["total_deliverables"]
    )

    with st.container(border=True):

        st.subheader(
            "TOTAL DELIVERABLES"
        )

        icon_col, value_col = st.columns(
            [1, 3]
        )

        with icon_col:
            st.markdown("### 📄")

        with value_col:
            st.markdown(
                f"# {total_deliverables}"
            )

        # Add padding to align with Programme card
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        st.caption(
            "Current CL32 Deliverables"
        )