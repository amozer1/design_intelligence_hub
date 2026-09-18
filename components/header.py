import streamlit as st
from datetime import datetime


PROJECT_MANAGERS = {
    "Ferry PS": "Conal Cunningham",
    "Flass Lane": "Conal Cunningham",

    "Rossall Outfall": "Michael Harbon",

    "Tally Ho": "Ebenezer Amoako",
    "Eccleston Bridge": "Ebenezer Amoako",
    "Pennington Flash": "Ebenezer Amoako",
    "Davyhulme ASP4": "Ebenezer Amoako"
}


def render_header(project, snapshot):

    design_manager = PROJECT_MANAGERS.get(
        project,
        "Not Assigned"
    )

    last_updated = datetime.today().strftime(
        "%d %b %Y"
    )

    st.markdown("""
    <style>

    .toolbar {
        background: #08264F;
        border: 1px solid #1B4B77;
        border-radius: 12px;
        padding: 12px 18px;
        margin-bottom: 18px;
    }

    .toolbar-label {
        color: #B7C7DA;
        font-size: 11px;
        font-weight: 600;
    }

    .toolbar-value {
        color: white;
        font-size: 13px;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.container(border=True):

        c0, c1, c2, c3, c4 = st.columns(
            [0.5, 3, 3, 2, 2],
            gap="medium"
        )

        with c0:

            st.write("")
            st.markdown("### ☰")

        with c1:

            st.caption("Project")

            st.selectbox(
                "",
                [project],
                label_visibility="collapsed"
            )

        with c2:

            st.caption("Current CL32 Snapshot")

            st.selectbox(
                "",
                [snapshot],
                label_visibility="collapsed"
            )

        with c3:

            st.caption("Design Manager")

            st.markdown(
                f"**{design_manager}**"
            )

        with c4:

            st.caption("System")

            icons = st.columns(2)

            with iconsst.markdown("🔔")

            with iconsst.markdown("⚙️")

            st.caption(
                f"Last Updated: {last_updated}"
            )