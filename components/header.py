import streamlit as st
from datetime import datetime


PROJECT_MANAGERS = {
    "Ferry PS": "Conal Cunningham",
    "Flass Lane": "Conal Cunningham",
    "Rossall Outfall": "Emil Takyi",
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

    st.markdown(
        """
        <style>

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.35; }
            100% { opacity: 1; }
        }

        .header-label {
            color: #7FB3FF;
            font-weight: 600;
        }

        .live-status {
            color: #4ADE80;
            font-weight: 700;
            animation: pulse 1.5s infinite;
            text-align: right;
            white-space: nowrap;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container(border=True):

        st.title("Design Performance Dashboard")

        left, right = st.columns([9, 2])

        with left:
            st.markdown(
                f"""
                <span class="header-label">Project:</span> {project}
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <span class="header-label">Current CL32 Snapshot:</span> {snapshot}
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <span class="header-label">Today:</span> {today}
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <span class="header-label">Design Manager:</span> {manager}
                """,
                unsafe_allow_html=True,
            )

        with right:
            st.markdown(
                """
                <div class="live-status">
                    Status: ● LIVE
                </div>
                """,
                unsafe_allow_html=True,
            )

