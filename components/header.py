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


def render_header(project):

    manager = PROJECT_MANAGERS.get(
        project,
        "Not Assigned"
    )

    today = datetime.now().strftime(
        "%d %b %Y"
    )

    st.title("UU DESIGN PROGRAMME DASHBOARD")
    st.caption(
        "CL31 & CL32 • Delivery Tracking • Forecasting"
    )

    with st.container(border=True):

        menu, project_col, date_col, tools_col, manager_col = st.columns(
            [0.5, 3, 3, 1.5, 2]
        )

        with menu:
            st.write("")
            st.markdown("## ☰")

        with project_col:
            st.caption("PROJECT")
            st.write(f"**{project}**")

        with date_col:
            st.caption("SNAPSHOT")
            st.write(f"**{today}**")

        with tools_col:
            st.caption("TOOLS")
            st.write("🔄 🔔 ❓ ⚙️")

        with manager_col:
            st.caption("DESIGN MANAGER")
            st.write(f"**{manager}**")

    st.markdown("")
