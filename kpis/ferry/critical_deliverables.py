import streamlit as st

from kpis.ferry.kpi_card_styles import (
    CARD_TITLE,
    CARD_VALUE,
    CARD_SUBTEXT,
    RED,
)


def render(
    critical_deliverables,
    delta
):

    with st.container(border=True):

        st.markdown(
            """
            <div style="
                color:white;
                font-size:12px;
                font-weight:700;
                margin-bottom:12px;
            ">
                CRITICAL DELIVERABLES
            </div>
            """,
            unsafe_allow_html=True
        )

        icon_col, value_col = st.columns([1, 2])

        with icon_col:

            st.markdown(
                """
                <div style="
                    color:#FF0000;
                    font-size:34px;
                ">
                    ⚠
                </div>
                """,
                unsafe_allow_html=True
            )

        with value_col:

            st.markdown(
                f"""
                <div style="
                    color:white;
                    font-size:40px;
                    font-weight:700;
                ">
                    {critical_deliverables}
                </div>
                """,
                unsafe_allow_html=True
            )

        bottom_left, bottom_right = st.columns([2, 1])

        with bottom_left:

            st.markdown(
                """
                <div style="
                    color:#CBD5E1;
                    font-size:11px;
                ">
                    vs last month
                </div>
                """,
                unsafe_allow_html=True
            )

        with bottom_right:

            st.markdown(
                f"""
                <div style="
                    background:{RED};
                    color:white;
                    border-radius:6px;
                    text-align:center;
                    padding:4px;
                    font-size:11px;
                    font-weight:700;
                ">
                    +{delta}
                </div>
                """,
                unsafe_allow_html=True
            )