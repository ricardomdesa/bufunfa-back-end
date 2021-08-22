from typing import Dict, List

from domain.investment import Investment
from singleton import Singleton


class InvestmentFactory(metaclass=Singleton):
    @staticmethod
    def build_from_doc_repo(doc: Dict) -> Investment:
        if doc:
            return Investment(
                doc["username"],
                doc["corretora"],
                doc["codigo"],
                doc["valor_medio"],
                doc["quantidade"],
                doc["tipo"],
                doc["valor_investido_atual"],
                doc["rendimento"],
            )
        return Investment()

    @staticmethod
    def build_many_from_docs_repo(docs: List[Dict]) -> List[Investment]:
        return [InvestmentFactory.build_from_doc_repo(doc) for doc in docs]
