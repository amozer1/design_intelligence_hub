import pandas as pd
import streamlit as st


TITLE = "#111827"
BODY = "#374151"
MUTED = "#6B7280"

GREEN = "#16A34A"
RED = "#DC2626"

ICON_BLUE = "#2563EB"
ICON_GOLD = "#D4AF37"


def format_date(value):

    if pd.isna(value):
        return "N/A"

    try:
        return pd.to_datetime(value).strftime(
            "%d %b %Y"
        )
    except Exception:
        return str(value)


def variance_colour(days):

    if days > 0:
        return GREEN

    if days < 0:
        return RED

    return "#6B7280"


def variance_text(days):

    if days > 0:
        return f"{days} Days"

    if days < 0:
        return f"{abs(days)} Days"

    return "On Time"


def get_metrics(cl32):

    latest_snapshot = cl32[
        cl32["SnapshotDate"]
        == cl32["SnapshotDate"].max()
    ]

    programme_row = latest_snapshot[
        latest_snapshot["Activity Name"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("planned project completion")
    ]

    contract_row = latest_snapshot[
        latest_snapshot["Activity Name"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("contract completion")
    ]

    programme_finish = "N/A"
    programme_baseline = "N/A"
    programme_variance = 0

    contract_finish = "N/A"
    contract_baseline = "N/A"
    contract_variance = 0

    if not programme_row.empty:

        programme_finish = format_date(
            programme_row.iloc[0]["Finish"]
        )

        programme_baseline = format_date(
            programme_row.iloc[0]["BL1 Finish"]
        )

        programme_variance = int(
            programme_row.iloc[0][
                "Variance - BL1 Finish Date"
            ]
        )

    if not contract_row.empty:

        contract_finish = format_date(
            contract_row.iloc[0]["Finish"]
        )

        contract_baseline = format_date(
            contract_row.iloc[0]["BL1 Finish"]
        )

        contract_variance = int(
            contract_row.iloc[0][
                "Variance - BL1 Finish Date"
            ]
        )

    return {
        "programme_finish": programme_finish,
        "programme_baseline": programme_baseline,
        "programme_variance": programme_variance,
        "contract_finish": contract_finish,
        "contract_baseline": contract_baseline,
        "contract_variance": contract_variance,
    }


def render(cl32):

    metrics = get_metrics(cl32)

    with st.container(border=True):

        left_col, right_col = st.columns(2)

        # =====================================
        # PROGRAMME FINISH
        # =====================================

        with left_col:

            st.markdown(
                """
                <div style="
                    color:#6B7280;
                    font-size:11px;
                    font-weight:700;
                    text-transform:uppercase;
                    margin-bottom:14px;
                ">
                    PROGRAMME FINISH
                </div>
                """,
                unsafe_allow_html=True
            )

            icon_col, date_col = st.columns([1, 4])

            with icon_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{ICON_BLUE};
                        font-size:30px;
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
                        font-size:22px;
                        font-weight:700;
                    ">
                        {metrics["programme_finish"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("")

            baseline_col, variance_col = st.columns([3, 2])

            with baseline_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{MUTED};
                        font-size:11px;
                    ">
                        Baseline:
                        {metrics["programme_baseline"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with variance_col:

                st.markdown(
                    f"""
                    <div style="
                        background:{variance_colour(metrics["programme_variance"])};
                        color:white;
                        border-radius:8px;
                        text-align:center;
                        padding:6px;
                        font-size:11px;
                        font-weight:700;
                    ">
                        {variance_text(metrics["programme_variance"])}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # =====================================
        # CONTRACT COMPLETION
        # =====================================

        with right_col:

            st.markdown(
                """
                <div style="
                    color:#6B7280;
                    font-size:11px;
                    font-weight:700;
                    text-transform:uppercase;
                    margin-bottom:14px;
                ">
                    CONTRACT COMPLETION
                </div>
                """,
                unsafe_allow_html=True
            )

            icon_col, date_col = st.columns([1, 4])

            with icon_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{ICON_GOLD};
                        font-size:30px;
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
                        font-size:22px;
                        font-weight:700;
                    ">
                        {metrics["contract_finish"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("")

            baseline_col, variance_col = st.columns([3, 2])

            with baseline_col:

                st.markdown(
                    f"""
                    <div style="
                        color:{MUTED};
                        font-size:11px;
                    ">
                        Baseline:
                        {metrics["contract_baseline"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with variance_col:

                st.markdown(
                    f"""
                    <div style="
                        background:{variance_colour(metrics["contract_variance"])};
                        color:white;
                        border-radius:8px;
                        text-align:center;
                        padding:6px;
                        font-size:11px;
                        font-weight:700;
                    ">
                        {variance_text(metrics["contract_variance"])}
                    </div>
                    """,
                    unsafe_allow_html=True
                )