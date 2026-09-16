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

        st.markdown("##### FRAMEWORKS")

        st.markdown("**UU Enterprise Framework**")
        st.markdown("• Pennington Flash")
        st.markdown("• Davyhulme ASP4")

        st.write("")

        st.markdown("**UU DD&B Framework**")
        st.markdown("🟣 Ferry PS")
        st.markdown("• Rossall Outfall")
        st.markdown("• Flass Lane")
        st.markdown("• Tally Ho")
        st.markdown("• Eccleston Bridge")

        st.divider()

        # ==================================================
        # NAVIGATION
        # ==================================================

        st.markdown("##### MAIN NAVIGATION")

        st.markdown("🏠 Executive Dashboard")
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

        st.divider()

        # ==================================================
        # SNAPSHOT HISTORY
        # ==================================================

        st.markdown("##### SNAPSHOT HISTORY")

        st.write(
            snapshot.strftime("%d %b %Y")
        )

        st.divider()

        # ==================================================
        # PROJECT HEALTH
        # ==================================================

        st.markdown("##### PROJECT HEALTH")

        st.write(
            f"Health Score: {metrics['health_score']}"
        )

        st.write(
            f"Design Readiness: {metrics['design_readiness']}%"
        )

        st.write(
            f"Critical Deliverables: {metrics['critical_deliverables']}"
        )

        st.write(
            f"High Risk Activities: {metrics['high_risk']}"
        )

        st.write(
            f"Upcoming Submissions: {metrics['upcoming_submissions']}"
        )

        st.divider()

        # ==================================================
        # PROJECT BASELINE
        # ==================================================

        st.markdown("##### PROJECT BASELINE")

        st.write(
            f"Baseline Finish: "
            f"{metrics['baseline_finish']:%d %b %Y}"
        )

        st.write(
            f"Current Forecast: "
            f"{metrics['forecast_finish']:%d %b %Y}"
        )

        st.write(
            f"Programme Drift: "
            f"{metrics['programme_drift']} Days"
        )