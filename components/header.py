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

    today = datetime.now().strftime("%d %b %Y")

    with st.container(border=True):

        a, b, c = st.columns([4, 2, 3])

        with a:
            st.subheader(project)

        with b:
            st.subheader(today)

        with c:
            st.subheader(manager)

        st.caption(
            "UU DESIGN PROGRAMME DASHBOARD • CL31 & CL32 • Delivery Tracking • Forecasting"
        )