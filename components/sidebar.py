import streamlit as st


def build_sidebar():

    st.sidebar.markdown(
        """
        # 🎯 Design Intelligence Hub

        *Design Smarter. Deliver Better.*
        """
    )

    st.sidebar.divider()

    # Framework Selector
    st.sidebar.subheader("Frameworks")

    framework = st.sidebar.selectbox(
        "Framework",
        [
            "UU DD&B Framework",
            "UU Enterprise Framework"
        ]
    )

    if framework == "UU DD&B Framework":
        project = st.sidebar.selectbox(
            "Project",
            [
                "Ferry PS",
                "Rossall Outfall",
                "Flass Lane",
                "Tally Ho",
                "Eccleston Bridge"
            ]
        )
    else:
        project = st.sidebar.selectbox(
            "Project",
            [
                "Pennington Flash",
                "Davyhulme ASP4"
            ]
        )

    st.sidebar.divider()

    st.sidebar.subheader("Navigation")

    page = st.sidebar.radio(
        "Go To",
        [
            "Executive Dashboard",
            "Deliverables",
            "Upcoming Submissions",
            "Programme Drift",
            "Design Readiness",
            "Critical Activities",
            "AI Insights",
            "Reports"
        ]
    )

    st.sidebar.divider()

    st.sidebar.subheader("Project Health")

    st.sidebar.metric(
        "Health Score",
        "58/100",
        "-4"
    )

    st.sidebar.metric(
        "Programme Drift",
        "+26 Days"
    )

    st.sidebar.metric(
        "Critical Activities",
        "18"
    )

    st.sidebar.metric(
        "Submissions (7 Days)",
        "5"
    )

    st.sidebar.divider()

    st.sidebar.subheader("Snapshot History")

    st.sidebar.markdown(
        """
        🔵 Sep-26 (Current)

        🟢 Aug-26

        🟠 Jul-26

        🟡 Jun-26

        🟣 May-26
        """
    )

    return framework, project, page
