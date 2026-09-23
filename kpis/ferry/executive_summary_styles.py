import streamlit as st


def load_executive_summary_styles():

    st.markdown(
        """
        <style>

        .exec-card{
            padding:12px;
            border-radius:12px;
            border:1px solid rgba(255,255,255,.08);
            background:#081322;
        }

        .exec-title{
            color:#DCE8F5;
            font-size:12px;
            font-weight:700;
            letter-spacing:.5px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )