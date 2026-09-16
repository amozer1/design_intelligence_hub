import streamlit as st


def render_frameworks():

    st.markdown("""
    <div class="sidebar-section">

        <div class="section-title">
            FRAMEWORKS
        </div>

    </div>
    """, unsafe_allow_html=True)

    with st.expander(
        "UU Enterprise Framework",
        expanded=False
    ):

        st.markdown("⚪ Pennington Flash")
        st.markdown("⚪ Davyhulme ASP4")

    with st.expander(
        "UU DD&B Framework",
        expanded=True
    ):

        st.markdown("""
        <div style="
            background:#6D28D9;
            border-radius:6px;
            padding:8px 12px;
            color:white;
            margin-bottom:8px;
            font-weight:600;
        ">
        🔴 Ferry PS
        </div>
        """, unsafe_allow_html=True)

        st.markdown("🟠 Rossall Outfall")
        st.markdown("🟢 Flass Lane")
        st.markdown("🟡 Tally Ho")
        st.markdown("🟢 Eccleston Bridge")

    st.markdown("""
    <hr style="
        border:none;
        border-top:1px solid rgba(59,130,246,0.15);
        margin-top:16px;
        margin-bottom:0px;
    ">
    """, unsafe_allow_html=True)