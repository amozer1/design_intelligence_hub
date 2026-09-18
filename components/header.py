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

    st.markdown("""
    <style>

    .header-card {
        background: #0D315F;
        border: 2px solid #2F6AA3;
        border-radius: 12px;
        padding: 18px;
        min-height: 95px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }

    .header-label {
        color: #DCE8F5;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.6px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .header-value {
        color: white;
        font-size: 18px;
        font-weight: 700;
        line-height: 1.2;
    }

    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(
        [2, 2, 2, 2, 1],
        gap="large"
    )

    with col1:
        st.markdown(
            f"""
            <div class="header-card">
                <div class="header-label">PROJECT</div>
                <div class="header-value">{project}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="header-card">
                <div class="header-label">SNAPSHOT</div>
                <div class="header-value">{snapshot}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="header-card">
                <div class="header-label">DESIGN MANAGER</div>
                <div class="header-value">{design_manager}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="header-card">
                <div class="header-label">LAST UPDATED</div>
                <div class="header-value">{last_updated}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            """
            <div class="header-card">
                <div class="header-label">SYSTEM</div>
                <div class="header-value">🔔 ⚙️</div>
            </div>
            """,
            unsafe_allow_html=True
        )