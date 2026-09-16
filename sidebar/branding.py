import streamlit as st


def render_branding():

    st.image(
        "assets/logo.png",
        width=85
    )

    st.markdown(
        """
        <p style="
            color:white;
            font-size:22px;
            font-weight:700;
            line-height:1.05;
            margin:0;
            padding:0;
        ">
            DESIGN INTELLIGENCE HUB
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="
            color:#CBD5E1;
            font-size:13px;
            margin:0;
            padding:0;
        ">
            Design Smarter. Deliver Better.
        </p>
        """,
        unsafe_allow_html=True
    )