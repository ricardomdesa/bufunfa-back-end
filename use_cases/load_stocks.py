import pandas as pd
import logging

LOGGER = logging.getLogger(__name__)


class LoadStocks:

    def __init__(self, stock_repo, stock_presenter):
        self.stock_repo = stock_repo
        self.stock_presenter = stock_presenter

    def run(self, stock_file):
        try:
            LOGGER.info("teste log", stock_file)
            df = pd.read_excel(stock_file, sheet_name='Stocks', dtype=str)
            df[['stock_current_price']] = df[['stock_current_price']].astype(float)
            docs = df.to_dict('records')
            self.stock_repo.add_many(docs)
            return self.stock_presenter.respond(docs)
        except Exception:
            return self.stock_presenter.respond_with_error()
