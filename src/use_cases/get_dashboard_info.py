from functools import reduce
import pdb
from statistics import mean

from singleton import Singleton

from domain.dashboard_info import DashboardInfo


class GetDashboardInfo(metaclass=Singleton):
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
            return self.__presenter.respond([dashboard.format_as_dict()])
        except Exception as e:
            return self.__presenter.respond_with_error('Error getting dashboard info')

    @staticmethod
    def __calculate_assets(investments):
        list_values = list(map(lambda x: x.format_as_dict()['valor_investido_atual'] if x.format_as_dict()['valor_investido_atual'] else 0, investments))
        print(list_values)
        return reduce((lambda x, y: x + y if x else 0), list_values)

    @staticmethod
    def __calculate_income(investments):
        list_values = list(map(lambda x: x.format_as_dict()['rendimento'] if x.format_as_dict()['rendimento'] else 0, investments))
        return round(mean(list_values), 2)
