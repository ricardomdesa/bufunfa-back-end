from singleton_decorator import singleton

from presenters.get_investment_presenter import GetInvestmentPresenter
from repositories.investment_repository import InvestmentRepository
from repositories.stock_repository import StockRepository
from use_cases.get_investments import GetInvestments


@singleton
class GetInvestmentController:

    def __init__(self, username: str):
        self.__investment_repo = InvestmentRepository(username)
        self.__stock_repo = StockRepository(username)
        self.__presenter = GetInvestmentPresenter()

    def get_investments(self):
        use_case = GetInvestments(self.__investment_repo, self.__stock_repo, self.__presenter)
        use_case.run()
