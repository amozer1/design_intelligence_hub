import streamlit as st


def render_branding():

    st.markdown("""
    <div style="
        background:#041124;
        padding:24px 20px 18px 20px;
        border-radius:12px;
    ">

        <div style="
            display:flex;
            align-items:center;
            gap:16px;
        ">

            <img src="data:image/png;base64,..."
                         <div style="
                    color:white;
                    font-size:24px;
                    font-weight:700;
                    line-height:1.05;
                ">
                    DESIGN<br>
                    INTELLIGENCE HUB
                </div>

                <div style="
                    color:#CBD5E1;
                    font-size:14px;
                    margin-top:6px;
                ">
                    Design Smarter. Deliver Better.
                </div>

            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)