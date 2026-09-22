import streamlit as st


def render(cl32):

    with st.container(border=True):

        st.markdown("### Executive Summary")

        st.markdown(
            """
            <div style="
                background:#062B5B;
                color:white;
                padding:10px;
                border-radius:8px;
                display:inline-block;
            ">
                AT RISK
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("Health Score: 55%")
        st.write("26 days behind baseline")
        st.write("31 activities with negative float")
        st.write("43 deliverables ≤5d float")

        st.write("Design Readiness: 37%")