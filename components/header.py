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
            color: #2563EB;
            font-weight: 600;
        }

        .dashboard-title {
            color: #111827;
            font-size: 2.3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .header-value {
            color: #374151;
        }

        .live-status {
            color: #22C55E;
            font-weight: 700;
            animation: pulse 1.5s infinite;
            text-align: right;
            white-space: nowrap;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # Accent strip

    st.markdown(
        """
        <div style="
            height:6px;
            background:#2563EB;
            border-radius:10px;
            margin-bottom:12px;
        ">
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.container(border=True):

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