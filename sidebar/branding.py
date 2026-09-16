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
            margin-top:-6px;
            margin-bottom:2px;
        ">
            DESIGN INTELLIGENCE HUB
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            color:#B8C7D9;
            font-size:13px;
            margin-bottom:8px;
        ">
            Design Smarter. Deliver Better.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()