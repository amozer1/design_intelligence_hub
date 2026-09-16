import streamlit as st


def render_navigation():

    st.markdown("""
    <style>

    .nav-divider{
        border-top:1px solid rgba(255,255,255,.08);
        margin:12px 0;
    }

    .nav-title{
        color:#B7C7DA;
        font-size:14px;
        font-weight:700;
        margin-bottom:10px;
    }

    div[data-testid="stButton"] button{

        background:transparent !important;

        color:#E2E8F0 !important;

        border:none !important;

        box-shadow:none !important;

        text-align:left !important;

        justify-content:flex-start !important;

        padding:6px 10px !important;

        min-height:34px !important;

        border-radius:8px !important;

        font-size:14px !important;

        font-weight:500 !important;
    }

    div[data-testid="stButton"] button:hover{

        background:rgba(124,58,237,.12) !important;

        color:white !important;
    }

    .nav-active{

        background:linear-gradient(
            90deg,
            #6624D6,
            #7C3AED
        );

        border-radius:8px;

        padding:8px 12px;

        color:white;

        font-size:14px;

        font-weight:600;

        margin-bottom:4px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="nav-divider"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-title">MAIN NAVIGATION</div>',
        unsafe_allow_html=True
    )

    pages = [
        "Executive Dashboard",
        "Deliverables",
        "Discipline Performance",
        "Programme Drift",
        "Design Readiness",
        "Upcoming Submissions",
        "Critical Path & Alerts",
        "Design Dependencies",
        "Queries & TQs",
        "AI Insights & Forecast",
        "Reports",
        "Data Explorer",
        "Settings"
    ]

    if "page" not in st.session_state:
        st.session_state.page = "Executive Dashboard"

    for page in pages:

        if st.session_state.page == page:

            st.markdown(
                f"""
                <div class="nav-active">
                    {page}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            if st.button(
                page,
                use_container_width=True,
                key=f"nav_{page}"
            ):
                st.session_state.page = page
                st.rerun()