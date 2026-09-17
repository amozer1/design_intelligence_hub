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

    health_score = round(
        max(
            0,
            min(
                100,
                (
                    (design_readiness * 0.60)
                    +
                    (max(0, 100 - critical_deliverables) * 0.20)
                    +
                    (max(0, 100 - high_risk) * 0.20)
                )
            )
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
        ring_colour = "#FF2D5E"

    st.markdown(
        """
        <div style="
            color:#B7C7DA;
            font-size:12px;
            font-weight:700;
            letter-spacing:0.5px;
            margin-top:8px;
            margin-bottom:18px;
        ">
            PROJECT HEALTH
        </div>
        """,
        unsafe_allow_html=True
    )

    donut_col, metrics_col = st.columns(
        [1.15, 1.85],
        gap="small"
    )

    with donut_col:

        fig = go.Figure(
            go.Pie(
                values=[
                    score,
                    max(0, 100 - score)
                ],
                hole=0.88,
                sort=False,
                textinfo="none",
                marker_colors=[
                    ring_colour,
                    "#405A87"
                ]
            )
        )

        fig.update_layout(
            height=130,
            margin=dict(
                l=0,
                r=0,
                t=15,
                b=0
            ),
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            annotations=[
                dict(
                    text=f"<b>{score}</b><br><span style='font-size:9px'>100</span>",
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
            config={"displayModeBar": False}
        )

    with metrics_col:

        st.write("")
        st.write("")

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

            left, right = st.columns([3, 1])

            with left:
                st.markdown(
                    f"""
                    <span style="
                        color:white;
                        font-size:14px;
                    ">
                        {label}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

            with right:
                st.markdown(
                    f"""
                    <span style="
                        color:white;
                        font-size:14px;
                        font-weight:700;
                    ">
                        {value}
                    </span>
                    """,
                    unsafe_allow_html=True
                )