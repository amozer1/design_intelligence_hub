import streamlit as st


PROJECT_MANAGERS = {
    "Ferry PS": "Conal Cunningham",
    "Flass Lane": "Conal Cunningham",
    "Rossall Outfall": "Michael Harbon",
    "Tally Ho": "Ebenezer Amoako",
    "Eccleston Bridge": "Ebenezer Amoako",
    "Pennington Flash": "Ebenezer Amoako",
    "Davyhulme ASP4": "Ebenezer Amoako"
}


def header_card(title, value):

    with st.container(border=True):

        st.markdown(
            f"<span style='color:#DCE8F5;font-size:12px;font-weight:700'>{title}</span>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<span style='color:white;font-size:22px;font-weight:700'>{value}</span>",
            unsafe_allow_html=True
        )


def render_header(project, snapshot):

    design_manager = PROJECT_MANAGERS.get(
        project,
        "Not Assigned"
    )

    last_updated = snapshot.replace(
        "CL32-",
        ""
    )

    c1, c2, c3, c4, c5 = st.columns(
        [2, 2, 2, 2, 1]
    )

    with c1:
        header_card("PROJECT", project)

    with c2:
        header_card("SNAPSHOT", snapshot)

    with c3:
        header_card("DESIGN MANAGER", design_manager)

    with c4:
        header_card("LAST UPDATED", last_updated)

    with c5:
        header_card("SYSTEM", "🔔 ⚙️")
