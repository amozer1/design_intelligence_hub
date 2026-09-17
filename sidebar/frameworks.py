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
        text-transform: uppercase;
    }

    /* Framework Header */
    .framework-group {
        color: #FFFFFF;
        font-size: 14px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 4px;
    }

    /* Reduce spacing */
    .element-container {
        margin-bottom: 0rem !important;
    }

    div[data-testid="stMarkdownContainer"] p {
        margin-bottom: 0 !important;
    }

    /* Asset buttons */
    div.stButton > button {
        width: 100%;
        text-align: left;
        justify-content: flex-start;
        background: transparent;
        border: none;
        color: #FFFFFF;
        padding: 4px 0 4px 18px;
        min-height: 28px;
        border-radius: 4px;
        font-size: 13px;
        font-weight: 500;
        box-shadow: none;
    }

    div.stButton > button:hover {
        background: rgba(255,255,255,0.08);
        color: #FFFFFF;
    }

    div.stButton > button:focus {
        border: none;
        box-shadow: none;
    }
    </style>
    """, unsafe_allow_html=True)

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    def asset_button(name):
        selected = st.session_state.project == name

        prefix = "🔴" if selected else "⚪"

        if st.button(
            f"{prefix}  {name}",
            key=f"asset_{name}",
            use_container_width=True,
        ):
            st.session_state.project = name
            st.rerun()

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-group">▾ UU Enterprise</div>',
        unsafe_allow_html=True
    )

    asset_button("Pennington Flash")
    asset_button("Davyhulme ASP4")

    st.divider()

    st.markdown(
        '<div class="framework-group">▾ UU DD&amp;B</div>',
        unsafe_allow_html=True
    )

    asset_button("Eccleston Bridge")
    asset_button("Ferry PS")
    asset_button("Rossall Outfall")
    asset_button("Flass Lane")
    asset_button("Tally Ho")