import datetime
import logging
from tempfile import SpooledTemporaryFile

import pandas as pd

LOGGER = logging.getLogger(__name__)


def _seekable(self):
    return self._file.seekable()


SpooledTemporaryFile.seekable = _seekable


class LoadStocks:
    def __init__(self, stock_repo, stock_presenter):
        self.stock_repo = stock_repo
        self.stock_presenter = stock_presenter

    def run(self, stock_file):
        try:
            df = pd.read_excel(stock_file, sheet_name="Stocks", dtype=str)
            df = self.__format_df(df)
            docs = df.to_dict("records")
            self.stock_repo.add_many(docs)
            return self.stock_presenter.respond(docs)
        except Exception:
            return self.stock_presenter.respond_with_error()

    def __format_df(self, df):
        df = df[["stock_name", "stock_code", "stock_current_price"]]
        df[["stock_current_price"]] = df[["stock_current_price"]].astype(float)
        df[["stock_code"]] = df.stock_code.astype(str)
        df[["stock_code"]] = df.stock_code.apply(lambda code: code + ".SA" if ".SA" not in code else code)
        date = datetime.date.today()
        df["stock_last_update"] = pd.to_datetime(date).strftime("%Y-%m-%d")
        return df
