from typing import List

from database.mongodb import db
from domain.stock import Stock
from factories.StockFactory import StockFactory


class StockRepository:
    def __init__(self):
        self.username = ""

    def set_username(self, username: str):
        self.username = username

    def add_one(self, stock: Stock):
        doc = stock.format_as_dict()
        doc["username"] = self.username
        db.stocks.insert_one(doc)

    def add_many(self, stocks: list):
        stock_list = []
        for a in stocks:
            a["username"] = self.username
            stock_list.append(a)

        db.stocks.delete_many({"username": self.username})
        db.stocks.insert_many(stock_list)

    def get_stocks(self):
        stocks = db.stocks.find({"username": self.username})
        return StockFactory.build_many_from_docs(stocks)

    def get_stock_by_code(self, code: str):
        stock = db.stocks.find_one({"username": self.username, "stock_code": code})
        return StockFactory.build_from_doc(stock)

    def update_all_by_code(self, stocks: List[dict]):
        # new_stock_list = list(map(lambda stock: self.__set_date(stock, date), stock_list_dict))
        self.add_many(stocks)

    @staticmethod
    def __set_date(dici, date):
        ret = dici
        ret["stock_last_update"] = date
        return ret

    def remove_by_code(self, code: str):
        db.stocks.delete_many({"username": self.username, "stock_code": code})

    def remove_all(self):
        db.stocks.delete_many({"username": self.username})
