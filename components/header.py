from datetime import datetime
import streamlit as st

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

    today = datetime.now().strftime("%d %b %Y")

    with st.container(border=True):

        c1, c2, c3, c4, c5 = st.columns(
            [0.5, 3, 3, 1.2, 2]
        )

        with c1:
            st.markdown("## ☰")

        with c2:
            st.caption("PROJECT")
            st.write(f"**{project}**")

        with c3:
            st.caption("SNAPSHOT")
            st.write(f"**{today}**")

        with c4:
            st.caption("TOOLS")
            st.write("🔄 🔔 ❓ ⚙️")

        with c5:
            st.caption("DESIGN MANAGER")
            st.write(f"**{manager}**")