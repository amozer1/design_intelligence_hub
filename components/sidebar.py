import streamlit as st


def build_sidebar(metrics, snapshot):

    with st.sidebar:

        # =====================================
        # BRANDING
        # =====================================

        st.markdown("## 🎯 Design Intelligence Hub")
        st.caption("Design Smarter. Deliver Better.")

        st.divider()

        # =====================================
        # FRAMEWORKS
        # =====================================

        st.markdown("##### FRAMEWORKS")

        with st.expander(
            "UU Enterprise Framework",
            expanded=True
        ):
            st.write("○ Pennington Flash")
            st.write("○ Davyhulme ASP4")

        with st.expander(
            "UU DD&B Framework",
            expanded=True
        ):
            st.success("Ferry PS")

            st.write("● Rossall Outfall")
            st.write("● Flass Lane")
            st.write("● Tally Ho")
            st.write("● Eccleston Bridge")

        st.divider()

        # =====================================
        # NAVIGATION
        # =====================================

        st.markdown("##### MAIN NAVIGATION")

        pages = [
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

        selected_page = st.radio(
            "Navigation",
            pages,
            index=0,
            label_visibility="collapsed"
        )

        st.divider()

        # =====================================
        # SNAPSHOT HISTORY
        # =====================================

        st.markdown("##### SNAPSHOT HISTORY")

        st.write(snapshot.strftime("%d %b %Y"))

        st.divider()

        # =====================================
        # PROJECT HEALTH
        # =====================================

        st.markdown("##### PROJECT HEALTH")

        st.metric(
            "Health Score",
            metrics["health_score"]
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

        st.divider()

        # =====================================
        # PROJECT BASELINE
        # =====================================

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

        return selected_page