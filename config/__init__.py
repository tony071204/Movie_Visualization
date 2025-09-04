"""Configuration Module - Settings và Theme"""
from config.settings import (
    # Environment variables
    SPACE_NAME,
    REGION,
    DATABASE_FILE,
    ACCESS_KEY,
    SECRET_KEY,
    PORT,
    CACHE_TIMEOUT,

)

from config.theme import (
    # Colors
    PROFESSIONAL_COLORS,
    CHART_COLORS,

    # Typography
    FONT_FAMILY,
    TITLE_FONT,
    AXIS_FONT,
    LEGEND_FONT,
    TICK_FONT,

    # Layout
    STANDARD_LAYOUT,

)

__all__ = [
    # Settings
    'SPACE_NAME',
    'REGION',
    'DATABASE_FILE',
    'ACCESS_KEY',
    'SECRET_KEY',
    'PORT',
    'CACHE_TIMEOUT',
    'validate_environment',
    'get_app_config',

    # Theme
    'PROFESSIONAL_COLORS',
    'CHART_COLORS',
    'FONT_FAMILY',
    'TITLE_FONT',
    'AXIS_FONT',
    'LEGEND_FONT',
    'TICK_FONT',
    'STANDARD_LAYOUT',
    'apply_standard_layout'
]
