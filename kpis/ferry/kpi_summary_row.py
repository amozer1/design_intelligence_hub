import streamlit as st

from kpis.ferry.total_deliverables import render as render_total
from kpis.ferry.critical_deliverables import render as render_critical
from kpis.ferry.average_float import render as render_float
from kpis.ferry.average_variance import render as render_variance


def render(metrics):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_total(metrics)

    with c2:
        render_critical(metrics)

    with c3:
        render_float(metrics)

    with c4:
        render_variance(metrics)