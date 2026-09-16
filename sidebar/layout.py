import streamlit as st


def render_sidebar():

    st.markdown("""
    <style>

    section[data-testid="stSidebar"]{
        background:linear-gradient(
            180deg,
            #00142D 0%,
            #001A38 100%
        );
    }

    section[data-testid="stSidebar"] .block-container{
        padding-top:0.75rem;
        padding-left:0.75rem;
        padding-right:0.75rem;
        padding-bottom:1rem;
    }

    hr{
        margin-top:8px !important;
        margin-bottom:8px !important;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        pass