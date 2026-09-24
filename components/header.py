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

        .header-panel {
            background: #10203A;
            padding: 20px;
            border-radius: 14px;
            border: 1px solid #1E3A5F;
            box-shadow:
                0 2px 6px rgba(0,0,0,0.15),
                0 12px 24px rgba(0,0,0,0.08);
            margin-bottom: 10px;
        }

        .dashboard-title {
            color: white;
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .header-label {
            color: #93C5FD;
            font-weight: 600;
        }

        .header-value {
            color: white;
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

    st.markdown(
        '<div class="header-panel">',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="dashboard-title">
            Design Performance Dashboard
        </div>
        """,
        unsafe_allow_html=True
    )

    left, right = st.columns([9, 2])

    with left:

        st.markdown(
            f"""
            <span class="header-label">Project:</span>
            <span class="header-value">{project}</span>

            &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;

            <span class="header-label">Current CL32 Snapshot:</span>
            <span class="header-value">{snapshot}</span>

            &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;

            <span class="header-label">Today:</span>
            <span class="header-value">{today}</span>

            &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;

            <span class="header-label">Design Manager:</span>
            <span class="header-value">{manager}</span>
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
        unsafe_allow_html=True
    )