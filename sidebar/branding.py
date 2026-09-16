import streamlit as st


def render_branding():

    st.image(
        "assets/logo.png",
        width=55
    )

    st.markdown(
        "### DESIGN\n### INTELLIGENCE HUB"
    )

    st.caption(
        "Design Smarter. Deliver Better."
    )

    st.divider()