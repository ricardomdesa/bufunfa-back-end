import logging

LOGGER = logging.getLogger(__name__)


class FetchCurrentStockPrices:
    def __init__(self, stock_repo, fetch_prices_presenter, stock_api):
        self.stock_repo = stock_repo
        self.fetch_prices_presenter = fetch_prices_presenter
        self.stock_api = stock_api

    def run(self):
        try:
            stocks = self.stock_repo.get_stocks()
            stocks_as_dict = list(map(lambda x: x.format_as_dict(), stocks))
            stocks_dict = self.stock_api.get_stock_data(stocks_as_dict)
            self.stock_repo.update_all_by_code(stocks_dict)
            return self.fetch_prices_presenter.respond(len(stocks_dict))
        except Exception:
            return self.fetch_prices_presenter.respond_with_error()
