import streamlit as st


def build_sidebar(metrics, snapshot):

    # ==================================================
    # SIDEBAR STYLING
    # ==================================================

    st.markdown("""
    <style>

    section[data-testid="stSidebar"]{
        background:
        linear-gradient(
            180deg,
            #041124 0%,
            #09132f 40%,
            #071224 100%);
        border-right:1px solid rgba(124,58,237,.25);
    }

    section[data-testid="stSidebar"] > div{
        padding-top:0.5rem;
    }

    .logo-card{
        padding:16px;
        border-radius:14px;
        background:
        linear-gradient(
            180deg,
            rgba(20,30,60,.9),
            rgba(10,20,40,.95));
        border:1px solid rgba(124,58,237,.2);
        margin-bottom:16px;
    }

    .section-title{
        color:#9aa4bd;
        font-size:11px;
        font-weight:700;
        letter-spacing:1px;
        margin-top:10px;
        margin-bottom:8px;
    }

    .active-project{
        background:
        linear-gradient(
            90deg,
            #7c3aed,
            #9333ea);
        color:white;
        padding:8px 12px;
        border-radius:8px;
        font-weight:600;
        margin-bottom:4px;
    }

    .active-nav{
        background:
        linear-gradient(
            90deg,
            #6d28d9,
            #7c3aed);
        color:white;
        padding:10px 12px;
        border-radius:8px;
        font-weight:600;
        margin-bottom:4px;
    }

    .nav-item{
        padding:6px 12px;
        color:#d7dbeb;
        border-radius:8px;
        margin-bottom:3px;
    }

    .nav-item:hover{
        background:rgba(255,255,255,.05);
    }

    .sidebar-card{
        background:rgba(255,255,255,.03);
        border:1px solid rgba(124,58,237,.18);
        border-radius:12px;
        padding:12px;
        margin-top:8px;
        margin-bottom:12px;
    }

    .health-score{
        text-align:center;
        color:white;
        font-size:40px;
        font-weight:700;
        line-height:1;
    }

    .health-sub{
        text-align:center;
        color:#98a4bd;
        font-size:12px;
    }

    .metric-row{
        display:flex;
        justify-content:space-between;
        padding:4px 0;
        color:white;
        font-size:13px;
    }

    .badge{
        float:right;
        background:#28354f;
        color:white;
        padding:2px 8px;
        border-radius:6px;
        font-size:11px;
        font-weight:600;
    }

    .green{color:#22c55e;}
    .yellow{color:#eab308;}
    .orange{color:#fb923c;}
    .red{color:#ef4444;}
    .purple{color:#a855f7;}
    .blue{color:#3b82f6;}

    hr{
        border:none;
        border-top:1px solid rgba(255,255,255,.06);
    }

    </style>
    """, unsafe_allow_html=True)

    # ==================================================
    # SIDEBAR
    # ==================================================

    with st.sidebar:

        # ---------------------------------------------
        # BRANDING
        # ---------------------------------------------

        st.markdown("""
        <div class="logo-card">
            <h2 style='margin:0;color:white;line-height:1.1;'>
                DESIGN<br>
                INTELLIGENCE HUB
            </h2>
            <div style='color:#9aa4bd;font-size:12px;'>
                Design Smarter. Deliver Better.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ---------------------------------------------
        # FRAMEWORKS
        # ---------------------------------------------

        st.markdown(
            "<div class='section-title'>FRAMEWORKS</div>",
            unsafe_allow_html=True
        )

        with st.expander("UU Enterprise Framework", expanded=True):
            st.markdown("⚪ Pennington Flash")
            st.markdown("⚪ Davyhulme ASP4")

        with st.expander("UU DD&B Framework", expanded=True):

            st.markdown("""
            <div class='active-project'>
                🔴 Ferry PS
            </div>
            """, unsafe_allow_html=True)

            st.markdown("🟠 Rossall Outfall")
            st.markdown("🟢 Flass Lane")
            st.markdown("🟡 Tally Ho")
            st.markdown("🟢 Eccleston Bridge")

        st.divider()

        # ---------------------------------------------
        # MAIN NAVIGATION
        # ---------------------------------------------

        st.markdown(
            "<div class='section-title'>MAIN NAVIGATION</div>",
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class='active-nav'>
            🏠 Executive Dashboard
        </div>
        """, unsafe_allow_html=True)

        nav_items = [
            "📋 Deliverables",
            "👥 Discipline Performance",
            "📈 Programme Drift",
            "🎯 Design Readiness",
            "📅 Upcoming Submissions",
            "⚠️ Critical Path & Alerts",
            "🔗 Design Dependencies",
            "❓ Queries & TQs",
            "🤖 AI Insights & Forecast",
            "📄 Reports",
            "🔎 Data Explorer",
            "⚙️ Settings"
        ]

        for item in nav_items:
            st.markdown(
                f"<div class='nav-item'>{item}</div>",
                unsafe_allow_html=True
            )

        st.divider()

        # ---------------------------------------------
        # SNAPSHOT HISTORY
        # ---------------------------------------------

        st.markdown(
            "<div class='section-title'>SNAPSHOT HISTORY</div>",
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class='sidebar-card'>

        <div class='purple'>
        ● {snapshot:%d %b %Y} (Current)
        <span class='badge'>52</span>
        </div>

        <div class='green'>
        ● 31 Aug 2026
        <span class='badge'>52</span>
        </div>

        <div class='orange'>
        ● 31 Jul 2026
        <span class='badge'>52</span>
        </div>

        <div class='blue'>
        ● 30 Jun 2026
        <span class='badge'>52</span>
        </div>

        <div class='purple'>
        ● 31 May 2026
        <span class='badge'>52</span>
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.button(
            "View all snapshots",
            use_container_width=True
        )

        st.divider()

        # ---------------------------------------------
        # PROJECT HEALTH
        # ---------------------------------------------

        st.markdown(
            "<div class='section-title'>PROJECT HEALTH</div>",
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class='sidebar-card'>

            <div class='health-score'>
                {metrics['health_score']}
            </div>

            <div class='health-sub'>
                /100
            </div>

            <hr>

            <div class='metric-row'>
                <span class='green'>● Design Readiness</span>
                <span>{metrics['design_readiness']}%</span>
            </div>

            <div class='metric-row'>
                <span class='yellow'>● Critical Deliverables</span>
                <span>{metrics['critical_deliverables']}</span>
            </div>

            <div class='metric-row'>
                <span class='red'>● High Risk Activities</span>
                <span>{metrics['high_risk']}</span>
            </div>

            <div class='metric-row'>
                <span class='orange'>● Upcoming Submissions</span>
                <span>{metrics['upcoming_submissions']}</span>
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # ---------------------------------------------
        # BASELINE
        # ---------------------------------------------

        st.markdown(
            "<div class='section-title'>PROJECT BASELINE (BL1)</div>",
            unsafe_allow_html=True
        )

        drift_colour = (
            "#ef4444"
            if metrics["programme_drift"] > 0
            else "#22c55e"
        )

        st.markdown(f"""
        <div class='sidebar-card'>

            <div class='metric-row'>
                <span>Baseline Finish</span>
                <span>
                    {metrics['baseline_finish']:%d %b %Y}
                </span>
            </div>

            <div class='metric-row'>
                <span>Current Forecast</span>
                <span>
                    {metrics['forecast_finish']:%d %b %Y}
                </span>
            </div>

            <div class='metric-row'>
                <span>Programme Drift</span>
                <span style='color:{drift_colour};
                             font-weight:700;'>
                    +{metrics['programme_drift']} Days
                </span>
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.caption(
            f"Data as of {snapshot:%d %b %Y %H:%M}"
        )