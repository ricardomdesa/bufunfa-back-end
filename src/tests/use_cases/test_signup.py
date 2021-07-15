from domain.user import User
from repositories.user_repository import UserRepository
from use_cases.signup import SignUp
import copy


class MockSignUpPresenter:
    def respond(self, resp):
        return resp

    def respond_with_error(self, message):
        return message


class MockUserRepository:
    def __init__(self):
        self.__user = {'name': '', 'username': '', 'password': ''}

    def add_user(self, user):
        self.__user = copy.deepcopy(user.format_as_dict())

    def find_by_username(self, username):
        return User(username, self.__user['password'], self.__user['name']) if username != 'teste' else None


def test_signup_correct_data():
    use_case = SignUp(MockUserRepository(), MockSignUpPresenter())
    data = {'name': 'teste', 'username': 'teste', 'password': '1234', 'confirmPassword': '1234'}
    response = use_case.run(data)
    assert response.format_as_dict()['username'] == 'teste'
    assert len(response.format_as_dict()['password']) == 192


# validations tests
def test_signup_different_passwords():
    use_case = SignUp(MockUserRepository(), MockSignUpPresenter())
    data = {'name': 'teste', 'username': 'teste', 'password': '1234', 'confirmPassword': '12345'}
    response = use_case.run(data)
    assert response == 'Senhas devem ser iguais'


def test_signup_invalid_username_size():
    use_case = SignUp(MockUserRepository(), MockSignUpPresenter())
    data = {'name': 'teste', 'username': 'tes', 'password': '1234', 'confirmPassword': '1234'}
    response = use_case.run(data)
    assert response == 'Username precisa ter no minimo 4 digitos'


def test_signup_invalid_name_size():
    use_case = SignUp(MockUserRepository(), MockSignUpPresenter())
    data = {'name': 't', 'username': 'teste', 'password': '1234', 'confirmPassword': '1234'}
    response = use_case.run(data)
    assert response == 'Nome ter mais que 1 digito'
