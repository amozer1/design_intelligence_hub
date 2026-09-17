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

    /* Asset labels */
    .framework-assets {
        color: #BFC9D9;
        font-size: 12px;
        margin-left: 20px;
        margin-bottom: 8px;
        line-height: 1.4;
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

    # Assets in display order
    assets = [
        "Pennington Flash",
        "Davyhulme ASP4",
        "Eccleston Bridge",
        "Ferry PS",
        "Rossall Outfall",
        "Flass Lane",
        "Tally Ho",
    ]

    # Default selection
    if "project" not in st.session_state:
        st.session_state.project = "Ferry PS"

    st.markdown(
        '<div class="framework-title">FRAMEWORKS</div>',
        unsafe_allow_html=True
    )

    # Framework headers (visual only)
    st.markdown(
        '<div class="framework-group">▾ UU Enterprise</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div class="framework-assets">
            Pennington Flash<br>
            Davyhulme ASP4
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="framework-group">▾ UU DD&amp;B</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div class="framework-assets">
            Eccleston Bridge<br>
            Ferry PS<br>
            Rossall Outfall<br>
            Flass Lane<br>
            Tally Ho
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.divider()

    # Single selection source
    selected_asset = st.radio(
        "Assets",
        assets,
        index=assets.index(st.session_state.project),
        label_visibility="collapsed",
        key="asset_selector"
    )

    # Update selected project
    if selected_asset != st.session_state.project:
        st.session_state.project = selected_asset
        st.rerun()