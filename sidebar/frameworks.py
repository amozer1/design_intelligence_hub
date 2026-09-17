import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    /* Section Title */
    .framework-title {
        color: #EAF2FF;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }

    /* Framework Header */
    .framework-group {
        color: #FFFFFF;
        font-size: 14px;
        font-weight: 700;
        margin-top: 6px;
        margin-bottom: 2px;
    }

    /* Radio Groups */
    div[role="radiogroup"] {
        gap: 0 !important;
    }

    /* Radio Rows */
    div[role="radiogroup"] label {
        padding: 2px 0 !important;
        margin: 0 !important;
        min-height: 24px !important;
    }

    /* Force ALL radio text white */
    div[data-baseweb="radio"] *,
    div[role="radiogroup"] p,
    div[role="radiogroup"] span {
        color: #FFFFFF !important;
        opacity: 1 !important;
        font-size: 13px !important;
        font-weight: 500 !important;
    }

    /* Reduce Streamlit spacing */
    .element-container {
        margin-bottom: 0rem !important;
    }

    div[data-testid="stMarkdownContainer"] p {
        margin-bottom: 0 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # Default Project
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

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    # -------------------------------
    # Enterprise Framework
    # -------------------------------

    st.markdown(
        '<div class="framework-group">▾ UU Enterprise Framework</div>',
        unsafe_allow_html=True
    )

    enterprise_index = (
        enterprise_projects.index(st.session_state.project)
        if st.session_state.project in enterprise_projects
        else None
    )

    enterprise_choice = st.radio(
        "Enterprise",
        enterprise_projects,
        index=enterprise_index,
        label_visibility="collapsed",
        key="enterprise_radio"
    )

    st.divider()

    # -------------------------------
    # DD&B Framework
    # -------------------------------

    st.markdown(
        '<div class="framework-group">▾ UU DD&B Framework</div>',
        unsafe_allow_html=True
    )

    ddb_index = (
        ddb_projects.index(st.session_state.project)
        if st.session_state.project in ddb_projects
        else None
    )

    ddb_choice = st.radio(
        "DD&B",
        ddb_projects,
        index=ddb_index,
        label_visibility="collapsed",
        key="ddb_radio"
    )

    # -------------------------------
    # Single Selection Logic
    # -------------------------------

    current_project = st.session_state.project

    if (
        current_project not in enterprise_projects
        and enterprise_choice in enterprise_projects
    ):
        st.session_state.project = enterprise_choice
        st.rerun()

    if (
        current_project not in ddb_projects
        and ddb_choice in ddb_projects
    ):
        st.session_state.project = ddb_choice
        st.rerun()

    # Detect actual changes
    if enterprise_choice != current_project and enterprise_choice in enterprise_projects:
        st.session_state.project = enterprise_choice
        st.rerun()

    if ddb_choice != current_project and ddb_choice in ddb_projects:
        st.session_state.project = ddb_choice
        st.rerun()