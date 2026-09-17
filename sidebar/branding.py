import streamlit as st


def render_branding():

    st.markdown("""
    <style>

    .hub-title {
        color: #FFFFFF;
        font-size: 24px;
        font-weight: 700;
        line-height: 1.2;
        margin-bottom: 4px;
    }

    .hub-subtitle {
        color: #B7C7DA;
        font-size: 13px;
        margin-bottom: 16px;
    }

    </style>
    """, unsafe_allow_html=True)

    # Logo
    st.image(
        "assets/logo.png",  # update path if required
        width=90
    )

    st.markdown(
        """
        <div class="hub-title">
            Design Management Hub
        </div>

        <div class="hub-subtitle">
            Delivering Better Design Decisions
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()