from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_login import LoginManager

from settings import get_settings


def app_factory():

    settings = get_settings()

    app = FastAPI()

    origins = {settings.WEBAPP_URL}

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=[
            "X-Content-Filename",
            "Content-Disposition",
            "application/x-www-form-urlencoded",
        ],
    )

    login_manager = LoginManager(settings.SECRET, "/login")
    return app, login_manager
