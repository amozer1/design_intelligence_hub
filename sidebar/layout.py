import streamlit as st


def render_sidebar():

    with st.sidebar:

        # ==================================================
        # BRANDING
        # ==================================================

        branding_container = st.container()

        # ==================================================
        # FRAMEWORKS
        # ==================================================

        st.divider()

        frameworks_container = st.container()

        # ==================================================
        # MAIN NAVIGATION
        # ==================================================

        st.divider()

        navigation_container = st.container()

        # ==================================================
        # SNAPSHOT HISTORY
        # ==================================================

        st.divider()

        snapshots_container = st.container()

        # ==================================================
        # PROJECT HEALTH
        # ==================================================

        st.divider()

        health_container = st.container()

        # ==================================================
        # PROJECT BASELINE
        # ==================================================

        st.divider()

        baseline_container = st.container()

        # ==================================================
        # FOOTER
        # ==================================================

        st.divider()

        footer_container = st.container()