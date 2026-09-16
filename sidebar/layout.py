import streamlit as st


def render_sidebar():

    st.markdown("""
    <style>

    section[data-testid="stSidebar"]{
        background:linear-gradient(
            180deg,
            #03112B 0%,
            #041124 100%
        );
    }

    .sidebar-section{
        padding:16px 0;
        border-bottom:1px solid rgba(59,130,246,0.15);
    }

    .section-title{
        color:#94A3B8;
        font-size:11px;
        font-weight:600;
        letter-spacing:1px;
        margin-bottom:12px;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        pass
