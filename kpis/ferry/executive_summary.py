import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_styles import (
    load_executive_summary_styles
)

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


def build_gauge(score):

    colour = "#FF1744"

    if score >= 80:
        colour = "#22C55E"

    elif score >= 60:
        colour = "#F59E0B"

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[
                score,
                100 - score,
                100
            ],
            hole=0.84,
            rotation=180,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    colour,
                    "#667085",
                    "rgba(0,0,0,0)"
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
                    size=24,
                    color="white"
                )
            )
        ]
    )

    return fig


def render(cl32):

    load_executive_summary_styles()

    metrics = get_metrics(cl32)

    score = metrics["health_score"]

    readiness = metrics["design_readiness"]

    programme_drift = metrics["programme_drift"]

    high_risk = metrics["high_risk"]

    critical_deliverables = metrics[
        "critical_deliverables"
    ]

    status = get_status(score)

    with st.container(border=True):

        st.caption(
            "EXECUTIVE SUMMARY (AI GENERATED)"
        )

        st.markdown(
            f"## {status}"
        )

        left, right = st.columns(
            [1, 2.5]
        )

        with left:

            st.plotly_chart(
                build_gauge(score),
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )

        with right:

            st.write("")

            if programme_drift > 0:
                st.write(
                    f"✅ {programme_drift} days behind baseline"
                )

            if high_risk > 0:
                st.write(
                    f"✅ {high_risk} activities with negative float"
                )

            if critical_deliverables > 0:
                st.write(
                    f"✅ {critical_deliverables} deliverables ≤5d float"
                )

        st.divider()

        st.caption(
            "DESIGN READINESS INDEX"
        )

        st.markdown(
            f"### {readiness}%"
        )

        st.caption(
            f"Status: {status}"
        )