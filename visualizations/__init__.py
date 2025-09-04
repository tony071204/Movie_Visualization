"""Visualizations Module - Export all chart functions"""

# Bar Charts
from visualizations.bar_charts import (
    create_top_films_chart,
    create_first_month_chart,
    create_efficiency_chart,
    create_peak_timing_chart
)

# Scatter Charts
from visualizations.scatter_charts import (
    create_gross_vs_admissions_chart,
    create_gross_vs_theatre_chart
)

# Comparison Charts
from visualizations.comparsion_charts import create_comparison_chart

# Time Series Charts
from visualizations.time_series_charts import create_decay_chart

# Metrics
from visualizations.metrics import (
    render_total_films_metric,
    render_total_gross_metric,
    render_avg_gross_metric,
    render_top_film_metric
)

# Tables
from visualizations.tables import (
    render_summary_table,
    render_db_stats
)

# Insights
from visualizations.insights import (
    render_insights_text,
    render_insights_markdown
)

__all__ = [
    # Bar Charts
    'create_top_films_chart',
    'create_first_month_chart',
    'create_efficiency_chart',
    'create_peak_timing_chart',

    # Scatter Charts
    'create_gross_vs_admissions_chart',
    'create_gross_vs_theatre_chart',

    # Comparison & Time Series
    'create_comparison_chart',
    'create_decay_chart',

    # Metrics
    'render_total_films_metric',
    'render_total_gross_metric',
    'render_avg_gross_metric',
    'render_top_film_metric',

    # Tables & Insights
    'render_summary_table',
    'render_db_stats',
    'render_insights_text',
    'render_insights_markdown'
]
