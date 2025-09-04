"""Main Layout Module"""
from shiny import ui
from ui.styles import get_custom_css
from ui.tabs import *


def create_dashboard_ui():
    """Create complete dashboard UI"""
    return ui.page_fluid(
        # Custom CSS
        ui.tags.head(
            ui.tags.style(get_custom_css())
        ),

        # Header
        ui.div(
            ui.h1("🎬 Movie Box Office Analytics Dashboard"),
            ui.p("Interactive visualization of movie box office performance data"),
            class_="dashboard-header"
        ),

        # Metrics Row
        ui.row(
            ui.column(3, ui.output_ui("total_films_metric")),
            ui.column(3, ui.output_ui("total_gross_metric")),
            ui.column(3, ui.output_ui("avg_gross_metric")),
            ui.column(3, ui.output_ui("top_film_metric"))
        ),

        # Navigation Tabs
        ui.navset_tab(
            create_about_tab(),
            create_rankings_tab(),
            create_performance_tab(),
            create_trends_tab(),
            create_insights_tab()
        )
    )
