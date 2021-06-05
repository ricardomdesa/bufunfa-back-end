from singleton_decorator import singleton


@singleton
class GetStocks:
    def __init__(self, stock_repo, get_stock_presenter):
        self.__stock_repo = stock_repo
        self.__presenter = get_stock_presenter

    def run(self):
        try:
            stocks = self.__stock_repo.get_stocks_by_username()
            return self.__presenter.respond(stocks)
        except Exception:
            return self.__presenter.respond_with_error()
