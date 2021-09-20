import logging

from database import db
from factories import InvestmentFactory

LOGGER = logging.getLogger(__name__)


class InvestmentRepository:
    def __init__(self):
        self.username = ""

    def set_username(self, username: str):
        self.username = username

    def add_many(self, investments: list):
        self.remove_all_by_username()
        db.investments.insert_many(investments)

    def update_all_by_username(self, investments: list):
        for inv in investments:
            filter = {
                "username": self.username,
                "codigo": inv["codigo"],
                "corretora": inv["corretora"],
            }

            new_values = {
                "$set": {
                    "valor_medio": inv["valor_medio"],
                    "quantidade": inv["quantidade"],
                    "tipo": inv["tipo"],
                    "valor_investido": inv["valor_investido"],
                    "valor_investido_atual": inv["valor_investido_atual"],
                    "rendimento": inv["rendimento"],
                }
            }
            db.investments.update_one(filter, new_values)

    def get_investments_by_username(self):
        investments = db.investments.find({"username": self.username})
        # investments = list(map(lambda item: item, investments))
        return InvestmentFactory.build_many_from_docs_repo(investments)

    def get_investment_by_code(self, code: str):
        investments = db.investments.find({"username": self.username, "codigo": code})
        return InvestmentFactory.build_many_from_docs_repo(investments)

    def remove_by_code(self, code: str):
        db.investments.delete_many({"username": self.username, "codigo": code})

    def remove_all_by_username(self):
        db.investments.delete_many({"username": self.username})
