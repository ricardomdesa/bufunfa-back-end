from database.mongodb import db
from domain.stock import Stock


class StockRepository:

    def __init__(self, username: str):
        self.username = username

    def add_one(self, stock: Stock):
        doc = stock.format_as_dict()
        doc['username'] = self.username
        db.stocks.insert_one(doc)

    def add_many(self, stocks: list):
        db.stocks.delete_many({})
        db.stocks.insert_many(stocks)

    def get_stocks_by_username(self):
        stocks = db.stocks.find({'username': self.username})
        return [Stock(stock['stock_name'], stock['stock_code'], stock['stock_current_price']) for stock in stocks] if stocks else []

    @staticmethod
    def get_stock_by_code(code: str):
        stock = db.stocks.find_one({"code": code})
        return Stock(stock['name'], stock['code'], stock['current_price']) if stock else None

    @staticmethod
    def remove_by_code(code: str):
        db.stocks.delete_many({"code": code})
