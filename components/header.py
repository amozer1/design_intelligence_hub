import streamlit as st


def render_header(project, snapshot):

    st.markdown("""
    <style>

    .header-bar{
        background:#08264F;
        border:1px solid #1B4B77;
        border-radius:12px;
        padding:14px 18px;
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

    .upload-btn{
        background:#6D28D9;
        color:white;
        padding:8px 18px;
        border-radius:8px;
        text-align:center;
        font-weight:600;
        border:none;
    }

    .last-updated{
        color:#B7C7DA;
        font-size:11px;
        text-align:right;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.container(border=True):

        c1, c2, c3, c4, c5 = st.columns(
            [3, 3, 2, 1, 2]
        )

        with c1:

            st.selectbox(
                "Project",
                [project],
                label_visibility="visible"
            )

        with c2:

            st.selectbox(
                "Current CL32 Snapshot",
                [snapshot],
                label_visibility="visible"
            )

        with c3:

            st.write("")
            st.button(
                "⬆ Upload New CL32",
                use_container_width=True
            )

        with c4:

            st.write("")
            st.write("")

            icons = st.columns(4)

            icons[0].write("🔄")
            icons[1].write("🔔")
            icons[2].write("❓")
            icons[3].write("⚙️")

        with c5:

            st.selectbox(
                "Design Manager",
                [
                    "Ebenezer Amoako"
                ],
                label_visibility="visible"
            )

            st.caption(
                f"Last Updated: {snapshot}"
            )