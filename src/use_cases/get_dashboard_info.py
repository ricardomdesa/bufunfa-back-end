import logging
from functools import reduce

from domain.dashboard_info import DashboardInfo
from singleton import Singleton


class GetDashboardInfo(metaclass=Singleton):
    def __init__(self, investment_repo, dashboard_info_presenter):
        self.__investment_repo = investment_repo
        self.__presenter = dashboard_info_presenter

    def run(self):
        try:
            investments = self.__investment_repo.get_investments_by_username()
            assets = self.__calculate_assets(investments)
            income_value = self.__calculate_income_value(investments)
            income_perc = self.__calculate_income_perc(income_value, assets)
            dashboard = DashboardInfo(assets, income_perc, income_value)
            return self.__presenter.respond([dashboard.format_as_dict()])
        except Exception as error:
            logging.error(f"Error getting dashboard info: {error}")
            return self.__presenter.respond_with_error(f"Error getting dashboard info: {error}")

    @staticmethod
    def __calculate_assets(investments):
        list_values = list(
            map(
                lambda x: x.format_as_dict()["valor_investido_atual"]
                if x.format_as_dict()["valor_investido_atual"]
                else 0,
                investments,
            )
        )
        return reduce((lambda x, y: x + y if x else 0), list_values)

    @staticmethod
    def __calculate_income_value(investments):
        list_income_values = list(
            map(
                lambda x: x.format_as_dict()["valor_investido_atual"] - x.format_as_dict()["valor_investido"]
                if x.format_as_dict()["valor_investido_atual"]
                else x.format_as_dict()["valor_investido"],
                investments,
            )
        )
        return sum(list_income_values)

    @staticmethod
    def __calculate_income_perc(income_value: float = 0, assets: float = 0):
        return round(income_value / assets, 2) if assets > 0 else 0
