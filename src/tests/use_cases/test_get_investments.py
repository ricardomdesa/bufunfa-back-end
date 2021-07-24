# from presenters.get_investment_presenter import GetInvestmentPresenter
# from repositories.investment_repository import InvestmentRepository
# from repositories.stock_repository import StockRepository
from tests.use_cases.mocks.investment_mock import INVESTMENT_MOCK
from tests.use_cases.mocks.mock_investment_presenter import MockInvestmentPresenter
from tests.use_cases.mocks.mock_investment_repo import MockInvestmentRepo
from tests.use_cases.mocks.mock_stock_repo import MockStockRepo
from use_cases.get_investments import GetInvestments


def test_run_wrong_empty_db():
    investment_repo = MockInvestmentRepo()
    investment_repo.set_username("teste1")
    investment_repo.set_db_data(list())

    stock_repo = MockStockRepo()
    stock_repo.set_username("teste")

    presenter = MockInvestmentPresenter()

    presenter_response = GetInvestments(investment_repo, stock_repo, presenter).run()
    assert presenter_response == []


def test_run():
    investment_repo = MockInvestmentRepo()
    investment_repo.set_username("teste")
    investment_repo.set_db_data(INVESTMENT_MOCK)
    stock_repo = MockStockRepo()
    stock_repo.set_username("teste")
    presenter = MockInvestmentPresenter()

    presenter_response = GetInvestments(investment_repo, stock_repo, presenter).run()
    assert presenter_response == [
        {
            "username": "teste",
            "corretora": "xp",
            "codigo": "TEST3.SA",
            "valor_medio": 20.0,
            "quantidade": 100,
            "tipo": "acao",
            "valor_investido": 2000.0,
            "valor_investido_atual": 2260.0,
            "rendimento": 0.13,
            "current_stock_price": 22.6,
        }
    ]
