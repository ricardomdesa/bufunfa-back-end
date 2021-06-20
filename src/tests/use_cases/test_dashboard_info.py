from use_cases.get_dashboard_info import GetDashboardInfo

from tests.use_cases.mocks.mock_investment_repo import MockInvestmentRepo
from tests.use_cases.mocks.investment_mock import INVESTMENT_MOCK_TWO


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
    assert True
