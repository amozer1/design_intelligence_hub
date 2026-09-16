import streamlit as st


def build_sidebar(metrics, snapshot):

    with st.sidebar:

        # ==================================================
        # BRANDING
        # ==================================================

        st.title("🎯 Design Intelligence Hub")
        st.caption("Design Smarter. Deliver Better.")

        st.divider()

        # ==================================================
        # FRAMEWORKS
        # ==================================================

        st.subheader("Frameworks")

        with st.expander(
            "UU Enterprise Framework",
            expanded=False
        ):
            st.markdown("• Pennington Flash")
            st.markdown("• Davyhulme ASP4")

        with st.expander(
            "UU DD&B Framework",
            expanded=True
        ):
            st.markdown("🟣 Ferry PS")
            st.markdown("• Rossall Outfall")
            st.markdown("• Flass Lane")
            st.markdown("• Tally Ho")
            st.markdown("• Eccleston Bridge")

        st.divider()

        # ==================================================
        # NAVIGATION
        # ==================================================

        st.subheader("Navigation")

        navigation_items = [
            "🏠 Executive Dashboard",
            "📋 Deliverables",
            "📊 Discipline Performance",
            "📈 Programme Drift",
            "🎯 Design Readiness",
            "📅 Upcoming Submissions",
            "⚠️ Critical Path & Alerts",
            "🔗 Design Dependencies",
            "❓ Queries & TQs",
            "🤖 AI Insights & Forecast",
            "📄 Reports",
            "🔍 Data Explorer",
            "⚙️ Settings",
        ]

        for item in navigation_items:
            st.button(
                item,
                use_container_width=True
            )

        st.divider()

        # ==================================================
        # SNAPSHOT
        # ==================================================

        st.subheader("Snapshot")

        st.write(
            snapshot.strftime("%d %b %Y")
        )

        st.divider()

        # ==================================================
        # PROJECT HEALTH
        # ==================================================

        st.subheader("Project Health")

        st.metric(
            "Health Score",
            metrics["health_score"]
        )

        st.metric(
            "Design Readiness",
            f"{metrics['design_readiness']}%"
        )

        st.metric(
            "Critical Deliverables",
            metrics["critical_deliverables"]
        )

        st.metric(
            "High Risk Activities",
            metrics["high_risk"]
        )

        st.metric(
            "Upcoming Submissions",
            metrics["upcoming_submissions"]
        )

        st.divider()

        # ==================================================
        # PROJECT BASELINE
        # ==================================================

        st.subheader("Project Baseline")

        st.write(
            f"Baseline Finish: "
            f"{metrics['baseline_finish']:%d %b %Y}"
        )

        st.write(
            f"Forecast Finish: "
            f"{metrics['forecast_finish']:%d %b %Y}"
        )

        st.write(
            f"Programme Drift: "
            f"{metrics['programme_drift']} Days"
        )