import pandas as pd
import logging
from tempfile import SpooledTemporaryFile

LOGGER = logging.getLogger(__name__)


def _seekable(self):
    return self._file.seekable()


SpooledTemporaryFile.seekable = _seekable


class LoadInvestments:

    def __init__(self, transaction_repo, transaction_presenter):
        self.transaction_repo = transaction_repo
        self.transaction_presenter = transaction_presenter

    def run(self, file):
        try:
            df = pd.read_excel(file, sheet_name='Carteira', dtype=str)
            df = df[['corretora', 'codigo', 'valor_medio', 'quantidade', 'tipo']]
            df[['valor_medio']] = df[['valor_medio']].astype(float)
            df[['quantidade']] = df[['quantidade']].astype(int)
            df['username'] = self.transaction_repo.username
            docs = df.to_dict('records')
            self.transaction_repo.add_many(docs)
            return self.transaction_presenter.respond(docs)
        except Exception as e:
            raise Exception(e)
            return self.transaction_presenter.respond_with_error()