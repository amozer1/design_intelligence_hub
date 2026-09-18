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

    today = datetime.now().strftime(
        "%d %b %Y"
    )

    st.markdown(
        f"""
        <div style="
            background:#062447;
            border:1px solid #1d4e89;
            border-radius:12px;
            padding:18px;
            margin-bottom:15px;
        ">
            <div style="
                color:white;
                font-size:28px;
                font-weight:700;
                margin-bottom:2px;
            ">
                UU DESIGN PROGRAMME DASHBOARD
            </div>

            <div style="
                color:#9db8d8;
                font-size:13px;
                margin-bottom:16px;
            ">
                CL31 & CL32 • Delivery Tracking • Forecasting
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3, c4, c5 = st.columns(
        [0.4, 2.7, 2.7, 1.2, 1.8]
    )

    with c1:
        st.markdown("## ☰")

    with c2:
        st.metric(
            "Project",
            project
        )

    with c3:
        st.metric(
            "Current CL32 Snapshot",
            snapshot
        )

    with c4:
        st.markdown(
            """
            ### 🔄 🔔 ❓ ⚙️
            """
        )

    with c5:
        st.metric(
            "Design Manager",
            manager
        )
        st.caption(
            f"Last Updated: {today}"
        )