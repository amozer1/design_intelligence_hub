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

    updated = datetime.now().strftime("%d %b %Y")

    st.markdown("""
    <style>

    div[data-testid="stVerticalBlockBorderWrapper"]{
        border:1px solid #1E4976 !important;
        border-radius:12px !important;
    }

    .dashboard-title{
        color:white;
        font-size:24px;
        font-weight:700;
        margin-bottom:0;
    }

    .dashboard-subtitle{
        color:#9BB3D1;
        font-size:13px;
        margin-bottom:15px;
    }

    .stTextInput input{
        background-color:#0B2D5B !important;
        color:white !important;
        border:1px solid #2F5F98 !important;
        border-radius:8px !important;
    }

    .stTextInput label{
        color:#A7BDD8 !important;
        font-size:12px !important;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.container(border=True):

        st.markdown(
            '<div class="dashboard-title">UU DESIGN PROGRAMME DASHBOARD</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="dashboard-subtitle">CL31 & CL32 • Delivery Tracking • Forecasting</div>',
            unsafe_allow_html=True
        )

        c1, c2, c3, c4, c5 = st.columns(
            [0.4, 3, 3, 1.2, 2]
        )

        with c1:
            st.markdown("### ☰")

        with c2:
            st.text_input(
                "Project",
                value=project,
                disabled=True,
                key="hdr_project"
            )

        with c3:
            st.text_input(
                "Current CL32 Snapshot",
                value=snapshot,
                disabled=True,
                key="hdr_snapshot"
            )

        with c4:
            st.write("")
            st.markdown(
                """
                ### 🔄 🔔 ❓ ⚙️
                """
            )

        with c5:
            st.caption("Design Manager")
            st.markdown(f"**{manager}**")
            st.caption(f"Last Updated: {updated}")