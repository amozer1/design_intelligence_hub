import streamlit as st

def render_sidebar():

    st.markdown("""
    <style>

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background: #00142D;
    }

    /* Main sidebar padding */
    section[data-testid="stSidebar"] .block-container {
        padding-top: 0.5rem;
        padding-left: 0.75rem;
        padding-right: 0.75rem;
        padding-bottom: 0.5rem;
    }

    /* Reduce gaps between Streamlit elements */
    section[data-testid="stSidebar"] .element-container {
        margin-bottom: 0rem !important;
    }

    /* Framework headers */
    .framework-group {
        color: white;
        font-size: 14px;
        font-weight: 700;
        margin-top: 6px;
        margin-bottom: 2px;
    }

    /* Framework title */
    .framework-title {
        color: #D6E2F0;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 6px;
        letter-spacing: .5px;
    }

    /* Radio group spacing */
    div[role="radiogroup"] {
        gap: 0 !important;
    }

    /* Radio rows */
    div[data-baseweb="radio"] {
        margin: 0 !important;
        padding: 0 !important;
    }

    div[data-baseweb="radio"] label {
        margin: 0 !important;
        padding-top: 2px !important;
        padding-bottom: 2px !important;
        min-height: 24px !important;
    }

    /* Make project names white */
    div[data-baseweb="radio"] * {
        color: #FFFFFF !important;
        opacity: 1 !important;
    }

    /* Optional: slightly brighter selected item */
    div[data-baseweb="radio"]:has(input:checked) p {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    /* Divider spacing */
    hr {
        margin: 8px 0 !important;
        border-top: 1px solid rgba(255,255,255,0.12) !important;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        pass