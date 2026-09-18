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

        st.title("Design Performance Dashboard")

        st.write(
            f"**Project:** {project}    "
            f"&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp; "
            f"**Current CL32 Snapshot:** {snapshot}    "
            f"&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp; "
            f"**Date:** {today}    "
            f"&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp; "
            f"**Design Manager:** {manager}",
            unsafe_allow_html=True
        )