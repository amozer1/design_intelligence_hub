import streamlit as st

from kpis.ferry.programme_completion_utils import (
    calculate_variance,
    variance_colour,
    variance_text,
)

from kpis.ferry.programme_completion_styles import (
    TITLE,
    MUTED,
    ICON_BLUE,
    ICON_GOLD,
)


def render(
    programme_finish,
    programme_baseline,
    contract_completion,
    contract_baseline,
):

    programme_variance = calculate_variance(
        programme_finish,
        programme_baseline
    )

    contract_variance = calculate_variance(
        contract_completion,
        contract_baseline
    )

    with st.container(border=True):

        left_col, right_col = st.columns(2)

        # ==================================
        # PROGRAMME FINISH
        # ==================================

        with left_col:

            st.markdown(
                """
                <div style="
                    color:#6B7280;
                    font-size:11px;
                    font-weight:700;
                    margin-bottom:16px;
                    text-transform:uppercase;
                ">
                    Programme Finish
                </div>
                """,
                unsafe_allow_html=True
            )

            icon_col, date_col = st.columns(
                [1, 4]
            )

            with icon_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{ICON_BLUE};
                        font-size:28px;
                    ">
                        📅
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with date_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{TITLE};
                        font-size:20px;
                        font-weight:700;
                    ">
                        {programme_finish}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("")

            baseline_col, badge_col = st.columns(
                [3, 2]
            )

            with baseline_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{MUTED};
                        font-size:11px;
                    ">
                        Baseline:
                        {programme_baseline}
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
                    ">
                        {variance_text(programme_variance)}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # ==================================
        # CONTRACT COMPLETION
        # ==================================

        with right_col:

            st.markdown(
                """
                <div style="
                    color:#6B7280;
                    font-size:11px;
                    font-weight:700;
                    margin-bottom:16px;
                    text-transform:uppercase;
                ">
                    Contract Completion
                </div>
                """,
                unsafe_allow_html=True
            )

            icon_col, date_col = st.columns(
                [1, 4]
            )

            with icon_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{ICON_GOLD};
                        font-size:28px;
                    ">
                        🤝
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with date_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{TITLE};
                        font-size:20px;
                        font-weight:700;
                    ">
                        {contract_completion}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("")

            baseline_col, badge_col = st.columns(
                [3, 2]
            )

            with baseline_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{MUTED};
                        font-size:11px;
                    ">
                        Baseline:
                        {contract_baseline}
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
                    ">
                        {variance_text(contract_variance)}
                    </div>
                    """,
                    unsafe_allow_html=True
                )