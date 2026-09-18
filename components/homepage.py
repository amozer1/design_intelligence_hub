import streamlit as st


def card_placeholder(title, height=250):

    with st.container(border=True):

        st.markdown(
            f"##### {title}"
        )

        st.markdown(
            f"""
            <div style="height:{height}px;"></div>
            """,
            unsafe_allow_html=True
        )


def render_homepage(
    project,
    snapshot,
    metrics,
    cl31,
    cl32
):

    st.markdown("""
    <style>

    .stApp {
        background: #061F3B;
    }

    div[data-testid="stVerticalBlock"] {
        gap: 0.75rem;
    }

    </style>
    """, unsafe_allow_html=True)

    # ==================================================
    # HEADER
    # ==================================================

    with st.container(border=True):

        st.markdown("### HEADER")

        st.markdown(
            """
            <div style="height:70px;"></div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # ==================================================
    # KPI ROW
    # ==================================================

    k1, k2, k3, k4, k5, k6, k7 = st.columns(7)

    with k1:
        card_placeholder("Executive Summary", 60)

    with k2:
        card_placeholder("Programme Finish", 60)

    with k3:
        card_placeholder("Contract Completion", 60)

    with k4:
        card_placeholder("Total Deliverables", 60)

    with k5:
        card_placeholder("Critical Deliverables", 60)

    with k6:
        card_placeholder("Avg Float", 60)

    with k7:
        card_placeholder("Avg Variance", 60)

    st.write("")

    # ==================================================
    # ROW 1
    # ==================================================

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)

    with r1c1:
        card_placeholder(
            "Executive Summary",
            300
        )

    with r1c2:
        card_placeholder(
            "Deliverables by Status",
            300
        )

    with r1c3:
        card_placeholder(
            "Deliverables by Discipline",
            300
        )

    with r1c4:
        card_placeholder(
            "Upcoming Submissions",
            300
        )

    st.write("")

    # ==================================================
    # ROW 2
    # ==================================================

    r2c1, r2c2, r2c3, r2c4 = st.columns(4)

    with r2c1:
        card_placeholder(
            "Critical Deliverables",
            250
        )

    with r2c2:
        card_placeholder(
            "What's Changed",
            250
        )

    with r2c3:
        card_placeholder(
            "Top 5 Biggest Slippers",
            250
        )

    with r2c4:
        card_placeholder(
            "Discipline Health",
            250
        )

    st.write("")

    # ==================================================
    # ROW 3
    # ==================================================

    r3c1, r3c2, r3c3, r3c4, r3c5 = st.columns(5)

    with r3c1:
        card_placeholder(
            "AI Risk Forecast",
            250
        )

    with r3c2:
        card_placeholder(
            "Design Dependencies",
            250
        )

    with r3c3:
        card_placeholder(
            "Queries & TQs",
            250
        )

    with r3c4:
        card_placeholder(
            "AI Insights",
            250
        )

    with r3c5:
        card_placeholder(
            "Quick Actions",
            250
        )

    st.write("")

    # ==================================================
    # FOOTER
    # ==================================================

    f1, f2, f3, f4, f5 = st.columns(5)

    with f1:
        card_placeholder("Data Status", 40)

    with f2:
        card_placeholder("Last Refresh", 40)

    with f3:
        card_placeholder("Snapshots Loaded", 40)

    with f4:
        card_placeholder("Activities Tracked", 40)

    with f5:
        card_placeholder("Powered By", 40)