from presenters import StockPresenter
from repositories import StockRepository
from use_cases import LoadStocks


class StockController:
    def __init__(self):
        self.stock_repo = StockRepository()
        self.stock_presenter = StockPresenter()

    def set_username(self, username: str):
        self.stock_repo.set_username(username)

    def load_stocks(self, stock_file):
        return LoadStocks(self.stock_repo, self.stock_presenter).run(stock_file)
