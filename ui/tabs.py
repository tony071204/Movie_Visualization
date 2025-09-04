"""Individual Tabs Module"""
from shiny import ui


def create_about_tab():
    """Create About tab"""
    return ui.nav_panel(
        "📋 About This Project", ui.div(
            ui.div(
                ui.h4("🗃️ Data Source"),
                ui.p(
                    "The analysis is based on movie box office data sourced from numero.co, containing comprehensive performance metrics across multiple weeks and distribution channels."),
                ui.h4("🔍 Business Questions Addressed"),
                ui.tags.ol(
                    ui.tags.li(
                        "Which films generate the highest total box office revenue?"),
                    ui.tags.li(
                        "How does first-month performance correlate with overall success?"),
                    ui.tags.li(
                        "What is the relationship between theatre distribution and revenue?"),
                    ui.tags.li(
                        "How efficiently do films monetize their audience reach?"),
                    ui.tags.li(
                        "What are the typical revenue decay patterns over time?")),
                ui.h4("📈 Dashboard Sections"),
                ui.tags.ul(
                    ui.tags.li(
                        "Overall Rankings - Top performers by total and first-month revenue"),
                    ui.tags.li(
                        "Performance Analysis - Efficiency metrics and distribution strategies"),
                    ui.tags.li(
                        "Trends Over Time - Revenue decay patterns and peak timing analysis"),
                    ui.tags.li(
                        "Data Insights - Summary statistics and strategic recommendations")),
                class_="about-section")))


def create_rankings_tab():
    """Create Rankings tab"""
    return ui.nav_panel(
        "📊 Overall Rankings",
        ui.row(
            ui.column(
                6,
                ui.card(
                    ui.card_header(
                        "🏆 Top 10 Films by Total Gross Earnings"),
                    ui.div(
                        ui.output_ui("top_films_chart"),
                        class_="plot-container")
                )
            ),
            ui.column(
                6,
                ui.card(
                    ui.card_header(
                        "🚀 First Month Performance Champions"),
                    ui.div(
                        ui.output_ui("first_month_chart"),
                        class_="plot-container")
                )
            )
        ),
        ui.br(),
        ui.row(
            ui.column(
                12,
                ui.card(
                    ui.card_header(
                        "📈 Performance Comparison: Total vs First Month"),
                    ui.div(
                        ui.output_ui("comparison_chart"),
                        class_="plot-container")
                )
            )
        )
    )


def create_performance_tab():
    """Create Performance Analysis tab"""
    return ui.nav_panel(
        "🎯 Performance Analysis",
        ui.row(
            ui.column(
                6,
                ui.card(
                    ui.card_header("💰 Revenue vs Audience Reach"),
                    ui.div(
                        ui.output_ui("gross_vs_admissions_chart"),
                        class_="plot-container")
                )
            ),
            ui.column(
                6,
                ui.card(
                    ui.card_header("🏛️ Distribution Strategy Impact"),
                    ui.div(
                        ui.output_ui("gross_vs_theatre_chart"),
                        class_="plot-container")
                )
            )
        ),
        ui.br(),
        ui.row(
            ui.column(
                12,
                ui.card(
                    ui.card_header("🎭 Performance Efficiency Analysis"),
                    ui.div(
                        ui.output_ui("efficiency_chart"),
                        class_="plot-container")
                )
            )
        )
    )


def create_trends_tab():
    """Create Trends Over Time tab"""
    return ui.nav_panel(
        "📈 Trends Over Time",
        ui.row(
            ui.column(
                6,
                ui.card(
                    ui.card_header("📉 Revenue Decay Analysis"),
                    ui.div(
                        ui.output_ui("decay_chart"),
                        class_="plot-container")
                )
            ),
            ui.column(
                6,
                ui.card(
                    ui.card_header("🎪 Peak Performance Timing"),
                    ui.div(
                        ui.output_ui("peak_timing_chart"),
                        class_="plot-container")
                )
            )
        ),
        ui.br()
    )


def create_insights_tab():
    """Create Data Insights tab"""
    return ui.nav_panel(
        "📋 Data Insights", ui.row(
            ui.column(
                4, ui.card(
                    ui.card_header("🏅 Top Performers Summary"),
                    ui.output_table("summary_table"))),
            ui.column(
                4, ui.card(
                    ui.card_header("📊 Database Statistics"),
                    ui.div(
                        ui.output_text_verbatim("db_stats"),
                        class_="stats-container"))),
            ui.column(
                4, ui.card(
                    ui.card_header("🎯 Performance Insights"),
                    ui.output_ui("insights_text")))),
        ui.br(),
        ui.row(
            ui.column(
                12, ui.card(
                    ui.card_header(
                        "📊 Box Office Performance Insights & Strategic Recommendations"),
                    ui.div(
                        ui.output_ui("insights_markdown"),
                        class_="markdown-content")))))
