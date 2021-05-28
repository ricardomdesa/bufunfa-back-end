from repositories.stock_repository import StockRepository
from use_cases.load_stocks import LoadStocks
from presenters.stock_presenter import StockPresenter


class StockController:

    def __init__(self, username: str):
        self.stock_repo = StockRepository(username)
        self.stock_presenter = StockPresenter()

    def load_stocks(self, stock_file):
        return LoadStocks(self.stock_repo, self.stock_presenter).run(stock_file)

