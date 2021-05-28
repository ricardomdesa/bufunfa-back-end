from typing import List

from domain.stock import Stock
from tests.use_cases.mocks.stock_mock import STOCK_MOCK


class MockStockRepo:

    def __init__(self, username: str):
        self.__stocks = STOCK_MOCK
        self.username = username

    def update_all_by_code(self, stocks: List[Stock]):
        self.__stocks = list(map(lambda stock: stock, stocks))

    @staticmethod
    def __set_date_in_stock(stock, data):
        stock.last_update = data
        return stock

    def add_many(self, stock_list):
        self.__stocks = stock_list

    def remove_by_code(self):
        self.__stocks = []

    def remove_all(self):
        self.__stocks = []

    def get_stock_by_code(self, code: str):
        stock = self.__stocks[0]
        return Stock(stock['stock_name'], stock['stock_code'], stock['stock_current_price'], stock['stock_last_update'])

    def get_stocks(self):
        return [
            Stock(stock['stock_name'], stock['stock_code'], stock['stock_current_price'], stock['stock_last_update'])
            for stock in
            self.__stocks]
