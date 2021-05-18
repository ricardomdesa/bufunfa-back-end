from repositories.transaction_repository import TransactionRepository
from use_cases.load_transactions import LoadTransactions
from presenters.transaction_presenter import TransactionPresenter


class TransactionController:

    def __init__(self, username: str):
        self.transaction_repo = TransactionRepository(username)
        self.transaction_presenter = TransactionPresenter()

    def load_transactions(self, file):
        return LoadTransactions(self.transaction_repo, self.transaction_presenter).run(file)

