from presenters import FetchStockPricesPresenter
from repositories import StockRepository
from stock_price_api import YahooApiService
from use_cases import FetchCurrentStockPrices


class FetchCurrentStockPriceController:
    def __init__(self):
        self.stock_repo = StockRepository()
        self.stock_api = YahooApiService()

    def set_username(self, username: str):
        self.stock_repo.set_username(username)

    def fetch_current_stock_price(self):
        return FetchCurrentStockPrices(self.stock_repo, FetchStockPricesPresenter(), self.stock_api).run()
