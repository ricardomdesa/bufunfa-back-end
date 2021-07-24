import logging

from pymongo import MongoClient

from environment import DB_AUTHENTICATION_DATABASE, DB_HOST, DB_PASSWORD, DB_USER

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def create_connection():
    db_connection = MongoClient(
        DB_HOST,
        serverSelectionTimeoutMS=120000,
        connectTimeoutMS=240000,
        username=DB_USER,
        password=DB_PASSWORD,
        authSource=DB_AUTHENTICATION_DATABASE,
    ).bufunfa
    logging.info(f"Connected to mongo: {DB_HOST}")
    return db_connection


db = create_connection()
