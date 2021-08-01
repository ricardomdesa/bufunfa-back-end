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
            df = pd.read_csv(stock_file, sep=",", dtype=str)
            # import pdb;pdb.set_trace()
            self.__validate_column_names(df)
            df = self.__format_df(df)
            docs = df.to_dict("records")
            self.stock_repo.add_many(docs)
            return self.stock_presenter.respond(docs)
        except AttributeError:
            return self.stock_presenter.respond_with_error("arquivo csv fora do padrao esperado")
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

    def __validate_column_names(self, df):
        column_names = ["stock_name", "stock_code", "stock_current_price", "follow"]
        for column in column_names:
            if column not in df.columns:
                raise AttributeError
        return df
