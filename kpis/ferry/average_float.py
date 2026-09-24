import streamlit as st

from kpis.ferry.kpi_card_utils import float_colour


def render(avg_float):

    colour = float_colour(avg_float)

    with st.container(border=True):

        st.markdown(
            """
            <div style="
                color:white;
                font-size:12px;
                font-weight:700;
                margin-bottom:12px;
            ">
                AVG FLOAT
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                font-size:34px;
                color:{colour};
                text-align:center;
                font-weight:700;
            ">
                ◔
            </div>

            <div style="
                font-size:40px;
                color:white;
                text-align:center;
                font-weight:700;
            ">
                {avg_float}
            </div>

            <div style="
                font-size:12px;
                color:#CBD5E1;
                text-align:center;
            ">
                days
            </div>
            """,
            unsafe_allow_html=True
        )