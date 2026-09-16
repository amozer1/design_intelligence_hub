import streamlit as st


def render_branding():

    left, right = st.columns([1.2, 4])

    with left:
        st.image("assets/logo.png", width=70)

    with right:

        st.markdown("""
        <div style="
            color:white;
            font-size:28px;
            font-weight:800;
            line-height:1.05;
            margin-top:2px;
        ">
            DESIGN<br>
            INTELLIGENCE HUB
        </div>

        <div style="
            color:#cbd5e1;
            font-size:15px;
            margin-top:8px;
        ">
            Design Smarter. Deliver Better.
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        "<div style='height:20px'></div>",
        unsafe_allow_html=True
    )