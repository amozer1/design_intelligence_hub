import streamlit as st
import plotly.graph_objects as go


def render_health(metrics):

    st.markdown("##### PROJECT HEALTH")

    col1, col2 = st.columns([1, 2])

    with col1:

        score = metrics["health_score"]

        fig = go.Figure(
            go.Pie(
                values=[score, 100 - score],
                hole=0.75,
                sort=False,
                rotation=90,
                marker_colors=["#ff1744", "#2f3b52"],
                textinfo="none",
            )
        )

        fig.update_layout(
            height=140,
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            annotations=[
                dict(
                    text=f"<b>{score}</b><br>/100",
                    x=0.5,
                    y=0.5,
                    showarrow=False,
                    font=dict(size=20, color="white"),
                )
            ],
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False},
        )

    with col2:

        st.markdown(
            f"""
🟢 Design Readiness&nbsp;&nbsp;&nbsp;&nbsp;**{metrics['design_readiness']}%**

🟡 Critical Deliverables&nbsp;&nbsp;&nbsp;&nbsp;**{metrics['critical_deliverables']}**

🟠 High Risk Activities&nbsp;&nbsp;&nbsp;&nbsp;**{metrics['high_risk']}**

🟨 Upcoming Submissions&nbsp;&nbsp;&nbsp;&nbsp;**{metrics['upcoming_submissions']}**
"""
        )