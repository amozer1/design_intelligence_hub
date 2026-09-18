import streamlit as st


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

    .section-title {
        color: white;
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ==================================================
    # HEADER PLACEHOLDER
    # ==================================================

    with st.container(border=True):

        st.markdown(
            "### HEADER"
        )

    st.write("")

    # ==================================================
    # KPI STRIP
    # ==================================================

    k1, k2, k3, k4, k5, k6, k7 = st.columns(7)

    with k1:
        st.container(border=True).markdown if False else None
        st.info("Executive Summary")

    with k2:
        st.info("Programme Finish")

    with k3:
        st.info("Contract Completion")

    with k4:
        st.info("Total Deliverables")

    with k5:
        st.info("Critical Deliverables")

    with k6:
        st.info("Avg Float")

    with k7:
        st.info("Avg Variance")

    st.write("")

    # ==================================================
    # ROW 1
    # ==================================================

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)

    with r1c1:

        with st.container(border=True):
            st.markdown("### Executive Summary")
            st.write("Placeholder")

    with r1c2:

        with st.container(border=True):
            st.markdown("### Deliverables by Status")
            st.write("Placeholder")

    with r1c3:

        with st.container(border=True):
            st.markdown("### Deliverables by Discipline")
            st.write("Placeholder")

    with r1c4:

        with st.container(border=True):
            st.markdown("### Upcoming Submissions")
            st.write("Placeholder")

    st.write("")

    # ==================================================
    # ROW 2
    # ==================================================

    r2c1, r2c2, r2c3, r2c4 = st.columns(4)

    with r2c1:

        with st.container(border=True):
            st.markdown("### Critical Deliverables")
            st.write("Placeholder")

    with r2c2:

        with st.container(border=True):
            st.markdown("### What's Changed")
            st.write("Placeholder")

    with r2c3:

        with st.container(border=True):
            st.markdown("### Top 5 Biggest Slippers")
            st.write("Placeholder")

    with r2c4:

        with st.container(border=True):
            st.markdown("### Discipline Health")
            st.write("Placeholder")

    st.write("")

    # ==================================================
    # ROW 3
    # ==================================================

    r3c1, r3c2, r3c3, r3c4, r3c5 = st.columns(5)

    with r3c1:

        with st.container(border=True):
            st.markdown("### AI Risk Forecast")
            st.write("Placeholder")

    with r3c2:

        with st.container(border=True):
            st.markdown("### Design Dependencies")
            st.write("Placeholder")

    with r3c3:

        with st.container(border=True):
            st.markdown("### Queries & TQs")
            st.write("Placeholder")

    with r3c4:

        with st.container(border=True):
            st.markdown("### AI Insights")
            st.write("Placeholder")

    with r3c5:

        with st.container(border=True):
            st.markdown("### Quick Actions")
            st.write("Placeholder")

    st.write("")

    # ==================================================
    # FOOTER
    # ==================================================

    footer1, footer2, footer3, footer4, footer5 = st.columns(5)

    with footer1:
        with st.container(border=True):
            st.markdown("**Data Status**")

    with footer2:
        with st.container(border=True):
            st.markdown("**Last Refresh**")

    with footer3:
        with st.container(border=True):
            st.markdown("**Snapshots Loaded**")

    with footer4:
        with st.container(border=True):
            st.markdown("**Activities Tracked**")

    with footer5:
        with st.container(border=True):
            st.markdown("**Powered By**")
