import streamlit as st


PROJECT_MANAGERS = {
    "Ferry PS": "Conal Cunningham",
    "Flass Lane": "Conal Cunningham",

    "Tally Ho": "Ebenezer Amoako",
    "Eccleston Bridge": "Ebenezer Amoako",
    "Pennington Flash": "Ebenezer Amoako",
    "Davyhulme ASP4": "Ebenezer Amoako",

    "Rossall Outfall": "Michael Harbon"
}


def render_header(project, snapshot):

    design_manager = PROJECT_MANAGERS.get(
        project,
        "Not Assigned"
    )

    last_updated = snapshot.replace(
        "CL32-",
        ""
    )

    c1, c2, c3, c4, c5 = st.columns(
        [2, 2, 2, 2, 1]
    )

    with c1:

        with st.container(border=True):

            st.caption("PROJECT")

            st.markdown(
                f"### {project}"
            )

    with c2:

        with st.container(border=True):

            st.caption("SNAPSHOT")

            st.markdown(
                f"### {snapshot}"
            )

    with c3:

        with st.container(border=True):

            st.caption("DESIGN MANAGER")

            st.markdown(
                f"### {design_manager}"
            )

    with c4:

        with st.container(border=True):

            st.caption("LAST UPDATED")

            st.markdown(
                f"### {last_updated}"
            )

    with c5:

        with st.container(border=True):

            st.caption("SYSTEM")

            st.markdown(
                "### 🔔 ⚙️"
            )