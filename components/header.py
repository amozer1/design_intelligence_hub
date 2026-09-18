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
        left, right = st.columns([9, 1])

        with left:
            st.write(
                f"**Project:** {project}    "
                f"|    "
                f"**Current CL32 Snapshot:** {snapshot}    "
                f"|    "
                f"**Today:** {today}    "
                f"|    "
                f"**Design Manager:** {manager}"
            )

        with right:
            st.write(f"**Status:** {status}")
        `