from singleton import Singleton
from business_exceptions.invalid_user_values_error import InvalidUserValuesError
from domain.user import User
from utils.authentication_utils import hash_password


class SignUp(metaclass=Singleton):
    def __init__(self, user_repo, signup_presenter):
        self.__user_repo = user_repo
        self.__signup_presenter = signup_presenter

    def run(self, data):
        try:
            self.__validate(data)
            self.__check_if_username_exists(data)
            user = User(data['username'], hash_password(data['password']), data['name'])
            self.__user_repo.add_user(user)
            return self.__signup_presenter.respond(user)
        except InvalidUserValuesError as err:
            return self.__signup_presenter.respond_with_error(err.message)

    def __validate(self, date):
        try:
            self.__validate_passwords(date)
            self.__validate_username_size(date)
            self.__validate_name_size(date)
        except InvalidUserValuesError as error:
            raise error

    @staticmethod
    def __validate_passwords(data):
        if data['password'] != data['confirmPassword']:
            raise InvalidUserValuesError('Senhas devem ser iguais')

    @staticmethod
    def __validate_username_size(data):
        if len(data['username']) < 5:
            raise InvalidUserValuesError('Username ter mais que 3 digitos')

    @staticmethod
    def __validate_name_size(data):
        if len(data['name']) < 2:
            raise InvalidUserValuesError('Nome ter mais que 1 digito')

    def __check_if_username_exists(self, data):
        if self.__user_repo.find_by_username(data['username']):
            raise InvalidUserValuesError('Usuario ja cadastrado')
