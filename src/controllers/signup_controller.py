from singleton_decorator import singleton

from presenters.signup_presenter import SignUpPresenter
from repositories.user_repository import UserRepository
from use_cases.signup import SignUp


@singleton
class SignUpController:
    def __init__(self):
        self.__user_repo = UserRepository()
        self.__signup_presenter = SignUpPresenter()

    def signup(self, data):
        use_case = SignUp(self.__user_repo, self.__signup_presenter)
        return use_case.run(data)
