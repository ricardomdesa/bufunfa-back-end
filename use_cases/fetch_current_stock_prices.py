import logging

LOGGER = logging.getLogger(__name__)


class FetchCurrentStockPrices:

    def __init__(self, stock_repo):
        self.stock_repo = stock_repo

    def run(self):
        stocks = self.__get_stock_list()
        adjusted_stock_codes = self.__get_adjusted_stock_codes(stocks)
        LOGGER.info(adjusted_stock_codes)

    def __get_stock_list(self):
        return self.stock_repo.get_stocks_by_username()

    @staticmethod
    def __get_adjusted_stock_codes(stocks: list):
        return [stock.code + '.SA' for stock in stocks]

