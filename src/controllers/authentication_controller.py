from datetime import timedelta

from presenters.authentication_presenter import AuthenticationPresenter
from repositories.user_repository import UserRepository

# from singleton import Singleton
from utils.authentication_utils import verify_password


class AuthenticationController:
    def __init__(self, login_manager):
        self.__login_manager = login_manager
        self.__repository = UserRepository()
        self.__presenter = AuthenticationPresenter()

    def authenticate_user(self, username: str, password: str):
        user = self.__repository.find_by_username(username)
        if user:
            if verify_password(user.password, password):
                access_token = self.__login_manager.create_access_token(
                    data={"sub": username}, expires=timedelta(hours=4)
                )
                return self.__presenter.respond(access_token)
            else:
                return self.__presenter.respond_with_error(f"Invalid password for user: {user.username}")
        else:
            return self.__presenter.respond_with_error("Invalid username")
