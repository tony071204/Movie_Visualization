"""Comparison Charts Module"""
import plotly.graph_objects as go
import pandas as pd
from shiny import ui
from config.theme import *
from visualizations.utils import apply_standard_layout
import traceback


def create_comparison_chart(total_df, first_month_df):
    """Create comparison chart between total and first month"""
    try:
        if total_df.empty or first_month_df.empty:
            return ui.div(
                ui.p("Insufficient data for comparison chart."),
                class_="error-message"
            )

        comparison_df = pd.merge(
            total_df[['title', 'total_gross']],
            first_month_df[['title', 'total_gross']],
            on='title',
            how='inner',
            suffixes=('_total', '_first_month')
        )

        if comparison_df.empty:
            return ui.div(
                ui.p("No matching films found for comparison."),
                class_="error-message"
            )

        comparison_df = comparison_df.sort_values('total_gross_total')

        highest_total_idx = comparison_df['total_gross_total'].idxmax()
        highest_first_idx = comparison_df['total_gross_first_month'].idxmax()

        total_colors = [
            PROFESSIONAL_COLORS['highlight'] if idx == highest_total_idx
            else PROFESSIONAL_COLORS['primary']
            for idx in comparison_df.index
        ]

        first_month_colors = [
            PROFESSIONAL_COLORS['highlight'] if idx == highest_first_idx
            else PROFESSIONAL_COLORS['secondary']
            for idx in comparison_df.index
        ]

        fig = go.Figure()

        fig.add_trace(go.Bar(
            name='Total Gross',
            x=comparison_df['title'],
            y=comparison_df['total_gross_total'],
            marker_color=total_colors,
            texttemplate='%{y:$,.0s}',
            textposition='outside',
            textfont=dict(family=FONT_FAMILY, size=12, color='black')
        ))

        fig.add_trace(go.Bar(
            name='First Month Gross',
            x=comparison_df['title'],
            y=comparison_df['total_gross_first_month'],
            marker_color=first_month_colors,
            texttemplate='%{y:$,.0s}',
            textposition='outside',
            textfont=dict(family=FONT_FAMILY, size=12, color='black')
        ))

        apply_standard_layout(
            fig,
            title='Total vs First Month Performance Comparison',
            xaxis_title="Film Title",
            yaxis_title="Gross Earnings ($)",
            barmode='group',
            height=550,
            xaxis_tickangle=-45
        )

        return ui.HTML(
            fig.to_html(include_plotlyjs=True, div_id="comparison_plot"))

    except Exception as e:
        error_msg = f"Error generating comparison chart: {str(e)}"
        print(f"Chart error: {traceback.format_exc()}")
        return ui.div(ui.p(error_msg), class_="error-message")
