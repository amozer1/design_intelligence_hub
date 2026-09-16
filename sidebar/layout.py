import streamlit as st


def render_sidebar():

    st.markdown("""
    <style>

    /* Sidebar Background */

    section[data-testid="stSidebar"]{
        background: linear-gradient(
            180deg,
            #021022 0%,
            #041124 100%
        );
    }

    /* Standard Section Card */

    .sidebar-section{
        padding:16px;
        margin-bottom:12px;
        border-radius:12px;
        background:rgba(255,255,255,0.03);
        border:1px solid rgba(255,255,255,0.05);
    }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:

        # ==========================================
        # BRANDING
        # ==========================================

        st.markdown(
            '<div class="sidebar-section"></div>',
            unsafe_allow_html=True
        )

        # ==========================================
        # FRAMEWORKS
        # ==========================================

        st.markdown(
            '<div class="sidebar-section"></div>',
            unsafe_allow_html=True
        )

        # ==========================================
        # NAVIGATION
        # ==========================================

        st.markdown(
            '<div class="sidebar-section"></div>',
            unsafe_allow_html=True
        )

        # ==========================================
        # SNAPSHOTS
        # ==========================================

        st.markdown(
            '<div class="sidebar-section"></div>',
            unsafe_allow_html=True
        )

        # ==========================================
        # HEALTH
        # ==========================================

        st.markdown(
            '<div class="sidebar-section"></div>',
            unsafe_allow_html=True
        )

        # ==========================================
        # BASELINE
        # ==========================================

        st.markdown(
            '<div class="sidebar-section"></div>',
            unsafe_allow_html=True
        )

        # ==========================================
        # FOOTER
        # ==========================================

        st.markdown(
            '<div class="sidebar-section"></div>',
            unsafe_allow_html=True
        )