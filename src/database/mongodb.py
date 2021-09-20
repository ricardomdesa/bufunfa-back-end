import logging

from pymongo import MongoClient

from settings import get_settings

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def create_connection():
    settings = get_settings()
    db_connection = MongoClient(
        settings.DB_HOST,
        serverSelectionTimeoutMS=120000,
        connectTimeoutMS=240000,
        username=settings.DB_USER,
        password=settings.DB_PASSWORD,
        authSource=settings.DB_AUTHENTICATION_DATABASE,
    ).bufunfa
    logging.info(f"Connected to mongo: {settings.DB_HOST}")
    return db_connection


db = create_connection()
