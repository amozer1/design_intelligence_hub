import streamlit as st

from kpis.ferry.deliverables_utils import (
    get_metrics,
)

from kpis.ferry.deliverables_styles import (
    ICON_PURPLE,
)


def render(cl32):

    metrics = get_metrics(cl32)

    total_deliverables = metrics[
        "total_deliverables"
    ]

    with st.container(border=True):

        st.markdown(
            """
            <style>
            .deliverables-card {
                height: 205px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }
            </style>

            <div class="deliverables-card">
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div style="
                color:#111827;
                font-size:16px;
                font-weight:700;
            ">
                TOTAL DELIVERABLES
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div style="
                display:flex;
                align-items:center;
                gap:12px;
                margin-top:20px;
            ">
                <span style="
                    color:{ICON_PURPLE};
                    font-size:30px;
                ">
                    📄
                </span>

                <span style="
                    color:#111827;
                    font-size:42px;
                    font-weight:700;
                ">
                    {total_deliverables}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

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