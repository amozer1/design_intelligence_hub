import streamlit as st
import plotly.graph_objects as go

from utils.project_metrics import (
    get_current_snapshot,
    get_project_metrics,
)


CARD_BG = "#081322"


def build_gauge(score):

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[
                score,
                100 - score,
                100
            ],
            hole=0.78,
            rotation=180,
            sort=False,
            direction="clockwise",
            textinfo="none",
            marker=dict(
                colors=[
                    "#FF3131",
                    "#94A3B8",
                    "rgba(0,0,0,0)"
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
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        annotations=[
            dict(
                text=f"{score}%",
                x=0.50,
                y=0.42,
                showarrow=False,
                font=dict(
                    size=40,
                    color="white"
                )
            )
        ]
    )

    return fig


def get_status(score):

    if score >= 80:
        return "ON TRACK"

    if score >= 60:
        return "WATCHLIST"

    return "AT RISK"


def render(cl32):

    current_df, _ = get_current_snapshot(
        cl32
    )

    metrics = get_project_metrics(
        current_df
    )

    score = metrics["health_score"]

    readiness = metrics[
        "design_readiness"
    ]

    programme_drift = metrics[
        "programme_drift"
    ]

    high_risk = metrics[
        "high_risk"
    ]

    critical_deliverables = metrics[
        "critical_deliverables"
    ]

    status = get_status(score)

    st.markdown(
        f"""
        <div style="
            background:{CARD_BG};
            border-radius:16px;
            padding:16px;
        ">
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.container(border=True):

        st.caption(
            "EXECUTIVE SUMMARY (AI GENERATED)"
        )

        if status == "ON TRACK":
            st.success(status)

        elif status == "WATCHLIST":
            st.warning(status)

        else:
            st.error(status)

        gauge_col, insight_col = st.columns(
            [1.4, 2.6]
        )

        with gauge_col:

            st.plotly_chart(
                build_gauge(score),
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )

        with insight_col:

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

            if (
                programme_drift <= 0
                and high_risk <= 0
                and critical_deliverables <= 0
            ):
                st.write(
                    "✅ No material delivery risks identified"
                )

        st.caption(
            "Design Readiness Index"
        )

        st.markdown(
            f"## {readiness}%"
        )

        if score >= 80:
            st.success(
                "Trending positively"
            )

        elif score >= 60:
            st.warning(
                "Requires monitoring"
            )

        else:
            st.error(
                "Delivery risk increasing"
            )