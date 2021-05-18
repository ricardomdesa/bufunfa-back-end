from database.mongodb import db
from domain.investment import Investment


class TransactionRepository:

    def __init__(self, username: str):
        self.username = username

    def add_many(self, transactions: list):
        self.remove_all_by_username()
        db.transactions.insert_many(transactions)

    def get_stocks_by_username(self):
        transactions = db.transactions.find_many({'username': self.username})
        return [Investment(transaction['username'],
                           transaction['corretora'],
                           transaction['codigo'],
                           transaction['valor_medio'],
                           transaction['quantidade'],
                           transaction['tipo']) for transaction in transactions] if transactions else []

    def remove_by_code(self, code: str):
        db.stocks.delete_many({"username": self.username, "code": code})

    def remove_all_by_username(self):
        db.transactions.delete_many({'username': self.username})
