import streamlit as st


def render_branding():

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(
            "assets/logo.png",
            width=55
        )

    with col2:

        st.markdown("""
        <div style="
            color:white;
            font-weight:700;
            font-size:16px;
            line-height:1.1;
            margin-top:2px;
        ">
            DESIGN<br>
            INTELLIGENCE HUB
        </div>

        <div style="
            color:#cbd5e1;
            font-size:11px;
            margin-top:4px;
        ">
            Design Smarter. Deliver Better.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:12px'></div>",
                unsafe_allow_html=True)