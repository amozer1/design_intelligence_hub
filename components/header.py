import streamlit as st
from datetime import datetime

PROJECT_MANAGERS = {
    "Ferry PS": "Conal Cunningham",
    "Flass Lane": "Conal Cunningham",
    "Rossall Outfall": "Michael Harbon",
    "Tally Ho": "Ebenezer Amoako",
    "Eccleston Bridge": "Ebenezer Amoako",
    "Pennington Flash": "Ebenezer Amoako",
    "Davyhulme ASP4": "Ebenezer Amoako",
}


def render_header(project, snapshot):

    manager = PROJECT_MANAGERS.get(
        project,
        "Not Assigned"
    )

    today = datetime.now().strftime(
        "%d %b %Y"
    )

    with st.container(border=True):

        # Branding
        st.markdown("## UU DESIGN PROGRAMME DASHBOARD")
        st.caption(
            "CL31 & CL32 • Delivery Tracking • Forecasting"
        )

        st.divider()

        col1, col2, col3, col4, col5 = st.columns(
            [0.4, 3, 3, 1.2, 2]
        )

        with col1:
            st.markdown("## ☰")

        with col2:
            st.caption("Project")
            st.metric(
                label="",
                value=project
            )

        with col3:
            st.caption("Current CL32 Snapshot")
            st.metric(
                label="",
                value=snapshot
            )

        with col4:
            st.caption("Tools")
            st.write("🔄")
            st.write("🔔")
            st.write("❓")
            st.write("⚙️")

        with col5:
            st.caption("Design Manager")
            st.metric(
                label="",
                value=manager
            )

            st.caption(
                f"Last Updated: {today}"
            )