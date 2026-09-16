import streamlit as st

from sidebar.layout import render_sidebar
from sidebar.branding import render_branding


st.set_page_config(
    page_title="Design Intelligence Hub",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

slots = render_sidebar()

# FIRST container
with slots["branding"]:
    render_branding()

st.title("Dashboard")