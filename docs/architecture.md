# Architecture Document — Movie Box Office Analytics Dashboard

## 1. Overview

The application is a **read-only analytics dashboard** built with [Python Shiny](https://shiny.posit.co/py/). It pulls a SQLite database from DigitalOcean Spaces on startup, processes the data with pandas, and renders all charts as self-contained Plotly HTML fragments injected into the Shiny UI. There are **no user-driven input controls** — every reactive output is computed once per session and never re-triggered.

---

## 2. Technology Stack

| Layer | Technology |
|---|---|
| Web framework | Python Shiny (`shiny==1.4.0`) |
| ASGI server | Uvicorn |
| Charting | Plotly (`plotly==6.0.1`) |
| Data processing | pandas + numpy |
| Database | SQLite via `sqlite3` stdlib |
| Cloud storage | DigitalOcean Spaces via `boto3` |
| Env management | `python-dotenv` |

---

## 3. Module Map

```
app.py                       ← entry point; wires all layers together
│
├── config/
│   ├── __init__.py          ← re-exports everything from settings + theme
│   ├── settings.py          ← reads .env; single source for all env vars
│   └── theme.py             ← color palette, typography dicts, STANDARD_LAYOUT
│
├── database/
│   ├── __init__.py          ← exposes initialize_database()
│   ├── downloader.py        ← boto3 download from DO Spaces + 1-hour mtime cache
│   └── connection.py        ← get_db_connection(), execute_query() → DataFrame
│
├── data/
│   ├── queries.py           ← raw SQL string constants only (no execution)
│   └── processors.py        ← calls execute_query(), adds formatted columns,
│                               returns DataFrames
│
├── visualizations/
│   ├── utils.py             ← apply_standard_layout() shared helper
│   ├── bar_charts.py        ← top films, first month, efficiency, peak timing
│   ├── comparsion_charts.py ← total vs first-month grouped bar (typo in filename)
│   ├── scatter_charts.py    ← gross vs admissions, gross vs theatre count
│   ├── time_series_charts.py← revenue decay lines for top 5 films
│   ├── metrics.py           ← KPI cards (total films, total gross, avg, top film)
│   ├── tables.py            ← summary table + db stats text
│   └── insights.py          ← dynamic insight text + static markdown
│
├── ui/
│   ├── layout.py            ← create_dashboard_ui() → page_fluid(...)
│   ├── tabs.py              ← one create_*_tab() function per nav tab
│   └── styles.py            ← get_custom_css() → CSS string (uses theme colors)
│
└── server/
    └── handlers.py          ← create_server() → server_function(input, output, session)
```

---

## 4. Startup Sequence

`app.py` executes these steps **at module load time** (before any request arrives):

```
1. database.initialize_database()
       └─ downloader.download_database()
              ├─ if movie.db exists AND age < 3600s → use cache, skip download
              ├─ if DO Spaces credentials missing → create empty movie.db, continue
              └─ else → boto3 downloads movie.db from DO Spaces

2. ui.layout.create_dashboard_ui()
       └─ builds the full Shiny UI tree (no data fetched here)

3. server.handlers.create_server()
       └─ defines all @reactive.Calc and @output functions, returns server_function

4. App(app_ui, server)  ← standard Shiny App object

5. if __name__ == "__main__": uvicorn.run("app:app", ...)
```

The database file path returned by step 1 is stored in `database.connection.DB_PATH` (module-level global). All subsequent SQL calls use that path.

---

## 5. Data Flow (per session)

```
Browser opens app
        │
        ▼
Shiny session starts → server_function(input, output, session) called
        │
        ▼
@reactive.Calc functions (lazy, cached for session lifetime)
  top_films_data()       → processors.get_top_films()
  first_month_data()     → processors.get_first_month_data()
  admissions_data()      → processors.get_admissions_data()
  theatre_data()         → processors.get_theatre_data()
  weekly_trends_data()   → processors.get_weekly_trends()
        │
        │ each processor:
        │   execute_query(SQL_CONSTANT)  →  sqlite3 + pd.read_sql()  →  DataFrame
        │   df['formatted_*'] = df['*'].apply(format_number)         ← adds display column
        │   return DataFrame
        │
        ▼
@output / @render.ui functions — called when the browser renders that output_ui()
  visualization_module.create_*_chart(dataframe)
        │
        │ each visualization:
        │   build Plotly Figure object
        │   apply_standard_layout(fig, ...)  ←  injects STANDARD_LAYOUT + fonts
        │   return ui.HTML(fig.to_html(include_plotlyjs=True, div_id="..."))
        │
        ▼
HTML fragment sent to browser, Plotly renders chart client-side
```

The 3 metrics that don't use a `@reactive.Calc` (`total_films`, `total_gross`, `avg_gross`) call `execute_query()` directly inside their render function — they bypass the cached DataFrame layer.

---

## 6. Database Schema

```sql
films       (id INTEGER PK, title TEXT)
weeks       (filmID INTEGER FK→films.id, week INTEGER)
box_office  (filmID INTEGER FK→films.id,
             week INTEGER,
             gross REAL,
             totalAdmissions REAL,
             theatreCount REAL)
```

All analytical queries join these three tables. The top-level aggregation pattern is:

```sql
SELECT f.title, SUM/AVG(b.<metric>)
FROM films f
JOIN weeks w ON f.id = w.filmID
JOIN box_office b ON w.filmID = b.filmID AND w.week = b.week
GROUP BY f.title
ORDER BY ... DESC
LIMIT 10;
```

---

## 7. Configuration System

`config/settings.py` reads all environment variables. `config/__init__.py` re-exports them alongside all theme constants, so any module can write:

```python
from config import settings          # access settings.PORT, settings.SPACE_NAME …
from config.theme import *           # access PROFESSIONAL_COLORS, FONT_FAMILY …
```

`config/__init__.py` lists two symbols in `__all__` (`validate_environment`, `get_app_config`) that do **not** exist in any file — ignore them.

---

## 8. Theming and Design System

All visual design is centralised in `config/theme.py`:

- **`PROFESSIONAL_COLORS`** — named dict of 11 hex values (primary, secondary, accents, neutrals, highlight)
- **`CHART_COLORS`** — ordered list of 10 hex values for sequential series coloring
- **`TITLE_FONT` / `AXIS_FONT` / `LEGEND_FONT` / `TICK_FONT`** — Plotly font dicts; all use `FONT_FAMILY` (Inter)
- **`STANDARD_LAYOUT`** — dict applied to every chart via `apply_standard_layout()`

`visualizations/utils.py:apply_standard_layout(fig, title, xaxis_title, yaxis_title, **kwargs)` merges `STANDARD_LAYOUT` with per-chart overrides and calls `fig.update_layout()`. Charts that need non-standard axes (e.g. log scale in scatter charts) call `fig.update_layout()` directly instead.

`ui/styles.py:get_custom_css()` generates a CSS string at runtime by interpolating `PROFESSIONAL_COLORS` and `FONT_FAMILY` into f-string templates. It is injected as `<style>` in the page `<head>` by `ui/layout.py`.

---

## 9. UI Structure

```
page_fluid
├── <style>              ← get_custom_css()
├── .dashboard-header    ← static h1 + p
├── ui.row               ← 4 × output_ui(metric)   [KPI row, always visible]
└── ui.navset_tab
    ├── About            ← static HTML only
    ├── Overall Rankings ← top_films_chart, first_month_chart, comparison_chart
    ├── Performance      ← gross_vs_admissions_chart, gross_vs_theatre_chart, efficiency_chart
    ├── Trends           ← decay_chart, peak_timing_chart
    └── Data Insights    ← summary_table (render.table), db_stats (render.text),
                            insights_text (render.ui), insights_markdown (render.ui)
```

Every chart placeholder uses `ui.output_ui("output_id")`. The `output_id` string must match the function name decorated with `@output` in `server/handlers.py`.

---

## 10. Reactive Model

Python Shiny uses a **pull-based reactive graph**. The key rules for this app:

1. **`@reactive.Calc`** memoises its return value for the session lifetime. Because there are no `input.*` reads anywhere, the calc is computed exactly once and never invalidated.
2. **`@output` + `@render.ui`** functions call the reactive calc (e.g. `top_films_data()`) to get the DataFrame, then pass it to a visualization function. The return value must be a Shiny `ui` object — here always `ui.HTML(...)`.
3. **`@render.table`** (summary_table) expects a plain DataFrame return value; Shiny renders it as an HTML table automatically.
4. **`@render.text`** (db_stats) expects a plain string.

---

## 11. Error Handling Pattern

Every visualization function follows the same pattern:

```python
def create_*_chart(df):
    try:
        if df.empty:
            return ui.div(ui.p("...message..."), class_="error-message")
        # ... build fig ...
        return ui.HTML(fig.to_html(...))
    except Exception as e:
        return ui.div(ui.p(f"Error: {str(e)}"), class_="error-message")
```

`database/connection.py:execute_query()` catches SQL errors and returns an empty DataFrame (or a caller-supplied `default_value`), so visualization functions always receive a valid (possibly empty) DataFrame, never an exception.

When the database cannot be downloaded (missing credentials or network error), `download_database()` creates an empty `movie.db` and returns its path. The app starts, all queries return empty DataFrames, and every chart shows an "No data available" message instead of crashing.

---

## 12. Known Quirks

| Item | Detail |
|---|---|
| Filename typo | `visualizations/comparsion_charts.py` — missing 'i'. All imports use this exact name. Do not rename without updating `server/handlers.py`. |
| Metrics bypass cache | `metrics.py` calls `execute_query()` directly rather than using a `@reactive.Calc`, so it issues its own DB queries each render. |
| `__all__` phantom exports | `config/__init__.py` lists `validate_environment` and `get_app_config` in `__all__` but neither function is defined. |
| `DB_PATH` global | `database/connection.py` stores the resolved DB path in a module-level global. It is set once on first connection and never changes during the process lifetime. |
| `include_plotlyjs=True` | Every chart call embeds the full Plotly JS bundle in its HTML fragment. This is intentional (no CDN dependency) but means the first chart on each tab is large. |
