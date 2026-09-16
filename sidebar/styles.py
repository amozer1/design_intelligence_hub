import streamlit as st


def load_sidebar_styles():

    st.markdown(
        """
        <style>

        section[data-testid="stSidebar"]{
            background:#081322;
        }

        .section-title{
            font-size:11px;
            font-weight:700;
            color:#9ca3af;
            letter-spacing:1px;
        }

        .sidebar-card{
            padding:12px;
            border-radius:12px;
            border:1px solid rgba(255,255,255,.08);
            background:rgba(255,255,255,.03);
        }

        </style>
        """,
        unsafe_allow_html=True
    )