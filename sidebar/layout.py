import streamlit as st

from sidebar.branding import render_branding


def render_sidebar():

    with st.sidebar:

        # ==========================================
        # BRANDING
        # ==========================================

        render_branding()

        # ==========================================
        # FRAMEWORKS
        # ==========================================

        st.markdown("""
        <div class="sidebar-block frameworks">
            FRAMEWORKS
        </div>
        """, unsafe_allow_html=True)

        # ==========================================
        # NAVIGATION
        # ==========================================

        st.markdown("""
        <div class="sidebar-block navigation">
            MAIN NAVIGATION
        </div>
        """, unsafe_allow_html=True)

        # ==========================================
        # SNAPSHOTS
        # ==========================================

        st.markdown("""
        <div class="sidebar-block snapshots">
            SNAPSHOT HISTORY
        </div>
        """, unsafe_allow_html=True)

        # ==========================================
        # HEALTH
        # ==========================================

        st.markdown("""
        <div class="sidebar-block health">
            PROJECT HEALTH
        </div