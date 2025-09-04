"""Server Handlers Module"""
from shiny import reactive, render
import data.processors

# Import từ visualizations package thay vì từng file
import visualizations.metrics
import visualizations.bar_charts
import visualizations.comparsion_charts
import visualizations.scatter_charts
import visualizations.time_series_charts
import visualizations.tables
import visualizations.insights


def create_server():
    """Create server function with all handlers"""

    def server_function(input, output, session):

        # ========== REACTIVE DATA ==========
        @reactive.Calc
        def top_films_data():
            return data.processors.get_top_films()

        @reactive.Calc
        def first_month_data():
            return data.processors.get_first_month_data()

        @reactive.Calc
        def admissions_data():
            return data.processors.get_admissions_data()

        @reactive.Calc
        def theatre_data():
            return data.processors.get_theatre_data()

        @reactive.Calc
        def weekly_trends_data():
            return data.processors.get_weekly_trends()

        # ========== METRICS OUTPUTS ==========
        @output
        @render.ui
        def total_films_metric():
            return visualizations.metrics.render_total_films_metric()

        @output
        @render.ui
        def total_gross_metric():
            return visualizations.metrics.render_total_gross_metric()

        @output
        @render.ui
        def avg_gross_metric():
            return visualizations.metrics.render_avg_gross_metric()

        @output
        @render.ui
        def top_film_metric():
            return visualizations.metrics.render_top_film_metric(
                top_films_data())

        # ========== CHART OUTPUTS ==========
        @output
        @render.ui
        def top_films_chart():
            return visualizations.bar_charts.create_top_films_chart(
                top_films_data())

        @output
        @render.ui
        def first_month_chart():
            return visualizations.bar_charts.create_first_month_chart(
                first_month_data())

        @output
        @render.ui
        def comparison_chart():
            return visualizations.comparsion_charts.create_comparison_chart(
                top_films_data(),
                first_month_data()
            )

        @output
        @render.ui
        def gross_vs_admissions_chart():
            return visualizations.scatter_charts.create_gross_vs_admissions_chart(
                admissions_data())

        @output
        @render.ui
        def gross_vs_theatre_chart():
            return visualizations.scatter_charts.create_gross_vs_theatre_chart(
                theatre_data())

        @output
        @render.ui
        def efficiency_chart():
            return visualizations.bar_charts.create_efficiency_chart(
                theatre_data())

        @output
        @render.ui
        def decay_chart():
            return visualizations.time_series_charts.create_decay_chart(
                weekly_trends_data())

        @output
        @render.ui
        def peak_timing_chart():
            return visualizations.bar_charts.create_peak_timing_chart(
                weekly_trends_data())

        # ========== TABLE & TEXT OUTPUTS ==========
        @output
        @render.table
        def summary_table():
            return visualizations.tables.render_summary_table(top_films_data())

        @output
        @render.text
        def db_stats():
            return visualizations.tables.render_db_stats()

        @output
        @render.ui
        def insights_text():
            return visualizations.insights.render_insights_text(
                top_films_data(),
                weekly_trends_data()
            )

        @output
        @render.ui
        def insights_markdown():
            return visualizations.insights.render_insights_markdown()

    return server_function
