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
        padding: 4px 0;
    }

    </style>
    """, unsafe_allow_html=True)

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    # ==================================================
    # UU ENTERPRISE FRAMEWORK
    # ==================================================

    st.markdown(
        '<div class="framework-group">▾ UU Enterprise Framework</div>',
        unsafe_allow_html=True
    )

    enterprise_projects = [
        "Pennington Flash",
        "Davyhulme ASP4"
    ]

    selected_enterprise = (
        st.session_state.project
        if st.session_state.project in enterprise_projects
        else None
    )

    if selected_enterprise:
        idx = enterprise_projects.index(selected_enterprise)
    else:
        idx = None

    enterprise_choice = st.radio(
        "Enterprise",
        enterprise_projects,
        index=idx if idx is not None else 0,
        label_visibility="collapsed",
        key="enterprise_radio"
    )

    # ==================================================
    # UU DD&B FRAMEWORK
    # ==================================================

    st.markdown(
        '<div class="framework-group">▾ UU DD&B Framework</div>',
        unsafe_allow_html=True
    )

    ddb_projects = [
        "Ferry PS",
        "Rossall Outfall",
        "Flass Lane",
        "Tally Ho",
        "Eccleston Bridge"
    ]

    selected_ddb = (
        st.session_state.project
        if st.session_state.project in ddb_projects
        else None
    )

    if selected_ddb:
        idx = ddb_projects.index(selected_ddb)
    else:
        idx = 0

    ddb_choice = st.radio(
        "DD&B",
        ddb_projects,
        index=idx,
        label_visibility="collapsed",
        key="ddb_radio"
    )

    selected = (
        enterprise_choice
        if enterprise_choice in enterprise_projects
        and enterprise_choice != selected_enterprise
        else ddb_choice
    )

    if selected != st.session_state.project:
        st.session_state.project = selected
        st.rerun()