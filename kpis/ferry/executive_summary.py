import streamlit as st
import plotly.graph_objects as go

from utils.project_metrics import (
    get_current_snapshot,
    get_project_metrics,
)


CARD_BG = "#08244D"
CARD_BORDER = "#1F4E8C"


def get_status(score):

    if score >= 80:
        return "ON TRACK"

    if score >= 60:
        return "WATCHLIST"

    return "AT RISK"


def get_trend(cl32):

    snapshots = sorted(
        cl32["SnapshotDate"].dropna().unique()
    )

    if len(snapshots) < 2:
        return 0

    current_df = cl32[
        cl32["SnapshotDate"] == snapshots[-1]
    ]

    previous_df = cl32[
        cl32["SnapshotDate"] == snapshots[-2]
    ]

    current_metrics = get_project_metrics(
        current_df
    )

    previous_metrics = get_project_metrics(
        previous_df
    )

    return (
        current_metrics["health_score"]
        - previous_metrics["health_score"]
    )


def build_insights(metrics):

    insights = []

    if metrics["programme_drift"] > 0:
        insights.append(
            f"{metrics['programme_drift']} days behind baseline"
        )

    if metrics["high_risk"] > 0:
        insights.append(
            f"{metrics['high_risk']} activities with negative float"
        )

    if metrics["critical_deliverables"] > 0:
        insights.append(
            f"{metrics['critical_deliverables']} deliverables ≤5d float"
        )

    if not insights:
        insights.append(
            "No material delivery risks identified"
        )

    return insights[:3]


def build_gauge(score):

    if score >= 80:
        score_colour = "#22C55E"
    elif score >= 60:
        score_colour = "#FFC107"
    else:
        score_colour = "#FF2D2D"

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[
                score,
                100 - score,
                100
            ],
            hole=0.80,
            rotation=180,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    score_colour,
                    "#65748B",
                    "rgba(0,0,0,0)"
                ]
            )
        )
    )

    fig.update_layout(
        height=260,
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        annotations=[
            dict(
                text=f"{score}%",
                x=0.5,
                y=0.42,
                showarrow=False,
                font=dict(
                    size=52,
                    color="white"
                )
            )
        ]
    )

    return fig


def render(cl32):

    current_df, _ = get_current_snapshot(
        cl32
    )

    metrics = get_project_metrics(
        current_df
    )

    score = metrics["health_score"]

    readiness = metrics["design_readiness"]

    trend = get_trend(cl32)

    status = get_status(score)

    insights = build_insights(metrics)

    status_colour = {
        "AT RISK": "#5B1833",
        "WATCHLIST": "#6B4F00",
        "ON TRACK": "#14532D"
    }

    st.markdown(
        f"""
        <div style="
            background:{CARD_BG};
            border:1px solid {CARD_BORDER};
            border-radius:14px;
            padding:20px;
            min-height:520px;
        ">
        """,
        unsafe_allow_html=True
    )

    header_left, header_right = st.columns(
        [4, 2]
    )

    with header_left:

        st.markdown(
            """
            <div style="
                color:#AEBBD0;
                font-size:14px;
                font-weight:600;
                letter-spacing:0.5px;
            ">
                EXECUTIVE SUMMARY (AI GENERATED)
            </div>
            """,
            unsafe_allow_html=True
        )

    with header_right:

        st.markdown(
            f"""
            <div style="
                background:{status_colour[status]};
                color:white;
                border-radius:10px;
                padding:10px;
                text-align:center;
                font-weight:700;
                white-space:nowrap;
            ">
                {status}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    gauge_col, insight_col = st.columns(
        [2, 3]
    )

    with gauge_col:

        st.plotly_chart(
            build_gauge(score),
            use_container_width=True,
            config={"displayModeBar": False}
        )

    with insight_col:

        st.markdown("<br>", unsafe_allow_html=True)

        for insight in insights:

            st.markdown(
                f"""
                <div style="
                    color:white;
                    font-size:18px;
                    font-weight:600;
                    margin-bottom:24px;
                    line-height:1.5;
                ">
                    ✅ {insight}
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        """
        <div style="
            color:#B8C3D6;
            font-size:14px;
            margin-top:10px;
        ">
            Design Readiness Index
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="
            font-size:56px;
            font-weight:700;
            color:white;
            line-height:1;
            margin-top:6px;
        ">
            {readiness}%
        </div>
        """,
        unsafe_allow_html=True
    )

    trend_arrow = "↑" if trend >= 0 else "↓"
    trend_colour = "#22C55E" if trend >= 0 else "#EF4444"

    st.markdown(
        f"""
        <div style="
            display:inline-block;
            margin-top:10px;
            padding:6px 12px;
            background:#083344;
            color:white;
            border-radius:20px;
            font-weight:600;
        ">
            <span style="color:{trend_colour}">
                {trend_arrow}
            </span>
            {abs(trend)} vs last snapshot
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )