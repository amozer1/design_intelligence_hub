import streamlit as st

from sidebar.layout import render_sidebar


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
# SIDEBAR
# ==================================================

render_sidebar()

# ==================================================
# MAIN PAGE
# ==================================================

st.title("Dashboard")

st.write("Main page content goes here...")