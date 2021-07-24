import os

from dotenv import load_dotenv

load_dotenv()

WEBAPP_URL = os.getenv("WEBAPP_URL")

SECRET = os.getenv("SECRET")

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_AUTHENTICATION_DATABASE = os.getenv("DB_AUTHENTICATION_DATABASE")
