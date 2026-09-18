import streamlit as st


def render_header(project, snapshot):

    st.markdown("""
    <style>

    .hub-header {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 20px;
    }

    .hub-label {
        color: #6B7280;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: .5px;
        margin-bottom: 4px;
    }

    .hub-value {
        color: #111827;
        font-size: 20px;
        font-weight: 700;
    }

    .hub-sub {
        color: #6B7280;
        font-size: 13px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="hub-header">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([4, 3, 3])

    with col1:

        st.markdown(
            '<div class="hub-label">Project</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="hub-value">{project}</div>',
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            '<div class="hub-label">Current Snapshot</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="hub-value">{snapshot}</div>',
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            '<div class="hub-label">Design Manager</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="hub-value">Ebenezer Amoako</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="hub-sub">Design Intelligence Hub</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)