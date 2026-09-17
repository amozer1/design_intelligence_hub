import streamlit as st


def render_frameworks():

    st.markdown("""
    <style>

    .framework-title {
        color: #EAF2FF;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
        text-transform: uppercase;
    }

    .framework-group {
        color: #FFFFFF;
        font-size: 14px;
        font-weight: 700;
        margin-top: 8px;
        margin-bottom: 4px;
    }

    /* Remove Streamlit spacing */
    .element-container {
        margin-bottom: 0rem !important;
    }

    /* Asset buttons */
    div.stButton > button {
        width: 100%;
        text-align: left;
        justify-content: flex-start;
        background: transparent;
        border: none;
        color: #FFFFFF;
        padding: 4px 8px 4px 24px;
        min-height: 28px;
        border-radius: 4px;
        box-shadow: none;
    }

    div.stButton > button:hover {
        background: rgba(255,255,255,0.08);
        color: white;
    }

    div.stButton > button:focus {
        box-shadow: none;
    }

    .asset-selected {
        background: rgba(47,125,246,0.15);
        border-left: 3px solid #2F7DF6;
        padding: 6px 8px 6px 12px;
        margin-left: 12px;
        margin-bottom: 2px;
        border-radius: 4px;
        color: #FFFFFF;
        font-size: 13px;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    def asset_item(name):
        selected = st.session_state.project == name

        if selected:
            st.markdown(
                f"""
                <div class="asset-selected">
                    {name}
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            _, col = st.columns([0.05, 0.95])

            with col:
                if st.button(
                    name,
                    key=f"asset_{name}",
                    use_container_width=True,
                ):
                    st.session_state.project = name
                    st.rerun()

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    # Enterprise
    st.markdown(
        '<div class="framework-group">▾ UU Enterprise</div>',
        unsafe_allow_html=True
    )

    asset_item("Pennington Flash")
    asset_item("Davyhulme ASP4")

    st.divider()

    # DD&B
    st.markdown(
        '<div class="framework-group">▾ UU DD&amp;B</div>',
        unsafe_allow_html=True
    )

    asset_item("Eccleston Bridge")
    asset_item("Ferry PS")
    asset_item("Rossall Outfall")
    asset_item("Flass Lane")
    asset_item("Tally Ho")