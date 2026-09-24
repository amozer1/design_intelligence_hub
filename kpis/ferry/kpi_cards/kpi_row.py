import streamlit as st

from kpis.ferry.total_deliverables import render as total_render
from kpis.ferry.critical_deliverables import render as critical_render
from kpis.ferry.average_float import render as float_render
from kpis.ferry.average_variance import render as variance_render


def render(metrics):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        total_render(
            metrics["total_deliverables"],
            metrics["deliverables_delta"]
        )

    with c2:
        critical_render(
            metrics["critical_deliverables"],
            metrics["critical_delta"]
        )

    with c3:
        float_render(
            metrics["avg_float"]
        )

    with c4:
        variance_render(
            metrics["avg_variance"]
        )