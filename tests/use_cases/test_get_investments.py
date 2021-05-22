# from presenters.get_investment_presenter import GetInvestmentPresenter
# from repositories.investment_repository import InvestmentRepository
# from repositories.stock_repository import StockRepository
from tests.use_cases.mocks.mock_investment_presenter import MockInvestmentPresenter
from tests.use_cases.mocks.mock_investment_repo import MockInvestmentRepo
from tests.use_cases.mocks.mock_stock_repo import MockStockRepo
from use_cases.get_investments import GetInvestments


def test_run():
    investment_repo = MockInvestmentRepo('teste')
    stock_repo = MockStockRepo('teste')
    presenter = MockInvestmentPresenter()
    # investment_repo = InvestmentRepository('ricardo')
    # stock_repo = StockRepository('ricardo')
    # presenter = GetInvestmentPresenter()

    presenter_response = GetInvestments(investment_repo, stock_repo, presenter).run()

    assert presenter_response.body != b'{"message": "Erro ao buscar lista de investmentos"}'
