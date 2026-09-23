import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


CARD_BG = "#FFFFFF"
HEADER_BG = "#FF0000"
BORDER = "#00FF00"


def build_gauge(score):

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
                    "#FF0000",
                    "#BBBBBB",
                    "rgba(0,0,0,0)"
                ]
            )
        )
    )

    fig.update_layout(
        height=140,
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        annotations=[
            dict(
                text=f"{score}%",
                x=0.5,
                y=0.42,
                showarrow=False,
                font=dict(
                    size=18,
                    color="black"
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

    st.markdown(
        f"""
        <style>

        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background:{CARD_BG} !important;
            border:4px solid {BORDER} !important;
            border-radius:12px !important;
            padding:20px !important;
        }}

        div[data-testid="stVerticalBlockBorderWrapper"] * {{
            color:black !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    with st.container(border=True):

        st.markdown(
            f"""
            <div style="
                background:{HEADER_BG};
                color:white !important;
                padding:10px;
                border-radius:8px;
                font-size:12px;
                font-weight:700;
                margin-bottom:15px;
            ">
                EXECUTIVE SUMMARY (AI GENERATED)
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"## {status}"
        )

        left, right = st.columns([1, 2])

        with left:

            st.plotly_chart(
                build_gauge(score),
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )

            st.write("Design Readiness")

            st.markdown(
                f"### {readiness}%"
            )

        with right:

            st.write(
                f"Programme behind baseline by {programme_drift} days."
            )

            st.write(
                f"{high_risk} activities with negative float."
            )

            st.write(
                f"{critical_deliverables} critical deliverables."
            )