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

    st.markdown(
        """
        <style>

        div[data-testid="stHorizontalBlock"]{
            align-items:center;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]{
            border:1px solid #183B63 !important;
            border-radius:12px !important;
            background:#071D3A;
        }

        .stSelectbox label{
            color:white !important;
            font-size:12px !important;
            font-weight:600 !important;
        }

        .stSelectbox > div > div{
            background-color:#0C2950 !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    with st.container(border=True):

        col1, col2, col3, col4, col5 = st.columns(
            [0.5, 3.5, 3, 1.5, 2]
        )

        with col1:
            st.markdown("### ☰")

        with col2:
            st.selectbox(
                "Project",
                [project],
                disabled=True,
                key="header_project"
            )

        with col3:
            st.selectbox(
                "Current CL32 Snapshot",
                [today],
                disabled=True,
                key="header_date"
            )

        with col4:
            st.caption("Actions")
            st.write("🔄  🔔  ❓  ⚙️")

        with col5:
            st.caption("User")
            st.write(f"👤 {manager}")