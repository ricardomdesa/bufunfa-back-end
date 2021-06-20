from singleton import Singleton


class GetStocks(metaclass=Singleton):
    def __init__(self, stock_repo, get_stock_presenter):
        self.__stock_repo = stock_repo
        self.__presenter = get_stock_presenter

    def run(self):
        try:
            stocks = self.__stock_repo.get_stocks()
            stocks_dict = list(map(lambda x: x.format_as_dict(), stocks))
            return self.__presenter.respond(stocks_dict)
        except Exception:
            return self.__presenter.respond_with_error()
