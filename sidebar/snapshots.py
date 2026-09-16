import streamlit as st


def render_snapshots(
    snapshot_dates,
    current_snapshot
):

    st.markdown(
        "<div class='section-title'>SNAPSHOT HISTORY</div>",
        unsafe_allow_html=True
    )

    for dt in snapshot_dates:

        label = dt.strftime("%d %b %Y")

        if dt == current_snapshot:
            label += " (Current)"

        st.write(label)