import logging
from tempfile import SpooledTemporaryFile

import pandas as pd

from domain.investment import Investment

LOGGER = logging.getLogger(__name__)


def _seekable(self):
    return self._file.seekable()


SpooledTemporaryFile.seekable = _seekable


class LoadInvestments:
    def __init__(self, investment_repo, investment_presenter):
        self.investment_repo = investment_repo
        self.investment_presenter = investment_presenter

    def run(self, file):
        try:
            df = pd.read_csv(file, sep=",", dtype=str)
            df = self.__validate_columns_names(df)
            df = df[["corretora", "codigo", "valor_medio", "quantidade", "tipo"]]
            df = self.__format_columns(df)
            docs = df.to_dict("records")
            validated_docs = self.__get_investments_dict_to_repository(docs)
            self.investment_repo.add_many(validated_docs)
            return self.investment_presenter.respond(validated_docs)
        except AttributeError:
            return self.investment_presenter.respond_with_error("arquivo csv fora do padrao esperado")
        except Exception:
            return self.investment_presenter.respond_with_error()

    def __format_columns(self, df):
        df[["valor_medio"]] = df[["valor_medio"]].astype(float)
        df[["quantidade"]] = df[["quantidade"]].astype(int)
        df[["codigo"]] = df[["codigo"]].astype(str)
        df[["codigo"]] = df.codigo.apply(lambda code: code + ".SA" if ".SA" not in code else code)
        df["username"] = self.investment_repo.username
        return df

    def __get_investments_dict_to_repository(self, investments_dict):
        objects = self.__create_investment_object_from_dict_to_validate(investments_dict)
        return list(map(lambda investment: investment.format_as_dict(), objects))

    @staticmethod
    def __create_investment_object_from_dict_to_validate(investment_dict):
        return (
            [
                Investment(
                    investment["username"],
                    investment["corretora"],
                    investment["codigo"],
                    investment["valor_medio"],
                    investment["quantidade"],
                    investment["tipo"],
                )
                for investment in investment_dict
            ]
            if investment_dict
            else []
        )

    def __validate_columns_names(self, df):
        columns = ["corretora", "codigo", "valor_medio", "quantidade", "tipo"]
        for column in columns:
            if column not in df.columns:
                raise AttributeError
        return df
