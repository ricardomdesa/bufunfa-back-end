from presenters import SignUpPresenter
from repositories import UserRepository
from use_cases import SignUp


class SignUpController:
    def __init__(self):
        self.__user_repo = UserRepository()
        self.__signup_presenter = SignUpPresenter()

    def signup(self, data):
        use_case = SignUp(self.__user_repo, self.__signup_presenter)
        return use_case.run(data)
