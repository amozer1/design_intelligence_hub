import streamlit as st


def render_baseline(metrics):

    st.markdown(
        "<div class='section-title'>PROJECT BASELINE</div>",
        unsafe_allow_html=True
    )

    st.write(
        f"Baseline: "
        f"{metrics['baseline_finish']:%d %b %Y}"
    )

    st.write(
        f"Forecast: "
        f"{metrics['forecast_finish']:%d %b %Y}"
    )

    st.write(
        f"Drift: "
        f"{metrics['programme_drift']} Days"
    )