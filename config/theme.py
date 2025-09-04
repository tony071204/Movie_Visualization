# Professional Color Palette & Design System
PROFESSIONAL_COLORS = {
    'primary': '#2E4057',      # Deep Navy Blue
    'secondary': '#048A81',    # Teal Green
    'accent1': '#54C6EB',      # Light Blue
    'accent2': '#F18F01',      # Orange
    'accent3': '#C73E1D',      # Deep Red
    'neutral1': '#6C757D',     # Gray
    'neutral2': '#ADB5BD',     # Light Gray
    'success': '#28A745',      # Green
    'warning': '#FFC107',      # Yellow
    'background': '#F8F9FA',   # Light Background
    'highlight': '#FFD700'     # Gold for highlighting top performers
}

CHART_COLORS = [
    PROFESSIONAL_COLORS['primary'],    # Deep Navy
    PROFESSIONAL_COLORS['secondary'],  # Teal
    PROFESSIONAL_COLORS['accent1'],    # Light Blue
    PROFESSIONAL_COLORS['accent2'],    # Orange
    PROFESSIONAL_COLORS['accent3'],    # Deep Red
    PROFESSIONAL_COLORS['success'],    # Green
    PROFESSIONAL_COLORS['warning'],    # Yellow
    PROFESSIONAL_COLORS['neutral1'],   # Gray
    '#9B59B6',                         # Purple
    '#E67E22'                          # Dark Orange
]

# Consistent Typography
FONT_FAMILY = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
TITLE_FONT = dict(family=FONT_FAMILY, size=22,
                  color=PROFESSIONAL_COLORS['primary'])
AXIS_FONT = dict(family=FONT_FAMILY, size=16,
                 color=PROFESSIONAL_COLORS['neutral1'])
LEGEND_FONT = dict(family=FONT_FAMILY, size=14,
                   color=PROFESSIONAL_COLORS['neutral1'])
TICK_FONT = dict(family=FONT_FAMILY, size=14,
                 color=PROFESSIONAL_COLORS['neutral1'])

# Standard Layout Configuration
STANDARD_LAYOUT = {
    'plot_bgcolor': 'rgba(248,249,250,0.8)',
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'font': dict(family=FONT_FAMILY),
    'legend': dict(
        orientation="h",
        yanchor="top",
        y=-0.2,
        xanchor="center",
        x=0.5,
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor=PROFESSIONAL_COLORS['neutral2'],
        borderwidth=1,
        font=LEGEND_FONT
    ),
    'margin': dict(b=100, t=60, l=60, r=60)
}
