import streamlit as st


def render_navigation():

    st.markdown("""
    <style>

    .nav-title {
        color: #B7C7DA;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }

    /* Radio group spacing */
    div[role="radiogroup"] {
        gap: 0 !important;
    }

    /* Radio item spacing */
    div[role="radiogroup"] label {
        padding: 3px 0 !important;
        margin: 0 !important;
    }

    /* Radio text styling */
    div[data-baseweb="radio"] * {
        color: white !important;
        opacity: 1 !important;
        font-size: 13px !important;
        font-weight: 500 !important;
    }

    /* Reduce Streamlit spacing */
    .element-container {
        margin-bottom: 0rem !important;
    }

    </style>
    """, unsafe_allow_html=True)

    if "page" not in st.session_state:
        st.session_state.page = "Executive Dashboard"

    pages = [
        "🏠 Executive Dashboard",
        "📄 Deliverables",
        "📊 Discipline Performance",
        "📈 Programme Drift",
        "🕒 Design Readiness",
        "📅 Upcoming Submissions",
        "⚠️ Critical Path & Alerts",
        "🔗 Design Dependencies",
        "❓ RFIs & TQs",
        "🤖 AI Insights & Forecast",
        "📋 Reports",
        "🗄️ Data Explorer",
        "⚙️ Settings"
    ]

    st.markdown(
        '<div class="nav-title">MAIN NAVIGATION</div>',
        unsafe_allow_html=True
    )

    selected = st.radio(
        "",
        pages,
        label_visibility="collapsed"
    )

    page_name = selected.split(" ", 1)[1]

    if page_name != st.session_state.page:
        st.session_state.page = page_name
        st.rerun()

    st.markdown(
        """
        <hr style="
            border:none;
            border-top:1px solid rgba(220,232,245,0.20);
            margin:14px 0;
        ">
        """,
        unsafe_allow_html=True
    )


