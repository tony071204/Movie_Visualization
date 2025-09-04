"""
Movie Dashboard - Entry Point
"""
import os
import uvicorn
from shiny import App

# Import from other module
from config import settings
from database import initialize_database
from ui.layout import create_dashboard_ui
from server.handlers import create_server

# 1. Initialize database
print("=" * 50)
print("Movie Box Office Dashboard")
print("=" * 50)
print("Initializing database...")
db_path = initialize_database()

# 2. Create UI
print("Building user interface...")
app_ui = create_dashboard_ui()

# 3. Create server
print("Setting up server...")
server = create_server()

# 4. Create app
app = App(app_ui, server)

# 5. Run
if __name__ == "__main__":
    port = settings.PORT
    print(f"🚀 Running on port {port}")
    print("=" * 50)
    uvicorn.run("app:app", host="0.0.0.0", port=port)
