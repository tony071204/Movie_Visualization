import plotly.graph_objects as go
import numpy as np
import pandas as pd
from shiny import ui
from config.theme import *


def create_gross_vs_admissions_chart(df):
    """Create gross vs admissions scatter plot"""
    try:
        if df.empty:
            return ui.div(
                ui.p("No admissions data available."),
                class_="error-message")

        df_filtered = df[(df['total_admissions'] > 0) &
                         (df['total_gross'] > 0)].copy()

        if df_filtered.empty:
            return ui.div(
                ui.p("No valid data for logarithmic visualization."),
                class_="error-message")

        fig = go.Figure()

        colors = ['#2E4057', '#048A81', '#54C6EB', '#F18F01', '#C73E1D',
                  '#28A745', '#FFC107', '#6C757D', '#9B59B6', '#E67E22']

        if len(df_filtered) > 2:
            x_trend = df_filtered['total_admissions'].values
            y_trend = df_filtered['total_gross'].values

            log_x = np.log10(x_trend)
            log_y = np.log10(y_trend)
            coeffs = np.polyfit(log_x, log_y, 1)

            correlation = np.corrcoef(log_x, log_y)[0, 1]

            x_min, x_max = x_trend.min(), x_trend.max()
            x_trend_smooth = np.logspace(np.log10(x_min), np.log10(x_max), 100)
            y_trend_smooth = (10 ** coeffs[1]) * (x_trend_smooth ** coeffs[0])

            fig.add_trace(go.Scatter(
                x=x_trend_smooth,
                y=y_trend_smooth,
                mode='lines',
                name=f'Power Law Trend (r={correlation:.3f})',
                line=dict(color='#DC143C', width=5, dash='solid'),
                showlegend=True,
                hoverinfo='skip'
            ))

        for i, row in df_filtered.iterrows():
            revenue_per_admission = row['total_gross'] / row['total_admissions']
            bubble_size = max(16, min(36, 12 + revenue_per_admission / 2.5))

            fig.add_trace(
                go.Scatter(
                    x=[row['total_admissions']],
                    y=[row['total_gross']],
                    mode='markers', name=row['title'][: 18] + "..."
                    if len(row['title']) > 18 else row['title'],
                    marker=dict(
                        size=bubble_size, color=colors[i % len(colors)],
                        opacity=0.8, line=dict(width=3, color='white'),
                        symbol='circle'),
                    hovertemplate=(
                        "<b>%{customdata[0]}</b><br>"
                        "Total Admissions: %{x:,.0f}<br>"
                        "Total Gross: %{customdata[1]}<br>"
                        "Revenue per Admission: $%{customdata[2]:.2f}<br>"
                        "Market Position: %{customdata[3]}<br>"
                        "<extra></extra>"),
                    customdata=[[row['title'],
                                 row['formatted_total_gross'],
                                 revenue_per_admission, "Premium"
                                 if revenue_per_admission > 15 else "Standard"]],
                    showlegend=True))

        fig.update_layout(
            plot_bgcolor='rgba(248,249,250,0.8)', paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family=FONT_FAMILY),
            title=dict(
                text='Revenue vs Audience Reach Analysis', x=0.5,
                font=TITLE_FONT),
            xaxis=dict(
                title='Total Admissions', type='log',
                gridcolor='rgba(128,128,128,0.2)', showgrid=True,
                zeroline=False, title_font=AXIS_FONT, tickfont=TICK_FONT,
                tickvals=[10000, 50000, 100000, 500000, 1000000, 2000000,
                          5000000],
                ticktext=['10K', '50K', '100K', '500K', '1M', '2M', '5M']),
            yaxis=dict(
                title='Total Gross Revenue ($)', type='log',
                gridcolor='rgba(128,128,128,0.2)', showgrid=True,
                zeroline=False, title_font=AXIS_FONT, tickfont=TICK_FONT,
                tickvals=[20000000, 50000000, 100000000, 200000000, 500000000,
                          1000000000, 2000000000, 5000000000],
                ticktext=['$20M', '$50M', '$100M', '$200M', '$500M', '$1B',
                          '$2B', '$5B']),
            height=550,
            legend=dict(
                orientation="h", yanchor="top", y=-0.2, xanchor="center", x=0.5,
                bgcolor='rgba(255,255,255,0.8)', bordercolor='rgba(0,0,0,0.2)',
                borderwidth=1, font=LEGEND_FONT),
            margin=dict(r=60, b=120))

        return ui.HTML(
            fig.to_html(include_plotlyjs=True, div_id="admissions_plot"))
    except Exception as e:
        return ui.div(ui.p(f"Error: {str(e)}"), class_="error-message")


