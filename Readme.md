# Movie Box Office Analytics Dashboard

## Background
The film industry invests billions annually in theatrical releases, yet lacks accessible tools for analyzing box office performance patterns. With over 10,000 films released yearly across various markets, stakeholders need data-driven insights to optimize distribution strategies and maximize revenue potential. This dashboard transforms raw box office data into actionable insights through interactive visualizations.

## Business Problem
Film distributors and studio executives face critical decisions with limited analytical support:
- **Distribution Planning**: How many theaters should initially screen a film to maximize ROI?
- **Revenue Forecasting**: When does box office revenue typically peak and what's the expected decay rate?
- **Market Penetration**: What's the optimal balance between wide and limited release strategies?
- **Performance Benchmarking**: How does a film's trajectory compare to historical top performers?
- **Investment Timing**: When should marketing spend be concentrated for maximum impact?

## Project Objective
Build a comprehensive analytics dashboard that enables data-driven decision making for theatrical releases by:
1. Visualizing revenue decay patterns across 10-week theatrical runs
2. Analyzing correlations between distribution scale (theater count) and box office performance
3. Comparing first-month performance metrics against total lifetime earnings
4. Providing interactive benchmarking against top 10 performers in the database
5. Calculating efficiency metrics (revenue per theater, revenue per admission)
6. Link to project website: https://coral-app-hqnkj.ondigitalocean.app/

## Data Source
- **Database Type**: SQLite relational database
- **Tables Structure**:
  - `films`: Movie titles and metadata 
  - `weeks`: Weekly tracking data for each film
  - `box_office`: Detailed revenue, admissions, and theater count
- **Original Source**: [numero.co](https://numero.co) box office tracking service
- **Storage Solution**: DigitalOcean Spaces (S3-compatible object storage)
- **Data Pipeline**: Automated download with 1-hour local caching
- **Update Mechanism**: Pull from cloud storage on application startup

## Tech Stack

### Core Technologies
| Component | Technology | Purpose |
|-----------|------------|---------|
| **Web Scraping** | Selenium | Dynamic content extraction from box office sites |
| **Data Processing** | Python 3.8+ | Data cleaning, preprocessing, and transformation |
| **Database** | SQL/SQLite | Structured data storage and analytics workflows |
| **Web Framework** | Python Shiny | Reactive web application development |
| **Visualizations** | Plotly | Interactive charts with zoom/pan capabilities |
| **Deployment** | DigitalOcean | Cloud hosting and database storage |
| **Server** | Uvicorn | ASGI server for production deployment |

### Supporting Libraries
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **boto3**: AWS SDK for DigitalOcean Spaces integration
- **python-dotenv**: Environment variable management
- **plotly.express**: High-level charting interface
- **plotly.graph_objects**: Custom chart configurations

## Project Structure
```
movie-dashboard/
│
├── app.py                     # Main application entry point
├── .env                       # Environment variables (DO_SPACES credentials)  
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── config/                    # Application configuration
│   ├── __init__.py
│   ├── settings.py            # Environment variables and app config
│   └── theme.py               # Color schemes, fonts, and layout constants
│
├── database/                  # Database operations
│   ├── __init__.py
│   ├── connection.py          # SQLite connection management
│   └── downloader.py          # DigitalOcean Spaces sync logic
│
├── data/                      # Data access layer
│   ├── __init__.py
│   ├── queries.py             # SQL query definitions
│   └── processors.py          # Data transformation and formatting
│
├── visualizations/            # Chart generation modules
│   ├── __init__.py
│   ├── bar_charts.py          # Top films and efficiency charts
│   ├── scatter_charts.py      # Log-scale distribution analysis
│   ├── comparison_charts.py   # Total vs first-month comparisons
│   ├── time_series_charts.py  # Revenue decay patterns
│   ├── metrics.py             # KPI metric cards
│   ├── tables.py              # Summary tables
│   └── insights.py            # Text insights and recommendations
│
├── ui/                        # User interface components
│   ├── __init__.py
│   ├── layout.py              # Main dashboard structure
│   ├── styles.py              # CSS styling definitions
│   └── tabs.py                # Navigation tab components
│
└── server/                    # Server-side logic
    ├── __init__.py
    └── handlers.py            # Reactive event handlers and data flow
