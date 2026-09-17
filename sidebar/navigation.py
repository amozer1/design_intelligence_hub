import streamlit as st


def render_navigation():

    # ==================================================
    # SESSION STATE
    # ==================================================

    if "page" not in st.session_state:
        st.session_state.page = "Executive Dashboard"

    # ==================================================
    # CSS
    # ==================================================

    st.markdown("""
    <style>

    .nav-title {
        color: #B7C7DA;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 10px;
    }

    .nav-section {
        color: #FFFFFF;
        font-size: 11px;
        font-weight: 700;
        margin-top: 12px;
        margin-bottom: 4px;
        letter-spacing: 0.5px;
    }

    /* Remove Streamlit spacing */
    .element-container {
        margin-bottom: 0rem !important;
    }

    /* Navigation buttons */
    div[data-testid="stButton"] button {

        width: 100%;

        text-align: left !important;

        justify-content: flex-start !important;

        background: transparent !important;

        border: none !important;

        color: #EAF2FF !important;

        font-size: 13px !important;

        font-weight: 500 !important;

        min-height: 32px !important;

        padding: 4px 10px !important;

        border-radius: 6px !important;

        box-shadow: none !important;
    }

    div[data-testid="stButton"] button:hover {

        background: rgba(255,255,255,0.05) !important;

        color: white !important;
    }

    /* Active navigation item */
    .active-nav {

        background: linear-gradient(
            90deg,
            #2563EB,
            #1D4ED8
        );

        color: white;

        padding: 8px 12px;

        border-radius: 8px;

        font-size: 13px;

        font-weight: 600;

        margin-bottom: 2px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ==================================================
    # TITLE
    # ==================================================

    st.markdown(
        '<div class="nav-title">MAIN NAVIGATION</div>',
        unsafe_allow_html=True
    )

    # ==================================================
    # NAVIGATION STRUCTURE
    # ==================================================

    sections = {
        "OVERVIEW": [
            "Executive Dashboard",
            "Programme Drift",
            "AI Insights & Forecast"
        ],
        "DESIGN MANAGEMENT": [
            "Deliverables",
            "Discipline Performance",
            "Design Readiness",
            "Upcoming Submissions"
        ],
        "COORDINATION": [
            "Critical Path & Alerts",
            "Design Dependencies",
            "Queries & TQs"
        ],
        "TOOLS": [
            "Reports",
            "Data Explorer",
            "Settings"
        ]
    }

    # ==================================================
    # RENDER MENU
    # ==================================================

    for section, pages in sections.items():

        st.markdown(
            f'<div class="nav-section">{section}</div>',
            unsafe_allow_html=True
        )

        for page in pages:

            if st.session_state.page == page:

                st.markdown(
                    f"""
                    <div class="active-nav">
                        {page}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                if st.button(
                    page,
                    key=f"page_{page}",
                    use_container_width=True
                ):
                    st.session_state.page = page
                    st.rerun()