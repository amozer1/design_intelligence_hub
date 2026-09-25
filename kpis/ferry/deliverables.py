import streamlit as st

from kpis.ferry.deliverables_utils import (
    get_metrics,
)

from kpis.ferry.deliverables_styles import (
    ICON_PURPLE,
    BLUE,
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

        icon_col, value_col = st.columns([1, 4])

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
                    color:#111827;
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

        # ===================================
        # FOOTER
        # ===================================

        footer_col, badge_col = st.columns([3, 2])

        with footer_col:

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

        with badge_col:

            st.markdown(
                f"""
                <div style="
                    background:{BLUE};
                    color:white;
                    text-align:center;
                    border-radius:8px;
                    padding:8px 12px;
                    font-size:11px;
                    font-weight:700;
                ">
                    LIVE
                </div>
                """,
                unsafe_allow_html=True,
            )