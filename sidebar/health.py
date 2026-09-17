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
        (design_readiness * 0.6)
        + (max(0, 100 - critical_deliverables) * 0.2)
        + (max(0, 100 - high_risk) * 0.2)
    )

    health_score = round(
        max(0, min(100, health_score))
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

    st.markdown(
        """
        <div style="
            color:#B7C7DA;
            font-size:12px;
            font-weight:700;
            letter-spacing:0.5px;
            margin-bottom:6px;
        ">
            PROJECT HEALTH
        </div>
        """,
        unsafe_allow_html=True
    )

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[
                score,
                100 - score
            ],
            hole=0.78,
            sort=False,
            textinfo="none",
            marker=dict(
                colors=[
                    colour,
                    "#32466B"
                ]
            )
        )
    )

    fig.update_layout(
        height=200,
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
                y=0.52,
                showarrow=False,
                font=dict(
                    size=24,
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
            font-weight:700;
            font-size:12px;
            margin-top:-18px;
            margin-bottom:12px;
        ">
            {status}
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2 = st.columns([4, 1])

    with c1:
        st.write("🟢 Readiness")
    with c2:
        st.write(f"**{metrics['design_readiness']}%**")

    c1, c2 = st.columns([4, 1])

    with c1:
        st.write("🔴 Critical")
    with c2:
        st.write(f"**{metrics['critical_deliverables']}**")

    c1, c2 = st.columns([4, 1])

    with c1:
        st.write("🟠 High Risk")
    with c2:
        st.write(f"**{metrics['high_risk']}**")

    c1, c2 = st.columns([4, 1])

    with c1:
        st.write("🟡 Upcoming")
    with c2:
        st.write(f"**{metrics['upcoming_submissions']}**")