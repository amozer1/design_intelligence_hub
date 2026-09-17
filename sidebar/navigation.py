import streamlit as st


def render_navigation():

    # ==================================================
    # SESSION STATE
    # ==================================================

    if "page" not in st.session_state:
        st.session_state.page = "Executive Dashboard"

    # ==================================================
    # STYLING
    # ==================================================

    st.markdown("""
    <style>

    .nav-title {
        color: #B7C7DA;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 10px;
        border-bottom: 1px solid rgba(255,255,255,.10);
        padding-bottom: 6px;
    }

    div[data-testid="stButton"] button {

        width: 100%;

        background: transparent !important;

        color: #EAF2FF !important;

        border: none !important;

        border-radius: 8px !important;

        text-align: left !important;

        justify-content: flex-start !important;

        padding: 8px 12px !important;

        min-height: 36px !important;

        font-size: 14px !important;

        font-weight: 500 !important;

        box-shadow: none !important;
    }

    div[data-testid="stButton"] button:hover {

        background: rgba(255,255,255,.05) !important;
    }

    .active-nav {

        background: linear-gradient(
            90deg,
            #2563EB,
            #335CE5
        );

        color: white;

        padding: 10px 12px;

        border-radius: 8px;

        font-size: 14px;

        font-weight: 600;

        margin-bottom: 2px;
    }

    .submenu {
        color: #9FB5D1;
        font-size: 13px;
        padding-left: 34px;
        margin-top: 2px;
        margin-bottom: 2px;
    }

    .element-container {
        margin-bottom: 0rem !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # ==================================================
    # MENU
    # ==================================================

    menu_items = [
        ("🏠", "Executive Dashboard"),
        ("📄", "Deliverables"),
        ("📊", "Discipline Performance"),
        ("📈", "Programme Drift"),
        ("🕒", "Design Readiness"),
        ("📅", "Upcoming Submissions"),
        ("⚠️", "Critical Path & Alerts"),
        ("🔗", "Design Dependencies"),
        ("❓", "Queries & TQs"),
        ("🤖", "AI Insights & Forecast"),
        ("📋", "Reports"),
        ("🗄️", "Data Explorer"),
        ("⚙️", "Settings"),
    ]

    st.markdown(
        '<div class="nav-title">MAIN NAVIGATION</div>',
        unsafe_allow_html=True
    )

    for icon, page in menu_items:

        if st.session_state.page == page:

            st.markdown(
                f"""
                <div class="active-nav">
                    {icon} &nbsp; {page}
                </div>
                """,
                unsafe_allow_html=True
            )

            if page == "Upcoming Submissions":

                st.markdown(
                    '<div class="submenu">• Next 7 Days</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="submenu">• Next 30 Days</div>',
                    unsafe_allow_html=True
                )

        else:

            if st.button(
                f"{icon}  {page}",
                key=f"nav_{page}",
                use_container_width=True
            ):
                st.session_state.page = page
                st.rerun()

            if page == "Upcoming Submissions":

                st.markdown(
                    '<div class="submenu">• Next 7 Days</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="submenu">• Next 30 Days</div>',
                    unsafe_allow_html=True
                )