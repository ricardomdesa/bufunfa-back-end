from repositories.stock_repository import StockRepository
from use_cases.fetch_current_stock_prices import FetchCurrentStockPrices
from presenters.fetch_stock_prices_presenter import FetchStockPricesPresenter


class FetchCurrentStockPriceController:

    def __init__(self, username: str):
        self.stock_repo = StockRepository(username)

    def fetch_current_stock_price(self):
        return FetchCurrentStockPrices(self.stock_repo, FetchStockPricesPresenter()).run()

