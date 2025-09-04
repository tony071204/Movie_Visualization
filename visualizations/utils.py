"""Visualization Utilities"""
from config.theme import *


def apply_standard_layout(fig, title, xaxis_title, yaxis_title, **kwargs):
    """Apply consistent styling to all charts"""
    layout_dict = STANDARD_LAYOUT.copy()

    # Handle yaxis and xaxis properly when passed in kwargs
    xaxis_dict = dict(title=xaxis_title, title_font=AXIS_FONT,
                      tickfont=TICK_FONT)
    yaxis_dict = dict(title=yaxis_title, title_font=AXIS_FONT,
                      tickfont=TICK_FONT)

    # Merge with any custom xaxis/yaxis settings
    if 'xaxis' in kwargs:
        xaxis_dict.update(kwargs.pop('xaxis'))
    if 'yaxis' in kwargs:
        yaxis_dict.update(kwargs.pop('yaxis'))

    layout_dict.update({
        'title': dict(text=title, font=TITLE_FONT),
        'xaxis': xaxis_dict,
        'yaxis': yaxis_dict,
    })
    layout_dict.update(kwargs)
    fig.update_layout(**layout_dict)
    return fig
