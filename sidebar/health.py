import pandas as pd
import streamlit as st
import plotly.graph_objects as go


def calculate_health_metrics(cl32):

    if cl32.empty:
        return {
            "health_score": 0,
            "design_readiness": 0,
            "critical_deliverables": 0,
            "high_risk": 0,
            "upcoming_submissions": 0,
        }

    latest_snapshot = cl32["SnapshotDate"].max()

    df = cl32[
        cl32["SnapshotDate"] == latest_snapshot
    ].copy()

    numeric_cols = [
        "Activity % Complete",
        "Variance - BL1 Finish Date",
        "Total Float",
        "Remaining Duration",
    ]

    for col in numeric_cols:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    if "Finish" in df.columns:

        df["Finish"] = pd.to_datetime(
            df["Finish"],
            dayfirst=True,
            errors="coerce"
        )

    activities = df[
        df["Activity ID"]
        .astype(str)
        .str.contains("-", na=False)
    ].copy()

    design_readiness = round(
        activities["Activity % Complete"]
        .fillna(0)
        .mean(),
        0
    )

    critical_deliverables = len(
        activities[
            (activities["Total Float"] <= 0)
            &
            (activities["Activity % Complete"] < 100)
        ]
    )

    high_risk = len(
        activities[
            activities["Variance - BL1 Finish Date"] <= -14
        ]
    )

    today = pd.Timestamp.today()

    upcoming_submissions = len(
        activities[
            activities["Activity Name"]
            .astype(str)
            .str.contains(
                "submission|review|freeze",
                case=False,
                na=False
            )
            &
            (activities["Finish"] >= today)
            &
            (
                activities["Finish"]
                <= today + pd.Timedelta(days=30)
            )
        ]
    )

    health_score = (
        (design_readiness * 0.60)
        +
        (
            max(
                0,
                100 - critical_deliverables
            ) * 0.20
        )
        +
        (
            max(
                0,
                100 - high_risk
            ) * 0.20
        )
    )

    health_score = round(
        max(
            0,
            min(100, health_score)
        )
    )

    return {
        "health_score": int(health_score),
        "design_readiness": int(design_readiness),
        "critical_deliverables": int(critical_deliverables),
        "high_risk": int(high_risk),
        "upcoming_submissions": int(upcoming_submissions),
    }


def render_health(metrics):

    score = metrics["health_score"]

    if score >= 80:
        colour = "#22C55E"
        status = "ON TRACK"

    elif score >= 60:
        colour = "#F59E0B"
        status = "WATCH"

    else:
        colour = "#FF1F5A"
        status = "AT RISK"

    st.markdown("""
    <style>

    .health-title {
        color: white;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
    }

    .health-row {
        color: white;
        font-size: 13px;
        font-weight: 500;
    }

    .health-value {
        color: white;
        font-size: 13px;
        font-weight: 700;
        text-align: right;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="health-title">PROJECT HEALTH</div>',
        unsafe_allow_html=True
    )

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[
                score,
                max(0, 100 - score)
            ],
            hole=0.82,
            sort=False,
            textinfo="none",
            marker=dict(
                colors=[
                    colour,
                    "#31456A"
                ]
            )
        )
    )

    fig.update_layout(
        height=170,
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        annotations=[
            dict(
                text=f"<b>{score}</b><br>/100",
                x=0.5,
                y=0.5,
                showarrow=False,
                font=dict(
                    size=18,
                    color="white"
                )
            )
        ]
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )

    st.markdown(
        f"""
        <div style="
            text-align:center;
            color:{colour};
            font-size:12px;
            font-weight:700;
            margin-top:-10px;
            margin-bottom:12px;
        ">
            {status}
        </div>
        """,
        unsafe_allow_html=True
    )

    rows = [
        (
            "🟢 Readiness",
            f"{metrics['design_readiness']}%"
        ),
        (
            "🔴 Critical",
            metrics["critical_deliverables"]
        ),
        (
            "🟠 High Risk",
            metrics["high_risk"]
        ),
        (
            "🟡 Upcoming",
            metrics["upcoming_submissions"]
        ),
    ]

    for label, value in rows:

        col1, col2 = st.columns([4, 1])

        with col1:

            st.markdown(
                f"""
                <div class="health-row">
                    {label}
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div class="health-value">
                    {value}
                </div>
                """,
                unsafe_allow_html=True
            )