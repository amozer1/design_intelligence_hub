# components/homepage.py

import streamlit as st


def render_homepage():

    st.markdown("""
    <style>

    .stApp {
        background: #061F3B;
    }

    </style>
    """, unsafe_allow_html=True)

    st.info("HEADER")

    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)

    c1.info("KPI")
    c2.info("KPI")
    c3.info("KPI")
    c4.info("KPI")
    c5.info("KPI")
    c6.info("KPI")
    c7.info("KPI")

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)

    with r1c1:
        st.container(border=True)

    with r1c2:
        st.container(border=True)

    with r1c3:
        st.container(border=True)

    with r1c4:
        st.container(border=True)