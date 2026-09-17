import streamlit as st


def render_branding():

    st.markdown("""
    <style>

    .hub-container{
        margin-bottom:20px;
    }

    .hub-title{
        color:#FFFFFF;
        font-size:26px;
        font-weight:800;
        line-height:1.1;
        letter-spacing:-0.5px;
        margin-top:8px;
        margin-bottom:6px;
    }

    .hub-subtitle{
        color:#B7C7DA;
        font-size:13px;
        line-height:1.4;
        margin-bottom:18px;
    }

    .hub-divider{
        border:none;
        border-top:1px solid rgba(255,255,255,0.10);
        margin:18px 0;
    }

    </style>
    """, unsafe_allow_html=True)

    # Logo
    st.image(
        "assets/logo.png",  # update path if needed
        width=90
    )

    # Brand text
    st.markdown(
        """
        <div class="hub-container">

            <div class="hub-title">
                DESIGN INTELLIGENCE HUB
            </div>

            <div class="hub-subtitle">
                Design Smarter.<br>
                Deliver Better.
            </div>

        </div>

        <hr class="hub-divider">
        """,
        unsafe_allow_html=True
    )