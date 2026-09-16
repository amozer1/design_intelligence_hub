import streamlit as st


def render_navigation():

    st.markdown("### MAIN NAVIGATION")

    pages = [
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
        "Settings"
    ]

    if "page" not in st.session_state:
        st.session_state.page = "Executive Dashboard"

    for page in pages:

        active = st.session_state.page == page

        if st.button(
            page,
            use_container_width=True,
            type="primary" if active else "secondary",
            key=f"nav_{page}"
        ):
            st.session_state.page = page
            st.rerun()

    if st.session_state.page == "Upcoming Submissions":

        st.markdown("↳ Next 7 Days")
        st.markdown("↳ Next 30 Days")