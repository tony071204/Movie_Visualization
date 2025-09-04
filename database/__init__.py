"""Database Module"""
from database.connection import get_db_connection, execute_query
from database.downloader import download_database


def initialize_database():
    """Initialize database on startup"""
    return download_database()


__all__ = ['initialize_database', 'get_db_connection', 'execute_query']
