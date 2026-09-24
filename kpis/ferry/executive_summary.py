import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


def build_gauge(score):

    colour = "#EF4444"

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
            hole=0.82,
            rotation=180,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    colour,
                    "#CBD5E1",
                    "rgba(0,0,0,0)"
                ]
            )
        )
    )

    fig.update_layout(
        height=135,
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
                    size=24,
                    color="#111827"
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
    critical_deliverables = metrics["critical_deliverables"]

    status = get_status(score)

    status_colour = "#DC2626"

    status_upper = str(status).upper()

    if "TRACK" in status_upper:
        status_colour = "#16A34A"

    elif "WATCH" in status_upper:
        status_colour = "#CA8A04"

    st.markdown(
        """
        <style>

        .exec-card{
            background:#FFFFFF;
            border:1px solid #E5E7EB;
            border-radius:10px;
            padding:14px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="exec-card">',
        unsafe_allow_html=True
    )

    # =====================================
    # HEADER
    # =====================================

    title_col, status_col = st.columns([4, 1])

    with title_col:

        st.markdown(
            """
            <div style="
                color:#111827;
                font-size:15px;
                font-weight:700;
            ">
            EXECUTIVE SUMMARY
            </div>

            <div style="
                color:#6B7280;
                font-size:11px;
                margin-top:-4px;
            ">
            AI Generated
            </div>
            """,
            unsafe_allow_html=True
        )

    with status_col:

        st.markdown(
            f"""
            <div style="
                background:{status_colour};
                color:white;
                text-align:center;
                border-radius:6px;
                padding:6px;
                font-size:10px;
                font-weight:700;
            ">
            {status}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # =====================================
    # BODY
    # =====================================

    gauge_col, insight_col = st.columns([1, 2])

    with gauge_col:

        st.plotly_chart(
            build_gauge(score),
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

    with insight_col:

        insights = []

        if programme_drift > 0:
            insights.append(
                f"Programme is behind baseline by {programme_drift} days."
            )

        if high_risk > 0:
            insights.append(
                f"{high_risk} activities currently carry negative float."
            )

        if critical_deliverables > 0:
            insights.append(
                f"{critical_deliverables} critical deliverables require attention."
            )

        if not insights:

            insights.append(
                "No significant delivery risks identified."
            )

        for item in insights:

            st.markdown(
                f"""
                <div style="
                    color:#374151;
                    font-size:13px;
                    margin-bottom:12px;
                ">
                ✅ {item}
                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()

    # =====================================
    # FOOTER
    # =====================================

    footer_left, footer_right = st.columns([3, 1])

    with footer_left:

        st.markdown(
            """
            <div style="
                color:#6B7280;
                font-size:12px;
                font-weight:600;
            ">
            Design Readiness Index
            </div>
            """,
            unsafe_allow_html=True
        )

    with footer_right:

        st.markdown(
            f"""
            <div style="
                color:#16A34A;
                font-size:20px;
                font-weight:700;
                text-align:right;
            ">
            {readiness}%
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )