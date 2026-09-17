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
        + (max(0, 100 - critical_deliverables) * 0.20)
        + (max(0, 100 - high_risk) * 0.20)
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
        ring_colour = "#3BD671"
    elif score >= 60:
        ring_colour = "#F5A623"
    else:
        ring_colour = "#FF1F5A"

    st.markdown(
        """
        <div style='color:white;font-weight:700;font-size:12px'>
        PROJECT HEALTH
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1.1, 1.9])

    with col1:

        fig = go.Figure(
            go.Pie(
                values=[
                    score,
                    max(0, 100 - score)
                ],
                hole=0.90,
                sort=False,
                textinfo="none",
                marker_colors=[
                    ring_colour,
                    "#405A87"
                ]
            )
        )

        fig.update_layout(
            height=125,
            margin=dict(
                l=0,
                r=0,
                t=0,
                b=0
            ),
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            annotations=[
                dict(
                    text=f"<b>{score}</b><br>100",
                    x=0.5,
                    y=0.5,
                    showarrow=False,
                    font=dict(
                        size=12,
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

    with col2:

        rows = [
            (
                "🟢 Design Readiness",
                f"{metrics['design_readiness']}%"
            ),
            (
                "🟡 Critical Deliverables",
                str(metrics["critical_deliverables"])
            ),
            (
                "🟠 High Risk Activities",
                str(metrics["high_risk"])
            ),
            (
                "🟨 Upcoming Submissions",
                str(metrics["upcoming_submissions"])
            ),
        ]

        for label, value in rows:

            c1, c2 = st.columns([3, 1])

            with c1:
                st.markdown(
                    f"""
                    <span style="color:white;">
                    {label}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

            with c2:
                st.markdown(
                    f"""
                    <span style="color:white;font-weight:700;">
                    {value}
                    </span>
                    """,
                    unsafe_allow_html=True
                )