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

        st.markdown(
            """
            <div style="
                min-height:145px;
            ">
            """,
            unsafe_allow_html=True,
        )

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

        icon_col, value_col = st.columns(
            [1, 4]
        )

        with icon_col:

            st.markdown(
                f"""
                <div style="
                    color:{ICON_PURPLE};
                    font-size:30px;
                    margin-top:6px;
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
                    color:#111827;
                    font-size:40px;
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
        st.write("")

        st.markdown(
            """
            <div style="
                color:#6B7280;
                font-size:11px;
            ">
                Current CL32 Deliverables
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            </div>
            """,
            unsafe_allow_html=True,
        )