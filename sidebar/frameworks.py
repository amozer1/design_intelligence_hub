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

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    # Enterprise Framework

    st.markdown(
        '<div class="framework-group">▾ UU Enterprise Framework</div>',
        unsafe_allow_html=True
    )

    enterprise_projects = [
        "Pennington Flash",
        "Davyhulme ASP4"
    ]

    enterprise_choice = st.radio(
        "Enterprise",
        enterprise_projects,
        index=(
            enterprise_projects.index(st.session_state.project)
            if st.session_state.project in enterprise_projects
            else None
        ),
        label_visibility="collapsed",
        key="enterprise_radio"
    )

    st.divider()

    # DD&B Framework

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

    ddb_choice = st.radio(
        "DD&B",
        ddb_projects,
        index=(
            ddb_projects.index(st.session_state.project)
            if st.session_state.project in ddb_projects
            else None
        ),
        label_visibility="collapsed",
        key="ddb_radio"
    )

    # Selection Logic

    selected = st.session_state.project

    if enterprise_choice and enterprise_choice != selected:
        selected = enterprise_choice

    if ddb_choice and ddb_choice != selected:
        selected = ddb_choice

    if selected != st.session_state.project:
        st.session_state.project = selected
        st.rerun()