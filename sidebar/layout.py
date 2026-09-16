import streamlit as st


def render_sidebar():

    with st.sidebar:

        # ==========================================
        # BRANDING
        # ==========================================

        st.title("🎯 Design Intelligence Hub")

        st.caption(
            "Design Smarter. Deliver Better."
        )

        st.divider()

        # ==========================================
        # FRAMEWORKS
        # ==========================================

        st.markdown("##### FRAMEWORKS")

        with st.expander(
            "UU DD&B Framework",
            expanded=True
        ):
            st.write("Ferry PS")
            st.write("Rossall Outfall")
            st.write("Flass Lane")

        st.divider()

        # ==========================================
        # NAVIGATION
        # ==========================================

        st.markdown(
            "##### MAIN NAVIGATION"
        )

        st.button(
            "Executive Dashboard",
            use_container_width=True
        )

        st.button(
            "Deliverables",
            use_container_width=True
        )

        st.button(
            "Discipline Performance",
            use_container_width=True
        )

        st.button(
            "Programme Drift",
            use_container_width=True
        )

        st.button(
            "Design Readiness",
            use_container_width=True
        )

        st.divider()

        # ==========================================
        # SNAPSHOTS
        # ==========================================

        st.markdown(
            "##### SNAPSHOT HISTORY"
        )

        with st.container(border=True):

            st.write("Current Snapshot")
            st.write("Previous Snapshot")
            st.write("Historic Snapshot")

        st.divider()

        # ==========================================
        # HEALTH
        # ==========================================

        st.markdown(
            "##### PROJECT HEALTH"
        )

        with st.container(border=True):

            st.metric(
                "Health Score",
                "0"
            )

            st.metric(
                "Readiness",
                "0%"
            )

        st.divider()

        # ==========================================
        # BASELINE
        # ==========================================

        st.markdown(
            "##### PROJECT BASELINE"
        )

        with st.container(border=True):

            st.write("Baseline Finish")

            st.write("Current Forecast")

            st.write("Programme Drift")