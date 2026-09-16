import streamlit as st


def render_branding():

    st.image(
        "assets/logo.png",
        width=90
    )

    st.markdown(
        """
        <div style="
            color:white;
            font-size:24px;
            font-weight:700;
            line-height:1.1;
            margin-top:-4px;
        ">
            DESIGN INTELLIGENCE HUB
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            color:#CBD5E1;
            font-size:13px;
            margin-top:2px;
            margin-bottom:6px;
        ">
            Design Smarter. Deliver Better.
        </div>
        """,
        unsafe_allow_html=True
    )