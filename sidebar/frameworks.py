import streamlit as st


def render_frameworks():

    st.markdown("""
    <hr style="
        border:none;
        border-top:1px solid rgba(80,120,255,.15);
        margin:8px 0 12px 0;
    ">
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        color:#B7C7DA;
        font-size:16px;
        font-weight:700;
        margin-bottom:10px;
    ">
        FRAMEWORKS
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        color:white;
        font-size:15px;
        font-weight:600;
        margin-bottom:4px;
    ">
        ▾ UU Enterprise Framework
    </div>
    """, unsafe_allow_html=True)

    st.markdown("⚪ Pennington Flash")
    st.markdown("⚪ Davyhulme ASP4")

    st.markdown("<div style='height:8px'></div>",
                unsafe_allow_html=True)

    st.markdown("""
    <div style="
        color:white;
        font-size:15px;
        font-weight:600;
        margin-bottom:4px;
    ">
        ▾ UU DD&B Framework
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        background:linear-gradient(
            90deg,
            #6624D6,
            #7C3AED
        );
        border-radius:8px;
        padding:10px 12px;
        color:white;
        font-weight:600;
        margin-bottom:6px;
    ">
        🔴 Ferry PS
    </div>
    """, unsafe_allow_html=True)

    st.markdown("🟠 Rossall Outfall")
    st.markdown("🟢 Flass Lane")
    st.markdown("🟡 Tally Ho")
    st.markdown("🟢 Eccleston Bridge")
