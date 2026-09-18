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

    design_manager = PROJECT_MANAGERS.get(
        project,
        "Not Assigned"
    )

    updated = datetime.now().strftime(
        "%d %b %Y %H:%M"
    )

    with st.container(border=True):

        c1, c2, c3, c4, c5, c6 = st.columns(
            [0.4, 2.8, 2.8, 2.0, 1.0, 2.2]
        )

        with c1:
            st.markdown("### ☰")

        with c2:
            st.selectbox(
                "Project",
                [project],
                key="project_header"
            )

        with c3:
            st.selectbox(
                "Current CL32 Snapshot",
                [snapshot],
                key="snapshot_header"
            )

        with c4:
            st.write("")
            st.button(
                "⬆ Upload New CL32",
                type="primary",
                use_container_width=True
            )

        with c5:
            st.write("")
            st.write("🔄")
            st.write("🔔")

        with c6:
            st.markdown(
                f"""
**{design_manager}**

Last Updated: {updated}
                """
            )

    st.divider()


# PAGE
st.set_page_config(
    page_title="CL32 Dashboard",
    layout="wide"
)

render_header(
    project="Ferry PS",
    snapshot="30 Sep 2026"
)

st.title("CL32 Dashboard")