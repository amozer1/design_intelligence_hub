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

        title_col, spacer = st.columns([4, 1])

        with title_col:
            st.markdown(
                "## 🚀 Design Performance Dashboard"
            )

        st.markdown(
            f"""
**📁 Project:** {project}
&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
**📅 Date:** {today}
&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
**👤 Design Manager:** {manager}
            """
        )