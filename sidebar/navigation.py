import streamlit as st


def render_navigation():

    if "page" not in st.session_state:
        st.session_state.page = "Executive Dashboard"

    st.markdown("""
    <style>

    .nav-title{
        color:#B7C7DA;
        font-size:12px;
        font-weight:700;
        letter-spacing:.5px;
        margin-bottom:10px;
        padding-bottom:6px;
        border-bottom:1px solid rgba(255,255,255,.08);
    }

    div[data-testid="stButton"]{
        margin-bottom:2px !important;
    }

    div[data-testid="stButton"] button{

        width:100%;

        background:transparent !important;

        color:#FFFFFF !important;

        border:none !important;

        border-radius:8px !important;

        box-shadow:none !important;

        min-height:34px !important;

        padding:8px 12px !important;

        font-size:14px !important;

        font-weight:500 !important;

        text-align:left !important;

        justify-content:flex-start !important;

    }

    div[data-testid="stButton"] button:hover{

        background:rgba(255,255,255,.05) !important;

    }

    .active-nav{

        background:linear-gradient(
            90deg,
            #2563EB,
            #3B82F6
        );

        color:white;

        padding:10px 14px;

        border-radius:8px;

        font-size:14px;

        font-weight:600;

        margin-bottom:2px;

    }

    .submenu{

        padding-left:34px;

        color:#9FB5D1;

        font-size:12px;

        margin-top:-2px;

        margin-bottom:4px;

        line-height:1.8;

    }

    .element-container{
        margin-bottom:0rem !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="nav-title">MAIN NAVIGATION</div>',
        unsafe_allow_html=True
    )

    menu = [
        ("🏠", "Executive Dashboard"),
        ("📄", "Deliverables"),
        ("📊", "Discipline Performance"),
        ("📈", "Programme Drift"),
        ("🕒", "Design Readiness"),
        ("📅", "Upcoming Submissions"),
        ("⚠️", "Critical Path & Alerts"),
        ("🔗", "Design Dependencies"),
        ("❓", "Queries & TQs"),
        ("🌐", "AI Insights & Forecast"),
        ("📋", "Reports"),
        ("🗃️", "Data Explorer"),
        ("⚙️", "Settings")
    ]

    for icon, page in menu:

        if st.session_state.page == page:

            st.markdown(
                f"""
                <div class="active-nav">
                    {icon}&nbsp;&nbsp;{page}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            if st.button(
                f"{icon}  {page}",
                key=f"nav_{page}",
                use_container_width=True
            ):
                st.session_state.page = page
                st.rerun()

        # Upcoming Submissions children
        if page == "Upcoming Submissions":

            st.markdown(
                """
                <div class="submenu">
                    • Next 7 Days<br>
                    • Next 30 Days
                </div>
                """,
                unsafe_allow_html=True
            )