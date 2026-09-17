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

    for col in [
        "Activity % Complete",
        "Variance - BL1 Finish Date",
        "Total Float",
        "Remaining Duration",
    ]:

        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

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

    st.markdown(
        "<div class='section-title'>PROJECT HEALTH</div>",
        unsafe_allow_html=True
    )

    score = metrics["health_score"]

    fig = go.Figure(
        go.Pie(
            values=[
                score,
                max(0, 100 - score)
            ],
            hole=0.72,
            sort=False,
            textinfo="none",
            marker=dict(
                colors=[
                    "#ff1f5a",
                    "#2d3d5c"
                ]
            )
        )
    )

    fig.update_layout(
        height=180,
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
                    size=22,
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

    c1, c2 = st.columns([4, 1])

    with c1:
        st.caption("🟢 Design Readiness")
    with c2:
        st.caption(
            f"{metrics['design_readiness']}%"
        )

    c1, c2 = st.columns([4, 1])

    with c1:
        st.caption("🟡 Critical Deliverables")
    with c2:
        st.caption(
            str(metrics["critical_deliverables"])
        )

    c1, c2 = st.columns([4, 1])

    with c1:
        st.caption("🟠 High Risk Activities")
    with c2:
        st.caption(
            str(metrics["high_risk"])
        )

    c1, c2 = st.columns([4, 1])

    with c1:
        st.caption("🟨 Upcoming Submissions")
    with c2:
        st.caption(
            str(metrics["upcoming_submissions"])
        )