import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-title {
        color: #B7C7DA;
        font-size: 14px;
        font-weight: 700;
        margin-top: 8px;
        margin-bottom: 12px;
    }

    .framework-group {
        color: #DCE6F2;
        font-size: 14px;
        font-weight: 600;
        margin-top: 12px;
        margin-bottom: 8px;
    }

    /* Framework Buttons */

    div[data-testid="stButton"] button {

        width: 100%;

        background: #0A254A !important;

        color: white !important;

        border: 1px solid rgba(255,255,255,.08) !important;

        border-radius: 8px !important;

        padding: 8px 12px !important;

        min-height: 40px !important;

        font-size: 14px !important;

        font-weight: 500 !important;

        text-align: left !important;

        justify-content: flex-start !important;

        box-shadow: none !important;
    }

    div[data-testid="stButton"] button:hover {

        background: #12315C !important;

        border: 1px solid rgba(139,92,246,.4) !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

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

    for project in enterprise_projects:

        if st.button(
            project,
            key=f"project_{project}",
            use_container_width=True
        ):
            st.session_state.project = project
            st.rerun()

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

    for project in ddb_projects:

        active = st.session_state.project == project

        if active:

            st.markdown(f"""
            <div style="
                background: linear-gradient(
                    90deg,
                    #6D28D9,
                    #8B5CF6
                );
                color: white;
                padding: 10px 12px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: 600;
                margin-bottom: 6px;
            ">
                {project}
            </div>
            """, unsafe_allow_html=True)

        else:

            if st.button(
                project,
                key=f"project_{project}",
                use_container_width=True
            ):
                st.session_state.project = project
                st.rerun()