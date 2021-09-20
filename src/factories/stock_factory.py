from typing import Dict, List

from domain.entities.stock import Stock
from singleton import Singleton


class StockFactory(metaclass=Singleton):
    @staticmethod
    def build_from_doc(doc: Dict) -> Stock:
        if doc:
            return Stock(
                name=doc["stock_name"],
                code=doc["stock_code"],
                current_price=doc["stock_current_price"],
                last_update=doc.get("stock_last_update", ""),
            )
        return Stock()

    @staticmethod
    def build_many_from_docs(docs: List[Dict]) -> List[Stock]:
        return [StockFactory.build_from_doc(doc) for doc in docs]
