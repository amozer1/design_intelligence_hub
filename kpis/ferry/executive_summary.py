import streamlit as st
import plotly.graph_objects as go


CARD_BG = "#10203A"
CARD_BORDER = "#00AEEF"


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


def render(cl32):

    score = 55
    readiness = 37

    st.markdown(
        f"""
        <style>

        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background:{CARD_BG} !important;
            border:2px solid {CARD_BORDER} !important;
            border-radius:16px !important;
            box-shadow:0 8px 20px rgba(0,0,0,0.35) !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    with st.container(border=True):

        st.markdown(
            """
            <div style="
                color:#DDEAFF;
                font-size:12px;
                font-weight:600;
                letter-spacing:0.5px;
                margin-bottom:8px;
            ">
                EXECUTIVE SUMMARY (AI GENERATED)
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                display:inline-block;
                background:#E0005A;
                color:white;
                padding:6px 12px;
                border-radius:8px;
                font-size:12px;
                font-weight:700;
                margin-bottom:14px;
            ">
                AT RISK
            </div>
            """,
            unsafe_allow_html=True
        )

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

            st.markdown(
                "<br>",
                unsafe_allow_html=True
            )

            st.markdown(
                "✅ 26 days behind baseline"
            )

            st.markdown(
                "✅ 31 activities with negative float"
            )

            st.markdown(
                "✅ 43 deliverables ≤5d float"
            )

        st.markdown(
            """
            <div style="
                color:#DDEAFF;
                font-size:13px;
            ">
                Design Readiness Index
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                color:white;
                font-size:42px;
                font-weight:700;
            ">
                {readiness}%
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                display:inline-block;
                background:#0D6E95;
                padding:6px 12px;
                border-radius:16px;
                color:white;
                font-weight:600;
                font-size:12px;
            ">
                ↓ 7 vs last snapshot
            </div>
            """,
            unsafe_allow_html=True
        )