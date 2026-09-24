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
        return f"{abs(days)} Days Late"

    if days > 0:
        return f"{days} Days Early"

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
                color:#111827;
                font-size:16px;
                font-weight:700;
                margin-bottom:16px;
            ">
                PROGRAMME MILESTONES
            </div>
            """,
            unsafe_allow_html=True
        )

        # ===================================
        # PROGRAMME FINISH
        # ===================================

        icon_col, content_col = st.columns([1, 6])

        with icon_col:

            st.markdown(
                f"""
                <div style="
                    color:{ICON_BLUE};
                    font-size:28px;
                    margin-top:6px;
                ">
                    📅
                </div>
                """,
                unsafe_allow_html=True
            )

        with content_col:

            st.markdown(
                """
                <div style="
                    color:#6B7280;
                    font-size:11px;
                    font-weight:700;
                    text-transform:uppercase;
                ">
                    Programme Finish
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div style="
                    color:{TITLE};
                    font-size:28px;
                    font-weight:700;
                    margin-top:4px;
                ">
                    {programme_finish}
                </div>
                """,
                unsafe_allow_html=True
            )

            baseline_col, badge_col = st.columns([3, 2])

            with baseline_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{MUTED};
                        font-size:11px;
                        margin-top:8px;
                    ">
                        Baseline: {programme_baseline}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with badge_col:

                st.markdown(
                    f"""
                    <div style="
                        background:{variance_colour(programme_variance)};
                        color:white;
                        text-align:center;
                        border-radius:8px;
                        padding:6px;
                        font-size:11px;
                        font-weight:700;
                        margin-top:4px;
                    ">
                        {variance_text(programme_variance)}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.divider()

        # ===================================
        # CONTRACT COMPLETION
        # ===================================

        icon_col, content_col = st.columns([1, 6])

        with icon_col:

            st.markdown(
                f"""
                <div style="
                    color:{ICON_GOLD};
                    font-size:28px;
                    margin-top:6px;
                ">
                    🤝
                </div>
                """,
                unsafe_allow_html=True
            )

        with content_col:

            st.markdown(
                """
                <div style="
                    color:#6B7280;
                    font-size:11px;
                    font-weight:700;
                    text-transform:uppercase;
                ">
                    Contract Completion
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div style="
                    color:{TITLE};
                    font-size:28px;
                    font-weight:700;
                    margin-top:4px;
                ">
                    {contract_finish}
                </div>
                """,
                unsafe_allow_html=True
            )

            baseline_col, badge_col = st.columns([3, 2])

            with baseline_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{MUTED};
                        font-size:11px;
                        margin-top:8px;
                    ">
                        Baseline: {contract_baseline}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with badge_col:

                st.markdown(
                    f"""
                    <div style="
                        background:{variance_colour(contract_variance)};
                        color:white;
                        text-align:center;
                        border-radius:8px;
                        padding:6px;
                        font-size:11px;
                        font-weight:700;
                        margin-top:4px;
                    ">
                        {variance_text(contract_variance)}
                    </div>
                    """,
                    unsafe_allow_html=True
                )