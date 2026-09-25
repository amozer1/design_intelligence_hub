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
                height: 178px;
                display: flex;
                flex-direction: column;
            ">
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div style="
                color:#111827;
                font-size:16px;
                font-weight:700;
                margin-bottom:20px;
            ">
                TOTAL DELIVERABLES
            </div>
            """,
            unsafe_allow_html=True,
        )

        icon_col, value_col = st.columns([1, 3])

        with icon_col:

            st.markdown(
                f"""
                <div style="
                    color:{ICON_PURPLE};
                    font-size:28px;
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
                    font-size:38px;
                    font-weight:700;
                    line-height:1;
                ">
                    {total_deliverables}
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            """
            <div style="
                margin-top:auto;
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