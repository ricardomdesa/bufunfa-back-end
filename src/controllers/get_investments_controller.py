import logging

from presenters import GetInvestmentPresenter
from repositories import InvestmentRepository, StockRepository
from use_cases import GetInvestments

LOGGER = logging.getLogger(__name__)


class GetInvestmentController:
    def __init__(self):
        self.__investment_repo = InvestmentRepository()
        self.__stock_repo = StockRepository()
        self.__presenter = GetInvestmentPresenter()

    def set_username(self, username: str):
        self.__investment_repo.set_username(username)
        self.__stock_repo.set_username(username)

    def get_investments(self):
        use_case = GetInvestments(self.__investment_repo, self.__stock_repo, self.__presenter)
        return use_case.run()
