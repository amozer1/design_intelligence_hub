import streamlit as st

from kpis.ferry.deliverables_utils import (
    get_metrics,
)

from kpis.ferry.deliverables_styles import (
    TITLE,
    MUTED,
    ICON_PURPLE,
)


def render(cl32):

    metrics = get_metrics(cl32)

    total_deliverables = (
        metrics["total_deliverables"]
    )

    with st.container(border=True):

        # ===================================
        # HEADER
        # ===================================

        st.markdown(
            """
            <div style="
                color:#111827;
                font-size:16px;
                font-weight:700;
                margin-bottom:22px;
            ">
                TOTAL DELIVERABLES
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ===================================
        # KPI
        # ===================================

        icon_col, value_col = st.columns([1, 5])

        with icon_col:

            st.markdown(
                f"""
                <div style="
                    color:{ICON_PURPLE};
                    font-size:32px;
                    margin-top:8px;
                ">
                    📄
                </div>
                """,
                unsafe_allow_html=True,
            )

        with value_col:

            st.markdown(
                f"""
                <div style="
                    color:{TITLE};
                    font-size:42px;
                    font-weight:700;
                    line-height:1;
                ">
                    {total_deliverables}
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.write("")
        st.write("")

        st.markdown(
            f"""
            <div style="
                color:{MUTED};
                font-size:11px;
            ">
                Current CL32 Deliverables
            </div>
            """,
            unsafe_allow_html=True,
        )