import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-title{
        color:#EAF2FF;
        font-size:12px;
        font-weight:700;
        letter-spacing:.6px;
        margin-bottom:12px;
    }

    .framework-header{
        color:#FFFFFF;
        font-size:14px;
        font-weight:700;
        margin-top:4px;
        margin-bottom:6px;
    }

    div[role="radiogroup"]{
        gap:0 !important;
    }

    div[role="radiogroup"] label{
        padding:2px 0 !important;
        margin:0 !important;
        min-height:24px !important;
    }

    div[data-baseweb="radio"] *,
    div[role="radiogroup"] p,
    div[role="radiogroup"] span{
        color:#FFFFFF !important;
        opacity:1 !important;
        font-size:13px !important;
        font-weight:500 !important;
    }

    .element-container{
        margin-bottom:0rem !important;
    }

    </style>
    """, unsafe_allow_html=True)

    frameworks = {
        "UU Enterprise": [
            "Pennington Flash",
            "Davyhulme ASP4"
        ],
        "UU DD&B": [
            "Ferry PS",
            "Rossall Outfall",
            "Flass Lane",
            "Tally Ho",
            "Eccleston Bridge"
        ]
    }

    # Default project
    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    current_project = st.session_state.project

    # Determine active framework
    active_framework = "UU DD&B"

    for fw, projects in frameworks.items():
        if current_project in projects:
            active_framework = fw
            break

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    # Enterprise
    enterprise_expanded = active_framework == "UU Enterprise"

    with st.expander(
        f"UU Enterprise ({len(frameworks['UU Enterprise'])})",
        expanded=enterprise_expanded,
    ):
        choice = st.radio(
            "Enterprise Projects",
            frameworks["UU Enterprise"],
            index=(
                frameworks["UU Enterprise"].index(current_project)
                if current_project in frameworks["UU Enterprise"]
                else 0
            ),
            label_visibility="collapsed",
            key="enterprise_project"
        )

        if choice != st.session_state.project:
            st.session_state.project = choice
            st.rerun()

    # DD&B
    ddb_expanded = active_framework == "UU DD&B"

    with st.expander(
        f"UU DD&B ({len(frameworks['UU DD&B'])})",
        expanded=ddb_expanded,
    ):
        choice = st.radio(
            "DD&B Projects",
            frameworks["UU DD&B"],
            index=(
                frameworks["UU DD&B"].index(current_project)
                if current_project in frameworks["UU DD&B"]
                else 0
            ),
            label_visibility="collapsed",
            key="ddb_project"
        )

        if choice != st.session_state.project:
            st.session_state.project = choice
            st.rerun()