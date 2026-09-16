import streamlit as st


def render_frameworks():

    st.markdown("""
    <div style="
        color:#94A3B8;
        font-size:11px;
        font-weight:600;
        letter-spacing:1px;
        margin-bottom:12px;
    ">
        FRAMEWORKS
    </div>
    """, unsafe_allow_html=True)

    with st.expander(
        "UU Enterprise Framework",
        expanded=False
    ):
        st.write("Pennington Flash")
        st.write("Davyhulme ASP4")

    with st.expander(
        "UU DD&B Framework",
        expanded=True
    ):
        st.markdown("""
        <div style="
            background:#6D28D9;
            border-radius:8px;
            padding:10px 12px;
            color:white;
            font-weight:600;
            margin-bottom:8px;
        ">
            ● Ferry PS
        </div>
        """, unsafe_allow_html=True)

        st.markdown("🟠 Rossall Outfall")
        st.markdown("🟢 Flass Lane")
        st.markdown("🟡 Tally Ho")
        st.markdown("🟢 Eccleston Bridge")