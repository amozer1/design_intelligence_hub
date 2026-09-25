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

        .dashboard-header {
            background: linear-gradient(
                135deg,
                #0F172A 0%,
                #1E3A8A 100%
            );
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 1rem;
            color: white;
            box-shadow: 0 6px 16px rgba(0,0,0,0.12);
        }

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.35; }
            100% { opacity: 1; }
        }

        .dashboard-title {
            font-size: 2rem;
            font-weight: 700;
            color: white;
            margin-bottom: 12px;
        }

        .header-label {
            color: #93C5FD;
            font-weight: 700;
        }

        .header-details {
            color: white;
            font-size: 0.95rem;
        }

        .live-status {
            color: #4ADE80;
            font-weight: 700;
            animation: pulse 1.5s infinite;
            text-align: right;
            white-space: nowrap;
            font-size: 1rem;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="dashboard-header">',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="dashboard-title">
            Design Performance Dashboard
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([9, 2])

    with left:

        st.markdown(
            f"""
            <div class="header-details">

            <span class="header-label">Project:</span>
            {project}

            &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;

            <span class="header-label">Current CL32 Snapshot:</span>
            {snapshot}

            &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;

            <span class="header-label">Today:</span>
            {today}

            &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;

            <span class="header-label">Design Manager:</span>
            {manager}

            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:

        st.markdown(
            """
            <div class="live-status">
                ● LIVE
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )