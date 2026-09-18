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

    st.markdown(
        f"""
        <div style="
            background:#062447;
            border:1px solid #1d4e89;
            border-radius:10px;
            padding:18px 24px;
            margin-bottom:15px;
        ">

            <div style="
                font-size:34px;
                font-weight:700;
                color:#FFFFFF;
                margin-bottom:12px;
                display:flex;
                align-items:center;
                gap:12px;
            ">
                📊 Design Performance Dashboard
            </div>

            <div style="
                color:#FFFFFF;
                font-size:18px;
                font-weight:600;
                line-height:1.5;
            ">
                Project: {project}
                &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
                Date: {today}
                &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
                Design Manager: {manager}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )