import streamlit as st
import plotly.graph_objects as go

from kpis.ferry.executive_summary_utils import (
    get_metrics,
    get_status,
)


PANEL_BG = "#DBEAFE"
BORDER = "#3B82F6"


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
                    "#94A3B8",
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
                    size=22,
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

    status_upper = str(status).upper()

    if "TRACK" in status_upper:
        badge_colour = "#16A34A"

    elif "WATCH" in status_upper:
        badge_colour = "#CA8A04"

    else:
        badge_colour = "#DC2626"

    st.markdown(
        f"""
        <style>

        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background:{PANEL_BG} !important;
            border:3px solid {BORDER} !important;
            border-radius:12px !important;
            padding:16px !important;
            box-shadow:0 4px 12px rgba(59,130,246,.20) !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    with st.container(border=True):

        header_left, header_right = st.columns([6, 1])

        with header_left:

            st.markdown(
                """
                <span style="
                    color:#1E293B;
                    font-size:13px;
                    font-weight:700;
                ">
                EXECUTIVE SUMMARY
                </span>

                <span style="
                    color:#64748B;
                    font-size:11px;
                    margin-left:6px;
                ">
                (AI GENERATED)
                </span>
                """,
                unsafe_allow_html=True
            )

        with header_right:

            st.markdown(
                f"""
                <div style="
                    background:{badge_colour};
                    color:white;
                    text-align:center;
                    padding:4px 8px;
                    border-radius:6px;
                    font-size:11px;
                    font-weight:700;
                ">
                {status}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")

        left, right = st.columns([1, 2])

        with left:

            st.plotly_chart(
                build_gauge(score),
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )

            st.caption("Design Readiness Index")

            st.markdown(
                f"""
                <span style="
                    color:#1E293B;
                    font-size:14px;
                    font-weight:700;
                ">
                {readiness}%
                </span>
                """,
                unsafe_allow_html=True
            )

        with right:

            if programme_drift > 0:

                st.markdown(
                    f"""
                    <div style="color:#1E293B;">
                    🔴 Programme is behind baseline by {programme_drift} days.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            if high_risk > 0:

                st.markdown(
                    f"""
                    <div style="color:#1E293B;">
                    🟠 {high_risk} activities with negative float.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            if critical_deliverables > 0:

                st.markdown(
                    f"""
                    <div style="color:#1E293B;">
                    🟡 Focus on {critical_deliverables} critical deliverables.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            if (
                programme_drift <= 0
                and high_risk <= 0
                and critical_deliverables <= 0
            ):

                st.markdown(
                    """
                    <div style="color:#1E293B;">
                    🟢 No material delivery risks identified.
                    </div>
                    """,
                    unsafe_allow_html=True
                )