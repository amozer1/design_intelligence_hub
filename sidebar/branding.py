import streamlit as st


def render_branding():

    st.markdown("""
    <style>

    .branding-wrapper{
        padding-bottom:12px;
    }

    .branding-row{
        display:flex;
        align-items:flex-start;
        gap:12px;
    }

    .branding-logo{
        width:52px;
        flex-shrink:0;
    }

    .branding-title{
        color:white;
        font-size:18px;
        font-weight:700;
        line-height:1.05;
        margin:0;
    }

    .branding-tagline{
        color:#C7D2FE;
        font-size:11px;
        margin-top:4px;
    }

    .branding-divider{
        height:1px;
        background:rgba(80,120,255,.15);
        margin-top:12px;
    }

    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(
            "assets/logo.png",
            width=52
        )

    with col2:

        st.markdown("""
        <div class="branding-title">
            DESIGN<br>
            INTELLIGENCE HUB
        </div>

        <div class="branding-tagline">
            Design Smarter. Deliver Better.
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="branding-divider"></div>',
        unsafe_allow_html=True
    )