import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-title {
        color: #EAF2FF;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }

    .framework-group {
        color: #FFFFFF;
        font-size: 14px;
        font-weight: 700;
        margin-top: 6px;
        margin-bottom: 6px;
    }

    .stButton > button {
        width: 100%;
        background: transparent;
        border: none;
        color: white;
        text-align: left;
        padding: 4px 0;
        min-height: 28px;
        font-size: 13px;
        font-weight: 500;
    }

    .stButton > button:hover {
        background: transparent;
        border: none;
        color: white;
    }

    </style>
    """, unsafe_allow_html=True)

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

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

    # Enterprise Framework

    st.markdown(
        '<div class="framework-group">▾ UU Enterprise Framework</div>',
        unsafe_allow_html=True
    )

    for project in enterprise_projects:

        icon = "🔴" if project == st.session_state.project else "⚪"

        if st.button(
            f"{icon}  {project}",
            key=f"ent_{project}",
            use_container_width=True
        ):
            st.session_state.project = project
            st.rerun()

    st.divider()

    # DD&B Framework

    st.markdown(
        '<div class="framework-group">▾ UU DD&B Framework</div>',
        unsafe_allow_html=True
    )

    for project in ddb_projects:

        icon = "🔴" if project == st.session_state.project else "⚪"

        if st.button(
            f"{icon}  {project}",
            key=f"ddb_{project}",
            use_container_width=True
        ):
            st.session_state.project = project
            st.rerun()