class MockStockRepo:

    def __init__(self):
        self.__stocks = None

    def add_many(self, stocks: list):
        self.__stocks = stocks

    def get_all_stocks(self):
        return self.__stocks
