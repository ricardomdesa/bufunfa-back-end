from functools import reduce
from statistics import mean

from singleton_decorator import singleton

from domain.dashboard_info import DashboardInfo


@singleton
class GetDashboardInfo:
    def __init__(self,
                 investment_repo,
                 dashboard_info_presenter):
        self.__investment_repo = investment_repo
        self.__presenter = dashboard_info_presenter

    def run(self):
        try:
            investments = self.__investment_repo.get_investments_by_username()
            assets = self.__calculate_assets(investments)
            income = self.__calculate_income(investments)
            dashboard = DashboardInfo(assets, income)
            return self.__presenter.respond(dashboard.format_as_dict())
        except Exception as error:
            return self.__presenter.respond_with_error(error)

    @staticmethod
    def __calculate_assets(investments):
        list_values = list(map(lambda x: x.format_as_dict()['valor_investido'], investments))
        return reduce((lambda x, y: x + y), list_values)

    @staticmethod
    def __calculate_income(investments):
        list_values = list(map(lambda x: x.format_as_dict()['valor_investido'], investments))
        return mean(list_values)
