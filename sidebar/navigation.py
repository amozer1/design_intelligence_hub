import streamlit as st


def render_navigation():

    if "page" not in st.session_state:
        st.session_state.page = "Executive Dashboard"

    st.markdown("""
    <style>

    .nav-title {
        color: #B7C7DA;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-top: 12px;
        margin-bottom: 8px;
    }

    .nav-section {
        color: #FFFFFF;
        font-size: 12px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 4px;
    }

    div[data-testid="stButton"] button {

        width: 100%;

        background: transparent !important;

        color: #FFFFFF !important;

        border: none !important;

        border-radius: 6px !important;

        padding: 6px 10px !important;

        min-height: 32px !important;

        text-align: left !important;

        justify-content: flex-start !important;

        font-size: 13px !important;

        font-weight: 500 !important;

        box-shadow: none !important;
    }

    div[data-testid="stButton"] button:hover {

        background: rgba(255,255,255,0.06) !important;

        color: white !important;
    }

    .active-nav {

        background: linear-gradient(
            90deg,
            #2563EB,
            #1D4ED8
        );

        color: white;

        padding: 8px 12px;

        border-radius: 6px;

        font-size: 13px;

        font-weight: 600;

        margin-bottom: 2px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="nav-title">MAIN NAVIGATION</div>',
        unsafe_allow_html=True
    )

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

    for section, pages in sections.items():

        st.markdown(
            f'<div class="nav-section">{section}</div>',
            unsafe_allow_html=True
        )

        for page in pages:

            active = st.session_state.page == page

            if active:

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
                    key=f"nav_{page}",
                    use_container_width=True
                ):
                    st.session_state.page = page
                    st.rerun()