from database.mongodb import db
from domain.stock import Stock


class StockRepository:

    @staticmethod
    def add_one(stock: Stock):
        db.stocks.insert_one(stock.format_as_dict())

    @staticmethod
    def add_many(stocks: list):
        # docs = list(map(lambda stock: stock.format_as_dict(), stocks))
        db.stocks.delete_many({})
        db.stocks.insert_many(stocks)

    @staticmethod
    def get_all_stocks():
        stocks = db.stocks.find({})
        return [Stock(stock['name'], stock['code'], stock['current_price']) for stock in stocks] if stocks else []

    @staticmethod
    def get_stock_by_code(code: str):
        stock = db.stocks.find_one({"code": code})
        return Stock(stock['name'], stock['code'], stock['current_price']) if stock else None

    @staticmethod
    def remove_by_code(code: str):
        db.stocks.delete_many({"code": code})
