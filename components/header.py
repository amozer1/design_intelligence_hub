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

    with st.container(border=True):

        st.markdown(
            """
            ## UU DESIGN PROGRAMME DASHBOARD
            ##### CL31 & CL32 • Delivery Tracking • Forecasting
            """
        )

        st.divider()

        c1, c2, c3, c4, c5 = st.columns(
            [0.5, 3, 3, 1.5, 2]
        )

        with c1:
            st.markdown("## ☰")

        with c2:
            st.caption("PROJECT")
            st.markdown(
                f"### {project}"
            )

        with c3:
            st.caption("CURRENT SNAPSHOT")
            st.markdown(
                f"### {snapshot}"
            )

        with c4:
            st.caption("TOOLS")
            st.markdown(
                "### 🔄 🔔 ❓ ⚙️"
            )

        with c5:
            st.caption("DESIGN MANAGER")
            st.markdown(
                f"### {manager}"
            )

            st.caption(
                f"Updated {today}"
            )