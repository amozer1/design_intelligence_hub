import streamlit as st

from kpis.ferry.programme_completion_utils import (
    get_metrics,
)

from kpis.ferry.programme_completion_styles import (
    TITLE,
    MUTED,
    GREEN,
    RED,
    ICON_BLUE,
    ICON_GOLD,
)


def variance_colour(days):

    if days < 0:
        return RED

    if days > 0:
        return GREEN

    return "#6B7280"


def variance_text(days):

    if days < 0:
        return f"{abs(days)} Days"

    if days > 0:
        return f"{days} Days"

    return "On Time"


def render(cl32):

    metrics = get_metrics(cl32)

    programme_finish = metrics["programme_finish"]
    programme_baseline = metrics["programme_baseline"]
    programme_variance = metrics["programme_variance"]

    contract_finish = metrics["contract_finish"]
    contract_baseline = metrics["contract_baseline"]
    contract_variance = metrics["contract_variance"]

    with st.container(border=True):

        st.markdown(
            """
            <div style="
                min-height:260px;
            ">
            """,
            unsafe_allow_html=True,
        )

        # ===================================
        # HEADER
        # ===================================

        st.markdown(
            """
            <div style="
                color:#111827;
                font-size:16px;
                font-weight:700;
                margin-bottom:22px;
            ">
                PROGRAMME MILESTONES
            </div>
            """,
            unsafe_allow_html=True,
        )

        left_col, right_col = st.columns(2)

        # ===================================
        # PROGRAMME FINISH
        # ===================================

        with left_col:

            icon_col, date_col = st.columns([1, 5])

            with icon_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{ICON_BLUE};
                        font-size:32px;
                        margin-top:8px;
                    ">
                        📅
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with date_col:

                st.markdown(
                    """
                    <div style="
                        color:#6B7280;
                        font-size:11px;
                        font-weight:700;
                        text-transform:uppercase;
                        margin-bottom:10px;
                    ">
                        Programme Finish
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.markdown(
                    f"""
                    <div style="
                        color:{TITLE};
                        font-size:32px;
                        font-weight:700;
                        line-height:1.1;
                    ">
                        {programme_finish}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.write("")
            st.write("")

            baseline_col, badge_col = st.columns([3, 2])

            with baseline_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{MUTED};
                        font-size:11px;
                    ">
                        Baseline: {programme_baseline}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with badge_col:

                st.markdown(
                    f"""
                    <div style="
                        background:{variance_colour(programme_variance)};
                        color:white;
                        text-align:center;
                        border-radius:8px;
                        padding:8px 12px;
                        font-size:11px;
                        font-weight:700;
                    ">
                        {variance_text(programme_variance)}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        # ===================================
        # CONTRACT COMPLETION
        # ===================================

        with right_col