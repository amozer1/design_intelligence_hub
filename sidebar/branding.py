import streamlit as st


def render_branding():

    st.image(
        "assets/logo.png",
        width=80
    )

    st.markdown("### Design Management Hub")

    st.caption(
        "Delivering better design decisions"
    )

    st.divider()