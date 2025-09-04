"""Time Series Charts Module"""
import plotly.graph_objects as go
import pandas as pd
from shiny import ui
from config.theme import *


def create_decay_chart(df):
    """Create revenue decay chart"""
    try:
        if df.empty:
            return ui.div(
                ui.p("No decay data available."),
                class_="error-message")

        available_weeks = sorted(df['week'].unique())
        baseline_week = 0 if 0 in available_weeks else min(available_weeks)

        baseline_data = df[df['week'] == baseline_week][[
            'title', 'weekly_gross']].copy()
        baseline_data.columns = ['title', 'baseline_gross']

        if baseline_data.empty:
            return ui.div(
                ui.p(
                    f"No baseline week ({baseline_week}) data available for decay analysis."),
                class_="error-message")

        top_5_movies = df.groupby('title')['weekly_gross'].sum(
        ).sort_values(ascending=False).head(5).index.tolist()

        df_top5 = df[df['title'].isin(top_5_movies)].copy()
        baseline_data_top5 = baseline_data[baseline_data['title'].isin(
            top_5_movies)].copy()

        df_with_decay = pd.merge(df_top5, baseline_data_top5, on='title')
        df_with_decay = df_with_decay[df_with_decay['baseline_gross'] > 0]
        df_with_decay['decay_percent'] = (
            df_with_decay['weekly_gross'] / df_with_decay['baseline_gross']) * 100

        if df_with_decay.empty:
            return ui.div(
                ui.p("No valid decay data available after normalization."),
                class_="error-message")

        fig = go.Figure()

        films = [
            film for film in top_5_movies
            if film in df_with_decay['title'].unique()]

        for i, film in enumerate(films):
            film_data = df_with_decay[df_with_decay['title']
                                      == film].sort_values('week')

            if not film_data.empty and len(film_data) > 1:
                first_decay_week = min(
                    [w for w in film_data['week'].unique()
                     if w > baseline_week])
                first_decay = film_data[film_data['week'] == first_decay_week][
                    'decay_percent'].iloc[0] if len(
                    film_data[film_data['week'] == first_decay_week]) > 0 else 0
                final_week = film_data['week'].max()
                final_decay = film_data[film_data['week']
                                        == final_week]['decay_percent'].iloc[0]

                fig.add_trace(go.Scatter(
                    x=film_data['week'],
                    y=film_data['decay_percent'],
                    mode='lines+markers',
                    name=film[:15] + "..." if len(film) > 15 else film,
                    line=dict(
                        color=CHART_COLORS[i],
                        width=5,
                        shape='spline',
                        smoothing=0.2
                    ),
                    marker=dict(
                        size=10,
                        color=CHART_COLORS[i],
                        line=dict(width=3, color='white'),
                        symbol='circle'
                    ),
                    hovertemplate=(
                        "<b>%{fullData.name}</b><br>"
                        "Week %{x}<br>"
                        "Decay: %{y:.1f}% of baseline<br>"
                        f"Week {first_decay_week} Drop: {100-first_decay:.1f}%<br>"
                        f"Final Week Retention: {final_decay:.1f}%<br>"
                        "<extra></extra>"
                    ),
                    connectgaps=True
                ))

        fig.add_hline(
            y=100,
            line_dash="dash",
            line_color=PROFESSIONAL_COLORS['neutral1'],
            annotation_text=f"Baseline Week {baseline_week} (100%)",
            annotation_position="top right",
            annotation_font=dict(family=FONT_FAMILY, size=12)
        )

        fig.add_hline(
            y=50,
            line_dash="dot",
            line_color=PROFESSIONAL_COLORS['warning'],
            annotation_text="50% Retention",
            annotation_position="top right",
            annotation_font=dict(family=FONT_FAMILY, size=12)
        )

        fig.update_layout(
            plot_bgcolor='rgba(248,249,250,0.8)', paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family=FONT_FAMILY),
            title=dict(
                text=f'Revenue Decay Pattern - Top 5 Films (% of Week {baseline_week})',
                font=TITLE_FONT),
            legend=dict(
                orientation="h", yanchor="top", y=-0.15, xanchor="center",
                x=0.5, bgcolor='rgba(255,255,255,0.9)',
                bordercolor=PROFESSIONAL_COLORS['neutral2'],
                borderwidth=1, font=LEGEND_FONT),
            margin=dict(b=80, t=60, l=60, r=60),
            xaxis=dict(
                title='Week', tickmode='linear', tick0=min(available_weeks),
                dtick=1, gridcolor='rgba(128,128,128,0.2)', showgrid=True,
                zeroline=False,
                range=[min(available_weeks) - 0.2, max(available_weeks) + 0.2],
                title_font=AXIS_FONT, tickfont=TICK_FONT),
            yaxis=dict(
                title=f'Percentage of Week {baseline_week} (%)',
                gridcolor='rgba(128,128,128,0.2)', showgrid=True,
                zeroline=False,
                range=[0, max(
                    110, df_with_decay['decay_percent'].max() * 1.1)],
                ticksuffix='%', title_font=AXIS_FONT, tickfont=TICK_FONT),
            height=450, hovermode='x unified')

        return ui.HTML(fig.to_html(include_plotlyjs=True, div_id="decay_plot"))
    except Exception as e:
        return ui.div(
            ui.p(f"Error in decay chart: {str(e)}"),
            class_="error-message")
