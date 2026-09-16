import streamlit as st
from components.sidebar import build_sidebar

st.set_page_config(
    page_title="Design Intelligence Hub",
    page_icon="🎯",
    layout="wide"
)

framework, project, page = build_sidebar()

st.title("Design Intelligence Hub")

st.write(f"Framework: {framework}")
st.write(f"Project: {project}")
st.write(f"Page: {page}")