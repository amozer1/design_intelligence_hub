import streamlit as st


def render_frameworks():

    st.markdown("##### FRAMEWORKS")

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    st.markdown("**▾ UU Enterprise Framework**")

    for project in [
        "Pennington Flash",
        "Davyhulme ASP4"
    ]:

        if st.button(
            project,
            key=project,
            use_container_width=True
        ):
            st.session_state.project = project
            st.rerun()

    st.markdown("")

    st.markdown("**▾ UU DD&B Framework**")

    for project in [
        "Ferry PS",
        "Rossall Outfall",
        "Flass Lane",
        "Tally Ho",
        "Eccleston Bridge"
    ]:

        if st.button(
            project,
            key=project,
            use_container_width=True
        ):
            st.session_state.project = project
            st.rerun()