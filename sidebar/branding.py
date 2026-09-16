import streamlit as st


def render_branding():

    st.markdown("""
    <div style="
        display:flex;
        align-items:center;
        gap:10px;
        margin-bottom:8px;
    ">
        https://placehold.co/50x30

        <div>

            <div style="
                color:white;
                font-size:20px;
                font-weight:700;
                line-height:1.0;
            ">
                DESIGN<br>
                INTELLIGENCE HUB
            </div>

            <div style="
                color:#B8C7D9;
                font-size:12px;
                margin-top:3px;
            ">
                Design Smarter. Deliver Better.
            </div>

        </div>
    </div>

    <hr style="
        border:none;
        border-top:1px solid rgba(80,120,255,.15);
        margin:8px 0;
    ">
    """,
    unsafe_allow_html=True)