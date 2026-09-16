import streamlit as st


def render_branding():

    col_logo, col_text = st.columns(
        [1, 5],
        gap="small"
    )

    with col_logo:

        st.image(
            "assets/logo.png",
            width=50
        )

    with col_text:

        st.markdown("""
        <div style="
            color:white;
            font-size:20px;
            font-weight:700;
            line-height:1.0;
            margin:0;
            padding:0;
        ">
            DESIGN<br>
            INTELLIGENCE HUB
        </div>

        <div style="
            color:#C7D2FE;
            font-size:12px;
            margin-top:4px;
        ">
            Design Smarter. Deliver Better.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <hr style="
        border:none;
        border-top:1px solid rgba(80,120,255,.15);
        margin:8px 0;
    ">
    """, unsafe_allow_html=True)