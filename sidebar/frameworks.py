import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-title {
        color: #B7C7DA;
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .framework-group {
        color: white;
        font-size: 14px;
        font-weight: 600;
        margin-top: 12px;
        margin-bottom: 6px;
    }

    div[role="radiogroup"] label {
        padding: 3px 0 !important;
        margin: 0 !important;
    }

    div[data-baseweb="radio"] * {
        color: white !important;
        opacity: 1 !important;
        font-size: 13px !important;
    }

    </style>
    """, unsafe_allow_html=True)

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

    all_projects = enterprise_projects + ddb_projects

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    selected = st.radio(
        "",
        all_projects,
        index=all_projects.index(st.session_state.project),
        label_visibility="collapsed"
    )

    st.markdown(
        '<div class="framework-group">▾ UU Enterprise Framework</div>',
        unsafe_allow_html=True
    )

    for project in enterprise_projects:
        icon = "●" if selected == project else "○"
        st.markdown(f"{icon} {project}")

    st.divider()

    st.markdown(
        '<div class="framework-group">▾ UU DD&B Framework</div>',
        unsafe_allow_html=True
    )

    for project in ddb_projects:
        icon = "●" if selected == project else "○"
        st.markdown(f"{icon} {project}")

    if selected != st.session_state.project:
        st.session_state.project = selected
        st.rerun()