# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the App

```bash
# Activate the virtual environment first
source venv/Scripts/activate   # Windows bash
# or
venv\Scripts\activate          # Windows cmd

# Run the app (starts uvicorn on port 8000 by default)
python app.py

# Or run directly with uvicorn
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

There are no tests or linting configs in this project.

## Environment Variables

Create a `.env` file (gitignored) with:

```
DO_SPACES_NAME=<bucket name>
DO_SPACES_REGION=<region, e.g. nyc3>
DO_SPACES_ACCESS_KEY=<key>
DO_SPACES_SECRET_KEY=<secret>
DATABASE_FILE=<filename in the space, e.g. movie.db>
PORT=8000
```

If these are absent, the app falls back to an empty local SQLite database and runs without crashing.

## Architecture

The startup sequence in [app.py](app.py) mirrors the dependency order:
1. `database.initialize_database()` — downloads `movie.db` from DigitalOcean Spaces (S3-compatible) into the local directory, with a 1-hour file-mtime cache. Falls back to an empty SQLite DB if credentials are missing.
2. `ui.layout.create_dashboard_ui()` — builds the full Shiny UI tree.
3. `server.handlers.create_server()` — returns the Shiny server function containing all reactive outputs.
4. `App(app_ui, server)` — combines them into a standard Python Shiny ASGI app served by uvicorn.

### Data flow

```
DigitalOcean Spaces
       ↓  boto3 (database/downloader.py)
   movie.db  (SQLite, 3 tables: films / weeks / box_office)
       ↓  sqlite3 + pandas (database/connection.py)
   data/queries.py   — raw SQL strings
   data/processors.py — executes queries, adds formatted columns, returns DataFrames
       ↓
   visualizations/*  — each module receives a DataFrame, builds a Plotly figure,
                        and returns ui.HTML(fig.to_html(...)) for Shiny to render
       ↓
   server/handlers.py — @reactive.Calc wrappers around processors;
                         @output/@render.ui bindings to visualization functions
       ↓
   ui/tabs.py         — output_ui() placeholders wired to the output IDs above
   ui/layout.py       — assembles tabs + KPI row into page_fluid()
```

### Key design points

- **All charts return `ui.HTML`**: every visualization function calls `fig.to_html(include_plotlyjs=True, div_id=...)` and wraps it in `ui.HTML`. There is no widget-based approach.
- **`apply_standard_layout`** in [visualizations/utils.py](visualizations/utils.py) is the shared helper for applying the design system to Plotly figures. All chart modules import from `config.theme` for colors and fonts.
- **Reactive data is computed once per session** via `@reactive.Calc` in `server/handlers.py` and passed directly into visualization functions — there are no user-driven input controls/filters.
- **Typo in filename**: the comparison charts file is `visualizations/comparsion_charts.py` (missing the 'i'). Imports reference this exact name.
- **`config/settings.py`** is the single source for all env-var reads. Other modules import from `config` (not `config.settings`) because `config/__init__.py` re-exports as needed.

### SQLite schema (3 tables)

- `films(id, title)` — one row per film
- `weeks(filmID, week)` — one row per film-week combination
- `box_office(filmID, week, gross, totalAdmissions, theatreCount)` — performance data
