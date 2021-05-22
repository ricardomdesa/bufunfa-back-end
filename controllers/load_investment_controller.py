from repositories.investment_repository import InvestmentRepository
from use_cases.load_investments import LoadInvestments
from presenters.load_investment_presenter import LoadInvestmentPresenter


class LoadInvestmentController:

    def __init__(self, username: str):
        self.investment_repo = InvestmentRepository(username)
        self.investment_presenter = LoadInvestmentPresenter()

    def load_investments(self, file):
        return LoadInvestments(self.investment_repo, self.investment_presenter).run(file)

