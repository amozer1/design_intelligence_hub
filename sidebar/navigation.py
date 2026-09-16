import streamlit as st


NAV_ITEMS = [
    "Executive Dashboard",
    "Deliverables",
    "Discipline Performance",
    "Programme Drift",
    "Design Readiness",
    "Upcoming Submissions",
    "Critical Path & Alerts",
    "Design Dependencies",
    "Queries & TQs",
    "AI Insights & Forecast",
    "Reports",
    "Data Explorer",
    "Settings",
]


def render_navigation():

    st.markdown(
        "<div class='section-title'>MAIN NAVIGATION</div>",
        unsafe_allow_html=True
    )

    for item in NAV_ITEMS:

        st.button(
            item,
            use_container_width=True,
            key=f"nav_{item}"
        )
