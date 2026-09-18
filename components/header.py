import streamlit as st


PROJECT_MANAGERS = {
    "Ferry PS": "Conal Cunningham",
    "Flass Lane": "Conal Cunningham",

    "Tally Ho": "Ebenezer Amoako",
    "Eccleston Bridge": "Ebenezer Amoako",
    "Pennington Flash": "Ebenezer Amoako",
    "Davyhulme ASP4": "Ebenezer Amoako",

    "Rossall Outfall": "Michael Harbon"
}


def header_card(title, value):

    st.markdown(
        f"""
        <div style="
            background:#08264F;
            border:1px solid #1B4B77;
            border-radius:12px;
            padding:14px;
            height:80px;
        ">
            <div style="
                color:#DCE8F5;
                font-size:11px;
                font-weight:700;
                letter-spacing:0.6px;
                margin-bottom:10px;
                text-transform:uppercase;
            ">
                {title}
            </div>

            <div style="
                color:#FFFFFF;
                font-size:18px;
                font-weight:700;
                line-height:1.1;
            ">
                {value}
            </div>
        </div>
        """,
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

    col1, col2, col3, col4, col5 = st.columns(
        [2, 2, 2, 2, 1]
    )

    with col1:
        header_card(
            "Project",
            project
        )

    with col2:
        header_card(
            "Snapshot",
            snapshot
        )

    with col3:
        header_card(
            "Design Manager",
            design_manager
        )

    with col4:
        header_card(
            "Last Updated",
            last_updated
        )

    with col5:
        header_card(
            "System",
            "🔔 ⚙️"
        )