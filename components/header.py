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


def render_header(project, snapshot=None):

    manager = PROJECT_MANAGERS.get(
        project,
        "Not Assigned"
    )

    today = datetime.now().strftime(
        "%d %b %Y"
    )

    with st.container(border=True):

        col1, col2, col3, col4, col5 = st.columns(
            [0.5, 3, 3, 1.5, 2]
        )

        with col1:
            st.markdown("## ☰")

        with col2:
            st.caption("PROJECT")
            st.write(f"**{project}**")

        with col3:
            st.caption("DATE")
            st.write(f"**{today}**")

        with col4:
            st.caption("TOOLS")
            st.write("🔄 🔔 ❓ ⚙️")

        with col5:
            st.caption("DESIGN MANAGER")
            st.write(f"**{manager}**")