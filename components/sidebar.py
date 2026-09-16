import streamlit as st


def build_sidebar(metrics, snapshot):

    with st.sidebar():

        st.title("🎯 Design Intelligence Hub")
        st.caption("Design Smarter. Deliver Better.")

        st.divider()

        st.subheader("Frameworks")

        st.markdown("**UU Enterprise Framework**")
        st.write("Pennington Flash")
        st.write("Davyhulme ASP4")

        st.write("")

        st.markdown("**UU DD&B Framework**")
        st.write("Ferry PS")
        st.write("Rossall Outfall")
        st.write("Flass Lane")
        st.write("Tally Ho")
        st.write("Eccleston Bridge")

        st.divider()

        st.subheader("Navigation")

        st.write("Executive Dashboard")
        st.write("Deliverables")
        st.write("Discipline Performance")
        st.write("Programme Drift")
        st.write("Design Readiness")
        st.write("Upcoming Submissions")
        st.write("Critical Path & Alerts")
        st.write("Design Dependencies")
        st.write("Queries & TQs")
        st.write("AI Insights & Forecast")
        st.write("Reports")
        st.write("Data Explorer")
        st.write("Settings")

        st.divider()

        st.subheader("Snapshot History")

        st.write(
            snapshot.strftime("%d %b %Y")
        )

        st.divider()

        st.subheader("Project Health")

        st.write(
            f"Health Score: {metrics['health_score']}"
        )

        st.write(
            f"Readiness: {metrics['design_readiness']}%"
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

        st.subheader("Project Baseline")

        st.write(
            f"Baseline Finish: {metrics['baseline_finish']:%d %b %Y}"
        )

        st.write(
            f"Forecast Finish: {metrics['forecast_finish']:%d %b %Y}"
        )

        st.write(
            f"Programme Drift: {metrics['programme_drift']} Days"
        )