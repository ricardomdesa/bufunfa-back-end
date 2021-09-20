from presenters import LoadInvestmentPresenter
from repositories import InvestmentRepository
from use_cases import LoadInvestments


class LoadInvestmentController:
    def __init__(self):
        self.investment_repo = InvestmentRepository()
        self.investment_presenter = LoadInvestmentPresenter()

    def set_username(self, username: str):
        self.investment_repo.set_username(username)

    def load_investments(self, file):
        return LoadInvestments(self.investment_repo, self.investment_presenter).run(file)
