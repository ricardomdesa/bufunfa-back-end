from datetime import date, timedelta
from typing import List

import numpy as np
import pandas as pd
from pandas_datareader import data as pdr


class YahooApiService:
    """
    Api to get stock data from yahoo finance api

    Inputs: dictionary with:
        "stock_name"
        "stock_code"
        "stock_current_price"
        "stock_last_update"

    Returns a dictionary in the same format with current price and last update data

    """

    def get_stock_data(self, stocks_as_dict: List[dict]):
        stock_codes = [stock.get("stock_code") for stock in stocks_as_dict]
        yahoo_df = self.__fetch_data_from_finance(stock_codes)
        current_date, dici = self.__format_yahoo_df_response(yahoo_df)
        return self.__get_updated_stock_list(current_date, dici, stocks_as_dict)

    def __fetch_data_from_finance(self, stock_codes: list):
        start_date, end_date = self.__get_formatted_dates()
        return pdr.get_data_yahoo(stock_codes, start=start_date, end=end_date)

    @staticmethod
    def __get_formatted_dates():
        start_date = date.today() - timedelta(days=int(3))
        end_date = date.today()
        start_date = pd.to_datetime(start_date).strftime("%Y-%m-%d")
        end_date = pd.to_datetime(end_date).strftime("%Y-%m-%d")
        return start_date, end_date

    def __format_yahoo_df_response(self, stocks_df):
        t = stocks_df.index.values[-1]
        current_date = np.datetime_as_string(t, unit="D")
        df = stocks_df.loc[:, "Adj Close"]
        return current_date, df.iloc[-1:, :].applymap(lambda x: round(x, 2)).to_dict("records")

    def __get_updated_stock_list(self, current_date, dict_from_yahoo, stock_as_dict):
        assert len(dict_from_yahoo) == len(stock_as_dict)
        stock_list_dict = stock_as_dict

        dict_from_yahoo = {k: v for d in dict_from_yahoo for k, v in d.items()}

        for stock in stock_list_dict:
            stock_code = stock["stock_code"]
            stock["stock_last_update"] = current_date
            stock["stock_current_price"] = dict_from_yahoo.get(stock_code)

        return stock_list_dict
