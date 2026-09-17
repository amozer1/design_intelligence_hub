import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-title{
        color:#EAF2FF;
        font-size:12px;
        font-weight:700;
        letter-spacing:.6px;
        margin-bottom:10px;
    }

    .framework-group{
        color:white;
        font-size:14px;
        font-weight:700;
        margin-top:8px;
        margin-bottom:4px;
    }

    div[data-baseweb="radio"] *,
    div[role="radiogroup"] p,
    div[role="radiogroup"] span{
        color:white !important;
        opacity:1 !important;
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

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    current_project = st.session_state.project

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    # Detect active framework
    active_framework = None

    for fw, projects in frameworks.items():
        if current_project in projects:
            active_framework = fw
            break

    # Framework selector
    framework = st.selectbox(
        "",
        list(frameworks.keys()),
        index=list(frameworks.keys()).index(active_framework),
        label_visibility="collapsed"
    )

    # Project selector
    project = st.radio(
        "",
        frameworks[framework],
        label_visibility="collapsed"
    )

    if project != current_project:
        st.session_state.project = project
        st.rerun()

    st.markdown(
        """
        <hr style="
            border:none;
            border-top:1px solid rgba(220,232,245,0.20);
            margin:14px 0;
        ">
        """,
        unsafe_allow_html=True
    )