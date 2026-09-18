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

    updated = datetime.today().strftime(
        "%d %b %Y"
    )

    st.markdown("""
    <style>

    .header-bar{
        background:#08264F;
        border:1px solid #1B4B77;
        border-radius:12px;
        padding:12px 16px;
        margin-bottom:16px;
    }

    .header-label{
        color:#B7C7DA;
        font-size:11px;
        font-weight:600;
        margin-bottom:4px;
    }

    .header-value{
        color:white;
        font-size:13px;
        font-weight:600;
    }

    </style>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        c1, c2, c3, c4, c5 = st.columns(
            [3, 3, 2, 2, 2]
        )

        with c1:
            st.markdown(
                '<div class="header-label">Project</div>',
                unsafe_allow_html=True
            )

            st.selectbox(
                "",
                [project],
                label_visibility="collapsed"
            )

        with c2:
            st.markdown(
                '<div class="header-label">Current CL32 Snapshot</div>',
                unsafe_allow_html=True
            )

            st.selectbox(
                "",
                [snapshot],
                label_visibility="collapsed"
            )

        with c3:
            st.markdown(
                '<div class="header-label">Design Manager</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="header-value">
                    {design_manager}
                </div>
                """,
                unsafe_allow_html=True
            )

        with c4:
            st.markdown(
                '<div class="header-label">Last Updated</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="header-value">
                    {updated}
                </div>
                """,
                unsafe_allow_html=True
            )

        with c5:
            st.markdown(
                '<div class="header-label">System</div>',
                unsafe_allow_html=True
            )

            st.markdown(
