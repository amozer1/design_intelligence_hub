import streamlit as st


def build_sidebar(metrics, snapshot):

    with st.sidebar:

        # ==================================================
        # BRANDING
        # ==================================================

        with st.container():

            st.markdown("### 🎯 Design Intelligence Hub")
            st.caption("Design Smarter. Deliver Better.")

        # ==================================================
        # FRAMEWORKS
        # ==================================================

        with st.container():

            st.caption("FRAMEWORKS")

            st.markdown("**▼ UU Enterprise Framework**")

            st.markdown("○ Pennington Flash")
            st.markdown("○ Davyhulme ASP4")

            st.divider()

            st.markdown("**▼ UU DD&B Framework**")

            st.markdown(
                """
                <div class="active-project">
                    ● Ferry PS
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("● Rossall Outfall")
            st.markdown("● Flass Lane")
            st.markdown("● Tally Ho")
            st.markdown("● Eccleston Bridge")

        # ==================================================
        # MAIN NAVIGATION
        # ==================================================

        with st.container():

            st.caption("MAIN NAVIGATION")

            st.markdown(
                """
                <div class="active-nav">
                    🏠 Executive Dashboard
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("📋 Deliverables")
            st.markdown("📊 Discipline Performance")
            st.markdown("📈 Programme Drift")
            st.markdown("🎯 Design Readiness")
            st.markdown("📅 Upcoming Submissions")
            st.markdown("⚠️ Critical Path & Alerts")
            st.markdown("🔗 Design Dependencies")
            st.markdown("❓ Queries & TQs")
            st.markdown("🤖 AI Insights & Forecast")
            st.markdown("📄 Reports")
            st.markdown("🔍 Data Explorer")
            st.markdown("⚙️ Settings")

        # ==================================================
        # SNAPSHOT HISTORY
        # ==================================================

        with st.container():

            st.caption("SNAPSHOT HISTORY")

            st.info(
                snapshot.strftime("%B %Y")
            )

        # ==================================================
        # PROJECT HEALTH
        # ==================================================

        with st.container():

            st.caption("PROJECT HEALTH")

            st.metric(
                "Health Score",
                f"{metrics['health_score']}/100"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Readiness",
                    f"{metrics['design_readiness']}%"
                )

            with col2:
                st.metric(
                    "Critical",
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

        # ==================================================
        # PROJECT BASELINE
        # ==================================================

        with st.container():

            st.caption("PROJECT BASELINE")

            st.metric(
                "Baseline Finish",
                metrics["baseline_finish"].strftime("%d %b %Y")
            )

            st.metric(
                "Current Forecast",
                metrics["forecast_finish"].strftime("%d %b %Y")
            )

            st.metric(
                "Programme Drift",
                f"{metrics['programme_drift']} Days"
            )