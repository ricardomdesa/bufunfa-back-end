import pandas as pd
import logging
from tempfile import SpooledTemporaryFile

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
            df = pd.read_excel(stock_file, sheet_name='Stocks', dtype=str)
            df = df[['stock_name', 'stock_code', 'stock_current_price']]
            df[['stock_current_price']] = df[['stock_current_price']].astype(float)
            df['username'] = self.stock_repo.username
            docs = df.to_dict('records')
            self.stock_repo.add_many(docs)
            return self.stock_presenter.respond(docs)
        except Exception as e:
            raise Exception(e)
            return self.stock_presenter.respond_with_error()
