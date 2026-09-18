import streamlit as st
from datetime import datetime


def render_header(project, snapshot):

    today = datetime.today().strftime("%d %b %Y")

    st.markdown("""
    <style>

    .header-container{
        background:#FFFFFF;
        padding:20px 24px;
        border-radius:12px;
        border:1px solid #E5E7EB;
        margin-bottom:20px;
    }

    .header-label{
        color:#6B7280;
        font-size:11px;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:.5px;
    }

    .header-value{
        color:#111827;
        font-size:20px;
        font-weight:700;
    }

    .header-date{
        color:#6B7280;
        font-size:13px;
    }

    </style>
    """, unsafe_allow_html=True)

    left, middle, right = st.columns([4, 3, 2])

    with left:

        st.markdown(
            '<div class="header-label">Project</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="header-value">{project}</div>',
            unsafe_allow_html=True
        )

    with middle:

        st.markdown(
            '<div class="header-label">Current Snapshot</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="header-value">{snapshot}</div>',
            unsafe_allow_html=True
        )

    with right:

        st.markdown(
            '<div class="header-label">Design Manager</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="header-value">Ebenezer Amoako</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="header-date">
            Last Refreshed: {today}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()