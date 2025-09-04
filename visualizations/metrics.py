"""Metrics Cards Module"""
import pandas as pd
from shiny import ui
from database.connection import execute_query
from data.processors import format_number


def render_total_films_metric():
    """Render total films metric"""
    try:
        count = execute_query(
            "SELECT COUNT(*) as count FROM films").iloc[0]['count']
    except:
        count = 0
    return ui.div(
        ui.div(f"{count}", class_="metric-value"),
        ui.div("Total Films", class_="metric-label"),
        class_="metric-card"
    )


def render_total_gross_metric():
    """Render total gross metric"""
    try:
        total = execute_query(
            "SELECT SUM(gross) as total FROM box_office").iloc[0]['total']
        if pd.isna(total):
            total = 0
    except:
        total = 0
    return ui.div(
        ui.div(format_number(total), class_="metric-value"),
        ui.div("Total Box Office", class_="metric-label"),
        class_="metric-card"
    )


def render_avg_gross_metric():
    """Render average gross metric"""
    try:
        avg = execute_query(
            "SELECT AVG(gross) as avg FROM box_office").iloc[0]['avg']
        if pd.isna(avg):
            avg = 0
    except:
        avg = 0
    return ui.div(
        ui.div(format_number(avg), class_="metric-value"),
        ui.div("Average Daily Gross", class_="metric-label"),
        class_="metric-card"
    )


def render_top_film_metric(df):
    """Render top film metric"""
    try:
        if not df.empty:
            top_film = df.iloc[0]['title'][:15] + "..." if len(
                df.iloc[0]['title']) > 15 else df.iloc[0]['title']
        else:
            top_film = "N/A"
    except:
        top_film = "N/A"
    return ui.div(
        ui.div(top_film, class_="metric-value", style="font-size: 1.3rem;"),
        ui.div("Top Performing Film", class_="metric-label"),
        class_="metric-card"
    )
