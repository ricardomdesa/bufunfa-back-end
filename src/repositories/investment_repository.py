from database.mongodb import db
from domain.investment import Investment
from singleton_decorator import singleton
import logging

LOGGER = logging.getLogger(__name__)


@singleton
class InvestmentRepository:

    def __init__(self):
        self.username = ""

    def set_username(self, username: str):
        self.username = username

    def add_many(self, investments: list):
        self.remove_all_by_username()
        db.investments.insert_many(investments)

    def get_investments_by_username(self):
        investments = db.investments.find({'username': self.username})
        investments = list(map(lambda item: item, investments))
        return [Investment(investment['username'],
                           investment['corretora'],
                           investment['codigo'],
                           investment['valor_medio'],
                           investment['quantidade'],
                           investment['tipo']
                           ) for investment in investments] if investments else []

    def update_all_by_username(self, investments: list):
        for inv in investments:
            filter = {"username": self.username, "codigo": inv['codigo']}

            new_values = {"$set": {'corretora': inv['corretora'],
                                   'valor_medio': inv['valor_medio'],
                                   'quantidade': inv['quantidade'],
                                   'tipo': inv['tipo']}}

            db.investments.update_one(filter, new_values)

    def get_investment_by_code(self, code: str):
        investments = db.investments.find({'username': self.username, 'codigo': code})
        return [Investment(investment['username'],
                           investment['corretora'],
                           investment['codigo'],
                           investment['valor_medio'],
                           investment['quantidade'],
                           investment['tipo']
                           ) for investment in investments] if investments else []

    def remove_by_code(self, code: str):
        db.investments.delete_many({"username": self.username, "codigo": code})

    def remove_all_by_username(self):
        db.investments.delete_many({'username': self.username})
