import streamlit as st


def render_frameworks():

    st.markdown("##### FRAMEWORKS")

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    st.markdown("**▾ UU Enterprise Framework**")

    enterprise_projects = [
        "Pennington Flash",
        "Davyhulme ASP4"
    ]

    for project in enterprise_projects:

        active = st.session_state.project == project

        if st.button(
            f"⚪ {project}",
            key=f"framework_{project}",
            use_container_width=True,
            type="primary" if active else "tertiary",
        ):
            st.session_state.project = project
            st.rerun()

    st.markdown("")

    st.markdown("**▾ UU DD&B Framework**")

    ddb_projects = [
        ("🔴", "Ferry PS"),
        ("🟠", "Rossall Outfall"),
        ("🟢", "Flass Lane"),
        ("🟡", "Tally Ho"),
        ("🟢", "Eccleston Bridge"),
    ]

    for icon, project in ddb_projects:

        active = st.session_state.project == project

        if st.button(
            f"{icon} {project}",
            key=f"framework_{project}",
            use_container_width=True,
            type="primary" if active else "tertiary",
        ):
            st.session_state.project = project
            st.rerun()