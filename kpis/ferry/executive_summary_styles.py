import streamlit as st


def load_executive_summary_styles():

    st.markdown(
        """
        <style>

        [data-testid="stVerticalBlockBorderWrapper"] {
            background: red !important;
            border: 3px solid yellow !important;
            border-radius: 16px !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )