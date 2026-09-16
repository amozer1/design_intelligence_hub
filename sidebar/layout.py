import streamlit as st


def render_sidebar():

    st.markdown("""
    <style>

    section[data-testid="stSidebar"] {
        background: #081324;
    }

    .sidebar-divider {
        margin-top: 12px;
        margin-bottom: 12px;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:

        # ==================================================
        # BRANDING
        # ==================================================

        branding = st.container()

        st.divider()

        # ==================================================
        # FRAMEWORKS
        # ==================================================

        frameworks = st.container()

        st.divider()

        # ==================================================
        # MAIN NAVIGATION
        # ==================================================

        navigation = st.container()

        st.divider()

        # ==================================================
        # SNAPSHOT HISTORY
        # ==================================================

        snapshots = st.container()

        st.divider()

        # ==================================================
        # PROJECT HEALTH
        # ==================================================

        health = st.container()

        st.divider()

        # ==================================================
        # PROJECT BASELINE
        # ==================================================

        baseline = st.container()

        st.divider()

        # ==================================================
        # FOOTER
        # ==================================================

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