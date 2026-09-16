import streamlit as st


def render_sidebar():

    st.markdown("""
    <style>

    section[data-testid="stSidebar"] {
        background: #081324;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        pass