import logging

from presenters.dashboard_info_presenter import DashboardInfoPresenter
from repositories.investment_repository import InvestmentRepository
from use_cases.get_dashboard_info import GetDashboardInfo

LOGGER = logging.getLogger(__name__)


class GetDashboardInfoController:
    def __init__(self):
        self.__investment_repo = InvestmentRepository()
        self.__presenter = DashboardInfoPresenter()

    def set_username(self, username: str):
        self.__investment_repo.set_username(username)

    def get_dashboard(self):
        use_case = GetDashboardInfo(self.__investment_repo, self.__presenter)
        return use_case.run()
