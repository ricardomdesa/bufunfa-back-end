from domain.investment import Investment
from tests.use_cases.mocks.investment_mock import INVESTMENT_MOCK


class MockInvestmentRepo:

    def __init__(self, username: str):
        self.__investments = INVESTMENT_MOCK
        self.username = username

    def add_many(self, transaction: list):
        self.__investments = transaction

    def update_all_by_username(self, investments):
        self.__investments = investments

    def get_investments_by_username(self):
        return [Investment(investment['username'],
                           investment['corretora'],
                           investment['codigo'],
                           investment['valor_medio'],
                           investment['quantidade'],
                           investment['tipo']
                           ) for investment in self.__investments] if self.__investments else []

    def get_investment_by_code(self):
        investment = self.__investments[0]
        return Investment(investment['username'],
                          investment['corretora'],
                          investment['codigo'],
                          investment['valor_medio'],
                          investment['quantidade'],
                          investment['tipo']
                          )

    def remove_by_code(self):
        self.__investments = []

    def remove_all_by_username(self):
        self.__investments = []
