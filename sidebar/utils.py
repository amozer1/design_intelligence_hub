# sidebar/utils.py

import streamlit as st


def render_separator():

    st.markdown("""
    <hr style="
        margin: 16px 0;
        border: none;
        height: 1px;
        background: rgba(255,255,255,0.08);
    ">
    """, unsafe_allow_html=True)