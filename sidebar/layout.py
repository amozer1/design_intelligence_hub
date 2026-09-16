import streamlit as st

from sidebar.branding import render_branding


def render_sidebar():

    with st.sidebar:

        render_branding()

        # Frameworks Placeholder

        st.divider()
        st.info("FRAMEWORKS")

        # Navigation Placeholder

        st.divider()
        st.info("NAVIGATION")

        # Snapshot Placeholder

        st.divider()
        st.info("SNAPSHOTS")

        # Health Placeholder

        st.divider()
        st.info("HEALTH")

        # Baseline Placeholder

        st.divider()
        st.info("BASELINE")