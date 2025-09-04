"""Database Connection Module"""
import sqlite3
import pandas as pd

# Global database path
DB_PATH = None


def get_db_connection():
    """Get database connection"""
    global DB_PATH
    if DB_PATH is None:
        from database.downloader import download_database
        DB_PATH = download_database()

    try:
        return sqlite3.connect(DB_PATH)
    except Exception as e:
        print(f"Database connection error: {e}")
        return sqlite3.connect(':memory:')


def execute_query(query, default_value=None):
    """Execute SQL query safely"""
    try:
        conn = get_db_connection()
        result = pd.read_sql(query, conn)
        conn.close()
        return result
    except Exception as e:
        print(f"Query error: {e}")
        return pd.DataFrame() if default_value is None else default_value
