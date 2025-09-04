from shiny import ui
from config.theme import PROFESSIONAL_COLORS, FONT_FAMILY


def render_insights_text(top_films, weekly_data):
    """Render insights text"""
    try:
        if not top_films.empty and not weekly_data.empty:
            top_film = top_films.iloc[0]
            avg_revenue = top_films['total_gross'].mean()
            high_performers = len(
                top_films[top_films['total_gross'] > avg_revenue])

            insights_html = f"""
            <div style="padding: 20px; background: linear-gradient(135deg, {PROFESSIONAL_COLORS['background']} 0%, #e9ecef 100%); border-radius: 10px; font-family: {FONT_FAMILY};">
                <h5 style="color: {PROFESSIONAL_COLORS['primary']}; margin-bottom: 15px;">🔍 Key Performance Insights</h5>
                
                <div style="margin-bottom: 15px;">
                    <strong style="color: {PROFESSIONAL_COLORS['accent3']};">🏆 Market Leader:</strong><br>
                    <span style="color: {PROFESSIONAL_COLORS['primary']};">{top_film['title']} dominates with {top_film['formatted_total_gross']} in total earnings</span>
                </div>
                
                <div style="margin-bottom: 15px;">
                    <strong style="color: {PROFESSIONAL_COLORS['accent2']};">📊 Market Distribution:</strong><br>
                    <span style="color: {PROFESSIONAL_COLORS['primary']};">{high_performers} out of 10 films exceed average performance</span>
                </div>
                
                <div style="margin-bottom: 15px;">
                    <strong style="color: {PROFESSIONAL_COLORS['success']};">💡 Investment Insight:</strong><br>
                    <span style="color: {PROFESSIONAL_COLORS['primary']};">Strong correlation between theatre count and total revenue suggests distribution scale matters</span>
                </div>
                
                <div>
                    <strong style="color: {PROFESSIONAL_COLORS['secondary']};">🎯 Key Insight:</strong><br>
                    <span style="color: {PROFESSIONAL_COLORS['primary']};">Box office success is front-loaded - 70% of total revenue typically occurs in the first month</span>
                </div>
            </div>
            """
            return ui.HTML(insights_html)
        else:
            return ui.HTML(
                "<div class='error-message'><p>No insights available - please check your data</p></div>")
    except Exception as e:
        return ui.HTML(
            f"<div class='error-message'><p>Error generating insights: {str(e)}</p></div>")


def render_insights_markdown():
    """Render markdown insights"""
    try:
        markdown_content = """
# 📊 Box Office Performance Analysis

## 🔍 Key Findings

**Revenue Decay Pattern**: Most films drop to 50% of opening week performance by week 4

**Peak Performance**: 80-90% of films achieve peak performance in week 1

**Rapid Decline**: Revenue falls to 20-30% of opening levels by weeks 6-8

---

## 💡 Strategic Recommendations

### 🎯 Marketing Strategy
**Front-load 70-80% of marketing budget** to pre-release and opening week campaigns

### 🏛️ Distribution Strategy  
Secure **maximum theatre count for weeks 1-3**, then optimize based on performance

### 📈 Financial Planning
Build models expecting **50% revenue decline by week 4** for accurate forecasting

### 📱 Digital Release Timing
Launch premium VOD around **week 6-8** when theatrical revenue stabilizes

---

## 🎯 Bottom Line

> **Box office success is front-loaded.** Maximize opening week impact as revenue predictably declines 50%+ within the first month.
"""

        return ui.HTML(
            f'<div class="markdown-content">{ui.markdown(markdown_content)}</div>')
    except Exception as e:
        return ui.HTML(
            f"<div class='error-message'><p>Error generating markdown insights: {str(e)}</p></div>")
