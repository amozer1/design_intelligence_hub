import streamlit as st


def load_executive_summary_styles():

    st.markdown(
        """
        <style>

        .exec-title{
            color:#DCE8F5;
            font-size:12px;
            font-weight:700;
            letter-spacing:0.5px;
        }

        .exec-subtitle{
            color:#9CA3AF;
            font-size:11px;
            font-weight:600;
        }

        </style>
        """,
        unsafe_allow_html=True
    )