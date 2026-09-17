import streamlit as st


def render_frameworks():

    # ==================================================
    # DATA
    # ==================================================

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

    # ==================================================
    # SESSION STATE
    # ==================================================

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    # ==================================================
    # STYLING
    # ==================================================

    st.markdown("""
    <style>

    .framework-title{
        color:#B7C7DA;
        font-size:14px;
        font-weight:700;
        margin-bottom:12px;
    }

    .framework-group{
        color:#DCE6F2;
        font-size:14px;
        font-weight:600;
        margin-bottom:4px;
    }

    hr.framework-divider{
        border:none;
        border-top:1px solid rgba(255,255,255,0.12);
        margin:12px 0;
    }

    div[role="radiogroup"]{
        gap:2px;
    }

    div[role="radiogroup"] > label{
        padding:6px 8px;
        border-radius:6px;
        transition:all .2s ease;
    }

    div[role="radiogroup"] > label:hover{
        background:rgba(255,255,255,.05);
    }

    div[role="radiogroup"] label[data-baseweb="radio"]{
        margin-bottom:2px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    # ==================================================
    # ENTERPRISE
    # ==================================================

    st.markdown(
        '<div class="framework-group">▾ UU Enterprise Framework</div>',
        unsafe_allow_html=True
    )

    enterprise_index = 0
    if st.session_state.project in enterprise_projects:
        enterprise_index = enterprise_projects.index(
            st.session_state.project
        )

    enterprise_selected = st.radio(
        "Enterprise Framework",
        enterprise_projects,
        index=enterprise_index,
        label_visibility="collapsed",
        key="enterprise_framework"
    )

    st.markdown(
        '<hr class="framework-divider">',
        unsafe_allow_html=True
    )

    # ==================================================
    # DD&B
    # ==================================================

    st.markdown(
        '<div class="framework-group">▾ UU DD&B Framework</div>',
        unsafe_allow_html=True
    )

    ddb_index = 0
    if st.session_state.project in ddb_projects:
        ddb_index = ddb_projects.index(
            st.session_state.project
        )

    ddb_selected = st.radio(
        "DD&B Framework",
        ddb_projects,
        index=ddb_index,
        label_visibility="collapsed",
        key="ddb_framework"
    )

    # ==================================================
    # DETERMINE SELECTION
    # ==================================================

    current_selection = st.session_state.project

    if current_selection in enterprise_projects:
        selected_project = enterprise_selected
    else:
        selected_project = ddb_selected

    # handle switching frameworks
    if enterprise_selected != current_selection:
        selected_project = enterprise_selected

    if ddb_selected != current_selection:
        selected_project = ddb_selected

    if selected_project != st.session_state.project:
        st.session_state.project = selected_project
        st.rerun()