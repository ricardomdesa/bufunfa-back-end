from unittest.mock import Mock

from tests.use_cases.mocks.investment_mock import INVESTMENT_MOCK_TWO, INVESTMENT_MOCK_TWO_CALC_EMPTY
from tests.use_cases.mocks.mock_investment_repo import MockInvestmentRepo
from use_cases.get_dashboard_info import GetDashboardInfo


def test_dashboard_run():
    invest_repo = MockInvestmentRepo()
    invest_repo.set_username("test_dashboard")
    invest_repo.add_many(INVESTMENT_MOCK_TWO)
    presenter = Mock()
    GetDashboardInfo(invest_repo, presenter).run()
    presenter.respond.assert_called_with([{"assets": 5700, "income_perc": 0.12, "income_value": 700.0}])


def test_dashboard_run_without_current_price():
    invest_repo = MockInvestmentRepo()
    invest_repo.set_username("test_dashboard")
    presenter = Mock()
    invest_repo.add_many(INVESTMENT_MOCK_TWO_CALC_EMPTY)
    GetDashboardInfo(invest_repo, presenter).run()
    presenter.respond.assert_called_with([{"assets": 0, "income_perc": 0, "income_value": 5000}])
