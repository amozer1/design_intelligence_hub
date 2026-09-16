import streamlit as st


def build_sidebar(metrics, snapshot):

    with st.sidebar:

        # ==================================================
        # LOGO / BRANDING CARD
        # ==================================================
        with st.container(border=True):

            st.markdown("### 🎯 Design Intelligence Hub")
            st.caption("Design Smarter. Deliver Better.")

        # ==================================================
        # FRAMEWORKS CARD
        # ==================================================
        with st.container(border=True):

            st.markdown("##### FRAMEWORKS")

            st.markdown("**▼ UU Enterprise Framework**")
            st.markdown("◯ Pennington Flash")
            st.markdown("◯ Davyhulme ASP4")

            st.markdown("---")

            st.markdown("**▼ UU DD&B Framework**")

            st.markdown(
                """
                <div style="
                    background:#4338ca;
                    padding:8px 12px;
                    border-radius:8px;
                    margin-bottom:6px;
                    color:white;
                    font-weight:600;">
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
        # MAIN NAVIGATION CARD
        # ==================================================
        with st.container(border=True):

            st.markdown("##### MAIN NAVIGATION")

            nav_items = [
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

            for item in nav_items:

                if item == "🏠 Executive Dashboard":
                    st.markdown(
                        f"""
                        <div style="
                            background:#2563eb;
                            padding:8px 12px;
                            border-radius:8px;
                            margin-bottom:4px;
                            color:white;
                            font-weight:600;">
                            {item}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(item)

        # ==================================================
        # SNAPSHOT HISTORY CARD
        # ==================================================
        with st.container(border=True):

            st.markdown("##### SNAPSHOT HISTORY")

            st.metric(
                "Current Snapshot",
                snapshot.strftime("%d %b %Y")
            )

        # ==================================================
        # PROJECT HEALTH CARD
        # ==================================================
        with st.container(border=True):

            st.markdown("##### PROJECT HEALTH")

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

        # ==================================================
        # PROJECT BASELINE CARD
        # ==================================================
        with st.container(border=True):

            st.markdown("##### PROJECT BASELINE")

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