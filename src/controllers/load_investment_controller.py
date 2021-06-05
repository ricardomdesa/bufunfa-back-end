from repositories.investment_repository import InvestmentRepository
from use_cases.load_investments import LoadInvestments
from presenters.load_investment_presenter import LoadInvestmentPresenter


class LoadInvestmentController:

    def __init__(self):
        self.investment_repo = InvestmentRepository()
        self.investment_presenter = LoadInvestmentPresenter()

    def set_username(self, username: str):
        self.investment_repo.set_username(username)

    def load_investments(self, file):
        return LoadInvestments(self.investment_repo, self.investment_presenter).run(file)

