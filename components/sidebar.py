import streamlit as st


def build_sidebar(metrics, snapshot):

    with st.sidebar:

        # ==================================================
        # BRANDING
        # ==================================================

        st.markdown("## 🎯 Design Intelligence Hub")
        st.caption("Design Smarter. Deliver Better.")

        st.divider()

        # ==================================================
        # FRAMEWORKS
        # ==================================================

        st.markdown("##### FRAMEWORKS")

        st.markdown("**▼ UU Enterprise Framework**")
        st.markdown("○ Pennington Flash")
        st.markdown("○ Davyhulme ASP4")

        st.write("")

        st.markdown("**▼ UU DD&B Framework**")

        st.markdown(
            """
            <div style="
                background:#5B21B6;
                color:white;
                padding:8px 12px;
                border-radius:6px;
                margin:6px 0;
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

        st.divider()

        # ==================================================
        # NAVIGATION
        # ==================================================

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

        st.markdown(
            """
            <div style="
                background:#1D4ED8;
                color:white;
                padding:8px 12px;
                border-radius:6px;
                margin-bottom:6px;
                font-weight:600;">
                🏠 Executive Dashboard
            </div>
            """,
            unsafe_allow_html=True,
        )

        for item in nav_items[1:]:
            st.markdown(item)

        st.divider()

        # ==================================================
        # SNAPSHOT
        # ==================================================

        st.markdown("##### SNAPSHOT HISTORY")

        st.write(snapshot.strftime("%d %b %Y"))

        st.divider()

        # ==================================================
        # HEALTH
        # ==================================================

        st.markdown("##### PROJECT