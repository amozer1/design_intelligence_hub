import streamlit as st


def render_branding():

    st.markdown("""
    <div style="
        display:flex;
        align-items:center;
        gap:12px;
        padding:4px 0 8px 0;
    ">

        <img
            src="https://murphygroup.com/wp-content/uploadsvg

        <div>

            <div style="
                color:white;
                font-size:15px;
                font-weight:700;
                line-height:1.1;
            ">
                DESIGN<br>
                INTELLIGENCE HUB
            </div>

            <div style="
                color:#B8C7D9;
                font-size:11px;
                margin-top:2px;
            ">
                Design Smarter. Deliver Better.
            </div>

        </div>

    </div>

    <hr style="
        border:none;
        border-top:1px solid rgba(80,120,255,.15);
        margin:8px 0 10px 0;
    ">
    """, unsafe_allow_html=True)