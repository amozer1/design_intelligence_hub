import streamlit as st

from sidebar.layout import render_sidebar
from sidebar.branding import render_branding


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Design Intelligence Hub",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# SIDEBAR LAYOUT
# ==================================================

slots = render_sidebar()

# ==================================================
# BRANDING
# ==================================================

with slots["branding"]:
    render_branding()

# ==================================================
# MAIN PAGE
# ==================================================

st.title("Dashboard")