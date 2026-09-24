import streamlit as st

from kpis.ferry.kpi_card_styles import (
    CARD_TITLE,
    CARD_VALUE,
    CARD_SUBTEXT,
    ICON_BLUE,
    BLUE,
)


def render(
    total_deliverables,
    delta
):

    with st.container(border=True):

        st.markdown(
            f"""
            <div style="
                color:{CARD_TITLE};
                font-size:12px;
                font-weight:700;
                text-transform:uppercase;
                margin-bottom:12px;
            ">
                TOTAL DELIVERABLES
            </div>
            """,
            unsafe_allow_html=True
        )

        icon_col, value_col = st.columns([1, 2])

        with icon_col:

            st.markdown(
                f"""
                <div style="
                    color:{ICON_BLUE};
                    font-size:32px;
                ">
                    📄
                </div>
                """,
                unsafe_allow_html=True
            )

        with value_col:

            st.markdown(
                f"""
                <div style="
                    color:{CARD_VALUE};
                    font-size:40px;
                    font-weight:700;
                ">
                    {total_deliverables}
                </div>
                """,
                unsafe_allow_html=True
            )

        bottom_left, bottom_right = st.columns([2, 1])

        with bottom_left:

            st.markdown(
                f"""
                <div style="
                    color:{CARD_SUBTEXT};
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
                    background:{BLUE};
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