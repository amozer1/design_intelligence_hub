import streamlit as st


def render_branding():

    st.markdown(
        """
        <div style="
            background: linear-gradient(
                135deg,
                #0f172a 0%,
                #1e1b4b 100%
            );
            padding: 20px;
            border-radius: 12px;
            border-left: 4px solid #8b5cf6;
            margin-bottom: 12px;
        ">

            <div style="
                color: white;
                font-size: 22px;
                font-weight: 700;
                line-height: 1.1;
            ">
                🎯 DESIGN<br>
                INTELLIGENCE HUB
            </div>

            <div style="
                margin-top: 10px;
                color: #94a3b8;
                font-size: 12px;
            ">
                Design Smarter. Deliver Better.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
``