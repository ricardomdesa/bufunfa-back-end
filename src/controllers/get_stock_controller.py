from singleton_decorator import singleton

from presenters.get_stock_presenter import GetStockPresenter
from repositories.stock_repository import StockRepository
from use_cases.get_stocks import GetStocks


@singleton
class GetStockController:

    def __init__(self, username: str):
        self.__stock_repo = StockRepository(username)
        self.__presenter = GetStockPresenter()

    def get_stocks(self):
        use_case = GetStocks(self.__stock_repo, self.__presenter)
        return use_case.run()
