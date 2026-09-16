import streamlit as st


def render_sidebar():

    st.markdown("""
    <style>

    section[data-testid="stSidebar"] {
        background: #041124 !important;
    }

    section[data-testid="stSidebar"] > div {
        background: #041124 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        pass