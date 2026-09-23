import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


def build_gauge(score):

    colour = "#FF3B30"

    if score >= 80:
        colour = "#00C853"

    elif score >= 60:
        colour = "#FFD700"

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[
                score,
                100 - score,
                100
            ],
            hole=0.82,
            rotation=180,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    colour,
                    "#64748B",
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
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        annotations=[
            dict(
                text=f"{score}%",
                x=0.5,
                y=0.42,
                showarrow=False,
                font=dict(
                    size=34,
                    color="white"
                )
            )
        ]
    )

    return fig


def render(cl32):

    metrics = get_metrics(cl32)

    score = metrics["health_score"]

    readiness = metrics["design_readiness"]

    programme_drift = metrics["programme_drift"]

    high_risk = metrics["high_risk"]

    critical_deliverables = metrics[
        "critical_deliverables"
    ]

    status = get_status(score)

    left, right = st.columns(
        [1.2, 2.8]
    )

    with left:

        st.plotly_chart(
            build_gauge(score),
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

        m1, m2 = st.columns(2)

        with m1:

            st.caption(
                "Health"
            )

            st.markdown(
                f"### {score}%"
            )

        with m2:

            st.caption(
                "Readiness"
            )

            st.markdown(
                f"### {readiness}%"
            )

        st.caption(
            f"Status: {status}"
        )

    with right:

        st.markdown(
            "### Key Insights"
        )

        insights = []

        if programme_drift > 0:

            insights.append(
                f"Programme behind baseline by {programme_drift} days."
            )

        if high_risk > 0:

            insights.append(
                f"{high_risk} activities with negative float."
            )

        if critical_deliverables > 0:

            insights.append(
                f"{critical_deliverables} critical deliverables require attention."
            )

        if not insights:

            insights.append(
                "No material delivery risks identified."
            )

        for item in insights:

            st.write(
                f"• {item}"
            )