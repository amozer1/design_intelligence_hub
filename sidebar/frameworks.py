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

    # Keep radio states aligned with the active project
    if st.session_state.project in enterprise_projects:
        st.session_state.enterprise_radio = st.session_state.project
        st.session_state.ddb_radio = None

    elif st.session_state.project in ddb_projects:
        st.session_state.ddb_radio = st.session_state.project
        st.session_state.enterprise_radio = None

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    # Enterprise Framework

    st.markdown(
        '<div class="framework-group">▾ UU Enterprise Framework</div>',
        unsafe_allow_html=True
    )

    enterprise_choice = st.radio(
        "Enterprise",
        [None] + enterprise_projects,
        format_func=lambda x: "" if x is None else x,
        label_visibility="collapsed",
        key="enterprise_radio"
    )

    st.divider()

    # DD&B Framework

    st.markdown(
        '<div class="framework-group">▾ UU DD&B Framework</div>',
        unsafe_allow_html=True
    )

    ddb_choice = st.radio(
        "DD&B",
        [None] + ddb_projects,
        format_func=lambda x: "" if x is None else x,
        label_visibility="collapsed",
        key="ddb_radio"
    )

    # Selection Logic

    if enterprise_choice and enterprise_choice != st.session_state.project:
        st.session_state.project = enterprise_choice
        st.rerun()

    if ddb_choice and ddb_choice != st.session_state.project:
        st.session_state.project = ddb_choice
        st.rerun()