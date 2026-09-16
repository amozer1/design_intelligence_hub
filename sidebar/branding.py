import streamlit as st


def render_branding():

    col1, col2 = st.columns([1, 4])

    with col1:
        st.image(
            "assets/logo.png",
            width=60
        )

    with col2:

        st.markdown("""
        <div style="
            color:white;
            font-size:32px;
            font-weight:700;
            line-height:1.0;
        ">
            DESIGN<br>
            INTELLIGENCE HUB
        </div>

        <div style="
            color:#cbd5e1;
            font-size:16px;
            margin-top:8px;
        ">
            Design Smarter. Deliver Better.
        </div>
        """, unsafe_allow_html=True)