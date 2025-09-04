import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from shiny import ui
from config.theme import *
from visualizations.utils import apply_standard_layout
import traceback


def create_top_films_chart(df):
    """Create top films bar chart"""
    try:
        if df.empty:
            return ui.div(
                ui.p("No data available. Please check your database connection."),
                class_="error-message")

        fig = px.bar(
            df, x='total_gross', y='title',
            title='Top 10 Films with Highest Gross Earnings',
            labels={'title': 'Film Title', 'total_gross': 'Total Gross ($)'},
            orientation='h',
            hover_data={'title': True, 'total_gross': False, 'formatted_total_gross': True}
        )

        max_idx = df['total_gross'].idxmax()
        colors = [
            PROFESSIONAL_COLORS['highlight'] if idx == max_idx
            else PROFESSIONAL_COLORS['primary']
            for idx in df.index
        ]

        fig.update_traces(
            marker_color=colors,
            texttemplate='%{x:$,.0f}',
            textposition='outside',
            textfont=dict(family=FONT_FAMILY, size=14, color='black')
        )

        apply_standard_layout(
            fig,
            title='Top 10 Films with Highest Gross Earnings',
            xaxis_title="Total Gross ($)",
            yaxis_title="Film Title",
            showlegend=False,
            height=550,
            yaxis={'categoryorder': 'total ascending'}
        )

        return ui.HTML(
            fig.to_html(include_plotlyjs=True, div_id="top_films_plot"))

    except Exception as e:
        error_msg = f"Error generating chart: {str(e)}"
        print(f"Chart error: {traceback.format_exc()}")
        return ui.div(ui.p(error_msg), class_="error-message")


def create_first_month_chart(df):
    """Create first month performance chart"""
    try:
        if df.empty:
            return ui.div(
                ui.p(
                    "No first month data available. Please check your database connection."),
                class_="error-message")

        fig = px.bar(
            df, x='total_gross', y='title',
            title='Top 10 Films with Highest First Month Earnings',
            labels={'title': 'Film Title', 'total_gross': 'First Month Gross ($)'},
            orientation='h',
            hover_data={'title': True, 'total_gross': False, 'formatted_total_gross': True}
        )

        max_idx = df['total_gross'].idxmax()
        colors = [
            PROFESSIONAL_COLORS['highlight'] if idx == max_idx
            else PROFESSIONAL_COLORS['secondary']
            for idx in df.index
        ]

        fig.update_traces(
            marker_color=colors,
            texttemplate='%{x:$,.0f}',
            textposition='outside',
            textfont=dict(family=FONT_FAMILY, size=14, color='black')
        )

        apply_standard_layout(
            fig,
            title='Top 10 Films with Highest First Month Earnings',
            xaxis_title="First Month Gross ($)",
            yaxis_title="Film Title",
            showlegend=False,
            height=550,
            yaxis={'categoryorder': 'total ascending'}
        )

        return ui.HTML(
            fig.to_html(include_plotlyjs=True, div_id="first_month_plot"))

    except Exception as e:
        error_msg = f"Error generating chart: {str(e)}"
        print(f"Chart error: {traceback.format_exc()}")
        return ui.div(ui.p(error_msg), class_="error-message")


def create_efficiency_chart(df):
    """Create efficiency bar chart"""
    try:
        if df.empty:
            return ui.div(
                ui.p("No efficiency data available."),
                class_="error-message")

        df['efficiency'] = df['total_gross'] / df['avg_theatre_count']
        df['efficiency_formatted'] = df['efficiency'].apply(
            lambda x: f"${x:,.0f}")

        df_sorted = df.sort_values('efficiency', ascending=True)

        fig = px.bar(
            df_sorted,
            x='efficiency', y='title',
            title='Revenue Efficiency per Theatre',
            labels={'efficiency': 'Revenue per Theatre ($)', 'title': 'Film Title'},
            orientation='h',
            hover_data={'efficiency_formatted': True}
        )

        max_efficiency_idx = df_sorted['efficiency'].idxmax()
        colors = [
            PROFESSIONAL_COLORS['highlight'] if idx == max_efficiency_idx
            else PROFESSIONAL_COLORS['secondary']
            for idx in df_sorted.index
        ]

        fig.update_traces(
            marker_color=colors,
            texttemplate='%{x:$,.0f}',
            textposition='outside',
            textfont=dict(family=FONT_FAMILY, size=13, color='black')
        )

        apply_standard_layout(
            fig,
            title='Revenue Efficiency per Theatre',
            xaxis_title='Revenue per Theatre ($)',
            yaxis_title='Film Title',
            height=550
        )

        return ui.HTML(
            fig.to_html(include_plotlyjs=True, div_id="efficiency_plot"))
    except Exception as e:
        return ui.div(ui.p(f"Error: {str(e)}"), class_="error-message")


def create_peak_timing_chart(df):
    """Create peak timing bar chart"""
    try:
        if df.empty:
            return ui.div(
                ui.p("No peak timing data available."),
                class_="error-message")

        peak_weeks = df.groupby('title')['weekly_gross'].idxmax()
        peak_data = df.loc[peak_weeks][['title', 'week', 'weekly_gross']].copy()

        peak_data_sorted = peak_data.sort_values('weekly_gross')

        fig = px.bar(
            peak_data_sorted, x='title', y='week',
            title='Peak Performance Timing by Film',
            labels={'week': 'Peak Week', 'title': 'Film Title'},
            color='weekly_gross',
            color_continuous_scale=[[0, PROFESSIONAL_COLORS['secondary']],
                                    [1, PROFESSIONAL_COLORS['highlight']]]
        )

        fig.update_layout(
            plot_bgcolor='rgba(248,249,250,0.8)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family=FONT_FAMILY),
            title=dict(text='Peak Performance Timing by Film', font=TITLE_FONT),
            legend=dict(
                orientation="h", yanchor="top", y=-0.2, xanchor="center",
                x=0.5, bgcolor='rgba(255,255,255,0.9)',
                bordercolor=PROFESSIONAL_COLORS['neutral2'],
                borderwidth=1, font=LEGEND_FONT),
            margin=dict(b=100, t=60, l=60, r=60),
            height=450, coloraxis_showscale=False, xaxis_tickangle=-45,
            xaxis=dict(title_font=AXIS_FONT, tickfont=TICK_FONT),
            yaxis=dict(title_font=AXIS_FONT, tickfont=TICK_FONT)
        )

        return ui.HTML(
            fig.to_html(include_plotlyjs=True, div_id="peak_timing_plot"))
    except Exception as e:
        return ui.div(ui.p(f"Error: {str(e)}"), class_="error-message")
