import streamlit as st

from sidebar.styles import load_sidebar_styles
from sidebar.branding import render_branding
from sidebar.frameworks import render_frameworks
from sidebar.navigation import render_navigation
from sidebar.snapshots import render_snapshots
from sidebar.health import render_health
from sidebar.baseline import render_baseline


def build_sidebar(
    metrics,
    snapshot,
    snapshot_dates,
    projects,
    active_project
):

    load_sidebar_styles()

    with st.sidebar:

        render_branding()

        st.divider()

        render_frameworks(
            projects,
            active_project
        )

        st.divider()

        render_navigation()

        st.divider()

        render_snapshots(
            snapshot_dates,
            snapshot
        )

        st.divider()

        render_health(metrics)

        st.divider()

        render_baseline(metrics)