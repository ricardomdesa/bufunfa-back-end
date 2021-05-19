import logging
from pandas_datareader import data as pdr
from datetime import date, timedelta
import pandas as pd

LOGGER = logging.getLogger(__name__)


class FetchCurrentStockPrices:

    def __init__(self, stock_repo, fetch_prices_presenter):
        self.stock_repo = stock_repo
        self.fetch_prices_presenter = fetch_prices_presenter

    def run(self):
        try:
            stocks = self.stock_repo.get_stocks_by_username()
            stocks_df = self.__fetch_data_from_finance([stock.code for stock in stocks])
            stocks_dict = self.__get_dict_from_pdr_yahoo(stocks_df)
            self.stock_repo.update_all_by_code(stocks_dict)
            return self.fetch_prices_presenter.respond(stocks_dict)
        except Exception as error:
            return self.fetch_prices_presenter.respond_with_error()

    @staticmethod
    def __get_dates():
        start_date = date.today() - timedelta(days=int(3))
        end_date = date.today()
        start_date = pd.to_datetime(start_date).strftime('%Y-%m-%d')
        end_date = pd.to_datetime(end_date).strftime('%Y-%m-%d')
        return start_date, end_date

    def __fetch_data_from_finance(self, stock_codes: list):
        start_date, end_date = self.__get_dates()
        return pdr.get_data_yahoo(stock_codes, start=start_date, end=end_date)

    @staticmethod
    def __get_dict_from_pdr_yahoo(stocks_df):
        df = stocks_df.loc[:, 'Adj Close']
        dici = df.iloc[-1:, :].applymap(lambda x: round(x, 2)).to_dict('records')
        return dici[0]
