import streamlit as st


def render_frameworks():

    st.markdown("##### FRAMEWORKS")

    projects = {
        "UU Enterprise Framework": [
            "Pennington Flash",
            "Davyhulme ASP4"
        ],
        "UU DD&B Framework": [
            "Ferry PS",
            "Rossall Outfall",
            "Flass Lane",
            "Tally Ho",
            "Eccleston Bridge"
        ]
    }

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    for framework, items in projects.items():

        st.markdown(f"**▾ {framework}**")

        for project in items:

            active = st.session_state.project == project

            if st.button(
                project,
                use_container_width=True,
                key=f"project_{project}",
                type="primary" if active else "secondary"
            ):
                st.session_state.project = project
                st.rerun()