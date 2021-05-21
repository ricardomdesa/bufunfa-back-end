import logging
from pandas_datareader import data as pdr
from datetime import date, timedelta
import pandas as pd
import numpy as np

LOGGER = logging.getLogger(__name__)


class FetchCurrentStockPrices:

    def __init__(self, stock_repo, fetch_prices_presenter):
        self.stock_repo = stock_repo
        self.fetch_prices_presenter = fetch_prices_presenter

    def run(self):
        try:
            stocks = self.stock_repo.get_stocks()
            stocks_df = self.__fetch_data_from_finance([stock['stock_code'] for stock in stocks])
            stocks_dict = self.__get_dict_from_pdr_yahoo(stocks_df)
            self.stock_repo.update_all_by_code(stocks_dict)
            return self.fetch_prices_presenter.respond([])
        except Exception as error:
            raise error
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

    def __get_dict_from_pdr_yahoo(self, stocks_df):
        t = stocks_df.index.values[-1]
        current_date = np.datetime_as_string(t, unit='D')
        df = stocks_df.loc[:, 'Adj Close']
        dici = df.iloc[-1:, :].applymap(lambda x: round(x, 2)).to_dict('records')
        stock_list_dict = []
        for code, value in dici[0].items():
            new_stock = self.stock_repo.get_stock_by_code(code)
            new_stock.set_current_price(value)
            new_stock.set_last_update(current_date)
            stock_dict = new_stock.format_as_dict()
            stock_list_dict.append(stock_dict)
        return stock_list_dict
