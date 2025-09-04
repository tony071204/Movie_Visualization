"""SQL Queries Module"""

# Top Films Query
TOP_FILMS_QUERY = """
    SELECT f.title, SUM(b.gross) AS total_gross
    FROM films f
    JOIN weeks w ON f.id = w.filmID
    JOIN box_office b ON w.filmID = b.filmID AND w.week = b.week
    GROUP BY f.title
    ORDER BY total_gross DESC
    LIMIT 10;
"""

# First Month Query
FIRST_MONTH_QUERY = """
    SELECT f.title, SUM(b.gross) AS total_gross
    FROM films f
    JOIN weeks w ON f.id = w.filmID
    JOIN box_office b ON w.filmID = b.filmID AND w.week = b.week
    WHERE w.week BETWEEN 1 AND 4
    GROUP BY f.title
    ORDER BY total_gross DESC
    LIMIT 10;
"""

# Admissions Query
ADMISSIONS_QUERY = """
    SELECT f.title, 
           SUM(b.gross) AS total_gross, 
           SUM(b.totalAdmissions) AS total_admissions
    FROM films f
    JOIN weeks w ON f.id = w.filmID
    JOIN box_office b ON w.filmID = b.filmID AND w.week = b.week
    GROUP BY f.title
    ORDER BY total_gross DESC
    LIMIT 10;
"""

# Theatre Query
THEATRE_QUERY = """
    SELECT f.title, 
           SUM(b.gross) AS total_gross, 
           ROUND(AVG(b.theatreCount), 0) AS avg_theatre_count
    FROM films f
    JOIN weeks w ON f.id = w.filmID
    JOIN box_office b ON w.filmID = b.filmID AND w.week = b.week
    GROUP BY f.title
    ORDER BY total_gross DESC  
    LIMIT 10; 
"""

# Weekly Trends Query
WEEKLY_TRENDS_QUERY = """
    SELECT f.title, 
           w.week, 
           SUM(b.gross) AS weekly_gross
    FROM films f
    JOIN weeks w ON f.id = w.filmID
    JOIN box_office b ON w.filmID = b.filmID AND w.week = b.week
    WHERE f.title IN (
        SELECT f.title
        FROM films f
        JOIN weeks w ON f.id = w.filmID
        JOIN box_office b ON w.filmID = b.filmID AND w.week = b.week
        WHERE w.week BETWEEN 0 AND 10
        GROUP BY f.title
        ORDER BY SUM(b.gross) DESC
        LIMIT 10
    )
    AND w.week BETWEEN 0 AND 10
    GROUP BY f.title, w.week
    ORDER BY f.title, w.week;
"""

# Simple Queries
TOTAL_FILMS_QUERY = "SELECT COUNT(*) as count FROM films"
TOTAL_GROSS_QUERY = "SELECT SUM(gross) as total FROM box_office"
AVG_GROSS_QUERY = "SELECT AVG(gross) as avg FROM box_office"
MAX_GROSS_QUERY = "SELECT MAX(gross) as max FROM box_office"
