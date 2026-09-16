import streamlit as st


def render_sidebar():

    st.markdown("""
    <style>

    section[data-testid="stSidebar"]{
        background:#00142D;
    }

    /* Remove Streamlit's default sidebar padding */

    section[data-testid="stSidebar"] .block-container{
        padding-top:0.5rem;
        padding-left:0.2rem;
        padding-right:0.2rem;
        padding-bottom:0.5rem;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        pass