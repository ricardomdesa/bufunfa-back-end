from presenters import GetStockPresenter
from repositories import StockRepository
from use_cases import GetStocks


class GetStockController:
    def __init__(self):
        self.__stock_repo = StockRepository()
        self.__presenter = GetStockPresenter()

    def set_username(self, username: str):
        self.__stock_repo.set_username(username)

    def get_stocks(self):
        use_case = GetStocks(self.__stock_repo, self.__presenter)
        return use_case.run()
