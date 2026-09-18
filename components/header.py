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

    c1, c2, c3, c4, c5 = st.columns(
        [2, 2, 2, 2, 1],
        gap="medium"
    )

    with c1:

        with st.container(border=True):

            st.markdown("#### PROJECT")
            st.write(project)

    with c2:

        with st.container(border=True):

            st.markdown("#### SNAPSHOT")
            st.write(snapshot)

    with c3:

        with st.container(border=True):

            st.markdown("#### DESIGN MANAGER")
            st.write(design_manager)

    with c4:

        with st.container(border=True):

            st.markdown("#### LAST UPDATED")
            st.write(last_updated)

    with c5:

        with st.container(border=True):

            st.markdown("#### SYSTEM")
            st.write("🔔 ⚙️")