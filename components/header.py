import streamlit as st


PAGE_BG = "#061F3B"
CARD_BG = "#08264F"
CARD_BORDER = "#1B4B77"


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
            background:{CARD_BG};
            border:1px solid {CARD_BORDER};
            border-radius:12px;
            padding:16px;
            height:90px;
            box-shadow:0 2px 8px rgba(0,0,0,0.20);
        ">
            <div style="
                color:#B7C7DA;
                font-size:11px;
                font-weight:600;
                letter-spacing:.5px;
                margin-bottom:8px;
            ">
                {title}
            </div>

            <div style="
                color:white;
                font-size:16px;
                font-weight:700;
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

    cols = st.columns([2, 2, 2, 2, 1])

    with colsheader_card(
            "PROJECT",
            project
        )

    with colsheader_card(
            "SNAPSHOT",
            snapshot
        )

    with colsheader_card(
            "DESIGN MANAGER",
            design_manager
        )

    with colsheader_card(
            "LAST UPDATED",
            snapshot.replace("CL32-", "")
        )

    with colsheader_card(
            "SYSTEM",
            "🔔 ⚙"
        )