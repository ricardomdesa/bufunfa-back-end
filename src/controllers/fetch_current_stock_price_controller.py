from presenters.fetch_stock_prices_presenter import FetchStockPricesPresenter
from repositories.stock_repository import StockRepository
from stock_price_api.yahoo_api import YahooApiService
from use_cases.fetch_current_stock_prices import FetchCurrentStockPrices


class FetchCurrentStockPriceController:
    def __init__(self):
        self.stock_repo = StockRepository()
        self.stock_api = YahooApiService()

    def set_username(self, username: str):
        self.stock_repo.set_username(username)

    def fetch_current_stock_price(self):
        return FetchCurrentStockPrices(self.stock_repo, FetchStockPricesPresenter(), self.stock_api).run()
