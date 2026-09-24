import streamlit as st

from kpis.ferry.kpi_card_utils import variance_colour


def render(avg_variance):

    colour = variance_colour(avg_variance)

    with st.container(border=True):

        st.markdown(
            """
            <div style="
                color:white;
                font-size:12px;
                font-weight:700;
                margin-bottom:12px;
            ">
                AVG VARIANCE (BL1)
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                font-size:32px;
                color:{colour};
                text-align:center;
            ">
                ⚖
            </div>

            <div style="
                font-size:40px;
                color:{colour};
                text-align:center;
                font-weight:700;
            ">
                {avg_variance}
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