import streamlit as st


def build_sidebar():

    st.sidebar.markdown(
        """
        <style>

        [data-testid="stSidebar"]{
            background: linear-gradient(
                180deg,
                #081428 0%,
                #091737 50%,
                #06101f 100%
            );
        }

        .logo-title{
            display:flex;
            align-items:center;
            gap:12px;
            margin-bottom:10px;
        }

        .logo{
            font-size:34px;
        }

        .title{
            color:white;
            font-size:26px;
            font-weight:700;
            line-height:1.1;
        }

        .subtitle{
            color:#9ea7c8;
            font-size:12px;
            margin-top:2px;
        }

        .section-title{
            color:#b4bddb;
            font-size:12px;
            text-transform:uppercase;
            letter-spacing:1px;
            margin-top:18px;
            margin-bottom:12px;
            font-weight:600;
        }

        .framework{
            color:white;
            font-weight:600;
            margin-top:12px;
            margin-bottom:8px;
            padding-left:4px;
        }

        .project{
            color:#d7def4;
            padding:10px 12px;
            margin-bottom:4px;
            border-radius:8px;
            font-size:14px;
        }

        .project:hover{
            background:#152850;
        }

        .active-project{
            background:#7B2CF5;
            color:white;
            font-weight:600;
        }

        .menu-item{
            color:white;
            padding:12px;
            border-radius:8px;
            margin-bottom:6px;
            font-size:14px;
        }

        .active-menu{
            background:#7B2CF5;
            font-weight:600;
        }

        .menu-item:hover{
            background:#152850;
        }

        .snapshot-row{
            display:flex;
            justify-content:space-between;
            align-items:center;
            color:white;
            margin-bottom:8px;
            font-size:13px;
        }

        .snapshot-count{
            background:#17254b;
            padding:2px 8px;
            border-radius:6px;
        }

        .health-card{
            background:#0f1f42;
            border:1px solid #1d325f;
            border-radius:12px;
            padding:15px;
            margin-top:10px;
            color:white;
        }

        .metric{
            display:flex;
            justify-content:space-between;
            margin-bottom:8px;
            font-size:13px;
        }

        .green{color:#00D26A;}
        .amber{color:#FFB100;}
        .red{color:#FF3B5C;}

        .baseline-card{
            background:#0f1f42;
            border:1px solid #1d325f;
            border-radius:12px;
            padding:15px;
            margin-top:10px;
            color:white;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
        <div class="logo-title">
            <div class="logo">🎯</div>
            <div>
                <div class="title">DESIGN<br>INTELLIGENCE HUB</div>
                <div class="subtitle">
                    Design Smarter. Deliver Better.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        '<div class="section-title">Frameworks</div>',
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
        <div class="framework">▼ UU Enterprise Framework</div>

        <div class="project">
        ⚪ Pennington Flash
        </div>

        <div class="project">
        ⚪ Davyhulme ASP4
        </div>

        <div class="framework">▼ UU DD&B Framework</div>

        <div class="project active-project">
        🟣 Ferry PS
        </div>

        <div class="project">
        🟠 Rossall Outfall
        </div>

        <div class="project">
        🟢 Flass Lane
        </div>

        <div class="project">
        🟡 Tally Ho
        </div>

        <div class="project">
        🟢 Eccleston Bridge
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        '<div class="section-title">Main Navigation</div>',
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
        <div class="menu-item active-menu">
        🏠 Executive Dashboard
        </div>

        <div class="menu-item">📋 Deliverables</div>

        <div class="menu-item">📊 Discipline Performance</div>

        <div class="menu-item">📈 Programme Drift</div>

        <div class="menu-item">🎯 Design Readiness</div>

        <div class="menu-item">📅 Upcoming Submissions</div>

        <div class="menu-item">⚠️ Critical Path & Alerts</div>

        <div class="menu-item">🔗 Design Dependencies</div>

        <div class="menu-item">❓ Queries & TQs</div>

        <div class="menu-item">🤖 AI Insights & Forecast</div>

        <div class="menu-item">📄 Reports</div>

        <div class="menu-item">🔍 Data Explorer</div>

        <div class="menu-item">⚙️ Settings</div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        '<div class="section-title">Snapshot History</div>',
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
        <div class="snapshot-row">
            <span>🔵 30 Sep 2026 (Current)</span>
            <span class="snapshot-count">52</span>
        </div>

        <div class="snapshot-row">
            <span>🟢 31 Aug 2026</span>
            <span class="snapshot-count">52</span>
        </div>

        <div class="snapshot-row">
            <span>🟠 31 Jul 2026</span>
            <span class="snapshot-count">52</span>
        </div>

        <div class="snapshot-row">
            <span>🟡 30 Jun 2026</span>
            <span class="snapshot-count">52</span>
        </div>

        <div class="snapshot-row">
            <span>🟣 31 May 2026</span>
            <span class="snapshot-count">52</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
        <div class="section-title">
        Project Health
        </div>

        <div class="health-card">

        <div class="metric">
            <span>Design Readiness</span>
            <span class="green">78%</span>
        </div>

        <div class="metric">
            <span>Critical Deliverables</span>
            <span class="amber">18</span>
        </div>

        <div class="metric">
            <span>High Risk Activities</span>
            <span class="red">5</span>
        </div>

        <div class="metric">
            <span>Upcoming Submissions</span>
            <span class="amber">5</span>
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
        <div class="section-title">
        Project Baseline (BL1)
        </div>

        <div class="baseline-card">

        <div class="metric">
            <span>Baseline Finish</span>
            <span>24 Sep 2026</span>
        </div>

        <div class="metric">
            <span>Current Forecast</span>
            <span>20 Oct 2026</span>
        </div>

        <div class="metric">
            <span>Programme Drift</span>
            <span class="red">+26 Days</span>
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )