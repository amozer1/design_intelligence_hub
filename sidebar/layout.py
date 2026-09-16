import streamlit as st


def render_sidebar():

    with st.sidebar:

        branding = st.container()
        frameworks = st.container()
        navigation = st.container()
        snapshots = st.container()
        health = st.container()
        baseline = st.container()
        footer = st.container()

    return {
        "branding": branding,
        "frameworks": frameworks,
        "navigation": navigation,
        "snapshots": snapshots,
        "health": health,
        "baseline": baseline,
        "footer": footer,
    }