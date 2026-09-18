import streamlit as st
from datetime import datetime


PROJECT_MANAGERS = {
    "Ferry PS": "Conal Cunningham",
    "Flass Lane": "Conal Cunningham",
    "Rossall Outfall": "Michael Harbon",
    "Tally Ho": "Ebenezer Amoako",
    "Eccleston Bridge": "Ebenezer Amoako",
    "Pennington Flash": "Ebenezer Amoako",
    "Davyhulme ASP4": "Ebenezer Amoako",
}


def render_header(project, snapshot=None):

    manager = PROJECT_MANAGERS.get(
        project,
        "Not Assigned"
    )

    today = datetime.now().strftime(
        "%d %b %Y"
    )

    with st.container(border=True):

        st.markdown("## Design Performance Dashboard")
        st.caption(
            "CL31 & CL32 Delivery Performance • Forecasting • Programme Controls"
        )

        st.divider()

        col1, col2, col3 = st.columns([3, 2, 3])

        with col1:
            st.markdown(
                f"""
**PROJECT**

📁 {project}
                """
            )

        with col2:
            st.markdown(
                f"""
**DATE**

📅 {today}
                """
            )

        with col3:
            st.markdown(
                f"""
**DESIGN MANAGER**

👤 {manager}
                """
            )