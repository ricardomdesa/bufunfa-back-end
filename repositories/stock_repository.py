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

    def get_stock_by_code(self, code: str):
        stock = db.stocks.find_one({"username":self.username, "stock_code": code})
        return Stock(stock['stock_name'], stock['stock_code'], stock['stock_current_price']) if stock else None

    def update_all_by_code(self, stock_dict: dict):
        for code, value in stock_dict.items():
            db.stocks.update_one({'username': self.username, 'stock_code': code}, {'$set': {"stock_current_price": value}})

    def remove_by_code(self, code: str):
        db.stocks.delete_many({"username": self.username, "stock_code": code})