def create_gross_vs_theatre_chart(df):
    """Create gross vs theatre count scatter plot"""
    try:
        if df.empty:
            return ui.div(
                ui.p("No theatre data available."),
                class_="error-message")

        df_filtered = df[(df['avg_theatre_count'] > 10) &
                         (df['total_gross'] > 1000)].copy()

        if df_filtered.empty:
            return ui.div(
                ui.p("No valid data for visualization."),
                class_="error-message")

        fig = go.Figure()

        colors = ['#2E4057', '#048A81', '#54C6EB', '#F18F01', '#C73E1D',
                  '#28A745', '#FFC107', '#6C757D', '#9B59B6', '#E67E22']

        if len(df_filtered) > 2:
            x_trend = df_filtered['avg_theatre_count'].values
            y_trend = df_filtered['total_gross'].values

            log_x = np.log10(x_trend)
            log_y = np.log10(y_trend)
            correlation = np.corrcoef(log_x, log_y)[0, 1]

            coeffs = np.polyfit(log_x, log_y, 1)

            x_min, x_max = x_trend.min(), x_trend.max()
            x_trend_smooth = np.logspace(np.log10(x_min), np.log10(x_max), 100)
            y_trend_smooth = (10 ** coeffs[1]) * (x_trend_smooth ** coeffs[0])

            fig.add_trace(go.Scatter(
                x=x_trend_smooth,
                y=y_trend_smooth,
                mode='lines',
                name=f'Power Law Trend (r={correlation:.3f})',
                line=dict(color='#DC143C', width=5, dash='solid'),
                showlegend=True,
                hoverinfo='skip'
            ))

        for i, row in df_filtered.iterrows():
            efficiency = row['total_gross'] / \
                row['avg_theatre_count'] if row['avg_theatre_count'] > 0 else 0

            all_efficiencies = [
                r['total_gross'] / r['avg_theatre_count'] for _,
                r in df_filtered.iterrows()]
            efficiency_rank = sorted(
                all_efficiencies, reverse=True).index(efficiency) + 1
            bubble_size = max(16, 40 - (efficiency_rank * 2.5))

            penetration = "Wide Release" if row['avg_theatre_count'] > 3000 else "Limited Release"
            performance_tier = "Top Performer" if efficiency_rank <= 3 else "Standard"

            fig.add_trace(
                go.Scatter(
                    x=[row['avg_theatre_count']],
                    y=[row['total_gross']],
                    mode='markers', name=row['title'][: 15] + "..."
                    if len(row['title']) > 15 else row['title'],
                    marker=dict(
                        size=bubble_size, color=colors[i % len(colors)],
                        opacity=0.8, line=dict(width=3, color='white'),
                        symbol='circle'),
                    hovertemplate=(
                        "<b>%{customdata[0]}</b><br>"
                        "Theatre Count: %{x:,.0f}<br>"
                        "Total Gross: %{customdata[1]}<br>"
                        "Revenue/Theatre: $%{customdata[2]:,.0f}<br>"
                        "Strategy: %{customdata[3]}<br>"
                        "Performance: %{customdata[4]}<br>"
                        "<extra></extra>"),
                    customdata=[[row['title'],
                                 row['formatted_total_gross'],
                                 efficiency, penetration, performance_tier]],
                    showlegend=True))

        if len(df_filtered) > 0:
            max_theatres = df_filtered['avg_theatre_count'].max()
            max_gross = df_filtered['total_gross'].max()

            high_eff_x_start = np.sqrt(
                max_theatres * np.median(df_filtered['avg_theatre_count']))
            high_eff_y_start = np.sqrt(
                max_gross * np.median(df_filtered['total_gross']))

            fig.add_shape(
                type="rect",
                x0=high_eff_x_start,
                y0=high_eff_y_start,
                x1=max_theatres * 1.1,
                y1=max_gross * 1.1,
                fillcolor="rgba(40,167,69,0.15)",
                line=dict(color="rgba(40,167,69,0.4)", width=2, dash="dash"),
                layer="below"
            )

        fig.update_layout(
            plot_bgcolor='rgba(248,249,250,0.8)', paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family=FONT_FAMILY),
            title=dict(
                text='Distribution Strategy vs Revenue Performance', x=0.5,
                font=TITLE_FONT),
            xaxis=dict(
                title='Average Theatre Count', type='log',
                gridcolor='rgba(128,128,128,0.2)', showgrid=True,
                zeroline=False, title_font=AXIS_FONT, tickfont=TICK_FONT,
                tickvals=[20, 50, 100, 200, 500, 1000, 2000, 5000],
                ticktext=['20', '50', '100', '200', '500', '1K', '2K', '5K']),
            yaxis=dict(
                title='Total Gross Revenue ($)', type='log',
                gridcolor='rgba(128,128,128,0.2)', showgrid=True,
                zeroline=False, title_font=AXIS_FONT, tickfont=TICK_FONT,
                tickvals=[30000000, 50000000, 100000000, 200000000, 500000000,
                          1000000000, 2000000000, 5000000000],
                ticktext=['$30M', '$50M', '$100M', '$200M', '$500M', '$1B',
                          '$2B', '$5B']),
            height=550,
            legend=dict(
                orientation="h", yanchor="top", y=-0.2, xanchor="center", x=0.5,
                bgcolor='rgba(255,255,255,0.8)', bordercolor='rgba(0,0,0,0.2)',
                borderwidth=1, font=LEGEND_FONT),
            margin=dict(r=60, b=120))

        return ui.HTML(
            fig.to_html(include_plotlyjs=True, div_id="theatre_plot"))
    except Exception as e:
        return ui.div(ui.p(f"Error: {str(e)}"), class_="error-message")
