import streamlit as st


def load_executive_summary_styles():

    st.markdown(
        """
        <style>

        .exec-card{
            background:#081322;
            border:1px solid rgba(255,255,255,.08);
            border-radius:12px;
            padding:16px;
            margin-bottom:8px;
        }

        .exec-title{
            color:#DCE8F5;
            font-size:12px;
            font-weight:700;
            letter-spacing:.5px;
            margin-bottom:8px;
        }

        .exec-status{
            color:#FFFFFF;
            font-size:28px;
            font-weight:700;
            margin-bottom:12px;
        }

        .exec-label{
            color:#9CA3AF;
            font-size:11px;
            font-weight:600;
        }

        .exec-value{
            color:#FFFFFF;
            font-size:42px;
            font-weight:700;
        }

        </style>
        """,
        unsafe_allow_html=True
    )