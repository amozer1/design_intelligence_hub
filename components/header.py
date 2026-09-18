import streamlit as st
from datetime import datetime


PROJECT_MANAGERS = {
    "Ferry PS": "Conal Cunningham",
    "Flass Lane": "Conal Cunningham",
    "Rossall Outfall": "Michael Harbon",
    "Tally Ho": "Ebenezer Amoako",
    "Eccleston Bridge": "Ebenezer Amoako",
    "Pennington Flash": "Ebenezer Amoako",
    "Davyhulme ASP4": "Ebenezer Amoako",
}


def render_header(project, snapshot):

    design_manager = PROJECT_MANAGERS.get(
        project,
        "Not Assigned"
    )

    updated = datetime.today().strftime("%d %b %Y")

    st.markdown(
        f"""
        <style>

        .top-header {{
            background: linear-gradient(
                90deg,
                #08152d 0%,
                #0b1f42 100%
            );
            border: 1px solid rgba(70,120,255,.25);
            border-radius: 12px;
            padding: 12px 20px;
            margin-bottom: 20px;
        }}

        .top-row {{
            display:flex;
            justify-content:space-between;
            align-items:center;
        }}

        .left-side {{
            display:flex;
            align-items:center;
            gap:18px;
        }}

        .menu {{
            font-size:24px;
            color:white;
        }}

        .card {{
            border:1px solid rgba(255,255,255,.15);
            border-radius:8px;
            padding:8px 14px;
            min-width:230px;
            background:rgba(255,255,255,.03);
        }}

        .label {{
            color:#9fb3d9;
            font-size:11px;
            text-transform:uppercase;
        }}

        .value {{
            color:white;
            font-size:15px;
            font-weight:600;
        }}

        .right-side {{
            display:flex;
            align-items:center;
            gap:14px;
        }}

        .upload-btn {{
            background:#6c3cff;
            color:white;
            padding:10px 18px;
            border-radius:8px;
            font-size:14px;
            font-weight:600;
        }}

        .icon {{
            color:white;
            font-size:18px;
        }}

        .avatar {{
            width:38px;
            height:38px;
            border-radius:50%;
            background:#6c3cff;
            color:white;
            display:flex;
            align-items:center;
            justify-content:center;
            font-weight:700;
        }}

        .user-block {{
            display:flex;
            align-items:center;
            gap:10px;
        }}

        .user-info {{
            line-height:1.2;
        }}

        .user-name {{
            color:white;
            font-size:14px;
            font-weight:600;
        }}

        .updated {{
            color:#aebddb;
            font-size:11px;
        }}

        </style>

        <div class="top-header">
            <div class="top-row">

                <div class="left-side">

                    <div class="menu">☰</div>

                    <div class="card">
                        <div class="label">Project</div>
                        <div class="value">{project}</div>
                    </div>

                    <div class="card">
                        <div class="label">Current CL32 Snapshot</div>
                        <div class="value">{snapshot}</div>
                    </div>

                </div>

                <div class="right-side">

                    <div class="upload-btn">
                        ⬆ Upload New CL32
                    </div>

                    <div class="icon">🔄</div>
                    <div class="icon">🔔</div>
                    <div class="icon">❓</div>
                    <div class="icon">⚙️</div>

                    <div class="user-block">
                        <div class="avatar">
                            {"".join([x[0] for x in design_manager.split()[:2]])}
                        </div>

                        <div class="user-info">
                            <div class="user-name">
                                {design_manager}
                            </div>

                            <div class="updated">
                                Last Updated: {updated}
                            </div>
                        </div>
                    </div>

                </div>

            </div>
        </div>
        """,
        unsafe_allow_html=True
    )