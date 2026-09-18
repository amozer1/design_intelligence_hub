import streamlit as st


def render_header(project, snapshot):

    st.markdown("""
    <style>

    .header-card{
        background:#08264F;
        border:1px solid #1B4B77;
        border-radius:12px;
        padding:14px;
        margin-bottom:16px;
    }

    .header-label{
        color:#B7C7DA;
        font-size:11px;
        font-weight:600;
        margin-bottom:4px;
    }

    .header-value{
        color:white;
        font-size:14px;
        font-weight:600;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.container(border=True):

        col1, col2, col3, col4, col5 = st.columns(
            [3, 3, 2, 1.5, 2]
        )

        with col1:

            st.selectbox(
                "Project",
                [project],
                index=0
            )

        with col2:

            st.selectbox(
                "Current CL32 Snapshot",
                [snapshot],
                index=0
            )

        with col3:

            st.write("")
            st.button(
                "⬆ Upload New CL32",
                use_container_width=True,
                type="primary"
            )

        with col4:

            st.write("")
            st.write("")

            i1, i2, i3, i4 = st.columns(4)

            with i1:
                st.markdown("🔄")

            with i2:
                st.markdown("🔔")

            with i3:
                st.markdown("❓")

            with i4:
                st.markdown("⚙️")

        with col5:

            st.selectbox(
                "Design Manager",
                [
                    "Ebenezer Amoako"
                ],
                index=0
            )

            st.caption(
                f"Last Updated: {snapshot}"
            )
