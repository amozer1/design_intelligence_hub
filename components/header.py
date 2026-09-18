import streamlit as st


def render_header(project, snapshot):

    st.markdown(
        """
        <style>

        div[data-testid="stHorizontalBlock"]{
            align-items:center;
        }

        .header-title{
            color:white;
            font-size:28px;
            font-weight:700;
            margin-bottom:4px;
        }

        .header-subtitle{
            color:#B7C7DA;
            font-size:13px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    with st.container(border=True):

        left, centre, right = st.columns(
            [3, 3, 2]
        )

        with left:

            st.markdown(
                f"""
                <div class="header-title">
                {project}
                </div>

                <div class="header-subtitle">
                Design Management Hub
                </div>
                """,
                unsafe_allow_html=True
            )

        with centre:

            c1, c2 = st.columns(2)

            with c1:
                st.selectbox(
                    "Project",
                    [project],
                    label_visibility="collapsed"
                )

            with c2:
                st.selectbox(
                    "Snapshot",
                    [snapshot],
                    label_visibility="collapsed"
                )

        with right:

            st.button(
                "⬆ Upload CL32",
                use_container_width=True
            )

            i1, i2, i3, i4 = st.columns(4)

            with i1:
                st.markdown("🔄")

            with i2:
                st.markdown("🔔")

            with i3:
                st.markdown("❓")

            with i4:
                st.markdown("⚙️")