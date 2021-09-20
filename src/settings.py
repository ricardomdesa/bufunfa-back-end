from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    WEBAPP_URL: str = "http://localhost:8082"

    SECRET: str = "ccd2da9fce289fd997a4d13d3d10e927ba9426529c86c6f9d035030cd956a2e5"

    DB_HOST: str = "mongodb://localhost:27018/bufunfa"
    DB_USER: str = "mongoadmin"
    DB_PASSWORD: str = "secret"
    DB_AUTHENTICATION_DATABASE: str = "admin"


def get_settings():
    load_dotenv()
    return Settings()
