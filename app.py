import streamlit as st

from loaders.ferry_loader import load_ferry
from utils.project_metrics import (
    get_current_snapshot,
    get_project_metrics
)

from sidebar.sidebar import build_sidebar

from pages.kpis import render_kpis
from pages.executive_summary import render_executive_summary
from pages.deliverables import render_deliverables
from pages.discipline_performance import render_discipline_performance
from pages.submissions import render_submissions
from pages.changes import render_changes
from pages.ai_insights import render_ai_insights