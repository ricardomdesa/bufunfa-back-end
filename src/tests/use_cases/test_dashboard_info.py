from use_cases.get_dashboard_info import GetDashboardInfo

from tests.use_cases.mocks.mock_investment_repo import MockInvestmentRepo
from tests.use_cases.mocks.investment_mock import INVESTMENT_MOCK_TWO, INVESTMENT_MOCK_TWO_CALC_EMPTY


class Mock_Presenter:

    def respond(self, _):
        return _

    def respond_with_error(self, error):
        return error


def test_dashboard_run():
    invest_repo = MockInvestmentRepo()
    invest_repo.set_username("test_dashboard")
    invest_repo.add_many(INVESTMENT_MOCK_TWO)
    response = GetDashboardInfo(invest_repo, Mock_Presenter()).run()
    assert response == [{'assets': 5700, 'income': 0.15}]


def test_dashboard_run_without_current_price():
    invest_repo = MockInvestmentRepo()
    invest_repo.set_username("test_dashboard")
    invest_repo.add_many(INVESTMENT_MOCK_TWO_CALC_EMPTY)
    response = GetDashboardInfo(invest_repo, Mock_Presenter()).run()
    assert response == [{'assets': 0, 'income': 0}]
