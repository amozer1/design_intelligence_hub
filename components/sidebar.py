import streamlit as st


def build_sidebar(metrics, snapshot):

    with st.sidebar:

        # ==================================================
        # HEADER
        # ==================================================

        st.title("🎯 Design Intelligence Hub")
        st.caption("Design Smarter. Deliver Better.")

        st.markdown("<br>", unsafe_allow_html=True)

        # ==================================================
        # FRAMEWORKS
        # ==================================================

        st.caption("FRAMEWORKS")

        with st.container(border=True):

            st.markdown("**UU Enterprise Framework**")

            st.write("◯ Pennington Flash")
            st.write("◯ Davyhulme ASP4")

        st.markdown("<div style='height:30px'></div>",
                    unsafe_allow_html=True)

        with st.container(border=True):

            st.markdown("**UU DD&B Framework**")

            st.success("Ferry PS")

            st.write("Rossall Outfall")
            st.write("Flass Lane")
            st.write("Tally Ho")
            st.write("Eccleston Bridge")

        st.markdown("<div style='height:50px'></div>",
                    unsafe_allow_html=True)

        # ==================================================
        # NAVIGATION
        # ==================================================

        st.caption("MAIN NAVIGATION")

        with st.container(border=True):

            st.write("🏠 Executive Dashboard")
            st.write("📋 Deliverables")
            st.write("📊 Discipline Performance")
            st.write("📈 Programme Drift")
            st.write("🎯 Design Readiness")
            st.write("📅 Upcoming Submissions")
            st.write("⚠️ Critical Path & Alerts")
            st.write("🔗 Design Dependencies")
            st.write("❓ Queries & TQs")
            st.write("🤖 AI Insights & Forecast")
            st.write("📄 Reports")
            st.write("🔍 Data Explorer")
            st.write("⚙️ Settings")

        st.markdown("<div style='height:50px'></div>",
                    unsafe_allow_html=True)

        # ==================================================
        # SNAPSHOT HISTORY
        # ==================================================

        st.caption("SNAPSHOT HISTORY")

        with st.container(border=True):

            st.info(
                snapshot.strftime("%B %Y")
            )

        st.markdown("<div style='height:50px'></div>",
                    unsafe_allow_html=True)

        # ==================================================
        # PROJECT HEALTH
        # ==================================================

        st.caption("PROJECT HEALTH")

        with st.container(border=True):

            st.metric(
                "Health Score",
                f"{metrics['health_score']}/100"
            )

            c1, c2 = st.columns(2)

            with c1:
                st.metric(
                    "Readiness",
                    f"{metrics['design_readiness']}%"
                )

            with c2:
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

        st.markdown("<div style='height:50px'></div>",
                    unsafe_allow_html=True)

        # ==================================================
        # PROJECT BASELINE
        # ==================================================

        st.caption("PROJECT BASELINE")

        with st.container(border=True):

            st.metric(
                "Baseline Finish",
                metrics["baseline_finish"].strftime(
                    "%d %b %Y"
                )
            )

            st.metric(
                "Current Forecast",
                metrics["forecast_finish"].strftime(
                    "%d %b %Y"
                )
            )

            st.metric(
                "Programme Drift",
                f"{metrics['programme_drift']} Days"
            )

        st.markdown("<div style='height:30px'></div>",
                    unsafe_allow_html=True)