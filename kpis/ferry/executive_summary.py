import streamlit as st
import plotly.graph_objects as go


def build_gauge(score):

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            values=[score, 100 - score, 100],
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
                x=0.5,
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


def render(cl32):

    score = 55
    readiness = 37

    with st.container(border=True):

        st.caption(
            "EXECUTIVE SUMMARY (AI GENERATED)"
        )

        st.error("AT RISK")

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

            st.write("")

            st.write(
                "✅ 26 days behind baseline"
            )

            st.write(
                "✅ 31 activities with negative float"
            )

            st.write(
                "✅ 43 deliverables ≤5d float"
            )

        st.caption(
            "Design Readiness Index"
        )

        st.write(
            f"## {readiness}%"
        )

        st.info(
            "↓ 7 vs last snapshot"
        )