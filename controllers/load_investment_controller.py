from repositories.investment_repository import InvestmentRepository
from use_cases.load_investments import LoadInvestments
from presenters.load_investment_presenter import LoadInvestmentPresenter


class InvestmentController:

    def __init__(self, username: str):
        self.transaction_repo = InvestmentRepository(username)
        self.transaction_presenter = LoadInvestmentPresenter()

    def load_transactions(self, file):
        return LoadInvestments(self.transaction_repo, self.transaction_presenter).run(file)

