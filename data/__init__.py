"""Data Module - Queries và Processing"""
from data.queries import (
    # Query strings
    TOP_FILMS_QUERY,
    FIRST_MONTH_QUERY,
    ADMISSIONS_QUERY,
    THEATRE_QUERY,
    WEEKLY_TRENDS_QUERY,
    TOTAL_FILMS_QUERY,
    TOTAL_GROSS_QUERY,
    AVG_GROSS_QUERY,
    MAX_GROSS_QUERY
)

from data.processors import (
    # Data fetching functions
    get_top_films,
    get_first_month_data,
    get_admissions_data,
    get_theatre_data,
    get_weekly_trends,
    get_database_stats,

    # Utility functions
    format_number
)

__all__ = [
    # Queries
    'TOP_FILMS_QUERY',
    'FIRST_MONTH_QUERY',
    'ADMISSIONS_QUERY',
    'THEATRE_QUERY',
    'WEEKLY_TRENDS_QUERY',
    'TOTAL_FILMS_QUERY',
    'TOTAL_GROSS_QUERY',
    'AVG_GROSS_QUERY',
    'MAX_GROSS_QUERY',
    'WEEKS_COUNT_QUERY',
    'BOX_OFFICE_COUNT_QUERY',

    # Processors
    'get_top_films',
    'get_first_month_data',
    'get_admissions_data',
    'get_theatre_data',
    'get_weekly_trends',
    'get_database_stats',

    # Utilities
    'format_number'
]
