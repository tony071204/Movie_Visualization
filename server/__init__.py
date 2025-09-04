"""Server Module - Reactive Handlers"""
from server.handlers import create_server

# Re-export key functions for convenience
__all__ = [
    'create_server'
]

# Version info
__version__ = '1.0.0'
