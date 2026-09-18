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

    design_manager = PROJECT_MANAGERS.get(
        project,
        "Not Assigned"
    )

    updated = datetime.today().strftime(
        "%d %b %Y"
    )

    with st.container(border=True):

        c0, c1, c2, c3, c4 = st.columns(
            [0.4, 3.5, 3.5, 2.2, 1.2],
            gap="medium"
        )

        with c0:
            st.write("")
            st.markdown("☰")

        with c1:
            st.caption("Project")
            st.selectbox(
                "",
                [project],
                label_visibility="collapsed"
            )

        with c2:
            st.caption("Current CL32 Snapshot")
            st.selectbox(
                "",
                [snapshot],
                label_visibility="collapsed"
            )

        with c3:
            st.caption("Design Manager")
            st.markdown(f"**{design_manager}**")
            st.caption(f"Last Updated: {updated}")

        with c4:
            st.caption("System")

            s1, s2 = st.columns(2)

            with s1:
                st.write("🔔")

            with s2:
                st.write("⚙️")