import streamlit as st


def render_branding():

    st.markdown("""
    <div style="
        padding:20px;
        border-radius:12px;
        background:linear-gradient(
            135deg,
            #0f172a,
            #1e1b4b
        );
        border-left:4px solid #8b5cf6;
        margin-bottom:8px;
    ">

        <div style="
            font-size:24px;
            font-weight:700;
            color:white;
            line-height:1.1;
        ">
            DESIGN<br>
            INTELLIGENCE HUB
        </div>

        <div style="
            margin-top:8px;
            font-size:12px;
            color:#94a3b8;
        ">
            Design Smarter. Deliver Better.
        </div>

    </div>
    """, unsafe_allow_html=True)
