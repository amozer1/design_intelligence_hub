import streamlit as st


def render_branding():

    st.image(
        "assets/logo.png",
        width=90
    )

    st.markdown(
        """
        <span style="
        color:white;
        font-size:26px;
        font-weight:700;
        ">
        DESIGN
        </span>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <span style="
        color:white;
        font-size:26px;
        font-weight:700;
        ">
        INTELLIGENCE HUB
        </span>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <span style="
        color:#CBD5E1;
        font-size:14px;
        ">
        Design Smarter. Deliver Better.
        </span>
        """,
        unsafe_allow_html=True
    )

    st.divider()