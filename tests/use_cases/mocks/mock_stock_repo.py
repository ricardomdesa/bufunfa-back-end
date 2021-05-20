from datetime import date


class MockStockRepo:

    def __init__(self, username: str):
        self.__stocks = []
        self.username = username

    def update_all_by_code(self, stocks, data: date):
        self.__stocks = list(map(lambda stock: stock.set_last_update(data), stocks))
        print(self.__stocks)

    @staticmethod
    def __set_date_in_stock(stock, data):
        stock.last_update = data
        return stock

    def add_many(self, stock_list):
        self.__stocks = stock_list

    def remove_by_code(self):
        pass

    def get_stock_by_code(self, code: str):
        return self.__stocks[0]
