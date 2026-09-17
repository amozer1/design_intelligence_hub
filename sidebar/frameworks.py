import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-title{
        color:#DCE6F2;
        font-size:12px;
        font-weight:700;
        letter-spacing:.8px;
        margin-bottom:10px;
    }

    .framework-group{
        color:white;
        font-size:14px;
        font-weight:700;
        margin-top:8px;
        margin-bottom:6px;
    }

    hr.framework-divider{
        border:none;
        border-top:1px solid rgba(255,255,255,.12);
        margin:12px 0;
    }

    div[data-testid="stButton"] button{
        background:transparent !important;
        color:#EAF2FF !important;
        border:none !important;
        box-shadow:none !important;
        text-align:left !important;
        justify-content:flex-start !important;
        padding:3px 0 3px 8px !important;
        min-height:28px !important;
        font-size:13px !important;
        width:100%;
    }

    div[data-testid="stButton"] button:hover{
        background:rgba(255,255,255,.05) !important;
        border-radius:6px !important;
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

    st.markdown(
        '<div class="framework-group">▾ UU Enterprise Framework</div>',
        unsafe_allow_html=True
    )

    for project in enterprise_projects:

        icon = "●" if st.session_state.project == project else "○"

        if st.button(
            f"{icon}  {project}",
            key=f"enterprise_{project}",
            use_container_width=True
        ):
            st.session_state.project = project
            st.rerun()

    st.markdown(
        '<hr class="framework-divider">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-group">▾ UU DD&B Framework</div>',
        unsafe_allow_html=True
    )

    for project in ddb_projects:

        icon = "●" if st.session_state.project == project else "○"

        if st.button(
            f"{icon}  {project}",
            key=f"ddb_{project}",
            use_container_width=True
        ):
            st.session_state.project = project
            st.rerun()