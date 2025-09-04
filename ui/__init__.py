"""UI Module - Export main UI functions"""
from ui.layout import create_dashboard_ui
from ui.styles import get_custom_css
from ui.tabs import (
    create_about_tab,
    create_rankings_tab,
    create_performance_tab,
    create_trends_tab,
    create_insights_tab
)

__all__ = [
    'create_app_ui',
    'create_dashboard_ui',
    'get_custom_css',
    'create_about_tab',
    'create_rankings_tab',
    'create_performance_tab',
    'create_trends_tab',
    'create_insights_tab'
]
