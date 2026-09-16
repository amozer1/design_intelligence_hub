import streamlit as st


def render_sidebar():

    st.markdown("""
    <style>

    section[data-testid="stSidebar"] {
        background: #081324;
    }

    .sidebar-block {
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 12px;
        color: white;
        font-weight: 600;
    }

    .branding {
        background: #1e293b;
        border-left: 4px solid #8b5cf6;
    }

    .frameworks {
        background: #172554;
        border-left: 4px solid #3b82f6;
    }

    .navigation {
        background: #0f3d2e;
        border-left: 4px solid #22c55e;
    }

    .snapshots {
        background: #4a2c0d;
        border-left: 4px solid #f59e0b;
    }

    .health {
        background: #4c1d1d;
        border-left: 4px solid #ef4444;
    }

    .baseline {
        background: #312e81;
        border-left: 4px solid #6366f1;
    }

    .footer {
        background: #374151;
        border-left: 4px solid #9ca3af;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:

        st.markdown("""
        <div class="sidebar-block branding">
            BRANDING
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-block frameworks">
            FRAMEWORKS
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-block navigation">
            MAIN NAVIGATION
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-block snapshots">
            SNAPSHOT HISTORY
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-block health">
            PROJECT HEALTH
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-block baseline">
            PROJECT BASELINE
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sidebar-block footer">
            FOOTER
        </div>
        """, unsafe_allow_html=True)