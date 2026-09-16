import streamlit as st


def render_health(metrics):

    st.markdown(
        "<div class='section-title'>PROJECT HEALTH</div>",
        unsafe_allow_html=True
    )

    st.metric(
        "Health Score",
        metrics["health_score"]
    )

    st.metric(
        "Design Readiness",
        f"{metrics['design_readiness']}%"
    )

    st.metric(
        "Critical Deliverables",
        metrics["critical_deliverables"]
    )

    st.metric(
        "High Risk Activities",
        metrics["high_risk"]
    )

    st.metric(
        "Upcoming Submissions",
        metrics["upcoming_submissions"]
    )