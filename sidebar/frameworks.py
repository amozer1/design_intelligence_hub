import streamlit as st

def render_frameworks():

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    enterprise_projects = [
        "Pennington Flash",
        "Davyhulme ASP4"
    ]

    ddb_projects = [
        "Ferry PS",
        "Rossall Outfall",
        "Flass Lane",
        "Tally Ho",
        "Eccleston Bridge"
    ]

    all_projects = (
        enterprise_projects +
        ddb_projects
    )

    st.markdown("### FRAMEWORKS")

    selected_project = st.radio(
        "Project",
        all_projects,
        index=all_projects.index(st.session_state.project),
        label_visibility="collapsed"
    )

    st.session_state.project = selected_project

    st.markdown("---")

    st.markdown("**UU Enterprise Framework**")
    for p in enterprise_projects:
        icon = "🔴" if p == selected_project else "⚪"
        st.write(f"{icon} {p}")

    st.markdown("---")

    st.markdown("**UU DD&B Framework**")
    for p in ddb_projects:
        icon = "🔴" if p == selected_project else "⚪"
        st.write(f"{icon} {p}")