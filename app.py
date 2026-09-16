import streamlit as st

from sidebar.layout import render_sidebar
from sidebar.branding import render_branding
from sidebar.frameworks import render_frameworks


st.set_page_config(
    page_title="Design Intelligence Hub",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

render_sidebar()

with st.sidebar:

    render_branding()

    render_frameworks()

st.title("Dashboard")