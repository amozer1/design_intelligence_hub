# sidebar/frameworks.py

import streamlit as st


def project_card(project, active=False):

    if active:
        return f"""
        <div style="
            background:linear-gradient(
                90deg,
                #6624D6,
                #7C3AED
            );
            padding:12px;
            border-radius:8px;
            color:white;
            font-size:14px;
            font-weight:600;
            margin-bottom:6px;
        ">
            {project}
        </div>
        """
    else:
        return f"""
        <div style="
            background:rgba(255,255,255,.04);
            border:1px solid rgba(255,255,255,.06);
            padding:10px 12px;
            border-radius:8px;
            color:#E2E8F0;
            font-size:14px;
            margin-bottom:6px;
        ">
            {project}
        </div>
        """


def render_frameworks():

    st.markdown("##### FRAMEWORKS")

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    st.markdown("**▾ UU Enterprise Framework**")

    for project in [
        "Pennington Flash",
        "Davyhulme ASP4"
    ]:

        clicked = st.button(
            project,
            key=f"project_{project}",
            use_container_width=True
        )

        if clicked:
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

        active = st.session_state.project == project

        st.markdown(
            project_card(project, active),
            unsafe_allow_html=True
        )

        if st.button(
            f"Select {project}",
            key=f"select_{project}"
        ):
            st.session_state.project = project
            st.rerun()