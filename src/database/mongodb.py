from pymongo import MongoClient
import logging
from environment import DB_HOST, DB_USER, \
    DB_PASSWORD, DB_AUTHENTICATION_DATABASE

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def create_connection():
    db_connection = MongoClient(
        DB_HOST,
        serverSelectionTimeoutMS=120000,
        connectTimeoutMS=240000,
        username=DB_USER,
        password=DB_PASSWORD,
        authSource=DB_AUTHENTICATION_DATABASE).bufunfa
    logging.info(f"Connected to mongo: {DB_HOST}")
    return db_connection


db = create_connection()