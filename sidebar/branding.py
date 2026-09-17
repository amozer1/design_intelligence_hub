import streamlit as st


def render_branding():

    st.markdown(
        """
        <style>

        .hub-title {
            color: white;
            font-size: 28px;
            font-weight: 700;
            line-height: 1.1;
            margin-top: 0px;
            margin-bottom: 4px;
        }

        .hub-subtitle {
            color: #C9D6E5;
            font-size: 13px;
            margin-bottom: 12px;
        }

        .hub-divider {
            border: none;
            border-top: 1px solid rgba(255,255,255,0.12);
            margin-top: 12px;
            margin-bottom: 12px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Logo
    st.image(
        "assets/logo.png",
        width=75
    )

    # Title
    st.markdown(
        """
        <div class="hub-title">
            Design Management Hub
        </div>
        """,
        unsafe_allow_html=True
    )

    # Subtitle
    st.markdown(
        """
        <div class="hub-subtitle">
            Design Smarter. Deliver Better.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Divider
    st.markdown(
        """
        <hr class="hub-divider">
        """,
        unsafe_allow_html=True
    )