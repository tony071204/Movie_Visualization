"""Configuration Settings"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# DigitalOcean Spaces
SPACE_NAME = os.getenv('DO_SPACES_NAME')
REGION = os.getenv('DO_SPACES_REGION')
DATABASE_FILE = os.getenv('DATABASE_FILE')
ACCESS_KEY = os.getenv('DO_SPACES_ACCESS_KEY')
SECRET_KEY = os.getenv('DO_SPACES_SECRET_KEY')

# App settings
PORT = int(os.getenv('PORT', 8000))
CACHE_TIMEOUT = 3600  # 1 hour
