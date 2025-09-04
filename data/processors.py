"""Data Processing Module"""
import pandas as pd
from database.connection import execute_query
from data.queries import *


def format_number(x):
    """Format numbers for display"""
    if pd.isna(x):
        return "0"
    if x >= 1_000_000_000:
        return f"{x / 1_000_000_000:.2f}B"
    elif x >= 1_000_000:
        return f"{x / 1_000_000:.2f}M"
    elif x >= 1_000:
        return f"{x / 1_000:.2f}K"
    else:
        return f"{x:.2f}"


def get_top_films():
    """Get top 10 films data"""
    df = execute_query(TOP_FILMS_QUERY)
    if not df.empty:
        df['formatted_total_gross'] = df['total_gross'].apply(format_number)
    return df


def get_first_month_data():
    """Get first month performance data"""
    df = execute_query(FIRST_MONTH_QUERY)
    if not df.empty:
        df['formatted_total_gross'] = df['total_gross'].apply(format_number)
    return df


def get_admissions_data():
    """Get admissions data"""
    df = execute_query(ADMISSIONS_QUERY)
    if not df.empty:
        df['formatted_total_gross'] = df['total_gross'].apply(format_number)
    return df


def get_theatre_data():
    """Get theatre distribution data"""
    df = execute_query(THEATRE_QUERY)
    if not df.empty:
        df['formatted_total_gross'] = df['total_gross'].apply(format_number)
    return df


def get_weekly_trends():
    """Get weekly trends data"""
    return execute_query(WEEKLY_TRENDS_QUERY)


def get_database_stats():
    """Get database statistics"""
    films_count = execute_query(TOTAL_FILMS_QUERY).iloc[0]['count']
    total_gross = execute_query(TOTAL_GROSS_QUERY).iloc[0]['total']
    avg_gross = execute_query(AVG_GROSS_QUERY).iloc[0]['avg']
    max_gross = execute_query(MAX_GROSS_QUERY).iloc[0]['max']

    return {
        'films_count': films_count or 0,
        'total_gross': total_gross or 0,
        'avg_gross': avg_gross or 0,
        'max_gross': max_gross or 0
    }
