import streamlit as st


def render_executive_summary_layout():

    st.markdown(
        """
        <style>

        .element-container {
            margin-bottom: 0rem !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )