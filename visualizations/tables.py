"""Tables and Text Outputs Module"""
import pandas as pd
from shiny import ui
from database.connection import execute_query
from config.theme import PROFESSIONAL_COLORS, FONT_FAMILY


def render_summary_table(df):
    """Render summary table"""
    try:
        if df.empty:
            return pd.DataFrame({"Message": ["No data available"]})

        summary_df = df[['title', 'formatted_total_gross']].copy()
        summary_df.columns = ['Film Title', 'Total Gross']
        summary_df['Rank'] = range(1, len(summary_df) + 1)
        summary_df['Performance'] = [
            '🥇', '🥈', '🥉'] + ['🎖️'] * (len(summary_df) - 3)
        return summary_df[['Rank', 'Performance', 'Film Title', 'Total Gross']]
    except Exception as e:
        return pd.DataFrame({"Error": [f"Could not load data: {str(e)}"]})


def render_db_stats():
    """Render database statistics"""
    try:
        films_count = execute_query(
            "SELECT COUNT(*) as count FROM films").iloc[0]['count']
        weeks_count = execute_query(
            "SELECT COUNT(*) as count FROM weeks").iloc[0]['count']
        box_office_count = execute_query(
            "SELECT COUNT(*) as count FROM box_office").iloc[0]['count']
        total_gross = execute_query(
            "SELECT SUM(gross) as total FROM box_office").iloc[0]['total']
        avg_gross = execute_query(
            "SELECT AVG(gross) as avg FROM box_office").iloc[0]['avg']
        max_gross = execute_query(
            "SELECT MAX(gross) as max FROM box_office").iloc[0]['max']

        total_gross = total_gross if total_gross is not None else 0
        avg_gross = avg_gross if avg_gross is not None else 0
        max_gross = max_gross if max_gross is not None else 0

        return f"""📊 DATABASE OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📽️  Total Films: {films_count:,}
📅  Week Records: {weeks_count:,}
📈  Box Office Records: {box_office_count:,}

💰 FINANCIAL METRICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💎  Total Gross: ${total_gross:,.2f}
📊  Average Daily: ${avg_gross:,.2f}
🚀  Peak Daily: ${max_gross:,.2f}

📈 ANALYSIS SCOPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯  Top 10 performing films analyzed
📊  Performance metrics across multiple dimensions
⏱️  Time series analysis (weeks 0-10)
🎪  Distribution and efficiency analytics"""
    except Exception as e:
        return f"Error loading database statistics: {str(e)}"
