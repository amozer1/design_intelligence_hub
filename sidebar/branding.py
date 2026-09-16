import streamlit as st


def render_branding():

    st.markdown("""
    <style>

    .branding-container{
        padding-bottom:8px;
    }

    .branding-row{
        display:flex;
        align-items:flex-start;
        gap:10px;
    }

    .branding-logo{
        width:42px;
        flex-shrink:0;
    }

    .branding-title{
        color:#FFFFFF;
        font-size:17px;
        font-weight:700;
        line-height:1.05;
        margin:0;
        padding:0;
    }

    .branding-tagline{
        color:#B8C7D9;
        font-size:11px;
        line-height:1.2;
        margin-top:3px;
    }

    .branding-divider{
        height:1px;
        background:rgba(80,120,255,.15);
        margin-top:10px;
    }

    </style>
    """, unsafe_allow_html=True)

    logo_col, text_col = st.columns(
        [1, 4],
        gap="small"
    )

    with logo_col:

        st.image(
            "assets/logo.png",
            width=42
        )

    with text_col:

        st.markdown("""
        <div class="branding-title">
            DESIGN<br>
            INTELLIGENCE HUB
        </div>

        <div class="branding-tagline">
            Design Smarter. Deliver Better.
        </div>
        """,
        unsafe_allow_html=True)

    st.markdown(
        '<div class="branding-divider"></div>',
        unsafe_allow_html=True
    )