import streamlit as st
from datetime import datetime

st.markdown("""
<style>

/* Remove Streamlit top bar */
[data-testid="stHeader"] {
    display: none;
}

/* Remove floating deploy/menu controls */
[data-testid="stToolbar"] {
    display: none;
}

/* Remove top padding */
.block-container {
    padding-top: 0.5rem !important;
}

/* Dark background */
.stApp {
    background: #061F3B;
}

</style>
""", unsafe_allow_html=True)


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

    with st.container(border=True):

        st.markdown(
            f"""
### 📊 Executive Dashboard

**Project:** {project} &nbsp;&nbsp;&nbsp;&nbsp; |
&nbsp;&nbsp;&nbsp;&nbsp;
**Date:** {today}
&nbsp;&nbsp;&nbsp;&nbsp; |
&nbsp;&nbsp;&nbsp;&nbsp;
**Design Manager:** {manager}
            """
        )

        c1, c2, c3, c4 = st.columns(
            [3, 3, 2, 2]
        )

        with c1:
            st.info(f"📁 {project}")

        with c2:
            st.info(f"📅 {today}")

        with c3:
            st.info("🔄 Refresh")

        with c4:
            st.info(f"👤 {manager}")