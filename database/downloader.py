"""Database Downloader from DigitalOcean Spaces"""
import os
import time
import sqlite3
import boto3
from botocore.exceptions import ClientError
from config import settings


def download_database():
    """Download database from DigitalOcean Spaces"""
    local_db_path = './movie.db'

    # Check cache
    if os.path.exists(local_db_path):
        file_age = time.time() - os.path.getmtime(local_db_path)
        if file_age < settings.CACHE_TIMEOUT:
            file_size = os.path.getsize(local_db_path) / (1024 * 1024)
            print(f"Using cached database ({file_size:.2f} MB)")
            return local_db_path

    # Validate environment
    if not all([settings.SPACE_NAME, settings.ACCESS_KEY, settings.SECRET_KEY]):
        print("Missing environment variables. Creating empty database...")
        conn = sqlite3.connect(local_db_path)
        conn.close()
        return local_db_path

    print("Downloading database from DigitalOcean Spaces...")

    try:
        # Initialize S3 client
        session = boto3.session.Session()
        client = session.client(
            's3',
            region_name=settings.REGION,
            endpoint_url=f'https://{settings.REGION}.digitaloceanspaces.com',
            aws_access_key_id=settings.ACCESS_KEY,
            aws_secret_access_key=settings.SECRET_KEY
        )

        # Download file
        client.download_file(
            settings.SPACE_NAME,
            settings.DATABASE_FILE,
            local_db_path
        )

        print("Database downloaded successfully")
        return local_db_path

    except Exception as e:
        print(f"Download error: {e}")
        conn = sqlite3.connect(local_db_path)
        conn.close()
        return local_db_path
