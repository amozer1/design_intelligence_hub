import streamlit as st


def render_branding():

    logo, text = st.columns([1, 3])

    with logo:
        st.image("assets/logo.png", width=70)

    with text:

        st.markdown("""
        <div style="
            color:white;
            font-size:24px;
            font-weight:700;
            line-height:1.05;
            margin-top:6px;
        ">
            DESIGN<br>
            INTELLIGENCE HUB
        </div>

        <div style="
            color:#CBD5E1;
            font-size:14px;
            margin-top:6px;
        ">
            Design Smarter. Deliver Better.
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        "<div style='padding-bottom:16px'></div>",
        unsafe_allow_html=True
    )