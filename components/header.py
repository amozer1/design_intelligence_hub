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


def render_header(project, snapshot):

    manager = PROJECT_MANAGERS.get(
        project,
        "Not Assigned"
    )

    updated = datetime.now().strftime(
        "%d %b %Y %H:%M"
    )

    st.markdown("""
    <style>

    .stApp {
        background: #0b1020;
    }

    .navbar {
        background: linear-gradient(90deg,#07142b,#0b1c3d);
        border: 1px solid rgba(80,120,255,.25);
        border-radius: 12px;
        padding: 0.75rem;
        margin-bottom: 1rem;
    }

    div[data-testid="stButton"] button {
        background: #6d28ff !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }

    div[data-testid="stInfo"] {
        background-color: rgba(255,255,255,.03);
        border: 1px solid rgba(255,255,255,.12);
        border-radius: 8px;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.container(border=True):

        c1, c2, c3, c4, c5, c6 = st.columns(
            [0.4, 3, 3, 2, 1.2, 2]
        )

        # Menu
        with c1:
            st.markdown("### ☰")

        # Project Card
        with c2:
            st.caption("Project")
            st.info(project)

        # Snapshot Card
        with c3:
            st.caption("Current CL32 Snapshot")
            st.info(snapshot)

        # Upload Button Card
        with c4:
            st.write("")
            st.button(
                "⬆ Upload New CL32",
                use_container_width=True
            )

        # Icons Card
        with c5:
            st.write("")
            st.markdown(
                """
                🔄  🔔

                ❓  ⚙️
                """
            )

        # User Card
        with c6:
            st.caption("Design Manager")
            st.markdown(f"**{manager}**")
            st.caption(
                f"Last Updated: {updated}"
            )