
from use_cases.get_investments import GetInvestments
from tests.use_cases.mocks.mock_investment_repo import MockInvestmentRepo
from tests.use_cases.mocks.mock_stock_repo import MockStockRepo
from tests.use_cases.mocks.mock_investment_presenter import MockInvestmentPresenter


def test_run():
    investment_repo = MockInvestmentRepo('teste')
    stock_repo = MockStockRepo('teste')
    presenter = MockInvestmentPresenter()

    presenter_response = GetInvestments(investment_repo, stock_repo, presenter).run()
    print('updated = ', presenter_response[0].format_as_dict())
    assert presenter_response != 'error'